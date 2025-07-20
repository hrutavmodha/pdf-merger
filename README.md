# PDF Merger

A Python-based command-line tool for merging multiple PDF files into a single document.

## Features

- Merge multiple PDF files into a single document
- Simple command-line interface
- Preserves original PDF quality
- Supports various input PDF sizes and formats

## Requirements

- Python 3
- PyPDF2 library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hrutavmodha/pdf-merger.git
cd pdf-merger
```

2. Install the required dependencies:
```bash
pip install pypdf numpy
```

## Usage

To merge PDF files, use the following command:

```bash
python initialValidations.py -i input1.pdf input2.pdf -o output.pdf
```

Replace `input1.pdf`, `input2.pdf` with your input PDF files and `output.pdf` with your desired output filename.

## Project Structure

```
pdf-merger/
├── cli/
│   ├── initialValidations.py
│   └── merge.py  
├── documentation/            
└── README.md
```

## License

This project is licensed under the terms and conditions of [MIT License](./LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

- Hrutav Modha (@hrutavmodha)
