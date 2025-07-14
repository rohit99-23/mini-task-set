from twilio.rest import Client

# Twilio credentials
account_sid = 'AC35c443243b78aa8d1469fd8490700ec2'
auth_token = 'd924c3036918eaac9b0bee5c94ae2929'
twilio_number = '+16593007205'  # ✅ Removed space

# Receiver number and message input
target_number = input('Enter Receiver Number (with +91...): ')
user_message = input("Enter your message: ")

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body=user_message,
    from_=twilio_number,
    to=target_number
)

print("✅ Message sent! SID:", message.sid)

# Make Call
twiml_message = 'http://demo.twilio.com/docs/voice.xml'

call = client.calls.create(
    to=target_number,
    from_=twilio_number,
    url=twiml_message
)

print("📞 Call initiated! SID:", call.sid)
