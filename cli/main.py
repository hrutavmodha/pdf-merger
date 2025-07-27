from sys import platform as pf
import os
import webbrowser as web
from utils.merge import merge
from utils.arguements import args
from utils.validate import validate
validate(args)
merge(args.input, args.output)
if args.open:
    print('Opening the generated PDF')
    web.open(args.output)
if args.verbose:
    print(f'Received Input files as {args.input}')
    print(f'Received an Output file as {args.output}')
    print('Merge operation completed successfully.')
elif args.silent:
    print('Running in silent mode, no output will be displayed.')