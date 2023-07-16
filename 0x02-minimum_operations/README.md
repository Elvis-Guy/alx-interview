# Minimum Operations

This project is aimed at solving the problem of determining the fewest number of operations required to achieve a specific number of characters in a text file. The available operations are "Copy All" and "Paste."

## Problem Description

Given a number `n`, the task is to calculate the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

### Example

```python
n = 9

H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
