from twilio.rest import TwilioRestClient
import json


def load_admins_file():
    with open('config/credentials.json') as adminsFile:
        admins = json.load(adminsFile)
        return admins


def send_text_messages(receiver_number, expediteur_number, body):
    credentials = load_admins_file()
    client = TwilioRestClient(credentials[0]['ACCOUNT_SID'],
                              credentials[0]['AUTH_TOKEN'])
    client.messages.create(
        to=receiver_number,
        from_=expediteur_number,
        body=body)
