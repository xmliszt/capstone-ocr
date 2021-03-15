import sys
from PIL import Image

from src.pdf_handler import get_images
from src.extractor import OCRExtractor
from argparse import ArgumentParser
from pprint import pprint

parser = ArgumentParser(
    description="Simple OCR tool to extract text from an image")
parser.add_argument(
    '--mode',
    '-m',
    default=1,
    type=int,
    help=
    "Select mode of operation, default is 1. 1: Extract and return pure text from given image. 2: Extract and return list of word boxes and their positions in pixels from a given image. 3: Extract and return a list of lines and their positions in pixels from a given image."
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

args = parser.parse_args()

mode = args.mode
_input = args.input
isPDF = args.pdf

if mode < 1 or mode > 3:
    print("Select mode from 1~3. Details please see '-h' for help.")
    sys.exit(1)

if __name__ == "__main__":
    ocr = OCRExtractor()
    if isPDF:
        images = get_images(_input)
    else:
        images = [_input]

    for idx, image in enumerate(images):
        print("-" * 28 + " Image {:2}/{:2} ".format(idx + 1, len(images)) +
              "-" * 28)
        if not isPDF:
            image = Image.open(image)
        if mode == 1:
            txt = ocr.extract_txt(image)
            pprint(txt)
        if mode == 2:
            words = ocr.extract_word_boxes(image)
            pprint(words)
        if mode == 3:
            lines = ocr.extract_line_and_word_boxes(image)
            pprint(lines)
        print("-" * 70)
