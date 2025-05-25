class Solution(object):
    def reverse(self, x):
        upper_limit=2**31-1
        lower_limit= -2**31
        if x>0:
            reversed_value=int(str(x)[::-1])
        else:
            negative=str(x)[0]
            string=str(x)[1:][::-1]
            reversed_value=int(negative+string)
        if reversed_value>upper_limit or reversed_value<lower_limit:
            return 0
        return reversed_value