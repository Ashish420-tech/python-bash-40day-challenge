text = "Python Programming"
count = sum(1 for ch in text.lower() if ch in "aeiou")
print("Vowels:", count)
