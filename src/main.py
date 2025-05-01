import pandas as pd
import smtplib
from email.message import EmailMessage

# 1. Lire le fichier Excel
df = pd.read_excel("../tabs/test.xlsx")

# 2. Configuration SMTP (exemple avec Gmail)
smtp_server = 'smtp.office365.com' # 'smtp.gmail.com' pour un compte Gmail
smtp_port = 587
email_address = 'kodjopierre_atadegnon@reseau.eseo.fr'
email_password = 'K_P_9_reseaueseo'  # Utiliser un mot de passe d'application si possible

# 3. Connexion au serveur SMTP
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(email_address, email_password)

    for index, row in df.iterrows():
        nom = row['Nom']
        # titre = row['Titre']
        to_email = row['Email']

        # Création du message
        msg = EmailMessage()
        msg['Subject'] = f"Bonjour {nom}, un message pour vous"
        msg['From'] = email_address
        msg['To'] = to_email
        msg.set_content(f"""\
Bonjour {nom},

Ceci est un message automatique envoyé depuis un script Python.

[Pierre Atadegnon]
        """)

        # Envoi du mail
        smtp.send_message(msg)
        print(f"Email envoyé à {nom} ({to_email})")