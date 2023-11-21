def validPalindrome(s):
    if(s == s[::-1]):
        return True
    i, j = 0, len(s)-1
    while i<j:
        if s[i]!=s[j]:
            left_remove=s[i+1:j+1]
            right_remove=s[i:j]
            return left_remove==left_remove[::-1] or right_remove==right_remove[::-1]
        else:
            i+=1
            j-=1
    return True


s = input()
print(validPalindrome(s))
