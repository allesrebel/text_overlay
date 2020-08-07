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
parser.add_argument("ttf_font_size", type=int)
args = parser.parse_args()

if __name__ == '__main__':
    raw_png_data = BytesIO( sys.stdin.buffer.read() )
    png_data = Image.open( raw_png_data )

    font = ImageFont.truetype( args.ttf_font_path, args.ttf_font_size )

    left, upper, right, lower = png_data.getbbox() 
    border = Image.new( "RGB", (right, lower + args.ttf_font_size * 2 ), 'white')
    png_data_canvas = ImageDraw.Draw( border )
    new_left, new_upper, new_right, new_lower = border.getbbox()
    w, h = png_data_canvas.textsize( args.header, font = font )
    border.paste( png_data, (0, args.ttf_font_size) )
    
    png_data_canvas.text( xy = ( (right - w)//2, args.ttf_font_size//2 ), text = args.header, font = font, fill = 'black')
    png_data_canvas.text( xy = ( right/2 - w/2 - 10, new_lower - args.ttf_font_size - args.ttf_font_size//2 ), text = args.footer, font = font, fill = 'black' )
    border.save( sys.stdout.buffer , format='PNG' )
