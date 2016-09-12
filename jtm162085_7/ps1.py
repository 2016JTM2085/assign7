from collections import Counter
from operator import itemgetter
from itertools import *
l=list();
s=raw_input().split()
for item in (sorted(sorted(Counter(s).items()), key = itemgetter(1), reverse = True)[:3]):
    print item[0], item[1]

for i in s:
	k=len(i)
	for i in permutations(sorted(i),k):
    		l=i
	print "".join(l)
