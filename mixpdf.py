from PyPDF2 import PdfReader, PdfWriter

def create_bilingual_book(french_pdf_path, polish_pdf_path, output_pdf_path):
    # Charger les fichiers PDF
    french_reader = PdfReader(french_pdf_path)
    polish_reader = PdfReader(polish_pdf_path)
    writer = PdfWriter()

    # Vérifier que les deux PDF ont le même nombre de pages
    french_pages = len(french_reader.pages)
    polish_pages = len(polish_reader.pages)
    if french_pages != polish_pages:
        raise ValueError("Les deux PDF doivent avoir le même nombre de pages.")

    # Fusionner les pages en alternant
    for i in range(french_pages):
        writer.add_page(french_reader.pages[i])  # Ajouter la page française
        writer.add_page(polish_reader.pages[i])  # Ajouter la page polonaise

    # Enregistrer le PDF final
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)
        print(f"Livre bilingue généré : {output_pdf_path}")

# Chemins des fichiers PDF
french_pdf_path = "french_text.pdf"
polish_pdf_path = "polish_text.pdf"
output_pdf_path = "bilingual_book.pdf"

# Créer le livre bilingue
create_bilingual_book(french_pdf_path, polish_pdf_path, output_pdf_path)
