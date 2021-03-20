from collections import defaultdict


def clean(_string):
    return _string.replace("|", "").replace("\t", " ")


def cleanup(elements):
    output = {
        "title": "",
        "body": defaultdict(int)
    }

    para = ""
    crrt_page = None
    paragraph_count = 0

    cursor = 0
    found_first_para = False
    while cursor < len(elements):
        ele = elements[cursor]
        pn = ele.get("page")
        if crrt_page is None:
            crrt_page = pn
        txt = ele.get("content")
        print(pn, crrt_page, txt)
        if txt.startswith("|") and not found_first_para:
            pass
        elif txt.startswith("|") and found_first_para:  # End of one paragraph
            if para == "":
                pass
            else:
                # print(pn, crrt_page, para)
                if pn == crrt_page:
                    paragraph_count += 1
                    output["body"][paragraph_count] = para
                    para = ""
        elif txt.startswith("<h1>"):
            header = clean(txt.lstrip("<h1>"))
            output["title"] = header
        elif txt.startswith("<p>"):
            crrt_page = pn
            if not found_first_para:
                found_first_para = True
            txt = clean(txt.lstrip("<p>"))
            para += txt
        cursor += 1

    return output
