"""Task 3: Task Automation - Extract emails from a .txt file - CodeAlpha Python Internship"""
import re
import sys

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def extract_emails(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
        return

    emails = sorted(set(re.findall(EMAIL_PATTERN, text)))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(emails))

    print(f"Found {len(emails)} unique email(s). Saved to '{output_file}'.")


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    dst = sys.argv[2] if len(sys.argv) > 2 else "emails.txt"
    extract_emails(src, dst)
