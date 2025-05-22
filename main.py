import os
import json
from scripts.extract_clean import ocr_image
from scripts.structure_data import structure_text
from scripts.braille_translate import translate_to_braille

input_dir = "sample_input"
output_path = "output/structured_output.json"

structured_output = []

for filename in os.listdir(input_dir):
    if filename.endswith(".png"):
        image_path = os.path.join(input_dir, filename)
        text = ocr_image(image_path)
        paragraphs = structure_text(text, filename)
        for para in paragraphs:
            para["braille"] = translate_to_braille(para["paragraph"])
            structured_output.append(para)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(structured_output, f, indent=2, ensure_ascii=False)

print(f"Output written to {output_path}")
