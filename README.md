# ETL-pipeline
The pipeline extracts text from scanned documents or web pages, cleans and structures it, then translates it to Braille (using Liblouis), outputting JSON files aligned for AI training.
/sample_input/
Extract and Clean Text (OCR)
Task: Use OCR tools like Tesseract (and optionally Gemini/Qwen-VL) to extract and clean text.

How to do it:

Use pytesseract in extract_clean.py to read text from images.

Clean noise (remove special chars, fix encoding).

GitHub script:

bash
Copy
Edit
/scripts/extract_clean.py
STEP 3: Structure Data
Task: Format extracted text into structured JSON paragraphs with metadata.

How to do it:

Split text into paragraphs.

Add metadata (source filename, language).

Output structure as a list of dictionaries.

GitHub script:

bash
Copy
Edit
/scripts/structure_data.py
STEP 4: Translate to Braille
Task: Convert structured text into Braille using Liblouis.

How to do it:

Pass each paragraph to lou_translate.

Capture Braille output and pair with original paragraph.

GitHub script:

bash
Copy
Edit
/scripts/braille_translate.py
STEP 5: Combine All Steps (ETL)
Task: Combine Steps 2–4 into one flow.

How to do it:

Iterate over files in sample_input/.

Extract, structure, translate.

Write the full result to output/structured_output.json.

GitHub script:

bash
Copy
Edit
/scripts/main.py
STEP 6: Store Final Output
Task: Save cleaned, structured, Braille-translated data.

How to do it:

Save as a .json file in output/.

GitHub location:

bash
Copy
Edit
/output/structured_output.json
STEP 7: Documentation
Task: Explain your architecture, usage, and setup.

What to include:

Project purpose

Dependencies (Tesseract, Liblouis)

Folder structure

How to run

GitHub file:

Copy
Edit
/README.md
STEP 8: Demo Video
Task: Record a 2–3 minute screen recording showing the pipeline.

GitHub file:

bash
Copy
Edit
/demo_video.mp4
