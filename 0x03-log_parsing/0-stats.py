#!/usr/bin/python3

import sys
import datetime

def print_statistics(file_size, status_codes):
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
    total_file_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            try:
                # Parse the input line to extract file size and status code
                parts = line.split()
                file_size = int(parts[-1])
                status_code = int(parts[-2])

                # Update total file size and status code count
                total_file_size += file_size
                status_codes[status_code] = status_codes.get(status_code, 0) + 1

                if i % 10 == 0:
                    print_statistics(total_file_size, status_codes)

            except (ValueError, IndexError):
                # Skip the line if it does not follow the expected format
                continue

    except KeyboardInterrupt:
        # If a keyboard interruption (CTRL + C) occurs, print the final statistics
        print_statistics(total_file_size, status_codes)

if __name__ == "__main__":
    main()
