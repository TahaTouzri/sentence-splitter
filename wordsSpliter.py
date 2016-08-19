import nltk
all_english_words = nltk.corpus.words.words('en')

#------------------------------------------------------------------
#   class with methods to generate the all possible
#   sequences tree
#------------------------------------------------------------------
class word_class:
    def __init__(self,upper_word,word,sentence):
        self.sentence = sentence
        self.word=word
        self.upper_word = upper_word
        self.branches = []
        #initializing branches
        self.all_first_significant_words()
        #remove incomplete branches
        self.clean_branches_list()

    def all_first_significant_words(self):
        sentence = self.sentence
        significant_words=[]
        significant_word=""
        for c in sentence:
            significant_word+=c
            if (significant_word in all_english_words)and((len(self.word)>1) or (len(significant_word)>1)):
                new_sentence = sentence.replace(significant_word,"",1)
                #print(new_sentence)
                w = word_class(self,significant_word,new_sentence)
                significant_words.append(w)
                if significant_word == sentence:
                    w1=w
                    while w1.upper_word:
                        w1=w1.upper_word
                    w1.branches.append(w)
        return significant_words
    def clean_branches_list(self):
        branches=[]
        i=0
        for w in self.branches:
            #print(w.word)
            branches.append([w.word])
            w1=w
            while w1.upper_word:
                #print(w1.word)
                w1=w1.upper_word
                branches[i].append(w1.word)
            branches[i] = list(reversed(branches[i]))
            del(branches[i][0])
            i+=1
        self.branches = branches

#------------------------------------------------------------------
#this function is entended to compute the probability of each
#sequence and to return the best sequence
#------------------------------------------------------------------
def best_hypothesis(text,hypothesis_list):
    bigrams = list(nltk.bigrams([word.lower() for word in text]))
    best  = hypothesis_list[0]
    max_p = 0
    for hypothesis in hypothesis_list:
        bg= list(nltk.bigrams(hypothesis))
        #count probability
        p=0
        for el in bg:
            p+=bigrams.count(el)
        p=p/(len(hypothesis))
        if p>max_p:
            max_p= p
            best = hypothesis
    return(best)
#------------------------------------------------------------------
#                          use example
#------------------------------------------------------------------
#sentence = "hello my dear"
sentence="whatisyourname"
text = nltk.corpus.genesis.words('english-kjv.txt')
print(text)
word=word_class(None,"",sentence)
hypothesis_list=word.branches
print("all hypothesis:")
for hyp in hypothesis_list:
    print(hyp)
    print("-------------------------------")
print("best hypothesis:")
print(best_hypothesis(text,hypothesis_list))
