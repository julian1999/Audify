import smtplib
import sndhdr
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
server = smtplib.SMTP('smtp.gmail.com', 587)
print("IMPORTANT: MUST ENABLE ACCES FOR LESS SECURE APPS")
print("Login only available for gmail accounts")
username = input("Enter your gmail: ")
password = getpass()

#logging onto the server
server.ehlo()
server.starttls()
server.login(username, password)
#who the email will be sent to
toSend = input("Enter the email you would like to send result file to: ")
msg = MIMEMultipart()
#setting up the context of the email
msg['Subject'] = 'The result.wav file'
msg['From'] = username
msg['To'] = toSend
msg.preamble = 'Testing the email'
#the sound file that we will be sending
file = 'result.wav'
fp = open(file, 'rb')
audio = MIMEAudio(fp.read())
#giving the audio file a name
audio.add_header('Content-Disposition', 'attachment', filename=file)
#attaching the audio file to the email
msg.attach(audio)
print(sndhdr.what('result.wav'))
print("Sending the file")
#sending the email
server.sendmail('julianalbert99@gmail.com', toSend, msg.as_string())

