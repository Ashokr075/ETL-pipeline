# Braille ETL Pipeline

## Overview
This repository demonstrates a simplified data pipeline for extracting, cleaning, structuring, and translating unstructured text into Braille, designed for training AI models.

## Setup Instructions

1. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
2. Install [Liblouis](https://github.com/liblouis/liblouis).
3. Clone this repo and place PNG files into `sample_input/`.

## Run the Pipeline

```bash
python scripts/main.py
```

## Output

JSON with paragraph and Braille mapping is saved to `output/structured_output.json`.

## Example Output
```json
[
  {
    "paragraph": "Sample paragraph here.",
    "braille": "⠠⠎⠁⠍⠏⠇⠑ ⠏⠁⠗⠁⠛⠗⠁⠏⠓ ⠓⠑⠗⠑⠲",
    "source": "page1.png",
    "language": "en"
  }
]
```
