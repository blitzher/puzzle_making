"""
usage

save an image to <sour.png>
script will convert this image into a byteformat
and save it to a python file named <img.py>

move this file into your directory
and to write this back into an image, use

from img import data
puzzle_tools.write_png(data, (size_x, size_y))

after compiling to a .exe, the bytefile will be unnecessary
run this file after making the 
"""


from PIL import Image, ImageDraw, ImageFont
from math import ceil
import os, pyperclip

im = Image.open('sour.png')

byte_pack = im.tobytes()

t_quote = r'"""'
py_info = "%s %s %s %s" % ('data = ', t_quote, str(byte_pack), t_quote)

try:
	os.remove('img.py')
except: pass;

with open("img.py", 'w') as f:
	f.write(py_info)

try:
	from img import data
	im = Image.frombytes('RGB', (50,50), byte_pack)
	im.save('img.png')
except Exception as e:
	pass
