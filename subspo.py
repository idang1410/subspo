import argparse


def main(subs_file : str, origin_lang: str, dst_lang: str):
    print(f"{subs_file}, {origin_lang}, {dst_lang}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto translate substitles")
    parser.add_argument("file", help="The subs file")
    parser.add_argument("origin_lang", help="The original substitles langugage")
    parser.add_argument("dst_lang", help="The wanted language for the subs")
    args = parser.parse_args()
    main(args.file, args.origin_lang, args.dst_lang)