# Day 4

## [Merge Two Sorted Lists](./mergelinkedlists.py)

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

```python
1. [1, 2, 4],
   [1, 3, 4]
2. [0, 0, 2, 4, 7, 10],
   [0, 1, 1, 2, 3, 4, 4, 5, 20]
```

Expected Outputs:

```python
1. [1, 1, 2, 3, 4, 4]
2. [0, 0, 0, 1, 1, 2, 2, 3, 4, 4, 4, 5, 7, 10, 20]
```

## [Decode String](./decodestring.py)

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there won't be input like `3a` or `2[4]`.

Example Inputs:

```python
1. "3[a]2[bc]"
2. "a2[cb3[a]d]ef4[g]"
3. "10[leetcode]"
```

Expected Outputs:

```python
1. "aaabcbc"
2. "acbaaadcbaaadefgggg"
3. "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"
```
