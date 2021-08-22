# This file is only for testing purpose.
# Use this to check if server is able to authenticate and send email.
# Add email id (TO and FROM) and password before executing.
# server has to be changed in case you are not using Gmail.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our HTML email"""

    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """
Your mail reader does not support the report format.
Please visit us online!"""

    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)

    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)

    # Credentials (if needed) for sending the mail
    password = "Password"

    server.starttls()
    server.login(FROM,password)
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()

if __name__ == "__main__":
    """Executes if the script is run as main script (for testing purposes)"""

    email_content = """

<!DOCTYPE html>
<html>
    <body>
        <div style="background-color:#eee;padding:10px 20px;">
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">My newsletter</h2>
        </div>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px">
                <img src="https://dummyimage.com/500x300/000/fff&text=Dummy+image" style="height: 300px;">
                <div style="text-align:center;">
                    <h3>Article 1</h3>
                    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. A ducimus deleniti nemo quibusdam iste sint!</p>
                    <a href="#">Read more</a>
                </div>
            </div>
        </div>
    </body>
</html>

"""

    TO = 'senderemail@gmail.com'
    FROM ='receiveremail@gmail.com'

    py_mail("Test email subject", email_content, TO, FROM)
