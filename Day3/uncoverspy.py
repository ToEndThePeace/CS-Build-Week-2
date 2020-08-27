def uncover_spy(n, trust):
    """
    thinking hash tables -> pseudo-graph implementation
    this is a graph problem but not one that requires a graph class
    
    read in the data from trust in the format of
    {
        a: (trusts -> )[b, c, d, e, f],
        b: (trusts -> )[(NO ONE)]
    }
    AND
    {
        a: (trusted by -> )[b, c, d, e, f],
        b: (trusted by -> )[(NO ONE)]
    }
    with trusts and trusted_by dicts, we can easily solve this problem
    """
    trusts = {}
    trusted_by = {}
    seen = set()
    for i in trust:
        # i is a list [a, b] where person a trusts person b
        a, b = i
        if a not in seen:
            trusts[a] = []
            trusted_by[a] = []
            seen.add(a)
        trusts[a].append(b)
        if b not in seen:
            trusts[b] = []
            trusted_by[b] = []
            seen.add(b)
        trusted_by[b].append(a)
    for person in trusted_by:
        if len(trusts[person]) == 0 and len(trusted_by[person]) == n - 1:
            return person
    return -1
"""
n: 2
trust: [[1,2]]
2

n: 4
trust:
[[1,2], 
 [3,4]]
 -1

Input:
n: 3
trust:
[[1,3], 
 [2,3]]
Output:
3

Input:
n: 3
trust:
[[1,3], 
 [2,3], 
 [3,1]]
Output:
-1


Input:
n: 3
trust:
[[1,2], 
 [2,3]]
Output:
-1


Input:
n: 4
trust:
[[1,3], 
 [1,4], 
 [2,3], 
 [2,4], 
 [4,3]]
Output:
3


In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.

Example 1:

Input: n = 2, trust = [[1, 2]]
Output: 2
Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.
Example 2:

Input: n = 3, trust = [[1, 3], [2, 3]]
Output: 3
Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3, but Person 3 does not trust either Person 1 or Person 2. Thus, Person 3 is the spy.
Example 3:

Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
Output: -1
Explanation: Person 1 trusts Person 3, Person 2 trusts Person 3, and Person 3 trusts Person 1. Since everyone trusts at least one other person, there is no spy.
Example 4:

Input: n = 3, trust = [[1, 2], [2, 3]]
Output: -1
Explanation: Person 1 trusts Person 2, and Person 2 trusts Person 3. However, in this situation, we don't have any one person who is trusted by everyone else. So we can't determine who the spy is in this case.
Example 5:

Input: n = 4, trust = [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]]
Output: 3
Explanation: Person 1 trusts Person 3 and Person 4, Person 2 trusts Person 3 and Person 4, Person 4 trusts Person 3. Everyone trusts Person 3 but Person 3 does not trust anyone, so they are the spy.
[execution time limit] 4 seconds (py3)
"""