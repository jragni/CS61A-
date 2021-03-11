"""Write a function that takes in a number and determines if there are two 8s in a row"""


def double_eights(n):
    for i in range(1,len(str(n)):
        j = i-1
        if(n[i]==8 and n[j] == n[i]):
            return True

    return False
    