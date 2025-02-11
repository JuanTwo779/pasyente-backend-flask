
# Patient SMS Reminder Application (Mockup)

## Overview

This project is a mockup for a **Patient SMS Reminder Application**, designed to demonstrate the functionality of sending automated appointment reminders via SMS. The system uses **AWS services** to send SMS messages through a longcode, providing a seamless and efficient way to communicate with patients.

## Features

- **Appointment Reminders**: Automatically sends SMS reminders to patients about their scheduled appointments.
- **Longcode Integration**: Uses AWS services and a longcode to send personalized messages to patients.
- **Flask Backend**: The application is built using **Flask**, a lightweight Python web framework, providing a simple yet powerful backend for handling requests.
- **SMS Confirmation**: Patients can confirm their appointments by replying "YES" to the SMS, which is then recorded in the system.
- **Database Integration**: The app integrates with **MySQL** via **SQLAlchemy** to store patient details and appointment information.

## Technologies Used

- **Flask**: Web framework to handle backend operations.
- **AWS Services**: Utilizes **AWS** for sending SMS via longcodes, providing reliable messaging services.
- **Flask-SQLAlchemy**: To interact with the MySQL database for storing and retrieving patient appointment data.
- **Flask-WTF**: To simplify form handling, including patient input for appointment scheduling.
- **MySQL**: Used to store patient details, including phone numbers and appointment information.
- **Boto3**: AWS SDK for Python, to facilitate interaction with AWS services like **S3** and **SNS** for SMS functionality.

## Installation

### Prerequisites

- **Python 3.x**
- **MySQL Database** (Ensure you have access to a MySQL database for storing patient data)
- **AWS Account** (For SMS functionality using AWS services)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/patient-sms-reminder.git
   cd patient-sms-reminder
   ```

2. **Set up a Virtual Environment** (Optional, but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root of the project to store your AWS credentials and database configuration:
   ```
   AWS_ACCESS_KEY_ID=your_aws_access_key
   AWS_SECRET_ACCESS_KEY=your_aws_secret_key
   AWS_REGION=your_aws_region
   DATABASE_URL=mysql://username:password@localhost/db_name
   ```

5. **Run the Application**:
   ```bash
   flask run
   ```

6. **Access the Application**:
   Open a browser and go to `http://127.0.0.1:5000/` to use the application.

## Workflow

1. The system stores patient information (name, phone number, appointment date and time) in a MySQL database.
2. When an appointment is scheduled, the system automatically sends an SMS reminder using AWS services.
3. The patient can confirm the appointment by replying "YES" to the SMS, which is then updated in the system.
4. The user (admin) can view the patient's confirmation status and manage upcoming appointments.

## Future Enhancements

- **Multi-Language Support**: Add the ability to send SMS reminders in multiple languages based on patient preferences.
- **Web Interface**: Create an intuitive web interface for both patients and administrators to manage appointments and confirmations.
- **Analytics**: Provide statistics and analytics on appointment confirmations, no-shows, etc.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
