import sys

output_dict = {}
for i in sys.argv[1:]:
    j = i.split(':')
    #print(j)
    output_dict[j[0]] = j[1]
#print(output_dict)
for key,value in output_dict.items():
    print("ID:{} Name:{}".format(key,value))

