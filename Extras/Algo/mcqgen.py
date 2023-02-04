from transformers import pipeline
ARTICLE = """
The term KDD stands for Knowledge Discovery in Databases. It refers to the broad procedure of discovering knowledge in data and emphasizes the high-level applications of specific Data Mining techniques. It is a field of interest to researchers in various fields, including artificial intelligence, machine learning, pattern recognition, databases, statistics, knowledge acquisition for expert systems, and data visualization.

The main objective of the KDD process is to extract information from data in the context of large databases. It does this by using Data Mining algorithms to identify what is deemed knowledge.

The Knowledge Discovery in Databases is considered as a programmed, exploratory analysis and modeling of vast data repositories.KDD is the organized procedure of recognizing valid, useful, and understandable patterns from huge and complex data sets. Data Mining is the root of the KDD procedure, including the inferring of algorithms that investigate the data, develop the model, and find previously unknown patterns. The model is used for extracting the knowledge from the data, analyze the data, and predict the data.

The availability and abundance of data today make knowledge discovery and Data Mining a matter of impressive significance and need. In the recent development of the field, it isn't surprising that a wide variety of techniques is presently accessible to specialists and experts.

The knowledge discovery process is iterative and interactive, comprises of nine steps. The process is iterative at each stage, implying that moving back to the previous actions might be required. The process has many imaginative aspects in the sense that one cant presents one formula or make a complete scientific categorization for the correct decisions for each step and application type. Thus, it is needed to understand the process and the different requirements and possibilities in each stage.

The process begins with determining the KDD objectives and ends with the implementation of the discovered knowledge. At that point, the loop is closed, and the Active Data Mining starts. Subsequently, changes would need to be made in the application domain. For example, offering various features to cell phone users in order to reduce churn. This closes the loop, and the impacts are then measured on the new data repositories, and the KDD process again. Following is a concise description of the nine-step KDD process, Beginning with a managerial step:


This is the initial preliminary step. It develops the scene for understanding what should be done with the various decisions like transformation, algorithms, representation, etc. The individuals who are in charge of a KDD venture need to understand and characterize the objectives of the end-user and the environment in which the knowledge discovery process will occur (involves relevant prior knowledge).

Once defined the objectives, the data that will be utilized for the knowledge discovery process should be determined. This incorporates discovering what data is accessible, obtaining important data, and afterward integrating all the data for knowledge discovery onto one set involves the qualities that will be considered for the process. This process is important because of Data Mining learns and discovers from the accessible data. This is the evidence base for building the models. If some significant attributes are missing, at that point, then the entire study may be unsuccessful from this respect, the more attributes are considered. On the other hand, to organize, collect, and operate advanced data repositories is expensive, and there is an arrangement with the opportunity for best understanding the phenomena. This arrangement refers to an aspect where the interactive and iterative aspect of the KDD is taking place. This begins with the best available data sets and later expands and observes the impact in terms of knowledge discovery and modeling.

Now, we are prepared to include the knowledge into another system for further activity. The knowledge becomes effective in the sense that we may make changes to the system and measure the impacts. The accomplishment of this step decides the effectiveness of the whole KDD process. There are numerous challenges in this step, such as losing the "laboratory conditions" under which we have worked. For example, the knowledge was discovered from a certain static depiction, it is usually a set of data, but now the data becomes dynamic. Data structures may change certain quantities that become unavailable, and the data domain might be modified, such as an attribute that may have a value that was not expected previously.

"""

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summarized_text = summarizer(ARTICLE, max_length=1200, min_length=100, do_sample=False)

text = summarized_text[0].get('summary_text')
full_text = ARTICLE

import pke
import string
import spacy

nlp = spacy.load('en_core_web_sm')

# 1. create a MultipartiteRank extractor.
extractor = pke.unsupervised.MultipartiteRank()

stoplist = list(string.punctuation)
stoplist += pke.lang.stopwords.get('en')

# 2. load the content of the document.
extractor.load_document(input=nlp(full_text))

# 3. select the longest sequences of nouns and adjectives, that do
#    not contain punctuation marks or stopwords as candidates.
pos = {'NOUN', 'PROPN', 'ADJ'}
extractor.candidate_selection(pos=pos)

# 4. build the Multipartite graph and rank candidates using random
#    walk, alpha controls the weight adjustment mechanism, see
#    TopicRank for threshold/method parameters.
# extractor.candidate_weighting(alpha=1.1,
#                               threshold=0.74,
#                               method='average')
                              
extractor.candidate_weighting(alpha=1.5,
                              threshold=0.5,
                              method='average')

# 5. get the 10-highest scored candidates as keyphrases
keyphrases = extractor.get_n_best(n=5)
print(keyphrases)

import pprint
import itertools
import re
import pke
import string
from nltk.corpus import stopwords

def get_nouns_multipartite(text):
    out=[]
    # print('1')
    extractor = pke.unsupervised.MultipartiteRank()
    # print('1')
    # extractor.load_document(input=text)
    extractor.load_document(input=nlp(full_text))
    # print('1')
    #    not contain punctuation marks or stopwords as candidates.
    pos = {'PROPN'}
    #pos = {'VERB', 'ADJ', 'NOUN'}
    stoplist = list(string.punctuation)
    stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
    stoplist += stopwords.words('english')
    # extractor.candidate_selection(pos=pos, stoplist=stoplist)
    extractor.candidate_selection(pos=pos)
    # 4. build the Multipartite graph and rank candidates using random walk,
    #    alpha controls the weight adjustment mechanism, see TopicRank for
    #    threshold/method parameters.
    extractor.candidate_weighting(alpha=1.1,
                                  threshold=0.75,
                                  method='average')
    keyphrases = extractor.get_n_best(n=20)

    for key in keyphrases:
        out.append(key[0])

    return out

