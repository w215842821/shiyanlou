import sys

output_dict = {}

#jiang shuru d liebiao d yuansu zhuanhuan cheng zidian
def handle_data(i):
    j = i.split(':')
    output_dict[j[0]] = j[1]
    #print(output_dict)

def print_data(x,y):
    pass
    


if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print("ID:{} Name:{}".format(key, output_dict[key]))


    #print(output_dict)

