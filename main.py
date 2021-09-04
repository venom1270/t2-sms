import requests

with requests.Session() as session:
    session.get("https://horizont.t-2.net/prijava")
    print(session.cookies)

    login_data = {
        "username": "[USERNAME]@t-2.net",
        "password": "[PASSWORD]"
    }
    r = session.post("https://horizont.t-2.net/prijava", data=login_data)

    payload = {
        "group": "mobilna-telefonija",
        "handler": "poslji-sms",
        "action": "send_sms",
        "sender": "[SENDER NUMBER (386XXXXXXXX)]",
        "text_message": "[MESSAGE]",
        "mobile_prefix": "064",
        "reciver": "",
        "send_me[]": [
            "[RECIPIENT PHONE NUMBER (eg. 031XXXXXX)]",
        ]
    }
    session.post("https://horizont.t-2.net/sms/poslji-sms", data=payload)


