"""https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python"""

#Is it a palindrome?


def is_palindrome(s):
    if s.lower() == s.lower()[::-1]:
        return True
    else:
        return False