"""Write a function that takes in a nonnegative integer and sums its digits. (Using floor division and modulo might be helpful here!)"""

def sum_digits(x):
    x_ = str(x)
    ans = 0
    for num in x_:
        ans += int(num)
    return ans 
print(sum_digits(125))    