"""
This file is the main script for sending automated emails using data from an Excel file.
The script performs the following steps:
1. Reads the Excel file specified by the `EXCEL_PATH` variable.
2. Connects to the SMTP server using the provided credentials.
3. Iterates over each row in the Excel file and retrieves the necessary data.
4. Creates an email message with the subject, sender, recipient, and content.
5. Optionally adds attachments to the email.
6. Sends the email using the SMTP server.
7. Prints the status of each sent email.
8. Prints the total number of successfully sent emails.
Note: The script requires the `setup` and `attach` modules to be imported, which contain necessary configurations and functions.

Author: 9Pierrot
Date: 01/05/2025
"""

import pandas as pd


import smtplib
from email.message import EmailMessage

from setup import *
from attach import loadfile


# variable for the number of emails sent
emails_sent = 0

# read the Excel file
df = pd.read_excel(EXCEL_PATH)

# connect to the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(email_address, email_password)

    for index, row in df.iterrows():
        # declare here the variables getting the data from the Excel file
        # example for a table with the columns : Civilité, Nom, Email
        # | Civility  | Name  | Email  |
        # |-----------|-------|--------|
        # |    Ms.    |  Jane | email1 |
        # |    Mr.    |  Tom  | email2 |
        # |    ...    |  ...  |  ...   |
        # we will have to declare the variables as follows :

        to_civility = row['Civility']
        to_name = row['Name']
        to_email = row['Email']

        # create the email message
        msg = EmailMessage()
        msg['Subject'] = OBJECT
        msg['From'] = email_address
        msg['To'] = to_email
        msg.set_content(f"""
Hello {to_civility} {to_name},
{MESSAGE_CORPS}
{SIGNATURE}""")

        # add of the attachments
        if (USE_ATTACHMENT):
            for filename in os.listdir(ATTACHMENT_FOLDER):
                file_path = os.path.join(ATTACHMENT_FOLDER, filename)
                # verify if the file is a file and not a directory
                if os.path.exists(file_path):
                    # load the file to attach
                    data = loadfile(file_path)
                    msg.add_attachment(data.get("data"), data.get("maintype"), 
                            subtype=data.get("subtype"), filename=filename)
                    print(f"File added : {filename}")
                    
            
        emails_sent += 1
        # send the email
        smtp.send_message(msg)
        print(f"{emails_sent}. Mails sent {to_name} ({to_email})")
        

print(f"✅ {emails_sent} mails sent successfully !")