keywords = get_nouns_multipartite(full_text) 
print (keywords)
filtered_keys=[]
for keyword in keywords:
    if keyword.lower() in text.lower():
        filtered_keys.append(keyword)
        
print (filtered_keys)


# Extra
# filtered_keys = keywords

from nltk.tokenize import sent_tokenize
from flashtext import KeywordProcessor

def tokenize_sentences(text):
    sentences = [sent_tokenize(text)]
    sentences = [y for x in sentences for y in x]
    # Remove any short sentences less than 20 letters.
    sentences = [sentence.strip() for sentence in sentences if len(sentence) > 20]
    return sentences

def get_sentences_for_keyword(keywords, sentences):
    keyword_processor = KeywordProcessor()
    keyword_sentences = {}
    for word in keywords:
        keyword_sentences[word] = []
        keyword_processor.add_keyword(word)
    for sentence in sentences:
        keywords_found = keyword_processor.extract_keywords(sentence)
        for key in keywords_found:
            keyword_sentences[key].append(sentence)

    for key in keyword_sentences.keys():
        values = keyword_sentences[key]
        values = sorted(values, key=len, reverse=True)
        keyword_sentences[key] = values
    return keyword_sentences

sentences = tokenize_sentences(full_text)
# sentences = tokenize_sentences(summarized_text)
keyword_sentence_mapping = get_sentences_for_keyword(filtered_keys, sentences)
        
print(keyword_sentence_mapping)

import requests
import json
import re
import random
from pywsd.similarity import max_similarity
from pywsd.lesk import adapted_lesk
from pywsd.lesk import simple_lesk
from pywsd.lesk import cosine_lesk
from nltk.corpus import wordnet as wn

# Distractors from Wordnet
def get_distractors_wordnet(syn,word):
    distractors=[]
    word= word.lower()
    orig_word = word
    if len(word.split())>0:
        word = word.replace(" ","_")
    hypernym = syn.hypernyms()
    if len(hypernym) == 0: 
        return distractors
    for item in hypernym[0].hyponyms():
        name = item.lemmas()[0].name()
        #print ("name ",name, " word",orig_word)
        if name == orig_word:
            continue
        name = name.replace("_"," ")
        name = " ".join(w.capitalize() for w in name.split())
        if name is not None and name not in distractors:
            distractors.append(name)
    return distractors

def get_wordsense(sent,word):
    print(sent,word)
    word= word.lower()
    
    if len(word.split())>0:
        word = word.replace(" ","_")
    
    print('sysnset before',word)
    # synsets = wn.synsets(word)
    synsets = wn.synsets(word,'n')
    print('synsets',synsets)
    if synsets:
        wup = max_similarity(sent, word, 'wup', pos='n')
        adapted_lesk_output =  adapted_lesk(sent, word, pos='n')
        lowest_index = min (synsets.index(wup),synsets.index(adapted_lesk_output))
        return synsets[lowest_index]
    else:
        return None

# Distractors from http://conceptnet.io/
def get_distractors_conceptnet(word):
    word = word.lower()
    original_word= word
    if (len(word.split())>0):
        word = word.replace(" ","_")
    distractor_list = [] 
    url = "http://api.conceptnet.io/query?node=/c/en/%s/n&rel=/r/PartOf&start=/c/en/%s&limit=5"%(word,word)
    obj = requests.get(url).json()

    for edge in obj['edges']:
        link = edge['end']['term'] 

        url2 = "http://api.conceptnet.io/query?node=%s&rel=/r/PartOf&end=%s&limit=10"%(link,link)
        obj2 = requests.get(url2).json()
        for edge in obj2['edges']:
            word2 = edge['start']['label']
            if word2 not in distractor_list and original_word.lower() not in word2.lower():
                distractor_list.append(word2)
    
    print('conceptnet',word,distractor_list)
    return distractor_list

key_distractor_list = {}

print(keyword_sentence_mapping.keys())
for keyword in keyword_sentence_mapping:
    wordsense = get_wordsense(keyword_sentence_mapping[keyword][0],keyword)
    print('i',wordsense)
    if wordsense:
        distractors = get_distractors_wordnet(wordsense,keyword)
        if len(distractors) ==0:
            distractors = get_distractors_conceptnet(keyword)
        if len(distractors) != 0:
            key_distractor_list[keyword] = distractors
    else:
        
        distractors = get_distractors_conceptnet(keyword)
        if len(distractors) != 0:
            key_distractor_list[keyword] = distractors

print('kdl',key_distractor_list)
index = 1
print ("#############################################################################")
print ("NOTE::::::::  Since the algorithm might have errors along the way, wrong answer choices generated might not be correct for some questions. ")
print ("#############################################################################\n\n")
for each in key_distractor_list:
    sentence = keyword_sentence_mapping[each][0]
    pattern = re.compile(each, re.IGNORECASE)
    output = pattern.sub( " _______ ", sentence)
    print ("%s)"%(index),output)
    choices = [each.capitalize()] + key_distractor_list[each]
    top4choices = choices[:4]
    random.shuffle(top4choices)
    optionchoices = ['a','b','c','d']
    for idx,choice in enumerate(top4choices):
        print ("\t",optionchoices[idx],")"," ",choice)
    print ("\nMore options: ", choices[4:20],"\n\n")
    index = index + 1