#wap to make dictionary.

dict = {"python":"programming language", "list":"list is a collection of data", 
"tuple":"tuple is like list but it is immutable", "string":"string is an array of characters"}

key = input("Enter word in lower case: ")

print(dict.get(key))