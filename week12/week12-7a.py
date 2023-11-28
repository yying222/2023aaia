#SOIT108_Base003
a = int(input())

ans = 0
for i in range(1, a+1):
    ans += i*i
    
print(ans, end='')