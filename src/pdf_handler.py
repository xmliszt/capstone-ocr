from pdf2image import convert_from_path


# Convert given PDF into images and output them as a list
def get_images(pdf):
    if not pdf.endswith('.pdf'):
        raise TypeError("Input file must be PDF!")
    return convert_from_path(pdf)
