import subprocess

def translate_to_braille(text, lang='en'):
    with open("temp.txt", "w", encoding="utf-8") as f:
        f.write(text)
    result = subprocess.run(["lou_translate", f"{lang}-braille.ctb", "temp.txt"], capture_output=True, text=True)
    return result.stdout.strip()
