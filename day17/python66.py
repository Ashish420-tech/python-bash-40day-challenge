data ={"a":3,"b":1,"c":2}
result= dict(sorted(data.items(), key=lambda item: item[1]))
print(result)
