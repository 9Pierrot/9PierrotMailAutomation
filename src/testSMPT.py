import smtplib

smtp_server = 'smtp.office365.com'  
smtp_port = 587
email_address = 'kodjopierre_atadegnon@reseau.eseo.fr'
email_password = 'K_P_9_reseaueseo'

try:
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(email_address, email_password)
        print("✅ Connexion réussie au serveur SMTP !")
except Exception as e:
    print("❌ Erreur de connexion :", e)