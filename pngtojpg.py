#importing required packages and library
import os
import sys
from PIL import Image


# Loading .png image
# png_img = Image.open('./images/0.png').convert("RGB")

# # converting to jpg file
# #saving the jpg file
# png_img.save('./images/MyConvertedImage.jpg', 'jpeg')

os.chdir("./images")
def jpg_to_png():
    # os.chdir("./images")
    jpg_images = [image for image in os.listdir() if image.endswith('.jpg')]
    for jpg_image in jpg_images:
        try:
            new_name = jpg_image.split('.')[0] + '.png'
            Image.open(jpg_image).save(new_name, "png")
        except IOError as error:
            print('Couldn\'t read {} '.format(jpg_image))
    return print('выполнено')

def png_to_jpg():
    # os.chdir("./images")
    png_images = [image for image in os.listdir() if image.endswith('.png')]
    for png_image in png_images:
        try:
            new_name = png_image.split('.')[0] + '.jpg'
            Image.open(png_image).convert("RGB").save(new_name, "jpeg")
        except IOError as error:
            print('Couldn\'t read {} '.format(png_image))
    return print('выполнено')

def webp_to_png():
    # os.chdir("./images")
    webp_images = [image for image in os.listdir() if image.endswith('.webp')]
    for webp_image in webp_images:
        try:
            new_name = webp_image.split('.')[0] + '.png'
            Image.open(webp_image).save(new_name, "png")
        except IOError as error:
            print('Couldn\'t read {} '.format(webp_image))
    return print('выполнено')

convert = input("введите 1 или 2 \n1)jpg_to_png\n2)png_to_jpg\n3)webp_to_png\n")
if convert == '1':
    jpg_to_png()
if convert == '2':
    png_to_jpg()
if convert == '3':
    webp_to_png()
