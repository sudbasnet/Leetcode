def nextPermutation(stringSoFar, letters):
    permutations = []
    if len(letters) <= 1:
        return [stringSoFar + letters]
    for i in range(len(letters)):
        permutations += nextPermutation(stringSoFar +
                                        letters[i], letters[:i] + letters[i+1:])
    return permutations


def allPermutations(string: str) -> list[str]:
    return nextPermutation("", string)


print(allPermutations("abc"))

# O(n!) time complexity
