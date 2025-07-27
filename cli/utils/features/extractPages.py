from pypdf import PdfWriter, PdfReader
def extract_pages(input_path: str, output_path: str, pages: list):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for page_num in pages:
        if 1 <= page_num <= len(reader.pages):
            writer.add_page(reader.pages[page_num - 1])
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    print(f'Extracted pages saved to {output_path}')