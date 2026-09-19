"""Task 2: Stock Portfolio Tracker - CodeAlpha Python Internship"""

import csv

STOCK_PRICES = {
    "AAPL": 15000,
    "TSLA": 21000,
    "GOOGL": 12000,
    "MSFT": 28000,
    "AMZN": 11000,
}


def get_portfolio():
    portfolio = {}

    print(
        "Available stocks:",
        ", ".join(f"{s} (₹{p})" for s, p in STOCK_PRICES.items())
    )
    print("Enter stock name and quantity. Type 'done' when finished.\n")

    while True:
        name = input("Stock name: ").strip().upper()

        if name == "DONE":
            break

        if name not in STOCK_PRICES:
            print("Stock not found. Try again.\n")
            continue

        try:
            qty = int(input("Quantity: "))

            if qty <= 0:
                raise ValueError

        except ValueError:
            print("Enter a positive whole number.\n")
            continue

        portfolio[name] = portfolio.get(name, 0) + qty
        print(f"Added {qty} x {name}\n")

    return portfolio


def show_summary(portfolio):
    total = 0

    print("\n--- Portfolio Summary ---")
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>12}{'Value':>14}")

    for stock, qty in portfolio.items():
        value = qty * STOCK_PRICES[stock]
        total += value

        print(
            f"{stock:<8}{qty:>6}"
            f"{'₹' + str(STOCK_PRICES[stock]):>12}"
            f"{'₹' + str(value):>14}"
        )

    print(f"\nTotal investment: ₹{total}")

    return total


def save_results(portfolio, total):
    choice = input("\nSave result to file? (txt/csv/no): ").strip().lower()

    if choice == "txt":
        with open("portfolio.txt", "w", encoding="utf-8") as f:
            for stock, qty in portfolio.items():
                value = qty * STOCK_PRICES[stock]
                f.write(
                    f"{stock}: {qty} x ₹{STOCK_PRICES[stock]} = ₹{value}\n"
                )

            f.write(f"Total investment: ₹{total}\n")

        print("Saved to portfolio.txt")

    elif choice == "csv":
        with open("portfolio.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow(["Stock", "Quantity", "Price (₹)", "Value (₹)"])

            for stock, qty in portfolio.items():
                value = qty * STOCK_PRICES[stock]
                writer.writerow(
                    [stock, qty, STOCK_PRICES[stock], value]
                )

            writer.writerow(["TOTAL", "", "", total])

        print("Saved to portfolio.csv")


if __name__ == "__main__":
    portfolio = get_portfolio()

    if portfolio:
        total = show_summary(portfolio)
        save_results(portfolio, total)
    else:
        print("No stocks entered.")