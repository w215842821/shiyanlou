
def compute(base,value):
    #base.append(value)
    #print(base)
    j = 0
    for i in base:
        j = j +i
    result =j +value
    print(result)

if __name__ == '__main__':
    testlist = (10,20,30)
    compute(testlist, 15)
    compute(testlist, 25)
    compute(testlist, 35)

