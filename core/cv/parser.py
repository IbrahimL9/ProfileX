import pdfplumber

def extract_text_from_pdf(path):
    with pdfplumber.open(path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

if __name__ == "__main__":
    from pathlib import Path

    # Trouve le dossier racine du projet
    base_dir = Path(__file__).resolve().parents[2]
    pdf_path = base_dir / "data" / "cv_sample.pdf"

    text = extract_text_from_pdf(pdf_path)
    print(text[:1000])

