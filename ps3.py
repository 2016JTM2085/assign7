
import string

print "1. Add"
print "2. Delete"
print "3. modify"
print "4. show"
print "5. Exit "
k=int(raw_input());

d=dict();

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
		print "do you want to add(Y/N)"
		j=raw_input();
		if (j==Y):
			continue
		else:
			break
		
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
		print d[name]
		continue
		
	if (k==5)
		break

l=list();
print "enter name for which to generate collection center no."
name=raw_input();
for name in d:
	l=d[name]
	for values in l:
		a=str(bin(random.random()*10))[2:]
		print values , " = " a
		a+=a
		
print "CC_NO" , a

print "enter name for which to generate collection center no."
name=raw_input();
b=list();
for name in d:
	l=d[name]
	for var in l:
		var=var[0:3]
		b.append(var.upper())		
		
	print "H_CC_NO = " , "_".join(b);



