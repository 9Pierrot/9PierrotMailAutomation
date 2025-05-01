import os



# 2. Configuration SMTP (exemple avec Gmail)
smtp_server = 'smtp.office365.com' # 'smtp.gmail.com' pour un compte Gmail
smtp_port = 587
email_address = 'kodjopierre_atadegnon@reseau.eseo.fr'
email_password = 'K_P_9_reseaueseo'  # Utiliser un mot de passe d'application si possible


# configuration of the file path
BASE_PATH = os.path.dirname(__file__)
EXCEL_PATH = os.path.join(BASE_PATH, "../tabs/ClasseurTest.xlsx")
ATTACHMENT_FOLDER = os.path.join(BASE_PATH, "../attachments/")  # dossier contenant les pièces jointes



USE_ATTACHMENT = True  # True pour envoyer avec pièce jointe, False sinon

MESSAGE_CORPS = """
Ceci est un message automatique envoyé depuis un script Python pour automatiser l'envoie de mails.

C'est un test.
"""

SIGNATURE = """
Pierre Kodjo ATADEGNON
Etudiant en première année du cycle ingénieur à l'ESEO
+33 6 84 03 34 70
"""

