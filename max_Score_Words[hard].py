words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

alpha = [chr(65+i).lower() for i in range(0,26)]
score_dict = dict(zip(alpha,score))

for idx in range(0,len(words)):
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","d","g","o","o"]
    word = words[idx]
    other_words = words
    other_words.remove(word)
    max_words = max_word(word,other_words)
    
def max_word(word,other_words):
    for i in letters:
        if i in word:
            letters.remove(i)
        else:
            return 0
    for w in other_words:
        max_words = ''
        if len(letters) <len(w) and len(other_words)>0:
            continue
        elif len(other_)
        for l in letters:





