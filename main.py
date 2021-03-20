import sys
import os
from PIL import Image

from src.pdf_handler import get_images
from src.extractor import OCRExtractor
from src.writer import Writer

from argparse import ArgumentParser
from tqdm import tqdm

parser = ArgumentParser(
    description="Simple OCR tool to extract text from an image")
parser.add_argument(
    '--mode',
    '-m',
    default=1,
    type=int,
    help="Select mode of operation, default is 1. 1: Extract and return pure text from given image. 2: Extract and return list of word boxes and their positions in pixels from a given image. 3: Extract and return a list of lines and their positions in pixels from a given image."
)
parser.add_argument('--pdf',
                    default=False,
                    action="store_true",
                    help="Turn on PDF mode, the input file must be a PDF")
parser.add_argument('--input',
                    '-i',
                    required=True,
                    type=str,
                    help="Input path to perform OCR extraction.")
parser.add_argument('--output',
                    '-o',
                    required=True,
                    type=str,
                    help="Output filename")

args = parser.parse_args()

mode = args.mode
_input = args.input
isPDF = args.pdf
filename = args.output

if mode < 1 or mode > 3:
    print("Select mode from 1~3. Details please see '-h' for help.")
    sys.exit(1)

if __name__ == "__main__":
    ocr = OCRExtractor()
    writer = Writer()
    if isPDF:
        images = get_images(_input)
    else:
        images = [_input]

    idx = 0
    for image in tqdm(images, desc="Extracting..."):
        writer.append("-" * 28 +
                      " Image {:2}/{:2} ".format(idx + 1, len(images)) +
                      "-" * 28 + "\n")
        if not isPDF:
            image = Image.open(image)
        if mode == 1:
            txt = ocr.extract_txt(image)
            print(txt)
            writer.append(txt + "\n")
        if mode == 2:
            words = ocr.extract_word_boxes(image)
            writer.append(words + "\n")
        if mode == 3:
            lines = ocr.extract_line_and_word_boxes(image)
            writer.append(lines + "\n")
        writer.append("-" * 70 + "\n")
        idx += 1

    writer.write(filename + ".txt")
