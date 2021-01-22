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

def make_certi(serti, new_name):
    if not os.path.exists( 'Certificates' ):
        os.makedirs( 'Certificates' )

    # Save as a PDF
    serti.save( 'Certificates\\'+str(new_name)+'.pdf', "PDF", resolution=100.0)
    return 'Certificates\\'+str(new_name)+'.pdf'  

## temp 3
def Certi03( new_name , sp1 , sp2):
    serti = Image.open('Temp/certificate03.jpg')
    draw = ImageDraw.Draw(serti)

    # Load font
    font = ImageFont.truetype('Fonts/CaveatBrush-Regular.ttf', 60)

    # Check sizes and if it is needed to be shortened
    if ( len( new_name ) > 20 ):
        new_name = shorten( new_name, 20 )
 
    # Insert text into image template for name
    location = (320, 360)
    text_color = (255, 255, 255)
    draw.text(location, new_name, fill = text_color, font = font)

    # font for speaker 1
    font_s1 = ImageFont.truetype('Fonts/CourierPrime-Regular.ttf', 20)
    speaker_name1 = sp1

    # Insert text into image template for speaker
    location_s1 = (160, 650) # need to edit
    text_color_s1 = (225, 180, 87)
    draw.text(location_s1, speaker_name1, fill = text_color_s1, font = font_s1)    
    
    # font for speaker 2
    font_s = ImageFont.truetype('Fonts/CourierPrime-Regular.ttf', 20)
    speaker_name = sp2

    # Insert text into image template for speaker
    location_s = (690, 650) # need to edit
    text_color_s = (225, 180, 87)
    draw.text(location_s, speaker_name, fill = text_color_s, font = font_s)

    make_certi(serti , new_name)

## temp 4
def Certi04( new_name , sp1 , sp2):
    serti = Image.open('Temp/certificate04.jpg')
    draw = ImageDraw.Draw(serti)
    # Load font
    font = ImageFont.truetype('Fonts/CaveatBrush-Regular.ttf', 60)

    # Check sizes and if it is needed to be shortened
    if ( len( new_name ) > 20 ):
        new_name = shorten( new_name, 20 )
 
    # Insert text into image template for name
    location = (320, 340)
    text_color = (255, 255, 255)
    draw.text(location, new_name, fill = text_color, font = font)

    # font for speaker 1
    font_s1 = ImageFont.truetype('Fonts/CourierPrime-Regular.ttf', 20)
    speaker_name1 = sp1

    # Insert text into image template for speaker
    location_s1 = (200, 635) # need to edit
    text_color_s1 = (225, 180, 87)
    draw.text(location_s1, speaker_name1, fill = text_color_s1, font = font_s1)    
    
    # font for speaker 2
    font_s = ImageFont.truetype('Fonts/CourierPrime-Regular.ttf', 20)
    speaker_name = sp2

    # Insert text into image template for speaker
    location_s = (630, 635) # need to edit
    text_color_s = (225, 180, 87)
    draw.text(location_s, speaker_name, fill = text_color_s, font = font_s)

    make_certi(serti , new_name)

## temp 5
def Certi05( new_name , sp1 , sp2):
    serti = Image.open('Temp/certificate05.jpg')
    draw = ImageDraw.Draw(serti)

    # Load font
    font = ImageFont.truetype('Fonts/CaveatBrush-Regular.ttf', 60)

    # Check sizes and if it is needed to be shortened
    if ( len( new_name ) > 20 ):
        new_name = shorten( new_name, 20 )
        
    # Insert text into image template for name
    location = (300, 350)
    text_color = (239, 108, 70)
    draw.text(location, new_name, fill = text_color, font = font)

    # font for speaker 1
    font_s1 = ImageFont.truetype('Fonts/CourierPrime-Bold.ttf', 20)
    speaker_name1 = sp1

    # Insert text into image template for speaker
    location_s1 = (300, 670) # need to edit
    text_color_s1 = (239, 108, 70)
    draw.text(location_s1, speaker_name1, fill = text_color_s1, font = font_s1)    
    
    # font for speaker 2
    font_s = ImageFont.truetype('Fonts/CourierPrime-Bold.ttf', 20)
    speaker_name = sp2

    # Insert text into image template for speaker
    location_s = (670, 670) # need to edit
    text_color_s = (239, 108, 70)
    draw.text(location_s, speaker_name, fill = text_color_s, font = font_s)

    make_certi(serti , new_name)

