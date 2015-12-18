import string
from operator import mul
from itertools import chain

values = {j:i+1 for i,j in enumerate(string.ascii_lowercase)}
path = 'p022_names.txt'

with open(path, 'r') as f:
    names = f.next().replace('"','').split(',')

names.sort()
converted = [(i+1,[values[k.lower()] for k in j]) for i,j in enumerate(names)]
print sum([i[0] * sum(i[1]) for i in converted])
