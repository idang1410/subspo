from typing import List
import argparse
from googletrans import Translator 
from googletrans.models import Translated
import srt

LANG_DETECTION = "auto"
CHUNK_SIZE = 30


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


"""
Make one ticket (one object), and translte all in a bulk for one request.
Many tickets or requests will be seem like bot
"""
def translate(lines: List[str], dst_lang: str, origin_lang: str = None) -> List[Translated]: 
    translator = Translator()
    translated = []

    if not origin_lang: # language detection
        origin_lang = LANG_DETECTION

    for chunk in chunks(lines, CHUNK_SIZE):
        outputs = translator.translate(chunks, dest=dst_lang, src=origin_lang)
        transalted.extend(outputs)

    return translated 


def main(subs_file : str,  dst_lang: str, origin_lang: str):
    print(f"{subs_file}, {origin_lang}, {dst_lang}")
    with open(subs_file) as file:
        content = file.read()

    subs = list(srt.parse(content))
    lines_content = []
    for line in subs:
        lines_content.append(line.content)
    
    translated = translate(lines_content, dst_lang, origin_lang)
    for origin, new_content in zip(subs, translated):
        origin.content = new_content.text
    

    with open(f"{subs_file}.out", "w") as file:
        file.write(srt.compose(subs))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto translate substitles")
    parser.add_argument("file", help="The subs file")
    parser.add_argument("dst_lang", help="The wanted language for the subs")
    parser.add_argument("--origin_lang", help="The original substitles langugage", default=LANG_DETECTION)
    args = parser.parse_args()
    main(args.file,  args.dst_lang, args.origin_lang)