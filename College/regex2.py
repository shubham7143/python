import re

target_string = "My name is maximums and my luck numbers are 12 45 78"
# split on white space
word_list = re.split(r"\s+", target_string)
print(word_list)

target_string = "12-45-78"
result_string = re.split(r"\D", target_string, maxsplit=1)
print(result_string)
result = re.split(r"\D", target_string, maxsplit=3)
print(result)

target_string = "12,45,78,85-17-89"
result = re.split(r"-|,", target_string)
print(result)

target_string = "Python dot.com;is for,Python-developer"
result = re.split(r"[-;,.\s]\s*", target_string)
print(result)
