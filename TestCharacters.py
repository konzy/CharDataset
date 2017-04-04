# -*- coding: utf-8 -*-

# ------------------------------------ Imports ----------------------------------#

# Import python imaging libs
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont, ImageOps, ImageFilter

from itertools import chain
import sys

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

# Import operating system lib
import os
import unicodedata
import shutil
# Import random generator
from random import randint
import random

# ---------------------------------- Input and Output ---------------------------#

# Directory containing fonts
out_dir = './char'

# Output
font_dir = './fonts'

# ------------------------------------ Characters -------------------------------#

oriya = ['0x0b01', '0x0b77']
sinhala = ['0x0d90', '0x0ddf']
korean = ['0xac00', '0xd7af']
english = ['0x0030', '0x0039', '0x0041', '0x004e', '0x004e', '0x005b', '0x0061', '0x007a']
kannada = ['0x0C80', '0x0C81', '0x0C91', '0x0C92', '0x0C9f', '0x0CFF']


# -------------------------------------- Sizes ----------------------------------#

# Character sizes
font_sizes = (48, 52, 56, 64)

# Image size
image_size = 256

# Images per font file
num_images = 10

# Colors, gray on white (the fill for fonts are messed up)
font_color = 120
background_color = 255
# ------------------------------------ Cleanup ----------------------------------#

# def Cleanup():
#     shutil.rmtree(out_dir)
#     os.mkdir(out_dir)
#     return

# ------------------------------ Generate Characters ----------------------------#


def generate_characters(char_start, char_end, font_folder, destination_folder):
    # Process the font files
    for dir_name, dir_names, file_names in os.walk(font_dir + "/" + font_folder + "/"):
        # For each font do
        for filename in file_names:
            # Get font full file path
            font_resource_file = os.path.join(dir_name, filename)

            # For each character do
            for char_int in range(int(char_start, 16), int(char_end, 16)):
                # for char in characters:
                # For each font size do
                # ttf = TTFont(charInt, 0, verbose=0, allowVID=0, ignoreDecompileErrors=True, fontNumber=-1)
                # chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()]
                # for x in ttf["cmap"].tables)
                #
                # char = int(sys.argv[2], 0)
                # # print(Unicode[char])
                # # print(char in (x[0] for x in chars))
                #
                # if char in (x[0] for x in chars):
                for i in range(0, num_images):
                    font_size = randint(image_size / 5, image_size / 3)
                    valid_unicode = True
                    character = unichr(char_int)
                    try:
                        unicodedata.name(character)
                    except ValueError:
                        valid_unicode = False

                    if valid_unicode:
                        draw_character(character, font_resource_file, font_size, filename,
                                       font_folder, destination_folder)

    print destination_folder + "/" + font_folder + " is finished."
    return


def draw_character(char, font_resource_file, font_size, filename, font_folder, destination_folder):
    if type(char) is int:
        character = unichr(char)
    else:
        character = char
    # Convert the character into unicode
    # background_color = randint(0, 255)

    # Create character image :
    # Grayscale, image size, background color
    char_image = Image.new('L', (image_size, image_size), background_color)
    # Specify font : Resource file, font size
    font = ImageFont.truetype(font_resource_file, font_size)

    # Get character width and height
    (font_width, font_height) = font.getsize(character)

    # Draw text : Position, String,
    # Options = Fill color, Font

    img2 = Image.new('L', (font_width, font_height), background_color)
    draw2 = ImageDraw.Draw(img2)
    # font_color = (background_color + randint(50, 100)) % 255

    draw2.text((0, 0), character, fill=font_color, font=font)
    w = img2.rotate(randint(-25, 25), expand=1)
    width, height = w.size

    # Calculate x position
    x = randint(0, image_size - width - 10)
    # Calculate y position
    y = randint(0, image_size - height - 10)

    # Final file name
    file_name = out_dir + "/" + destination_folder + "/" + font_folder + "/" + character + '_' + \
        filename + '_fs_' + \
        str(font_size) + '_bc_' + \
        str(background_color) + '_fc_' + str(font_color) + '.png'

    # Save image
    char_image.paste(w, (x, y), w)
    char_image.save(file_name)
    # Print character file name
    # print file_name

    # to create the mishmash of two languages


def copy_files(source, destination_1, destination_2):
    for filename in os.listdir(source):
        if random.random() < 0.5:
            shutil.copy(source + "/" + filename, destination_1)
        else:
            shutil.copy(source + "/" + filename, destination_2)

# -------------------------------------- Main -----------------------------------#

# Do cleanup
# Cleanup()


# Generate characters
random.seed(21215)
generate_characters(english[2], english[3], "english", "test")
generate_characters(english[4], english[5], "english", "validation")
# generate_characters(kannada[1], kannada[2], "kannada", "test")
# generate_characters(kannada[3], kannada[4], "kannada", "validation")


__author__ = 'hensleyl4'
