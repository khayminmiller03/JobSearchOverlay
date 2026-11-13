import regex as re
import html

def clean_text(s : str) -> str:
    for string in s:
        if string.contains(r"[a-z][.:!?][A-Z]", regex=True):
            re.sub(r"[a-z][.:!?][A-Z]", r"[a-z][.:!?]+\s[A-Z]", string)
        if string.contains(r"#URL_|#EMAIL_|#PHONE_", regex=True):
            re.sub(r"#URL_|#EMAIL_|#PHONE_", "", string)
        if string.contains(r"&amp|&nbsp", regex=True):
            string = html.unescape(string)
    return s
