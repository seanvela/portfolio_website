import smtplib, ssl

def send_email(message):

# Basic setup to connect gmail to webpage

    host = "smtp.gmail.com"
    port = 465

    username = "seanvela7@gmail.com"
    password = "tgbzcgpwosmmqjdl"

    receiver = "seanvela7@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

