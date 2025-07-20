from sys import argv
from numpy import array, where
from merge import merge as merge
arg = array(argv)
inp = []
out = []
if argv[1] != '-i' or '-o' not in argv:
    raise IOError('Input and Output sources must be provided')
else:
    i = arg == '-i'
    o = arg == '-o'
    inp = arg[2: where(arg == '-o')[0][0]]
    out = arg[where(arg == '-o')[0][0] + 1]
    merge(list(inp), str(out))
for files in inp:
    if not files.endswith('.pdf'):
        raise FileNotFoundError('Only files with .pdf extension can be passed as arguements')
