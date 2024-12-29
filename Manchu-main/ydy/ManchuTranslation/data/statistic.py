from collections import Counter
tmp = []
with open("original_data.txt", "r", encoding="utf-8")as f:
    data = f.readlines()
    for i in data:
       tmp.append(i.split('\t')[0])

print(Counter(tmp))