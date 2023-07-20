# Log Parsing

This script reads log lines from standard input (stdin) line by line and computes various metrics based on the provided input format. It calculates the total file size and the number of lines for each status code encountered. The script prints the statistics after every 10 lines and/or when a keyboard interruption (CTRL + C) occurs.

## Input Format

The input log lines should follow the specified format:

```
 <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

```


If the line does not adhere to this format, it will be skipped.

## Usage

To generate log data, use the provided `0-generator.py` script. It generates random log lines with different IP addresses, dates, status codes, and file sizes.


## Metrics

The script calculates the following metrics:

1. Total File Size: The sum of all previous file sizes encountered in the log lines.

2. Number of Lines by Status Code: Counts the occurrences of each possible status code (200, 301, 400, 401, 403, 404, 405, and 500) and prints them in ascending order.

## Note

Please note that the output of the script will vary as the log generator produces random data. So, the output may not be the same as the provided example.

Feel free to modify the generator script or explore different log inputs to test the parsing script with various scenarios.

Happy log parsing!
