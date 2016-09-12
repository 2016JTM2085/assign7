
import string
import random

print "1. Add"
print "2. Delete"
print "3. modify"
print "4. show"
print "5. Exit "
k=int(raw_input());

d=dict();
l=list();

while True:
	print "enter value of choice"
	k=int(raw_input());
	if (k==1):
		print "enter name"
		name=str(raw_input());
		d.setdefault(name, [])
		print "City: ",
		city=raw_input();
		print "District:",
		dist=raw_input()
		print "State : ",
		state=raw_input();
		d[name].append(city)
		d[name].append(dist)
		d[name].append(state)
		continue

	if (k==2):
		name=raw_input();
		for name in d:
			del d[name]
                continue

	if (k==3):
		name=raw_input().strip();
		for name in d:
			del d[name]
		d.setdefault(name, [])
		print "City: ",
		city=raw_input();
		print "District:",
		dist=raw_input()
		print "State : ",
		state=raw_input();
		d[name].append(city)
		d[name].append(dist)
		d[name].append(state)
		continue

	if (k==4):
		name=raw_input();
		l=d[name]
		for var in l:
			print var
		continue
		
	if (k==5):
		break


print "enter name for which to generate collection center no."
name=raw_input();
for name in d.keys():
	l=d[name]
	for values in l:
		a=str(bin(int(random.random()*10)))[2:]
		print values, 
		print " = ",  
		print a
		a+=a

CC_NO=a		
print "CC_NO" , a

print "enter name for which to generate collection center no."
name=raw_input();
b=list();
for name in d.keys():
	l=d[name]
	for var in l:
		var=var[0:3]
		b.append(var.upper())		
	b.append(CC_NO)	
	print "H_CC_NO = " , "_".join(b);



