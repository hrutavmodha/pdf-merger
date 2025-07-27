import argparse
def parse_page_range(range_str):
    try:
        start, end = map(int, range_str.split('-'))
        return start, end
    except ValueError:
        raise argparse.ArgumentTypeError('Page range must be in format start-end (e.g., 1-5)')
parser = argparse.ArgumentParser(
    description='PDF Wrangler - A powerful tool for PDF operations'
)
parser.add_argument(
    '-i', '--input',
    nargs='+',
    help='Input PDF files'
)
parser.add_argument(
    '-o', '--output',
    help='Output PDF file path'
)
parser.add_argument(
    '--merge',
    action='store_true',
    help='Merge multiple PDF files into one'
)
parser.add_argument(
    '-s', '--split',
    action='store_true',
    help='Split the input PDF into individual pages'
)
parser.add_argument(
    '--rotate',
    type=int,
    choices=[90, 180, 270],
    help='Rotate pages by specified degrees'
)
parser.add_argument(
    '--pages',
    type=str,
    help='Specify pages to process (e.g., "1,3,5-7")'
)
parser.add_argument(
    '--extract',
    type=str,
    help='Extract specific pages (e.g., "1,3,5-7")'
)
parser.add_argument(
    '--title',
    help='Set the title metadata of the PDF'
)
parser.add_argument(
    '--author',
    help='Set the author metadata of the PDF'
)
parser.add_argument(
    '--subject',
    help='Set the subject metadata of the PDF'
)
parser.add_argument(
    '--open',
    action='store_true',
    help='Open the generated PDF after processing'
)
parser.add_argument(
    '-vb', '--verbose',
    action='store_true',
    help='Enable verbose output'
)
parser.add_argument(
    '-v', '--version',
    action='version',
    version='PDF Wrangler 1.1.0',
    help='Show the version of PDF Wrangler'
)
parser.add_argument(
    '-l', '--license',
    action='store_true',
    help='Show the license of PDF Wrangler'
)
parser.add_argument(
    '-a', '--about',
    action='version',
    version='PDF Wrangler is a powerful CLI tool for PDF operations including merging, splitting, rotation, and metadata management. Created by Hrutav Modha',
    help='Show information about PDF Wrangler'
)
args = parser.parse_args()