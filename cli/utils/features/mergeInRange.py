from pypdf import PdfWriter, PdfReader
def merge_with_range(input_files: list, output_path: str, ranges: dict = None):
    writer = PdfWriter()
    for input_file in input_files:
        reader = PdfReader(input_file)
        if ranges and input_file in ranges:
            start, end = ranges[input_file]
            for page_num in range(start - 1, min(end, len(reader.pages))):
                writer.add_page(reader.pages[page_num])
        else:
            for page in reader.pages:
                writer.add_page(page)
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    print(f'Merged PDF saved to {output_path}')