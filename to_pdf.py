"""
Name: Images2PDF

Description: This Python script Creates PDF file from List of Images using Pillow

===
Reference: Create PDF from a list of images
Link: https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images
===

Author: @GaganGulyani
"""


from PIL import Image
from pathlib import Path
from sys import argv


if len(argv) != 3:
  print('[ERROR] Invalid number of arguments given')
  print(f'[USAGE] python3 {Path(__file__).name} <path_to_images> <destination_path>')
  print(f'[Example] python3 {Path(__file__).name} ~/Pictures Output.pdf')
  exit(1)

# Path of image files (Second Command Line Argument)
path = Path(argv[1])

img_list = []

for image in path.iterdir():
  # Select only JPG files
  if 'jpg' == image.suffix[1:]:
    img_list.append(image)

img_list.sort(key = lambda x: x.name)

# Replacing Path objects with Image objects
img_list = [Image.open(im.absolute()) for im in img_list]

# Destination file (PDF) (Third Command Line Argument)
pdf_filename = f'{argv[2]}'

# Save First Image as PDF with All Other Images Appended to it
img_list[0].save(pdf_filename, "PDF", resolution=100.0, save_all = True, append_images=img_list[1:])
print(f'{len(img_list)} Images saved to {pdf_filename} Successfully!!')
