# Importar as bibliotecas:
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Gera e-mail
mail = MIMEMultipart()

# Corpo do e-mail
payload = """Olá! Tudo bem?

Este é um e-mail automático para testar o disparo de e-mail ensinado pelo curso de RPA Python!

Atenciosamente,

RPA Pythonico
"""

# Remetente do e-mail
mail['From'] = 'email_remetente@provedor.com'

# UM destinatário
mail['To'] = 'email_destinatario@provedor.com'

# MAIS DE UM destinatário
mail['To'] = 'email_destinatario@provedor.com, email_destinatario@provedor.com'

# Assunto do e-mail
mail['Subject'] = 'Email Automático - SMTPLIB'

# Anexa o CORPO (payload) do e-mail
mail.attach(MIMEText(payload, 'plain'))

# Abre conexão com SMTP
server = smtplib.SMTP('smtp.gmail.com', '587')
server.starttls()

# Se autentica na conexão SMTP
server.login(mail['From'], 'sua_senha')

# Colocar anexo
# file = open('seu_arquivo.py', 'rb')

# app = MIMEApplication(file.read(), 'py')
# app.add_header('Content-Disposition', 'attachment;filename=seu_arquivo.py')
# mail.attach(app)

# Envia e-mail
server.sendmail(mail['From'], mail['To'], mail.as_string())

# Encerra conexão SMTP
server.quit()