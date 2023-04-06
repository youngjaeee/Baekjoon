import math

a, b = map(int, input().split())
c = int(input())

hour = c//60
minute = c-(hour*60)

if b+minute <= 59:
    print((a+hour)%24, b+minute)
else:
    minute_p = (b+minute)%60
    hour = (a+hour+((b+minute)//60))%24
    print(hour, minute_p)