import smtplib
from email.message import EmailMessage
import sys
import os
import html
from dotenv import load_dotenv

load_dotenv("SMTP.env")

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
USERNAME = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_APP_PASS")
 
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: python3 {sys.argv[0]} <EMAIL> <SUBJECT> <MESSAGE>")
        sys.exit(0)
 
    email = sys.argv[1]
    subject = sys.argv[2]
    message = sys.argv[3]

    # Escape the message to use in HTML template
    safe_message = html.escape(message) 

    # HTML template to be changed to fit needs
    # "{safe_message}" is where the text from the command line will go
    html_template = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color: #333;">
        <div style="border:1px solid #ccc; padding:20px; border-radius:10px; background:#f9f9f9;">
          <h2 style="color:#2b6cb0;">New Message Received</h2>
          <p>{safe_message}</p>
          <hr>
          <p style="font-size:0.9em;color:#888;">This email was sent via Python.</p>
        </div>
      </body>
    </html>
    """

    msg = EmailMessage()
    msg["From"] = USERNAME
    msg["To"] = email
    msg["Subject"] = subject
    msg.set_content(message)
    msg.add_alternative(html_template, subtype="html")
 
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.login(USERNAME, PASSWORD)
        smtp.send_message(msg)
