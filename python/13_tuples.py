"""
Note:
The output of hash() depends on the Python version and implementation.
This solution is correct, but the hash value may differ from the sample output
shown on HackerRank or from older Python versions.
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))