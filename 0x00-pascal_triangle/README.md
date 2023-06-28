# Pascal's Triangle

Pascal's Triangle is a triangular arrangement of numbers named after the French mathematician Blaise Pascal, who introduced it in the 17th century. The triangle is constructed in such a way that each number in the triangle is the sum of the two numbers directly above it.

The triangle starts with a single row containing the number 1. Each subsequent row is constructed by adding a 1 at the beginning and end, and filling the numbers in between by summing the corresponding elements from the previous row.

Here's an example of Pascal's Triangle:


```markdown
 
          1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
     1 5 10 10 5 1
    1 6 15 20 15 6 1
    
    ......

```

Pascal's Triangle can be generated to any desired number of rows, and each row corresponds to the coefficients of the expanded binomial expression `(a + b)^n`, where n is the row number.


###### Here is the question

Create a function `def pascal_triangle(n)`: that returns a list of lists of integers representing the Pascal’s triangle of `n`:

* Returns an empty list if `n <= 0`
* You can assume `n` will be always an integer


```bash
 
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 

```
