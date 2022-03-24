from email.mime import image
from fileinput import filename
import smtplib
from email.message import EmailMessage   

class MailHandler:
    
    def __init__(self, host_email, host_passwd, server, port):
        self.email = host_email
        self.passwd = host_passwd
        self.server = server
        self.port = port
        self.smtp = smtplib.SMTP(server, port)
        self.attachment_path = None
        
    def setAttachPath(self, path):
        self.attachment_path = path
        
    def login(self):
        emailaddr = self.email
        passwd = self.passwd
        smtp = self.smtp
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        try:
            smtp.login(emailaddr, passwd)
            print('login successful')
        except:
            smtplib.SMTPAuthenticationError
            print('Authentication failed.')
            
    def closeConnection(self):
        smtp = self.smtp
        smtp.quit()
        print('Connection closed')
        
    def send(self, subject, body, recipient):
        smtp = self.smtp
        mail_subject = subject
        mail_body = body
        mail_recipient = recipient
        mail_sender = self.email
        mail_attachment_path = self.attachment_path
        envelope = EmailMessage()
        
        if mail_attachment_path != None:
            envelope['From'] = mail_sender
            envelope['To'] = mail_recipient
            envelope['Subject'] = mail_subject
            envelope.set_content(mail_body)
            
            with open(mail_attachment_path, 'rb') as picture:
                image_data = picture.read()
                envelope.add_attachment(image_data, maintype='image', subtype='jpg', filename='meme.jpg')
                picture.close()
        else:
            envelope['From'] = mail_sender
            envelope['To'] = mail_recipient
            envelope['Subject'] = mail_subject
            envelope.set_content(mail_body)
        
        try:
            smtp.send_message(envelope)
            print('Mail sent succesfully.')
        except (smtplib.SMTPException, smtplib.SMTPRecipientsRefused) as error:
            print('Unable to send mail.')
            print(error)