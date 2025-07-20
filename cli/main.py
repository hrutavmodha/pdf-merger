from sys import argv
from numpy import array, where
from merge import merge
import os
from sys import platform as pf
arg = array(argv)
inp = []
out = []
if len(arg) < 3:
    print('Input and Output sources must be provided')
else:
    i = arg == '-i'
    o = arg == '-o'
    inp = arg[2: where(arg == '-o')[0][0]]
    out = arg[where(arg == '-o')[0][0] + 1]
    merge(list(inp), str(out))
for files in inp:
    if not files.endswith('.pdf'):
        raise FileNotFoundError('Only files with .pdf extension can be passed as arguements')
if '--open' in arg:
    print('Opening the generated PDF')
    pdf = arg[where(arg == '-o')[0][0] + 1]
    os.system(f'start "" {pdf}' if pf == 'win32' else f'xdg-open {pdf}' if pf == 'linux' else f'open {pdf}' if pf == 'darwin' else 'Unsupported OS')