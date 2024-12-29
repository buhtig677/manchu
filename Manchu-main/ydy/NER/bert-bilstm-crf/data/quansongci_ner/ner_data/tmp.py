import random

f1 = open("train.txt", "w+", encoding="utf-8")
f2 = open("test.txt", "w+", encoding="utf-8")

with open("train_quansongci.data", "r+", encoding="utf-8")as f:
    data = f.read()
    data = data.split('\n\n')
    data = eval(str(data).replace("I","I-D").replace("B", "B-D"))
    train_data = random.sample(data, int(len(data) * 0.8))
    test_data = [i for i in data if i not in train_data]
    flag = 0
    for i in train_data:
        tmp_dic = {"id": str(flag), "text": [], "labels": []}
        for j in i.split('\n'):
            tmp_dic["text"].append(j.split(' ')[0])
            tmp_dic["labels"].append(j.split(' ')[1])
        f1.write(str(tmp_dic))
        f1.write('\n')
        flag += 1
    for i in test_data:
        tmp_dic = {"id": str(flag), "text": [], "labels": []}
        for j in i.split('\n'):
            tmp_dic["text"].append(j.split(' ')[0])
            tmp_dic["labels"].append(j.split(' ')[1])
        f2.write(str(tmp_dic))
        f2.write('\n')
        flag += 1

f1.close()
f2.close()