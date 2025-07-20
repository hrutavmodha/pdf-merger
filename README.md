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

**1. Clone the repository**

```bash
git clone https://github.com/hrutavmodha/pdf-merger.git
cd pdf-merger
```

**2. Install the required dependencies**

```bash
pip install pypdf numpy
```

## Usage

To merge PDF files in `test/` folder, use the following command:

```bash
python main.py -i test/file1.pdf test/file2.pdf -o test/output.pdf --open
```

The `--open` flag will automatically open the default PDF viewer of yout operating system.

## Project Structure

```
pdf-merger/
├── cli/
│   ├── main.py
│   └── merge.py              
└── README.md
```

## License

This project is licensed under the terms and conditions of [MIT License](./LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

- Hrutav Modha
