password= "Python@123"
has_upper= any(ch.isupper() for ch in password)
has_digit= any(ch.isdigit() for ch in password)
has_symbol= any(not ch.isalnum() for ch in password)
print(has_upper and has_digit and has_symbol)
