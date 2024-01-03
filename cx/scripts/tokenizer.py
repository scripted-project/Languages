from nltk.tokenizer import word_tokenize

class Tokenizer:
    def lex(self, source: str):
        tokens = word_tokenize(source)
        
        