import string
exclude = set(string.punctuation)
raw_string = "I am Sam Sam I am Do you like Green eggs and ham?"
trans_string = ''.join([ch for ch in raw_string if ch not in exclude])
list_string = trans_string.split(" ")

dic = {}
for str in list_string:
	dic[str]= dic[str] +1 if str in dic.keys() else 1 
print dic

		
