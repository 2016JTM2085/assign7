#!/usr/bin/python -tt
#Code for Problem Statement 2

import random
import math
count=0
cnt=0
for num in range(1000):

	X,Y=(random.random()*2- 1, random.random()*2-1)
	d=int(abs(math.sqrt(X**2 + Y**2)))
	if (d==0):
		cnt+=1		
	else:
		continue
	
			
k=float(float(cnt)/1000)
k=k*100
print k