## temp 6
def Certi06( new_name , sp1 , sp2):
    serti = Image.open('Temp/certificate06.jpg')
    draw = ImageDraw.Draw(serti)

    # Load font
    font = ImageFont.truetype('Fonts/CaveatBrush-Regular.ttf', 60)

    # Check sizes and if it is needed to be shortened
    if ( len( new_name ) > 20 ):
        new_name = shorten( new_name, 20 )
 
    # Insert text into image template for name
    location = (320, 360)
    text_color = (225, 180, 87)
    draw.text(location, new_name, fill = text_color, font = font)

    # font for speaker 1
    font_s1 = ImageFont.truetype('Fonts/CourierPrime-Regular.ttf', 20)
    speaker_name1 = sp1

    # Insert text into image template for speaker
    location_s1 = (235, 650) # need to edit
    text_color_s1 = (255, 255, 255)
    draw.text(location_s1, speaker_name1, fill = text_color_s1, font = font_s1)    
    
    # font for speaker 2
    font_s = ImageFont.truetype('Fonts/CourierPrime-Regular.ttf', 20)
    speaker_name = sp2

    # Insert text into image template for speaker
    location_s = (610, 650) # need to edit
    text_color_s = (255, 255, 255)
    draw.text(location_s, speaker_name, fill = text_color_s, font = font_s)

    make_certi(serti , new_name)


## temp 7
def Certi07( new_name , sp1 , sp2):
    serti = Image.open('Temp/certificate07.jpg')
    draw = ImageDraw.Draw(serti)

    # Load font
    font = ImageFont.truetype('Fonts/Lato-Bold.ttf', 68)

    # Check sizes and if it is needed to be shortened
    if ( len( new_name ) > 20 ):
        new_name = shorten( new_name, 20 )
        
    # Insert text into image template for name
    location = (375, 330)
    text_color = (240, 78, 63)
    draw.text(location, new_name, fill = text_color, font = font)

    # font for speaker 1
    font_s1 = ImageFont.truetype('Fonts/CourierPrime-Bold.ttf', 20)
    speaker_name1 = sp1

    # Insert text into image template for speaker
    location_s1 = (390, 670) # need to edit
    text_color_s1 = (240, 78, 63)
    draw.text(location_s1, speaker_name1, fill = text_color_s1, font = font_s1)    

    make_certi(serti , new_name)


## temp 8
def Certi08( new_name , sp1 , sp2):
    serti = Image.open('Temp/certificate08.jpg')
    draw = ImageDraw.Draw(serti)

    # Load font
    font = ImageFont.truetype('Fonts/CaveatBrush-Regular.ttf', 64)

    # Check sizes and if it is needed to be shortened
    if ( len( new_name ) > 20 ):
        new_name = shorten( new_name, 20 )
        
    # Insert text into image template for name
    location = (310, 340)
    text_color = (132, 204, 225)
    draw.text(location, new_name, fill = text_color, font = font)

    # font for speaker 1
    font_s1 = ImageFont.truetype('Fonts/CourierPrime-Regular.ttf', 20)
    speaker_name1 = sp1

    # Insert text into image template for speaker
    location_s1 = (235, 600) # need to edit
    text_color_s1 = (255, 202, 98)
    draw.text(location_s1, speaker_name1, fill = text_color_s1, font = font_s1)    
    
    # font for speaker 2
    font_s = ImageFont.truetype('Fonts/CourierPrime-Regular.ttf', 20)
    speaker_name = sp2

    # Insert text into image template for speaker
    location_s = (610, 600) # need to edit
    text_color_s = (255, 202, 98)
    draw.text(location_s, speaker_name, fill = text_color_s, font = font_s)

    make_certi(serti , new_name)
