from pypdf import PdfWriter, PdfReader
def add_metadata(output_path: str, metadata: dict):
    reader = PdfReader(output_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata(metadata)
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    print('Added metadata to the PDF')