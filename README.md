# capstone-ocr
Capstone OCR implementation

## How To Run?

### Install Tesseract
> MacOS

You need to have [Homebrew](https://attacomsian.com/blog/install-homebrew-macos) installed first!
```
brew install tesseract
brew install tesseract-lang
```

> Linux
```
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```
> Windows

[How to Install Tesseract on Windows](https://medium.com/quantrium-tech/installing-and-using-tesseract-4-on-windows-10-4f7930313f82)

### Create Virtual Environment for Python3
Create and activate virtual environment
> Linux & MacOS

```
virtualenv venv
source venv/bin/activate
```

> Windows

```
virtualenv venv
venv\Scripts\activate
```

Deactivate
```
deactivate
```

### Install depedencies
You need `pyocr` and `pdf2image`.
You can install them all via:
```
pip install -r requirements.txt
```

### Run the program

#### Options
- `-m`, `--mode`: Mode selection.
  - 1: Extract pure text from the image
  - 2: Extract words from image with their positions
  - 3: Extract lines from image with their positions and words
- `-i`, `--input`: Input path, can be a image or a PDF
- `--pdf`: If supply this flag, you need to input a PDF as input. The program will carry out extraction for every image and present all results.

#### Help
To get help:
```
python main.py -h
```

#### Examples

> Input a single image, extract pure text
```
python main.py -i img/1.png
```

> Input a single image, extract lines
```
python main.py -m 3 -i img/1.png
```

> Input a PDF, extract words
```
python main.py -m 2 -i img/2.pdf --pdf
```
