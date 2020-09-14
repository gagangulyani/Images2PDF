"""
==============
Name: Images2PDF

==============
Description:

This Python script Creates PDF file from List of Images using Pillow.

This script can come very handy if you have a lot of images and you want
to add them to a PDF file without using other apps which are usually full
of advertisements and background services and sometimes can be malicious or
spywares.

==============
Link to Repo:
https://github.com/gagangulyani/Images2PDF

==============
Author: @GaganGulyani
"""


from PIL import Image
from pathlib import Path
from sys import argv


def to_rgb(img):
    """This function converts and Returns Image Objects with RGBA to RGB
    It does not change the size (width and height) of the Image Object

    Args:
        img (Image Object): With RGBA or RGB channel

    Returns:
        Image Object: With RGB channels only
    """

    # If Image does not have Alha Channel
    if len(img.split()) != 4:
        # Return it without doing anything
        return img

    # Create New Image Object with White BG
    im = Image.new('RGB', img.size, (255, 255, 255))
    im.paste(img, mask=img.split()[3])
    return im


if len(argv) != 3:
    print('[ERROR] Invalid number of arguments given')
    print(
        f'[USAGE] python3 {Path(__file__).name} <path_to_images> <destination_path>')
    print(f'[Example] python3 {Path(__file__).name} ~/Pictures Output.pdf')
    exit(1)

# Path of image files (Second Command Line Argument)
path = Path(argv[1])

# Destination file (PDF) (Third Command Line Argument)
pdf_filename = f'{argv[2]}'

img_list = []
IMG_EXTENSIONS = ["jpg", "jpeg", "png", "bmp", "ico"]

for image in path.iterdir():
    # Select only Image Files
    if image.suffix[1:] in IMG_EXTENSIONS:
        img_list.append(image)

# if img_list is empty, exit
if not img_list:
    print('[ERROR] Images not found! Please Make sure the specified path contains Images')
    exit(1)

img_list.sort(key=lambda x: x.name)

# Replacing Path objects with Image objects
img_list = [to_rgb(Image.open(im.absolute())) for im in img_list]

# Save First Image as PDF with All Other Images Appended to it
img_list[0].save(pdf_filename, "PDF", resolution=100.0,
                 save_all=True, append_images=img_list[1:])
print(f'{len(img_list)} Images saved to {pdf_filename} Successfully!!')
