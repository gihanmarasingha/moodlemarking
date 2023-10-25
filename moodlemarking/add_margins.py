#!/usr/bin/env python3
import sys
from PyPDF2 import PdfReader, PdfWriter, PageObject, Transformation

def add_margins(original_file, new_file):
    # Read the existing PDF
    reader = PdfReader(original_file)
    writer = PdfWriter()

    # Loop through each page
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        
        # Get the dimensions of the original document
        original_width = page.mediabox[2]
        original_height = page.mediabox[3]
        
        # Create a new page with extended width but original height
        new_width = original_width + 200  # Adding 200 to the width for the right margin
        packet = PageObject.create_blank_page(width=new_width, height=original_height)
        
        # Calculate the x-position to align the old page with the new right margin
        x_position = new_width - original_width

        # Merge the old page onto the new one at the specific position
        packet.merge_page(page, expand=True)
        packet.add_transformation(Transformation().translate(x_position, 0))
        
        writer.add_page(packet)

    # Create a new PDF with added margins
    with open(new_file, "wb") as f:
        writer.write(f)

def main():
    # Check for command line arguments
    if len(sys.argv) < 3:
        print("Usage: python add_margins.py <original_file> <new_file>")
    else:
        original_file = sys.argv[1]
        new_file = sys.argv[2]
        add_margins(original_file, new_file)

if __name__ == "__main__":
    main()
