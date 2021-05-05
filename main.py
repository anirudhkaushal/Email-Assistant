import smtplib
import speech_recognition as sr
from email.message import EmailMessage

listener = sr.Recognizer()


def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source, phrase_time_limit=4)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('myemailid@gmail.com', 'mypassword')
    email = EmailMessage()
    email['From'] = 'myemailid@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'jerry': 'jerrysemailid@gmail.com',
    'tom': 'tomsemailid@gmail.com'
}


def get_email_info():
    print('Hi! I am your Email Assistant')
    print()

    print('To whom do you want to send the email?')
    name = get_info()
    receiver = email_list[name]
    print()

    print('What is the subject of your email?')
    subject = get_info()
    print()

    print('Tell me the content of your email')
    message = get_info()
    send_email(receiver, subject, message)
    print()

    print('Email sent successfully!')


get_email_info()
