import os
from pypdf import PdfReader


def test_pdf(create_zip):
    pdf_path = os.path.join(create_zip, 'Software Testing Kulikov.pdf')
    with open(pdf_path, 'rb') as pdf:
        reader = PdfReader(pdf)

        book_title = 'Тестирование программного обеспечения. Базовый курс.'
        book_version = "Версия книги 3.2.4 от 26.07.2023"
        page_1_text = reader.pages[1].extract_text()

        assert book_title in page_1_text
        assert book_version in page_1_text
