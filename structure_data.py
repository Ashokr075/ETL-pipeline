import json

def structure_text(text, source_file):
    paragraphs = text.split('\n\n')
    structured = [{"paragraph": p.strip(), "source": source_file, "language": "en"} for p in paragraphs if p.strip()]
    return structured
