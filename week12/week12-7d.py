# SOIT_108_Base_013
a = list(map(int,input().split()))

ans = 0
for i in a:
    if i>0: ans +=i
    
print(ans, end='')