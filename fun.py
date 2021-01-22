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

import Draw

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


error_list = []
error_count = 0

def make_sertifyMe(id, sp1, sp2, xfile, doemail):
    data = pd.read_excel(xfile) 
    # name_list = data["Name"].tolist() 
    # email_list = data["Email"].tolist()
  
    # Make certificate and check if it was successful
    if id == '03':
        for i in data.iloc:
            filename = Draw.Certi03(i[0] , sp1, sp2 )
            if doemail:
                EmailDo(filename)

    elif id == '04':
        for i in data.iloc:
            filename = Draw.Certi04(i[0] , sp1, sp2 )
            if doemail:
                EmailDo(filename)

    elif id == '05':
        for i in data.iloc:
            filename = Draw.Certi05(i[0] , sp1, sp2 )
            if doemail:
                EmailDo(filename)

    elif id == '06':
        for i in data.iloc:
            filename = Draw.Certi06(i[0] , sp1, sp2 )
            if doemail:
                EmailDo(filename)               

    elif id == '07':
        for i in data.iloc:
            filename = Draw.Certi07(i[0] , sp1, sp2 )
            if doemail:
                EmailDo(filename)

    elif id == '08':
        for i in data.iloc:
            filename = Draw.Certi08(i[0] , sp1, sp2 )
            if doemail:
                EmailDo(filename)

def EmailDo(file_name):
    # Successfully made certificate
    if file_name != -1:
        email_certi( file_name, i[1] )
        print("Sent to " + i[0])
    # Add to error list
    else:
        error_list.append(i[0] )
        error_count += 1

    # Print all failed IDs
    print(str(error_count) + " Errors- List:" + ','.join(error_list))