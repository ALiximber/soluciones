import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

texto = input("Texto: ")
sentencias = sent_tokenize(texto)
resumen = ' '.join(sentencias[:2])
print("Resumen:", resumen)
