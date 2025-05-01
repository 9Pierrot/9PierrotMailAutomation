"""
This file contains a script for testing SMTP (Simple Mail Transfer Protocol) connection using the smtplib module.
It imports the necessary modules and variables from the 'setup' module.
The script attempts to establish a connection with the SMTP server, perform a secure connection using starttls(), and login using the provided email address and password.
If the connection is successful, it prints a success message. Otherwise, it prints an error message with the exception details.
"""

import smtplib
from setup import *

try:
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(email_address, email_password)
        print("✅ Connexion réussie au serveur SMTP !")
except Exception as e:
    print("❌ Erreur de connexion :", e)