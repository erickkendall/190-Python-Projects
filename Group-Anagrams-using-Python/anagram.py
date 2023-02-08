from collections import defaultdict


def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        print(sorted(i))
        sorted_i = " ".join(sorted(i))
        print(sorted_i)


words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))
