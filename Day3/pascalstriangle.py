from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        initialize a response array
        loop over the numRows, generating each row as we go
        edges maintain their values because 0 is being added
        """
        # initialize our response
        res = []

        # loop over every row, this catches the 0 case and returns empty
        for i in range(numRows):
            # first pass implementation with specific edge case handling
            # create a list for the current row
            #             cur = []

            #             # handle edge cases
            #             if i == 0:
            #                 cur = [1]
            #             elif i == 1:
            #                 cur = [1, 1]
            #             else:
            #                 # fill the current row
            #                 cur = [1]
            #                 for j in range(1, i):
            #                     cur.append(res[-1][j - 1] + res[-1][j])
            #                 cur.append(1)

            # secondary implementation using a specialized
            # try/except block to handle adding end numbers
            cur = [1]
            for j in range(i):
                try:
                    cur.append(res[-1][j] + res[-1][j + 1])
                except IndexError:
                    cur.append(1)

            # third implementation testing to see if checking [j + 1] index exists
            # as a way to handle edge cases
#             cur = [1]
#             for j in range(i):
#                 if len(res[-1]) <= j + 1:
#                     cur.append(1)
#                 else:
#                     cur.append(res[-1][j] + res[-1][j + 1])

            # append that list to the response
            res.append(cur)

        return res


def print_triangle(t):
    if len(t) == 0:
        print("[ ]")
        return
    print("[")
    for row in t:
        print("  ", row)
    print("]", end="\n\n")


test = Solution()

ex1 = 0
ex2 = 1
ex3 = 2
ex4 = 3
ex5 = 4
ex6 = 10

print_triangle(test.generate(ex1))
print_triangle(test.generate(ex2))
print_triangle(test.generate(ex3))
print_triangle(test.generate(ex4))
print_triangle(test.generate(ex5))
print_triangle(test.generate(ex6))
