import pandas as pd
import smtplib
from email.message import EmailMessage

from setup import *
from attach import loadfile


# variables pour le nombre d'emails envoyés
emails_sent = 0

# 1. Lire le fichier Excel
df = pd.read_excel(EXCEL_PATH)

# 3. Connexion au serveur SMTP
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(email_address, email_password)

    for index, row in df.iterrows():
        civilite = row['Civilité']
        nom = row['Nom']
        # titre = row['Titre']
        to_email = row['Email']

        # Création du message
        msg = EmailMessage()
        msg['Subject'] = f"Bonjour {nom}, un message pour vous : Test 10"
        msg['From'] = email_address
        msg['To'] = to_email
        msg.set_content(f"""\
Bonjour {civilite} {nom},
{MESSAGE_CORPS}
{SIGNATURE}""")

        # Ajout de la pièce jointe
        if (USE_ATTACHMENT):
            for filename in os.listdir(ATTACHMENT_FOLDER):
                file_path = os.path.join(ATTACHMENT_FOLDER, filename)
                # Vérification de l'existence du fichier
                if os.path.exists(file_path):
                    # Ajout de la pièce jointe
                    msg.add_attachment(loadfile(file_path).get("data"), maintype=loadfile(file_path).get("maintype"), 
                            subtype=loadfile(file_path).get("subtype"), filename=filename)
                    print(f"Pièce jointe ajoutée : {filename}")
                    
            
        emails_sent += 1
        # Envoi du mail
        smtp.send_message(msg)
        print(f"{emails_sent}. Email envoyé à {nom} ({to_email})")
        

print(f"✅ {emails_sent} emails envoyés avec succès !")