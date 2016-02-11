# print(' '.join(sorted('hiiiia', key=str.lower, reverse=True)))

# print(list(reversed(['a', 'b', 'c'])));

d = {}

d['test'] = 3
d['foo'] = 5
d['blah'] = 7
# print(sorted(d.values()))

dict_list = [(key, d[key]) for key in d.keys()]
print(dict_list)
print(list(d.items()))