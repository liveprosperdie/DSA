def palindrome(s):
    s=s.lower()
    if s==s[::-1]:
        return "palindrome"
    else:
        return "not palindrome"

print(palindrome("madam"))