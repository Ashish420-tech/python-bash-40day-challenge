text="programming"
duplicates = sorted({ch for ch in text if text.count(ch)>1})
print(duplicates)
