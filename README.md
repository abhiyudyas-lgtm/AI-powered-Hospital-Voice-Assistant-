# AI-powered-Hospital-Voice-Assistant-

# 🏥 HospAI – AI Voice-Based Hospital Appointment Booking System

## Overview

HospAI is an AI-powered voice assistant that automates hospital appointment booking through phone calls. Patients can simply call a hospital number, provide their details using natural speech, and receive appointment confirmation without requiring human assistance.

The system uses Twilio Voice API for call handling, speech recognition for capturing patient responses, and an Excel-based database for storing appointment records.

## Features

* 📞 Voice-based appointment booking
* 🎤 Speech-to-text patient interaction
* 🏥 Automated hospital appointment scheduling
* 💾 Appointment storage using Excel database
* 🔄 Multi-step conversational workflow
* ⚡ Real-time call processing with Twilio
* 🛡️ Error handling and input validation
* 🔧 Modular and extensible architecture

## Technology Stack

* Python
* Flask
* Twilio Voice API
* OpenPyXL
* Ngrok
* Python Dotenv

## Project Structure

```text
HospAI/
│
├── app.py
├── config.py
├── create_excel.py
├── excel_db.py
├── appointments_main.xlsx
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/HospAI.git
cd HospAI
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
TWILIO_SID=your_twilio_sid
TWILIO_TOKEN=your_twilio_auth_token
TWILIO_NUMBER=your_twilio_phone_number
YOUR_NUMBER=your_phone_number
GEMINI_API_KEY=your_gemini_api_key
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

Expose the local server using Ngrok:

```bash
ngrok http 5000
```

To verify that the Twilio integration and call workflow are working correctly, run the test script:

python test_call.py

The script initiates a test call using your configured Twilio credentials and phone numbers.

Copy the generated HTTPS URL and configure it as the Voice Webhook URL in your Twilio phone number settings.

## Workflow

1. Patient calls the hospital number.
2. System asks for patient name.
3. System asks for disease/reason for visit.
4. System asks for preferred appointment time.
5. Appointment details are stored automatically.
6. Patient receives appointment confirmation through voice response.

## Future Enhancements

* SMS appointment confirmations and reminders
* AI-powered hospital information assistant
* Multilingual support (Hindi, Tamil, Telugu, etc.)
* Cloud deployment on AWS or Google Cloud
* Doctor availability management
* Integration with hospital management systems


This project is developed for educational and research purposes.
