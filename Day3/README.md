# Coding Challenges: Day 3

## [Pascal's Triangle](./pascalstriangle.py)

Given a non-negative integer `n`, generate all rows up to row `n` of Pascal's triangle.

>In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example Inputs:

``` python
1. 0
2. 1
3. 2
4. 3
5. 4
6. 10
```

Expected Outputs:

``` python
1. [ ]

2. [
    [1]
]

3. [
    [1],
    [1, 1]
]

4. [
    [1],
    [1, 1],
    [1, 2, 1]
]

5. [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1]
]

6. [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]
```
