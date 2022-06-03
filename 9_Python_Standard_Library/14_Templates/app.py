from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
import smtplib
from pathlib import Path

template = Template(Path("template.html").read_text())


message = MIMEMultipart()
message["form"] = "Mominul Islam"
message["to"] = "testuser@gmail.com"
message["subject"] = "This is a test"

# We can pass a dictionary that contains key-value pairs or parameters or templates
# We can also pass keyword arguments [Example: substitute(name="John")]
body = template.substitute({"name": "John"})

message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("faker_artwork.jpg").read_bytes))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@gmail.com", "test1234")
    smtp.send_message(message)
    print("Sent...")
