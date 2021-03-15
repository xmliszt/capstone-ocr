import sys
import pyocr
import pyocr.builders


class OCRExtractor:
    def __init__(self, lang='eng'):
        self.lang = lang
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found!")
            sys.exit(1)
        self.tool = tools[0]
        print("Using OCR tool '{}'".format(self.tool.get_name()))

    # Extract pure text as string
    def extract_txt(self, img):
        txt = self.tool.image_to_string(img,
                                        lang=self.lang,
                                        builder=pyocr.builders.TextBuilder())
        return txt

    # Extract list of word boxes
    # .content to get the text
    # .position to get the posisiton
    def extract_word_boxes(self, img):
        word_boxes = self.tool.image_to_string(
            img, lang=self.lang, builder=pyocr.builders.WordBoxBuilder())
        word_map = dict()
        for idx, word in enumerate(word_boxes):
            content = word.content
            position = word.position
            word_map[idx] = {"word": content, "position": position}
        return word_map

    # Extract list of line objects, each line has word boxes
    # .content to get whole line of text
    # .position to get position of the whole line
    # .word_boxes to get the list of word boxes in this line
    def extract_line_and_word_boxes(self, img):
        line_and_word_boxes = self.tool.image_to_string(
            img, lang=self.lang, builder=pyocr.builders.LineBoxBuilder())
        line_map = dict()
        for idx, line in enumerate(line_and_word_boxes):
            content = line.content
            position = line.position
            words = line.word_boxes
            word_map = dict()
            for idx, word in enumerate(words):
                word_map[idx] = {
                    "word": word.content,
                    "position": word.position
                }
            line_map[idx] = {
                "line": content,
                "position": position,
                "word_boxes": word_map
            }
        return line_map