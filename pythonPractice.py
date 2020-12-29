# Collections

# Counter
from collections import Counter


c = Counter('gallad')
print(c)
c = Counter(['1','1','2','3'])
print(c)
print(list(c.elements()))
c = Counter({'s': 1, 'b': 9})
print(c)
c = Counter(cats = 4, dogs=7)
print(c)
print(list(c.most_common(1)))