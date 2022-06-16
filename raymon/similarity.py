
#>>>>>>>> Similarity <<<<<<<<..................بايد اينجا کار کنم هنوز
#pip install sklearn

from sklearn.feature_extraction.text import TfidfVectorizer

documents = [open(f) for f in text_files]
tfidf = TfidfVectorizer().fit_transform(documents)
# no need to normalize, since Vectorizer will return normalized tf-idf
pairwise_similarity = tfidf * tfidf.T

corpus = ["I'd like an apple", 
...           "An apple a day keeps the doctor away", 
...           "Never compare an apple to an orange", 
...           "I prefer scikit-learn to Orange", 
...           "The scikit-learn docs are Orange and Blue"]                                                                                                                                                                                                   
vect = TfidfVectorizer(min_df=1, stop_words="english")                                                                                                                                                                                                   
tfidf = vect.fit_transform(corpus)                                                                                                                                                                                                                       
pairwise_similarity = tfidf * tfidf.T 

pairwise_similarity.toarray() 

import numpy as np     

arr = pairwise_similarity.toarray()     
np.fill_diagonal(arr, np.nan)                                                                                                                                                                                                                            

input_doc = "The scikit-learn docs are Orange and Blue"                                                                                                                                                                                                  
input_idx = corpus.index(input_doc)                                                                                                                                                                                                                      
input_idx                                                                                                                                                                                                                                                

result_idx = np.nanargmax(arr[input_idx])                                                                                                                                                                                                                
corpus[result_idx]           

n, _ = pairwise_similarity.shape                                                                                                                                                                                                                         
pairwise_similarity[np.arange(n), np.arange(n)] = -1.0

print(pairwise_similarity)

pairwise_similarity[input_idx].argmax()   

import nltk, string

from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt') # if necessary...


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]




print(cosine_sim('a little bird', 'a little bird'))
print(cosine_sim('a little bird', 'a little bird chirps'))
