yr = int(input("Enter Year:"))
mm = int(input("Enter Month (number) :"))
month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
         7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
cen = int(yr / 100)
ye = yr - 100 * cen
if mm == 1 or mm == 2:
    mon=mm+10
    ye = ye - 1
    week = (1 + int(2.6 * mon - .2) - 2 * cen + ye + int(ye / 4) + int(cen / 4)) % 7
else:
    mon = mm -2
    week = (1 + int(2.6 * mon - .2) - 2 * cen + ye + int(ye / 4) + int(cen / 4))%7

nly =[31, 28, 31, 30, 31, 30,
      31, 31, 30, 31, 30, 31]
ly =[31, 29, 31, 30, 31, 30,
     31, 31, 30, 31, 30, 31]
ld=0
if yr%4==0:
    ld=ly[mm-1]
else:
    ld = nly[mm-1]
print(month[mm], yr)
print("Su Mo Tu We Th Fr Sa")
d = 0-week
for i in range(5):

    for j in range(7):
        if d<0:
            print("  ", end=' ')
        elif d<=(ld-1):
            if float(d/9)<1:
                print(d + 1, end='  ')
            else:
                print(d + 1, end=' ')
        else:
            print("  ", end=' ')
        d += 1
    print()