import pandas as pd
import xlrd
import os.path
import smtplib
import email, smtplib, ssl
from email import encoders
from PIL import Image, ImageDraw, ImageFont
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

# Meant to convert full names to abbreviations
def shorten( text, _max ):
    t = text.split(" ")
    text = ''
    if len(t)>1:
        for i in t[:-1]:
            text += i[0] + '.'
    text += ' ' + t[-1]
    if len(text) < _max :
        return text
    else :
        return -1


# Add name
def make_certi( new_name ):

    #load template
    serti = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(serti)

    # Load font
    font = ImageFont.truetype('Fonts/CaveatBrush-Regular.ttf', 60)

    # Check sizes and if it is needed to be shortened
    if ( len( new_name ) > 20 ):
        new_name = shorten( new_name, 20 )

    # Insert text into image template
    location = (700, 345)
    text_color = (0, 137, 209)
    draw.text(location, new_name, fill = text_color, font = font)

    if not os.path.exists( 'certificates' ):
        os.makedirs( 'certificates' )

    # Save as a PDF
    serti.save( 'certificates\\'+str(new_name)+'.pdf', "PDF", resolution=100.0)
    return 'certificates\\'+str(new_name)+'.pdf'  

# Email the certificate as an attachment
def email_certi( filename, receiver ):
    username = '' # your e-mail id eg 'dscpsit'
    password = '' # your password eg 'raghav.psit123#'
    sender = username + '@gmail.com'

    msg = MIMEMultipart()
    msg['Subject'] = 'SertifyMe certificate'
    msg['From'] = username+'@gmail.com'
    # msg['Reply-to'] = username +'@gmail.com'
    msg['To'] = receiver

    # That is what u see if dont have an email reader:
    msg.preamble = 'Multipart massage.\n'
    
    # Body
    msg.attach(MIMEText( "Hello,\n\nPlease find attached your SertifyME certificate.\n\nGreetings." , "plain"))

    # Attachment
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)

    part.add_header("Content-Disposition",f"attachment; filename= {filename}",)
    msg.attach(part)
    text = msg.as_string()

    # Login and sending e-mail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, text)

data = pd.read_excel('names.xlsx') 
# name_list = data["Name"].tolist() 
# email_list = data["Email"].tolist()
error_list = []
error_count = 0

for i in data.iloc:
    # Make certificate and check if it was successful
    filename = make_certi(i[0])
        
    # Successfully made certificate
    if filename != -1:
        email_certi( filename, i[1] )
        print("Sent to " + i[0])
    # Add to error list
    else:
        error_list.append(i[0])
        error_count += 1

    # Print all failed IDs
    print(str(error_count) + " Errors- List:" + ','.join(error_list))
