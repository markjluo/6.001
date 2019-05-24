def isPalin(s):
    """Take a string as input,
        check if the string s is a palindrome"""

    def toChars(s):
        s = s.lower()
        ans = ''
        for letter in s:
            if letter in 'abcdefghijklmnopqrstuvwxyz':
                ans += letter
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print(isPalin('ALLLELLssLA'))
