# Useful python tools

```python
# flatten list of list
list(itertools.chain.from_iterable(list_of_lists))
# Cartesian product
itertools.product()
# char to number, number to char
ord(c)
chr(number)
# is number
isnumeric()
```

```python
from collections import defaultdict, Counter

input_string = "hello world"

# 3. Using collections.Counter
dict_cnt = Counter(input_string)

# 2. Using defaultdict(int)
dict_cnt = defaultdict(int)
for char in input_string:
    dict_cnt[char] += 1

# 1. Using for...in (with a regular dictionary)
dict_cnt = {}
for char in input_string:
    dict_cnt:
        dict_cnt[char] += 1
    else:
        dict_cnt[char] = 1
```