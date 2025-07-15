# PythonEmailReminderApp
A simple and lightweight Python tool for sending email reminders — perfect for tutors, teachers, or anyone who needs to keep track of upcoming sessions or events. Only 57 lines of code!

# Features
 Quickly send reminder emails to yourself, students, or anyone else

 Easy to use and modify

 No bulky frameworks — just clean, functional Python

 Send directly via Gmail (or your SMTP server of choice)

 Setup
Clone the repository

git clone https://github.com/yourusername/PythonEmailReminderApp.git
cd PythonEmailReminderApp
Install requirements (if any — for example, if you use dotenv or external packages)


pip install -r requirements.txt
Set up your email credentials
Inside reminder.py, replace the placeholders with your email and app password.
For Gmail, make sure:

2FA is enabled

You've created an App Password

 Usage
Just run the script:


python reminder.py
You'll be prompted to enter:

Your name

Student’s name and email

Session date and time

Custom message (optional)

The script will send out a cleanly formatted reminder email to both you and your student.

Notes
The script currently uses plain SMTP with Gmail. You can easily adapt it to work with Outlook, Yahoo, or other providers.

To keep things secure, you may want to store credentials in environment variables or use a .env file.

 License
MIT License

