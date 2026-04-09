## Usage: python crop_pdfs.py <input_dir> <top> <right> <bottom> <left> --switch-lr

import os
from pypdf import PdfReader, PdfWriter
import sys

def crop_pdf(input_path, output_path, margins, switch_lr_every_second=False):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    top, right, bottom, left = margins
    for i, page in enumerate(reader.pages):
        mediabox = page.mediabox
        # Switch left/right margins on every second page if flag is set
        if switch_lr_every_second and (i % 2 == 1):
            l, r = right, left
        else:
            l, r = left, right
        new_left = mediabox.left + l
        new_bottom = mediabox.bottom + bottom
        new_right = mediabox.right - r
        new_top = mediabox.top - top
        page.mediabox.lower_left = (new_left, new_bottom)
        page.mediabox.upper_right = (new_right, new_top)
        writer.add_page(page)
    with open(output_path, "wb") as f:
        writer.write(f)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Crop all PDFs in a directory.")
    parser.add_argument("input_dir", help="Directory containing PDFs to crop")
    parser.add_argument("top", type=float, help="Top margin (points)")
    parser.add_argument("right", type=float, help="Right margin (points)")
    parser.add_argument("bottom", type=float, help="Bottom margin (points)")
    parser.add_argument("left", type=float, help="Left margin (points)")
    parser.add_argument("--switch-lr", action="store_true", help="Switch left/right margins on every second page")
    args = parser.parse_args()

    margins = (args.top, args.right, args.bottom, args.left)
    output_dir = os.path.join(args.input_dir, "Cropped")
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(args.input_dir):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(args.input_dir, filename)
            output_path = os.path.join(output_dir, filename[:-4] + "_c.pdf")
            crop_pdf(input_path, output_path, margins, switch_lr_every_second=args.switch_lr)
            print(f"Cropped {filename} -> {os.path.basename(output_path)}")

if __name__ == "__main__":
    main()
