from twilio.rest import Client

account_sid = 'AC2224dcf8cdfd3eac664be83cf214f2aa'
auth_token = '[Redacted]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGa89d18db298d1d720bbad25b0fb8eadb',
    body='alo',
    to='+84822988755'
)

print(message.sid)