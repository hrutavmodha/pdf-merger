import os
def validate(args):
    for file in args.input:
        if not file.endswith('.pdf'):
            raise FileNotFoundError('Only PDF files can be passed as arguments')
        if not os.path.isfile(file):
            raise FileNotFoundError(f'The file "{file}" does not exist or is not a valid PDF file or the path is given wrong')