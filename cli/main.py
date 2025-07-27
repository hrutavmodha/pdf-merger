import webbrowser as web
from utils.core.arguements import args
from utils.core.validate import validate
from utils.core.merge import merge
from utils.features.parsePages import parsePages
from utils.features.split import split_pdf
from utils.features.rotatePages import rotate_pages
from utils.features.extractPages import extract_pages
from utils.features.metaData import add_metadata
def main():
    validate(args)
    metadata = {}
    if args.title:
        metadata['/Title'] = args.title
    if args.author:
        metadata['/Author'] = args.author
    if args.subject:
        metadata['/Subject'] = args.subject
    if args.split:
        if len(args.input) != 1:
            raise ValueError('Split operation requires exactly one input file')
        output_dir = args.output or 'split_output'
        split_pdf(args.input[0], output_dir)
    elif args.rotate is not None:
        if len(args.input) != 1:
            raise ValueError('Rotate operation requires exactly one input file')
        pages = parsePages(args.pages)
        rotate_pages(args.input[0], args.output, args.rotate, pages)
    elif args.extract:
        if len(args.input) != 1:
            raise ValueError('Extract operation requires exactly one input file')
        pages = parsePages(args.extract)
        if not pages:
            raise ValueError('No valid pages specified for extraction')
        extract_pages(args.input[0], args.output, pages)
    elif args.merge or (args.input and args.output):
        merge(args.input, args.output)
        if metadata:
            add_metadata(args.output, metadata)
    if args.open and args.output:
        print('Opening the generated PDF')
        web.open(args.output)
    if args.verbose:
        print(f'Input files: {args.input}')
        print(f'Output: {args.output}')
        if metadata:
            print(f'Added metadata: {metadata}')
        print('Operation completed successfully.')
if __name__ == '__main__':
    main()