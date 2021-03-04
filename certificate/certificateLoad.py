from datetime import datetime
from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np
import os
import sqlite3
from Dashboard.models import GotCertificate
from django.core.files.base import ContentFile
import csv

def doIHaveCertificate(id, name):
    entries = os.listdir('./certificate/output/')
    for i in entries:
        if i == str(id) + '. ' + str(name) + '.png':
            print('Found')
            return False
            exit()
    print('Not Found')
    return True

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def loadCertificate(username, Name, pkey):
    print('Username')
    print(pkey)
    flag = True

    date = datetime.today().strftime('%Y-%m-%d')

    name_to_print = Name
    date_to_print = date  # Change this date as per requirement

    # Load image in OpenCV
    image = cv2.imread("./certificate/org_Certificate.png")

    # Convert the image to RGB (OpenCV uses BGR)
    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Pass the image to PIL
    pil_im = Image.fromarray(cv2_im_rgb)

    draw = ImageDraw.Draw(pil_im)
    # use a truetype font
    font = ImageFont.truetype("./certificate/fonts/MLSJN.TTF", 35)  # You can change fonts from list given bottom
    font1 = ImageFont.truetype("./certificate/fonts/Lato-Black.TTF", 12)

    # Draw the text
    draw.text((int(181), int(122)), name_to_print, font=font, fill='red')
    draw.text((int(181), int(310)), date_to_print, font=font1, fill='red')

    # Get back the image to OpenCV
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    if flag:
            cv2.imshow('Certificate', cv2_im_processed)  # Shows sample image
            flag = False
    path = ''
    cv2.imwrite('./certificate/output/' + str(pkey) + '. ' + str(Name) + '.png', cv2_im_processed)


    cv2.imwrite('./media/certificate/' + str(pkey) + '. ' + str(Name) + '.png', cv2_im_processed)

    # os.startfile('output.png')
    #cv2.waitKey(0)

    cv2.destroyAllWindows()



    file_path = os.path.join('certificate/' + str(pkey) + '. ' + str(Name) + '.png')



    saveCertificate = GotCertificate(User= username, Fullname = Name, image=file_path, Date= date)
    saveCertificate.save()

    '''
    Other vareity of FONTS (Make sure you give proper path)

    MLSJN.TTF
    Lato-Black.ttf
    MATURASC.TTF
    OLDENGL.TTF
    VIVALDII.TTF
    copperplate gothic font.ttf


    '''



