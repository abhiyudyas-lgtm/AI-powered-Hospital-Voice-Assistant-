from flask import Flask, request, Response       
from twilio.twiml.voice_response import VoiceResponse, Gather
from urllib.parse import quote
from excel_db import save_appointment

app = Flask(__name__)

from config import (
    TWILIO_SID,
    TWILIO_TOKEN,
    TWILIO_NUMBER,
    YOUR_NUMBER,
    GEMINI_API_KEY
)


def twiml_response(response):
    """Return a proper TwiML response with the correct Content-Type.
    Flask defaults to text/html — Twilio requires text/xml or it shows
    'Application Error' and hangs up immediately."""
    return Response(str(response), mimetype='text/xml')   


def make_gather(step, message, extra_params=""):
    gather = Gather(
        input='speech',
        action=f'/process?step={step}{extra_params}',
        language='en-IN',
        speechTimeout='auto',
        timeout=10,
        actionOnEmptyResult=True,
        bargeIn=True
    )
    gather.say(message)
    return gather


# ===== ENTRY =====
@app.route("/", methods=['GET', 'POST'])
def incoming_call():
    print("New Call Started")
    response = VoiceResponse()
    response.append(
        make_gather(1, "Welcome to City Hospital. Please tell the patient name.")
    )
    response.say("We did not receive any input. Please call again. Goodbye.")
    return twiml_response(response)


@app.route("/process", methods=['POST'])
def process():
    step = request.args.get("step", "1")
    text = request.form.get("SpeechResult", "").strip()

    print(f"STEP: {step} | TEXT: {text}")

    response = VoiceResponse()

    # ---- Empty / no-speech handling ----
    if not text:
        response.append(
            make_gather(step, "Sorry, I didn't catch that. Please repeat.")
        )
        response.say("We could not hear you. Please call again.")
        return twiml_response(response)

    # ===== STEP 1 : NAME =====
    if step == "1":
        safe_name = quote(text)
        gather = Gather(
            input='speech',
            action=f"/process?step=2&name={safe_name}",
            language='en-IN',
            speechTimeout='auto',
            timeout=10,
            actionOnEmptyResult=True,
            bargeIn=True
        )
        gather.say(f"Thank you, {text}. Now please tell the disease or reason for visit.")
        response.append(gather)
        response.say("We did not receive input. Please call again.")
        return twiml_response(response)

    # ===== STEP 2 : DISEASE =====
    if step == "2":
        name = request.args.get("name", "")
        safe_name = quote(name)
        safe_disease = quote(text)

        gather = Gather(
            input='speech',
            action=f"/process?step=3&name={safe_name}&disease={safe_disease}",
            language='en-IN',
            speechTimeout='auto',
            timeout=10,
            actionOnEmptyResult=True,
            bargeIn=True
        )
        gather.say("Thank you. Please tell the preferred appointment time.")
        response.append(gather)
        response.say("We did not receive input. Please call again.")
        return twiml_response(response)

    # ===== STEP 3 : TIME =====
    if step == "3":
        name    = request.args.get("name", "Unknown")
        disease = request.args.get("disease", "Unknown")
        time    = text

        print(f"SAVING → Name: {name} | Disease: {disease} | Time: {time}")
        save_appointment(name, disease, time)

        response.say(
            f"Appointment confirmed for {name}, "
            f"regarding {disease}, at {time}. "
            f"Thank you for calling City Hospital. Goodbye!"
        )
        return twiml_response(response)

    # Fallback
    response.say("An unexpected error occurred. Please call again.")
    return twiml_response(response)


if __name__ == "__main__":
    app.run(debug=True)