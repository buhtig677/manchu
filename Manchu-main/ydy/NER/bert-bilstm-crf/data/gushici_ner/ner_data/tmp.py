import random

f1 = open("train.txt", "w+", encoding="utf-8")
f2 = open("test.txt", "w+", encoding="utf-8")

with open("train_gushici.data", "r+", encoding="utf-8")as f:
    data = f.read()
    data = data.split('\n\n')
    data = eval(str(data).replace("I","I-D").replace("B", "B-D"))
    train_data = random.sample(data, int(len(data) * 0.8))
    test_data = [i for i in data if i not in train_data]
    for i in train_data:
        f1.write(i)
        f1.write('\n\n')
    for i in test_data:
        f2.write(i)
        f2.write('\n\n')

f1.close()
f2.close()