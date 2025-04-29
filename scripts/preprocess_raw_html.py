from bs4 import BeautifulSoup
import re 

def preprocess_raw_html(raw_html):
    # remove the html tag on the text
    soup = BeautifulSoup(raw_html, 'html.parser')
    raw_text = soup.get_text()

    text = ""
    for phrase in raw_text.split("\n"):
        # if not re.match(r"^[a-zA-Z0-9]",phrase) and phrase.strip()!="":
        #     n=0
        #     while not (97<=ord(phrase[n])<=122 or 65<=ord(phrase[n])<=90):
        #         n+=1
        #     phrase = phrase[n:]

        if phrase.strip()!="":
            text+=phrase+" "
        
    # remove trailing whitespace
    text = text.strip()

    # remove the \n from the text
    # text = re.sub(r"\n", " ", text)

    # remove URLs
    text = re.sub(r"\b((?:https?|ftp|file):\/\/[-a-zA-Z0-9+&@#\/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#\/%=~_|])","",text)

    # remove the \' from the text
    matches = re.findall(r"\\'", text)
    for match in matches:
        text = text.replace(match,match[1:])

    return text


