import requests
from threading import Thread
import time
import os
import config


class ParsingProxy:
    def __init__(self, send, chat_id):
        self.send = send
        self.chat_id = chat_id
        self.a = requests.get(config.urlParse).text
        file = open('proxy/proxy.txt', 'w')
        file.write(self.a.replace('\n', ''))
        file.close()
        self.check_proxys()

    def check_proxy(self, proxy):
        try:
            if requests.get("https://www.citilink.ru/", proxies={"http": proxy, "https": proxy},
                            timeout=5).status_code == 200:
                with open('proxy/proxy.txt', mode='a') as vi:
                    if os.stat("proxy/proxy.txt").st_size == 0:
                        vi.write(proxy)
                        self.proxys.append(proxy)
                    else:
                        vi.write('\n'+proxy)
                        self.proxys.append(proxy)
        except Exception as er:
            pass

    def check_proxys(self):
        self.proxys = []
        with open('proxy/proxy.txt', mode='r') as file:
            gg = file.read().splitlines()
        self.send(self.chat_id, 'Кол-во залитых прокси: {}'.format(len(gg)))
        with open('proxy/proxy.txt', mode='w') as file:
            file.write('')
        for proxy in gg:
            Thread(target=self.check_proxy, args=[proxy]).start()
            time.sleep(0.4)
        self.send(self.chat_id, 'Рабочих прокси: {}'.format(len(self.proxys)))