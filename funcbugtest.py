result = 0
start = 1
end = 100

def compute():
    global start,end,result
    while start < (end+1):
        result += start
        start += 1
    print(result)

if __name__ == '__main__':
    compute()

