# Neste SCRIPT utilizei a forma de SSL para autenticação.
# Importanto biblioteca do SMTP!
import smtplib
arq = open('arquivo.txt', 'r')
texto = arq.read()
smtp = smtplib.SMTP("smtp.gmail.com:465")
# EXEMPLO smtp = smtplib.SMTP_SSL("smtp.gmail.com:465")
smtp.starttls()
smtp.login("email_legal@gmail.com", "senhamaneira")
# EXEMPLO smtp.login("email_legal@gmail.com", "senhamaneira")

remetente = "email_legal@gmail.com"
# EXEMPLO remetente = "email_legal@gmail.com"
destinatario = ["amigo_legal@hotmail.com"]
# EXEMPLO destinatario = ["amigo_legal@hotmail.com"]
# OBS: Vale lembrar que o destinatario obrigatoriamente deve ficar dentro de uma lista []
conteudo =  """From: %s
To: %s
Subject: ASSUNTO

Conteudo %s.""" % (remetente, destinatario, texto)
# OBS: NA mensagem recomendo que vocẽ crie o cabeçalho de email, para evitar problemas

smtp.sendmail(remetente, destinatario, conteudo)

smtp.quit
