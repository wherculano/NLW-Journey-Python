import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_addrs, body):
    from_addr = "diaj5qamnls7pxe2@ethereal.email"
    login = "diaj5qamnls7pxe2@ethereal.email"
    password = "x6qQ8VAG9dKyHrzFXP"

    msg = MIMEMultipart()
    msg["from"] = "example@email.com"
    msg["to"] = ", ".join(to_addrs)

    msg["Subject"] = "Trip Confirmation!"
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()
