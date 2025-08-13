import io, tempfile, os
from typing import List
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes

def _extract_from_images(images: List[Image.Image]) -> str:
    text_parts = []
    for img in images:
        text = pytesseract.image_to_string(img)
        text_parts.append(text)
    return "\n".join(text_parts)

def extract_text(content: bytes, content_type: str) -> str:
    if content_type == "application/pdf":
        images = convert_from_bytes(content, dpi=200)
        return _extract_from_images(images)
    else:
        img = Image.open(io.BytesIO(content)).convert("RGB")
        return pytesseract.image_to_string(img)
