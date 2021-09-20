import numpy as np
import jieba

# 余弦法求相似度


def cosine_similarity(sentence1: str, sentence2: str) -> float:
    seg1 = [word for word in jieba.cut(sentence1)]
    seg2 = [word for word in jieba.cut(sentence2)]
    word_list = list(set([word for word in seg1 + seg2]))
    get_word_vector_1 = []
    get_word_vector_2 = []
    for word in word_list:
        get_word_vector_1.append(seg1.count(word))
        get_word_vector_2.append(seg2.count(word))
    vec_1 = np.array(get_word_vector_1)
    vec_2 = np.array(get_word_vector_2)
    try:
        norm = "false"
        assert len(vec_1) == len(vec_2), "len(x) != len(y)"
        zero_list = [0] * len(vec_1)

        res = np.array([[vec_1[i] * vec_2[i], vec_1[i] * vec_1[i], vec_2[i] * vec_2[i]] for i in range(len(vec_1))])
        cos = sum(res[:, 0]) / (np.sqrt(sum(res[:, 1])) * np.sqrt(sum(res[:, 2])))
        sim = 0.5 + 0.5 * cos if norm else cos
        return sim

    except ZeroDivisionError:
        print("NULL")
        return 0


if __name__ == '__main__':

        path1 = input("原本文件:")
        path2 = input("对比文件:")
        save_path = "C:/1/save.txt"

        try:
            f1 = open(path1, 'r', encoding='UTF-8')
            f2 = open(path2, 'r', encoding='UTF-8')
            str1 = f1.read()
            str2 = f2.read()
            result = cosine_similarity(str1, str2)
            print("相似度 ：%.4f" % result)
            f = open(save_path, 'w', encoding='utf-8')
            f.write("文章相似度：%.4f" % result)
            f.close()

        except FileNotFoundError:
            print("error")
