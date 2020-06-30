"""
Super Simple Text Overlay onto PNG image bytestream
    stdin: bytestream of png
    stdout: bytestream of png
"""

from PIL import Image, ImageFont, ImageDraw, ImageColor
from io import BytesIO
import sys

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("header", type=str)
parser.add_argument("footer", type=str)
parser.add_argument("ttf_font_path", type=str)
args = parser.parse_args()

if __name__ == '__main__':
    raw_png_data = BytesIO( sys.stdin.buffer.read() )
    png_data = Image.open( raw_png_data )
    left, upper, right, lower = png_data.getbbox() 
    font = ImageFont.truetype( args.ttf_font_path, 40 )
    png_data_canvas = ImageDraw.Draw( png_data )
    png_data_canvas.text( xy = (10, 0), text = args.header, font = font )
    png_data_canvas.text( xy = (10, lower-47), text = args.footer, font = font )
    png_data.save( sys.stdout.buffer , format='PNG' )
