import fitz
import sys
import os
import json

from src.font import font_tags, fonts, headers_para
from src.cleaner import cleanup

filePath = sys.argv[1]

doc = fitz.open(filePath)

font_count, styles = fonts(doc)

font_size_tags = font_tags(font_count, styles)

elements = headers_para(doc, font_size_tags)

output_json = cleanup(elements)

filename = os.path.basename(filePath).split('.')[0]

if not os.path.exists("output"):
    os.mkdir("output")

output_path = os.path.join("output", filename + ".json")
with open(output_path, 'w', encoding='utf-8') as fp:
    json.dump(output_json, fp)

print("Done! Find your JSON file in {}".format(output_path))
