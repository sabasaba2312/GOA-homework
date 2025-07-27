def get_middle(s):
    if len(s) % 2 == 0:
        left = len(s)//2 - 1
        right = len(s)//2
        return s[left:right+1]
    else:
        mid = len(s)//2
        return s[mid]