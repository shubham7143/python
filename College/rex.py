import re
def starts_ends_with(str1):
    res = re.match(r'^(r).*(s)$',str1)
    if res:
        print(res.group())
    else:
        print("None")
str1 = "regularexp is for Python developers"
starts_ends_with(str1)
str2 = "regularexp is for Python"
starts_ends_with(str2)