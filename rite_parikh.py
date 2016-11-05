import sys
import string
import numpy
import cPickle
import numpy as np
import nltk

import pdb

classname = {'N':0, 'Y': 1,}
f1 = open('/data1/data/hansongbo/parikh_snli-master/raw_cs_cut_train', 'r')
f2 = open('/data1/data/hansongbo/parikh_snli-master/raw_cs_cut_test', 'r')
f = [f1, f2]


print "processing dataset: 2 dots to punch: ",
sys.stdout.flush()
w2 = {}
w_referred = {0: 0}  # reserve 0 for future padding
vocab_count = 1  # 0 is reserved for future padding
train_valid_test = []
for file in f:
    print ".",
    sys.stdout.flush()
    pairs = []
    lines = file.readlines()
    length = len(lines)
    i = 0
    while i < length:
        H = lines[i].strip().split('\t')[1]
        T = lines[i+1].strip().split('\t')[1]
        s1 = H.split(' ')
        s2 = T.split(' ')
        truth = classname[lines[i+2].strip()]
        i += 3 
	#print s1,s2,truth
        if truth != 3:  # exclude those '-' tags
            s1_words = []
            for word in s1:
                # strip some possible weird punctuations
                word = word.strip(string.punctuation)
                if not w_referred.has_key(word):
                    w_referred[word] = vocab_count
                    vocab_count += 1
                s1_words.append(w_referred[word])

            s2_words = []
            for word in s2:
                word = word.strip(string.punctuation)
                if not w_referred.has_key(word):
                    w_referred[word] = vocab_count
                    vocab_count += 1
                s2_words.append(w_referred[word])

            pairs.append((numpy.asarray(s1_words).astype('int32'),
                          numpy.asarray(s2_words).astype('int32'),
                          numpy.asarray(truth).astype('int32')))

    train_valid_test.append(pairs)
    file.close()

print "dumping converted datasets..."
save_file = open('/data1/data/hansongbo/parikh_snli-master/snli_1.0/RITE_ADD_GloVe_converted', 'wb')
cPickle.dump("dict: truth values and their corresponding class name\n"
             "the whole dataset, in list of list of tuples: list of train/valid/test set -> "
                "list of sentence pairs -> tuple with structure:"
                "(hypothesis, premise, truth class), all entries in numbers\n"
             "numpy.ndarray: a matrix with all referred words' embedding in its rows,"
                "embeddings are ordered by their corresponding word numbers.\n"
             "dict: the augmented GloVe word embedding. contains all possible tokens in SNLI."
                "All initial GloVe entries are included.\n"
             "dict w_referred: word to their corresponding number\n"
             "inverse of w_referred, number to words\n",
             save_file)

cPickle.dump(classname, save_file)
cPickle.dump(train_valid_test, save_file)
cPickle.dump(w_referred, save_file)
save_file.close()

