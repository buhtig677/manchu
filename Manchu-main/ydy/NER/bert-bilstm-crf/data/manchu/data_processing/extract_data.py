import csv
from collections import Counter
id = 0
li = []
for tmp in ["train", 'dev', 'test']:
    # f1 = open(tmp + ".txt", "w+", encoding='utf-8')
    with open("ner_" + tmp + ".tsv", "r+", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter='\t')
        for i in reader:
            tmp_dic = {"id": str(id)}
            li.extend(i[0].split(' '))
            # tmp_label = i[1].split(' ')
            # tmp_labels = []
            # for j in tmp_label:
            #     if '-' in j:
            #         tmp_split_label = j.split('-')
            #         li.append(tmp_split_label[0])
            #         tmp_labels.append(tmp_split_label[1] + '-' + tmp_split_label[0])
            #     else:
            #         tmp_labels.append(j)
            # tmp_dic['labels'] = tmp_labels
            # f1.write(str(tmp_dic))
            # f1.write('\n')
            id += 1
# 使用Counter统计词频
word_counts = Counter(li)

print(word_counts)
# 输出结果将显示每个单词出现的次数
words = list(set(li))
print(len(words))
f2 = open("words.txt", "w+", encoding='utf-8')
for word in words:
    f2.write(word)
    f2.write('\n')


# with open("train.txt", "r", encoding="utf-8") as fp:
#     train_data = fp.read().split("\n")
# for i in train_data:
#     print(i)
#     eval(i)