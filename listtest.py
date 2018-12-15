import sys
short_name = []
long_name = []
#print(sys.argv)
for i in sys.argv[1:]:
    if len(i)<=3:
        short_name.append(i)
       # print(short_name)
    else:
        long_name.append(i)
       # print(long_name)
for v in short_name:
    print(v,end=' ')
print()
for j in long_name:
    print(j,end=' ')
print()
#print(short_name)
#print(long_name)


