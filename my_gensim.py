import jieba
import gensim
from gensim import corpora
from gensim import models
from gensim import similarities
from setting import  MONGODB

l1 = list(MONGODB.content.find())
all_doc_list = []
for doc in l1:
    doc_list=[word for word in jieba.cut_for_search(doc.get("title"))]
    all_doc_list.append(doc_list)
print(all_doc_list)
dictionary = corpora.Dictionary(all_doc_list)
print(dictionary)
corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
print(corpus)
lsi = models.LsiModel(corpus)
print(lsi)
index = similarities.SparseMatrixSimilarity(lsi[corpus],num_features=len(dictionary.keys()))


def my_xsjzxs(a):
    doc_test_list = [word for word in jieba.cut_for_search(a)]
    print(doc_test_list)
    doc_test_vec = dictionary.doc2bow(doc_test_list)
    print(doc_test_vec)
    sim = index[lsi[doc_test_vec]]
    print(sim)
    cc = sorted(enumerate(sim), key=lambda item: -item[1])
    if cc[0][1] >= 0.75:
        text = l1[cc[0][0]]
    else:
        text = None

    return text