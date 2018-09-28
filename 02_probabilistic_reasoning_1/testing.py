import os
import datetime
import json
import pickle
import math


def prettyprint(dict):
    print(json.dumps(dict, indent=4))


def prettysave(dict):
    with open('prett.txt', 'w') as handle:
        handle.write(json.dumps(dict, indent=4))



print(datetime.datetime.now())

# main_folder = '20_newsgroups'
main_folder = 'mini_newsgroups'

cat_folders = os.listdir(main_folder)

# dictionary that contains a list of texts for each category. For training
docu_dict = {}
# dictionary for test data
test_dict = {}
#
concat_dict = {}
# list of unique words
vocab = []

# Document count regardless of category
doc_count = 0


def get_stop_words():
    with open('stop_words.txt', 'r') as handle:
        return handle.read().split()

stopwords = get_stop_words()

for folder in cat_folders:
    print("1")
    # files for a category
    files = os.listdir(os.path.join(main_folder, folder))

    fileindex = 0
    concat_txt = ''
    txtfiles = []
    testfiles = []

    for file in files:
        with open(os.path.join(main_folder, folder, file), 'r') as txtfile:
            try:
                txt = txtfile.read()

                # Clean up text
                # Get rid of header information
                txt = ' '.join(txt.split('\n\n')[1:])
                txt = txt.replace('>', '')

                if fileindex < 70:
                    fileindex += 1
                    concat_txt += txt
                    txtfiles.append(txt)

                    for word in txt.split():
                        if word not in stopwords:
                            if word not in vocab:
                                vocab.append(word)
                else:
                    testfiles.append(txt)
                doc_count += 1

            except UnicodeDecodeError:
                print('Error decoding and reading {}/{}/{}'.format(main_folder, folder, file))

    concat_dict[folder] = concat_txt
    docu_dict[folder] = txtfiles
    test_dict[folder] = testfiles

# print(len(all_txt.split()))


# get P(o|h)
def get_probs():
    for cat in cat_folders:
        # print(cat)
        prob_word_per_class[cat] = {}

        # Counts the number of words
        for word in vocab:
            prob_word_per_class[cat][word] = 1.0

        for word in concat_dict[cat].split():
            if word in vocab:
                prob_word_per_class[cat][word] += 1.0

        # Calculates probabilities
        for word in vocab:
            prob_word_per_class[cat][word] /= (len(concat_dict[cat]) + len(vocab))


prob_word_per_class = {}
get_probs()
with open('probs.pickle', 'wb') as handle:
    pickle.dump(prob_word_per_class, handle, protocol=pickle.HIGHEST_PROTOCOL)
prettysave(prob_word_per_class)
print(datetime.datetime.now())

# Generate P(H)
ph_values = {}
for cat, list in docu_dict.items():
    ph_values[cat] = len(list)/doc_count


# Finds group with max P(O | H) * P(H)
def guess(doc):
    max_group = 0
    max_p = 1
    for cat in cat_folders:
        # Calculates P(O | H) * P(H) for candidate group
        p = math.log(ph_values[cat])
        for word in doc.split():
            if word in vocab:
                p += math.log(prob_word_per_class[cat][word])
        if p > max_p or max_p == 1:
            max_p = p
            max_group = cat
    print(max_group)
    return max_group


def checkacc():
    right = 0
    wrong = 0
    total = 0
    for answer, docs in test_dict.items():
        print('Answer is {}. length of docs array is {}'.format(answer, len(docs)))
        for doc in docs:
            if guess(doc) == answer:
                right += 1
            else:
                wrong += 1
            total += 1
            print("In progress acc: " + str(right/total))
    print(right/total)
    return right/total
