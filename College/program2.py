# To calculate frequency of letters .

string = input()

set_string = list(set(string))
freq = {}

for i in set_string:
    freq[i] = string.count(i)


print(freq)
