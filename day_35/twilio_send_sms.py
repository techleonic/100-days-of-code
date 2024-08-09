from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+',
  body="Para que tengas un negrito con tu esposa y otro chelito con migo",
  to='+'
)

print(message.sid)
