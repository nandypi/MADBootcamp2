import smtplib
from email.mime.text import MIMEText

SMTP_HOST = "localhost"
SMTP_PORT = 1025

FROM = "mad2backend@gmail.com"


def send_email(to, subject, html_body):
    msg = MIMEText(html_body, "html")
    msg["Subject"] = subject
    msg["From"] = FROM
    msg["To"] = to

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.sendmail(FROM, [to], msg.as_string())


if __name__ == "__main__":

    html_body = """
<h1>Welcome to the Demo!</h1>
<p>We are excited to have you on board. Explore the features and enjoy your experience!</
    """

    send_email(
        "testUser@gmail.com",
        "✨ Welcome to the Demo!",
        html_body,
    )