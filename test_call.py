from twilio.rest import Client
from config import TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER, YOUR_NUMBER
import sys
 
NGROK_URL = "https://nicol-protonic-crudely.ngrok-free.dev"
 
if "PASTE" in NGROK_URL:
    print("ERROR: You forgot to update NGROK_URL in test_call.py!")
    print("Run 'ngrok http 5000', copy the https URL, paste it above.")
    sys.exit(1)
 
client = Client(TWILIO_SID, TWILIO_TOKEN)
 
call = client.calls.create(
    to=YOUR_NUMBER,
    from_=TWILIO_NUMBER,
    url=NGROK_URL
)
 
print("Call initiated:", call.sid)
print("Twilio will POST to:", NGROK_URL)
