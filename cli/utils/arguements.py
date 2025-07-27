import argparse
import os
parser = argparse.ArgumentParser(description='Merge multiple PDF files into one')
parser.add_argument('-i', '--input', nargs='+', required=True, help='Input PDF files to merge')
parser.add_argument('-o', '--output', required=True, help='Output PDF file path')
parser.add_argument('--open', action='store_true', help='Open the generated PDF after merging')
parser.add_argument('-vb', '--verbose', action='store_true', help='Enable verbose output')
parser.add_argument('-v', '--version', action='version', version='PDF Wrangler 1.0.0', help='Show the version of PDF Wrangler')
parser.add_argument('-s', '--split', action='store_true', help='Split the input PDF files into individual pages (not implemented yet)')
try:
    parser.add_argument('-l', '--license', action='version', version=os.popen(f'cat {os.path.abspath("../LICENSE")}').read(), help='Show the license of PDF Wrangler')
except Exception as e:
    pass
parser.add_argument('-a', '--about', action='version', version='PDF Wrangler is a tool to merge PDF files. It is free of cost and open-source CLI-based tool made by Hrutav Modha', help='Show information about PDF Wrangler')
args = parser.parse_args()