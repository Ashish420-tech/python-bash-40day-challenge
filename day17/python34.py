import string
text = "Hello, World"
clean ="".join(ch for ch in text if ch not in string.punctuation)
print(clean)
