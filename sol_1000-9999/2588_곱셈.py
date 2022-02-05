# 2588_곱셈
import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

c1 = b//100 #b의 백의자리
c2 = (b - c1*100)//10 # b의 십의자리
c3 = (b - c1*100 - c2*10) #b의 일의자리

print(a*c3)
print(a*c2)
print(a*c1)
print(a*b)