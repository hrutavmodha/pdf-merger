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

2. Setup Virtual Environment

Before installing dependencies, it's recommended to create and activate a virtual environment:

i. Create a virtual environment:
```bash
python -m venv venv
```

ii. Activate the virtual environment:

- On Windows:
```bash
.\venv\Scripts\activate
```

- On Linux and MacOS:
```bash
source venv/bin/activate
```

Once activated, proceed with the installation steps.

3. Install the required dependencies:
```bash
pip install PyPDF2 numpy
```

## Usage

To merge PDF files, use the following command:

```bash
cd ./cli
python main.py -i ../test/file1.pdf ../test/file2.pdf -o ../test/output.pdf
```

For testing purpose, I have provided the `test/` folder, which contains 2 PDFs. 

Either you can wrangle up with them, or can use your own PDFs!

## Project Structure

```
pdf-merger/
├── cli/
│   ├── main.py
│   └── merge.py
├── test/
    ├── file1.pdf
    ├── file2.pdf               
└── README.md
```

## License

This project is licensed under the terms and conditions of [MIT License](./LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

- Hrutav Modha (@hrutavmodha)
