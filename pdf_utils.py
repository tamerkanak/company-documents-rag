import pdfplumber
from typing import List

def extract_paragraphs_from_pdf(file) -> List[str]:
    paragraphs = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for para in text.split('\n\n'):
                    para = para.strip()
                    if len(para) > 30:
                        paragraphs.append(para)
    return paragraphs 