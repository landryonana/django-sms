from twilio.rest import Client

def send_sms(message):
    account_id = 'AC4406ad8c9ba51725edde77315b2674cb'
    auth_token = '04c64a103f11ec2ebed4d2128f76a121'
    client = Client(account_id, auth_token)
    for receiver in message.receiver_message.all():
        try:
            message = client.messages.create(
                body=f"{message.body}",
                from_="+12544574774",
                to=f"+237{receiver.telephone}"
            )
            return False
        except:
            return True