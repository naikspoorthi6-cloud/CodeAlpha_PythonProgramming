# Task3_EmailExtractor

A task automation script built in Python as **Task 3** of the CodeAlpha Python Programming Internship.

## About the Project
This script automates a repetitive job: finding email addresses in a text file. It reads a `.txt` file, extracts every email address using a regular expression, removes duplicates, and saves the result to a new file.

## Features
- Extracts all email addresses using `re`
- Removes duplicates and sorts the output
- Accepts input and output file names as command-line arguments
- Handles missing input file gracefully
- Prints how many unique emails were found

## Concepts Used
`re` (regular expressions), file handling, `sys.argv`, sets, exception handling

## Requirements
- Python 3.8 or higher
- No external libraries needed

## How to Run
Default (reads `input.txt`, writes `emails.txt`):
```bash
python email_extractor.py
```

Custom files:
```bash
python email_extractor.py mydata.txt results.txt
```

## Example
**input.txt**
```
Contact us at hello@example.com or support@codealpha.tech.
Sales: sales@example.com, personal: john.doe99@gmail.com
Duplicate: hello@example.com
```

**Console output**
```
Found 4 unique email(s). Saved to 'emails.txt'.
```

**emails.txt**
```
hello@example.com
john.doe99@gmail.com
sales@example.com
support@codealpha.tech
```

## Regex Pattern Used
```
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
```

## Project Structure
```
Task3_EmailExtractor/
├── email_extractor.py
├── input.txt
├── emails.txt  (generated output)
└── README.md
```

## Possible Improvements
- Scan multiple files or a whole folder
- Export to CSV
- Add a simple GUI

## Author
Spoorthi M Naik, CodeAlpha Python Programming Intern
