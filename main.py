import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('afif72371@gmail.com', 'afif#1234*')
    email = EmailMessage()
    email['From'] = 'afif72371@gmail.com'
    email ['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list ={
    'dude': 'afif72371@gmail.com',
    'school': '19299@noormohammadcollege.ac.bd'
}

def get_email_info():
     talk('to whom you want to send e-mail')
     name = get_info()
     receiver = email_list[name]
     print(receiver)
     talk('what is the subject of your email')
     subject = get_info()
     talk('Tell me the text in your email')
     message = get_info()
     send_email(receiver, subject, message )

get_email_info()
