"""This file contains the configuration settings for the MailAutomation application.
It defines the SMTP server, port, email address, and password for the sender's email.
It also specifies the base path, Excel file path, attachment folder path, and whether to use attachments.
The message body and signature are also defined in this file.
Please make sure to replace the placeholder values with the actual values before using this file."""


import os

smtp_server = 'smtp.office365.com' # SMTP server : use 'smtp.office365.com' for Office 365, 'smtp.gmail.com' for Gmail  !!!
smtp_port = 587
email_address = 'put your email here'  # sender email address 
email_password = 'put your password here'  # sender email password


BASE_PATH = os.path.dirname(__file__)
EXCEL_PATH = os.path.join(BASE_PATH, "../tabs/ClasseurTest.xlsx")  # path to the Excel file
ATTACHMENT_FOLDER = os.path.join(BASE_PATH, "../attachments/")          # path to the folder containing the attachments



USE_ATTACHMENT = False  # True to use attachments, False to not use them


OBJECT = "Put here the message subject"  # subject of the email

# message to be sent
MESSAGE_CORPS = """
paste your message here
"""

SIGNATURE = """paste your signature here
"""

