# Task2_StockPortfolio

A console-based Stock Portfolio Tracker built in Python as **Task 2** of the CodeAlpha Python Programming Internship.

## About the Project
The user enters stock names and quantities. The program looks up each price from a hardcoded dictionary, calculates the value of every holding, and shows the total investment. The result can optionally be saved to a `.txt` or `.csv` file.

## Features
- Hardcoded stock price dictionary (AAPL, TSLA, GOOGL, MSFT, AMZN)
- Accepts multiple stocks; repeated entries of the same stock are added together
- Input validation for unknown stocks and invalid quantities
- Formatted summary table with per-stock value and total
- Optional export to `portfolio.txt` or `portfolio.csv`

## Concepts Used
Dictionaries, user input/output, basic arithmetic, loops, file handling (`open`, `csv` module), exception handling

## Requirements
- Python 3.8 or higher
- No external libraries needed

## How to Run
```bash
python stock_tracker.py
```

## Sample Run
```
Stock name: aapl
Quantity: 2
Added 2 x AAPL

Stock name: tsla
Quantity: 1
Added 1 x TSLA

Stock name: done

--- Portfolio Summary ---
Stock     Qty     Price       Value
AAPL        2       180         360
TSLA        1       250         250

Total investment: $610

Save result to file? (txt/csv/no): csv
Saved to portfolio.csv
```

## Stock Prices Used
| Stock | Price ($) |
|-------|-----------|
| AAPL  | 180 |
| TSLA  | 250 |
| GOOGL | 140 |
| MSFT  | 330 |
| AMZN  | 130 |

You can edit the `STOCK_PRICES` dictionary in `stock_tracker.py` to add or change stocks.

## Project Structure
```
Task2_StockPortfolio/
├── stock_tracker.py
├── portfolio.txt / portfolio.csv  (generated output)
└── README.md
```

## Possible Improvements
- Fetch live prices from an API
- Save and reload portfolios
- Add profit/loss calculation

## Author
Spoorthi M Naik, CodeAlpha Python Programming Intern
