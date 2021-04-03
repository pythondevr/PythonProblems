from datetime import datetime

"""
Using Dicts
takes more excution time as using dicts have more conditional statements
"""

start=datetime.now()
doors={}
for i in range(0,100):
	if doors.get(i)==None:
		doors[i]="closed"
	for j in range(i+1,101,i+1):
		if doors.get(j)=="closed":
			doors[j]="open"
		else:
			doors[j]="closed"
del doors[0]
end = datetime.now()
print(end-start)


"""
Using python Lists
Consumes less Execution Time as it doesnt have more conditional statements.
"""
start=datetime.now()
doors = [False]*101
for i in range(1,101):
	for j in range(i,101,i):
		doors[j]= not doors[j]
doors.pop(0)
end = datetime.now()
print(end-start)