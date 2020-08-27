class Solution:
    def decodeString(self, s: str) -> str:
        """
        first thoughts:
        recursive solution
            when you find an open bracket, pass the character before it 
            as well as all the characters until the closing bracket into 
            the recursive function call
            need a stack (?) to keep track of current bracket depth
            this fixes edge cases like 2[abc2[a]ss], which would skip the ss
            if bracket depth was not accounted for when passing the substring

            while looping over the string, append all characters to return string up intil
            you hit a digit value?

        non-recursive would be easier to implement
            this reminds me of the pascal's triangle problem in a way, where it seemed as if
            a recursive implementation would be simpler but it was rather difficult
            to translate the understanding of the problem into code (because of return values)

            requires iterating over the original string
            when you encounter a digit, need to set some kind of flag? storing the data
            and parsing it into usable code is the issue here

            the problem is that it seems as if the string can be arbitrarily nested, and as such
            a recursive solution would (likely) be necessary to implement to pass all tests
        """
        # define a function that parses a string based on the given parameters and can be
        # called recursively

        def call(k: int, string: str) -> str:
            # print(k, string)
            if string.isalpha():
                return int(k) * string
            # iterate over the string until you find a digit, then proceed to the MATCHING bracket
            # this means we need to keep track of ther depth of the iterator (?)
            depth = 0
            i = 0
            res = []
            while i < len(string):
                # print(string)
                if string[i].isalpha():
                    res.append(string[i])
                    i += 1
                else:
                    # character is a digit
                    # so we loop until we find the closing bracket and pass both indices into a recursive call?
                    # first, we increment past the opening bracket (!) and save current i value

                    # this count value is needed for cases where the number is 10 or greater,
                    # where having 2 digits was causing the program to hang. It continues to iterate
                    # over the string until a non-digit is found and the amount of steps taken to
                    # find that character is stored for later use
                    count = 0
                    while string[i + 1].isnumeric():
                        count += 1
                        i += 1

                    j = i + 2
                    while j < len(string):
                        # print(f"depth: {depth}, i: {i}, j:{j}, curj: {string[j]}")
                        if string[j] == "[":
                            # increase the depth
                            depth += 1
                        elif string[j] == "]":
                            # check the depth
                            if depth == 0:
                                # we've found the matching bracket
                                # this means j is the end
                                # print(f"RECURSE: {string[i]}, {string[i+2:j]}")

                                # added "- count" so that 2+ digit integers could be processed
                                res.append(
                                    call(string[i - count: i + 1], string[i + 2:j]))
                                # when we find our target for recursion, increment i up to j + 1
                                # and break the inner j loop
                                i = j + 1
                                break
                            else:
                                # we're going up a level
                                depth -= 1
                        else:
                            # alpha characters are ignored for this recursive cehck portion
                            pass
                        # we're still checking the string one at a time
                        j += 1

            return "".join(res) * int(k)
        return call(1, s)


test = Solution()

ex1 = "3[a]2[bc]"
ex2 = "a2[cb3[a]d]ef4[g]"
ex3 = "10[leetcode]"

print(test.decodeString(ex1))
print(test.decodeString(ex2))
print(test.decodeString(ex3))
