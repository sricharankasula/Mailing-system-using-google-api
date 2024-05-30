from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from base64 import urlsafe_b64encode
import os
#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
# OAuth 2.0 setup
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
creds = None
if os.path.exists('token.json'):
    creds = flow.credentials
else:
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

# Gmail API setup
service = build('gmail', 'v1', credentials=creds)

# List of recipient email addresses
recipient_emails = []#add recipients' addressess
a=0
# Create a MIMEText object for the email content
for recipient_email in recipient_emails:
    message = MIMEText("Add your message hear")
    message['to'] =  recipient_email # Join the recipient emails with commas
    message['subject'] = 'HI-PLEX 2023'

# Send the email
    raw_message = urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    message = {'raw': raw_message}
    service.users().messages().send(userId='me', body=message).execute()
    print('Email sent successfully!')
    a=a+1
    print(a)
