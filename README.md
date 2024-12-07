# College Inquiry Assistant System

The **College Inquiry Assistant System** is an AI-powered chatbot designed to simplify and enhance the user experience when inquiring about a college. The system offers speech-based interaction, collects visitor information, captures images, and stores the data in a local database.

---

## Features

### 1. Speech Interaction
- Converts user speech into text using `speech_recognition`.
- Responds via text-to-speech using `pyttsx3`.

### 2. Automated Responses
Provides accurate and predefined responses to queries about:
- **Admissions:** Course details, intake capacity, and admission process.
- **Departments:** Information about various departments and HODs.
- **Campus Facilities:** Library, meditation halls, offices, and contact details.
- **Events and Activities:** Information about ongoing and upcoming events.

### 3. User Information Management
- Collects visitor details:
  - First and Last Name
  - Address
  - Phone Number (validated)
  - Purpose of visit
- Captures an image of the visitor using a webcam.

### 4. Data Storage
- Stores the collected information in an SQLite database (`user_info.db`):
  - Name, Address, Phone Number
  - Purpose of Visit
  - Date and Time
  - Path to the captured image.

---

## Technology Stack

- **Programming Language:** Python
- **Database:** SQLite
- **Libraries Used:**
  - `speech_recognition` - Speech-to-text conversion.
  - `pyttsx3` - Text-to-speech functionality.
  - `opencv-python` - Webcam integration for capturing images.
  - `re` - Input validation.
  - `datetime` - Timestamp management.

---

## Prerequisites

Ensure the following are installed on your system:

1. Python 3.x
2. Required Python libraries:
   ```bash
   pip install speechrecognition pyttsx3 opencv-python
