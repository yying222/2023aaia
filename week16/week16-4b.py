#SOIT107_ADVANCE_015
a, b = list(map(int,input().split()))

for i in range(a, b+1):
	if i%7==0:
		print(i, end=' ')