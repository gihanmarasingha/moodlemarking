#!/usr/bin/env python3
import sys
import argparse
from PyPDF2 import PdfReader, PdfWriter, PageObject, Transformation

def add_margin(original_file, new_file, margin_width):
    reader = PdfReader(original_file)
    writer = PdfWriter()

    for i in range(len(reader.pages)):
        page = reader.pages[i]
        
        original_width = page.mediabox[2]
        original_height = page.mediabox[3]
        
        new_width = original_width + margin_width
        packet = PageObject.create_blank_page(width=new_width, height=original_height)
        
        x_position = new_width - original_width

        packet.merge_page(page, expand=True)
        packet.add_transformation(Transformation().translate(x_position, 0))
        
        writer.add_page(packet)

    with open(new_file, "wb") as f:
        writer.write(f)

def main():
    parser = argparse.ArgumentParser(description="Add margins to a PDF file.")
    parser.add_argument("original_file", help="The original PDF file.")
    parser.add_argument("new_file", help="The new PDF file with added margins.")
    parser.add_argument("-m", "--margin", type=int, default=200, help="Width, in pixels, of the left margin (default is 200).")
    
    args = parser.parse_args()

    add_margin(args.original_file, args.new_file, args.margin)

if __name__ == "__main__":
    main()
