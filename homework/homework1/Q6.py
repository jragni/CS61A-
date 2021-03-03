def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    counter = 1
    while(n != 1):
        print(n)
        if(n%2 == 0):
            n = n/2
        else:
            n = 3*n+1
        count+=1 

    return count



def hailstoneRecursive(n, count=1):
    if(n==1):
        return count
    elif(n%2 == 0):
        return hailstoneRecursive(n/2,count+1)
    else:
        return hailstoneRecursive(3*n+1,count+1)