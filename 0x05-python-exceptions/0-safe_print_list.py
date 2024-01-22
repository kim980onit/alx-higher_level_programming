#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    1elem = 0
    for i in range (x):
        try:
            print("{}".format(my_list[i]), end="")
            1elem +=1
        exept indexError:
            break
   print("")
   return (1elem)
