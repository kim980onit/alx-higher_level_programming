#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x element of a list.

    Args:
        my list (list): the list to print elements from X(int): thhe number element of my_list to print.
   Return:the number of elemnts printed.
   """
   ret = 0
   for i in range (x):
       try:
           print("{}".format(my_list[i]), end="")
           ret +=1
        exept indexError:
            break
   print("")
   return (ret)
