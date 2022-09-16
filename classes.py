#import 

class Words:
    #punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    interesting_words = {}
    def __init__(self, file_contents):
        self.file_contents = file_contents
    
    def clean(self):
        words = self.file_contents.split()
        clean_words = []
        for word in words:
            word = word.strip()
            clean_word = ''
            for i in word:
                if i.isalnum():
                  clean_word += i 
            if clean_word == '': continue 
            clean_words.append(clean_word.lower())
        return clean_words 


    def count_words(self, words):
        for word in words:
            if word not in self.interesting_words and word not in self.uninteresting_words:
                self.interesting_words.update({word : 1})
            elif word in self.interesting_words and word not in self.uninteresting_words:    
                  self.interesting_words[word]+=1
            else: pass   
        return self.interesting_words

    def bild_dict(self):
        return self.count_words(self.clean())


