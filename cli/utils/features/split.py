from pypdf import PdfWriter, PdfReader
import os
def split_pdf(input_path: str, output_dir: str):
    reader = PdfReader(input_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_path = os.path.join(output_dir, f'page_{i + 1}.pdf')
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
    print(f'Split {len(reader.pages)} pages into {output_dir}')