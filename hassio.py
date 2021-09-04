import appdaemon.plugins.hass.hassapi as hass
import requests

class SendSms(hass.Hass):
    def initialize(self):
        self.listen_event(self.send, "SEND_SMS")
        print("SendSms initialized...")

    # In Home Assistant:
    #  - Fire Event: SEND_SMS
    #  - Include data:
    #   - message: message string
    #   - recipients: comma separated phone numbers string (no spaces)
    def send(self, event_name, data, kwargs):
        with requests.Session() as session:
            session.get("https://horizont.t-2.net/prijava")

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
                "text_message": data.get("message"),
                "mobile_prefix": "064",
                "reciver": "",
                "send_me[]": [

                ]
            }

            print("Data:")
            print(data)

            for recipient in data.get("recipients").split(","):
                payload.get("send_me[]").append(recipient)

            print("Sending payload:")
            print(payload)

            session.post("https://horizont.t-2.net/sms/poslji-sms", data=payload)




