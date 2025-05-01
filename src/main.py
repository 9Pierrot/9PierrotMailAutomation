import pandas as pd
import smtplib
from email.message import EmailMessage

# 1. Lire le fichier Excel
df = pd.read_excel("contacts.xlsx")

# 2. Configuration SMTP (exemple avec Gmail)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_address = 'ton.email@gmail.com'
email_password = 'ton_mot_de_passe'  # Utilise un mot de passe d'application

# 3. Connexion au serveur SMTP
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(email_address, email_password)

    for index, row in df.iterrows():
        nom = row['Nom']
        titre = row['Titre']
        to_email = row['Email']

        # Création du message
        msg = EmailMessage()
        msg['Subject'] = f"Bonjour {nom}, un message pour vous"
        msg['From'] = email_address
        msg['To'] = to_email
        msg.set_content(f"""\
Bonjour {nom},

Je vous écris en tant que {titre}. Ceci est un mail envoyé automatiquement via Python !

Bien cordialement,
[TON NOM]
        """)

        # Envoi du mail
        smtp.send_message(msg)
        print(f"Email envoyé à {nom} ({to_email})")