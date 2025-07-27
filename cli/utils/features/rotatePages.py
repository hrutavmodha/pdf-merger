from pypdf import PdfWriter, PdfReader
def rotate_pages(input_path: str, output_path: str, rotation: int, pages: list = None):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        if pages is None or (i + 1) in pages:
            page.rotate(rotation)
        writer.add_page(page)
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    print(f'Rotated pages saved to {output_path}')