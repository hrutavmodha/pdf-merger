from pypdf import PdfWriter
def merge(inp: list, out: str):
    merger = PdfWriter()
    for files in inp:
        merger.append(str(files))
    merger.write(out)
    merger.close()
    print(f'PDF generated and saved at path "{out}" successfully')