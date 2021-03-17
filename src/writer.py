import os


class Writer:
    def __init__(self):
        self.txt = ""

    def append(self, txt):
        self.txt += txt

    def write(self, filename):
        if not os.path.exists("output"):
            os.mkdir("output")

        output_path = os.path.join("output", filename)
        with open(output_path, "w", encoding="utf-8") as fh:
            fh.write(self.txt)
            print("Written to file: {}".format(output_path))
