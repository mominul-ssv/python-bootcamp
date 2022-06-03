from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path

# Multipurpose internet mail extension (mime). It's a standard for defining the format of an email.

message = MIMEMultipart()
message["form"] = "Mominul Islam"
message["to"] = "test@gmail.com"
message["subject"] = "Testing Python Email Module"

# 'attach()' method gets a payload
# This payload can be text, image or other types supported by the mime protocol
message.attach(MIMEText("Body", "plain"))
message.attach(MIMEImage(Path("faker_artwork.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:

    # Tell the smtp server that we want to send an email
    smtp.ehlo()

    # This puts smtp connection in 'tls' mode. (tls = transport layer security)
    smtp.starttls()

    # Log into smtp server
    smtp.login("test@gmail.com", "test1234")

    smtp.send_message(message)
    print("Sent...")
