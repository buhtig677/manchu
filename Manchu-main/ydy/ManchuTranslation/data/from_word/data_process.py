
characters = [i for i in "abcdefghijklmnopqrstuvwxyz"]
numbers = [i for i in "0123456789"]


def clean(words):
    manchu_translation = []
    others = []
    for word_interpretation in words:
        word = ""
        flag = 0
        for ind, character in enumerate(word_interpretation):
            if character == " " or character == "," or character in characters:
                word += character
            else:
                flag = ind
                break
        interpretation = word_interpretation[flag:]
        if "？" not in interpretation and "!" not in interpretation:  # 粗略的过滤，带有？的都不要了
            for e in interpretation.split('。'):
                if '.' in e:
                    manchu_translation.append(e)
                else:
                    if e != '\n':
                        others.append(e)
    corpus = []
    for m_t in manchu_translation:
        manchu = ""
        translation = ""
        if m_t.find("》") != -1:
            translation = m_t[::-1][:m_t[::-1].find("》")][::-1]  # 找到译文
        else:
            continue
        m_t = m_t.replace(translation, "")
        if m_t.find("《") != -1:
            m_t = m_t[:m_t.find("《")]  # 译文前一般有《》
        m_t = m_t[::-1]
        if m_t.find("：") != -1:
            manchu = m_t[:m_t.find("：")].strip(' ')[::-1]
        else:
            if m_t.find(":") != -1:
                manchu = m_t[:m_t.find(":")].strip(' ')[::-1]
            else:
                if m_t.find("；") != -1:
                    manchu = m_t[:m_t.find("；")].strip(' ')[::-1]
                else:
                    manchu = m_t[::-1]
        if len(manchu) > 0 and len(translation) > 0:
            corpus.append(manchu + "\t\t" + translation)
    f1 = open("manchu_translation.txt", 'w+',encoding="utf-8")
    print(len(corpus))
    print(len(list(set(corpus))))
    for c in corpus:
        f1.write(c.strip('\n'))
        f1.write('\n')

def clean_all(words):

    #首先清洗出单词
    manchu_translation = []
    others = []
    for word_interpretation in words:
        word = ""
        flag = 0
        for ind, character in enumerate(word_interpretation):
            if character == " " or character == "," or character in characters:
                word += character
            else:
                flag = ind
                break
        interpretation = word_interpretation[flag:]
        if "？" not in interpretation and "!" not in interpretation:  # 粗略的过滤，带有？的都不要了
            for e in interpretation.split('。'):
                if '.' in e:
                    manchu_translation.append(e)
                else:
                    if e != '\n':
                        others.append(e)

    pass

if __name__ == "__main__":

    with open("original_words_set.txt", "r", encoding="utf-8")as f:
        num = 0
        words = f.readlines()

    # words = ["sargan zhui shurgeme dargime chikirshame manggashame,gorokon ilifi emu gisun tuchikekuu.《11·聊》女子战战兢兢、羞羞缩缩，远远站着一言不发。[女战惕羞缩，遥立不作一语。]"]
    # words = ["choohan [名]师（《易》六十四卦之一）：na muke,choohan ohobi.《34·易》地水为师。"]
    # words = ["darabumbi [不及]让酒，敬酒，劝酒，把酒，酻：nure darabuki.《47·问》敬酒吧！huuntahan tukiyefi antaha de darabumi( darabume).《50·其》举杯给客人敬酒。uthai amba choman i nure darabuha.《11·聊》乃以大觥劝酒。"]
    clean_all(words)

