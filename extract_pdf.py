# librairie globales
import io
from io import StringIO
from os import listdir
from os.path import isfile, join
from pathlib import Path
import pandas

# pour convert_pdf_to_txt
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter,TextConverter,XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

# pour prepare_sentence
import nltk, os, subprocess, code, glob, re, traceback, sys, inspect
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


class extract_pdf:

    def __init__(self, path, langage="french"):
        self.path = path
        self.allfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        print(self.allfiles)
        self.langage = langage

    def convert_pdf_to_txt(self):

        pdf_folder = Path(self.path)
        # print(self.allfiles)
        list_txt = list()
        for files in self.allfiles:
            rsrcmgr = PDFResourceManager()
            retstr = BytesIO()
            codec = 'utf-8'
            laparams = LAParams()
            device = HTMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
            print(files)
            fp = open(pdf_folder / files, 'rb')
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            password = ""
            maxpages = 0
            caching = True
            pagenos = set()
            # text = files
            for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                          check_extractable=True):
                interpreter.process_page(page)

            text = retstr.getvalue()
            text = text.decode('utf-8')
            print("Longueur du doc : ")
            print(len(text))
            print("Début du doc : ")
            print(text[1:100])
            list_txt.append(text)
            print(len(list_txt))
            fp.close()
            device.close()
            retstr.close()

        return list_txt

    def prepare_sentence(self, list_txt):

        stop_words = set(stopwords.words(self.langage))
        clean_text_list = list()
        # Retrait de la ponctuation
        # text = re.sub('[^a-zA-Z]', ' ', sentence)
        for sentence in list_txt:
            print("Longueur du doc de base : ")
            print(len(sentence))
            print("Début du doc de base : ")
            print(sentence[1:100])
            # Conversion en minuscule
            text = sentence.lower()

            # Retrait des tags
            text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)

            # Retrait des numéros et caractères spéciaux
            text = re.sub("(\\d|\\W)+", " ", text)

            # Conversion en liste
            text = text.split()

            text = [word for word in text if not word in
                                                 stop_words]
            text = " ".join(text)
            print("Longueur du doc : ")
            print(len(text))
            print("Début du doc : ")
            print(text[1:100])
            clean_text_list.append(text)
        return clean_text_list

    def export_text(self, list_txt):

        for sentence in list_txt:
            text_file = open("./sample.txt", "w")
            n = text_file.write(sentence)
            text_file.close()

    def extract_specific_text(self, list_txt, type_of_text):

        if type_of_text == 'title':
            regex = r'HelveticaNeueLTStd-Md\'; font-size:41px">(.*?)\n<br></span></div>'
        if type_of_text == 'paragraph':
            regex = r'DINOT-Regular\'; font-size:11px">(.*?)</span><span style="font-family: b\'BYVFCF+'
        list_specific_t = list()
        for sentence in list_txt:
            elements_to_grep = re.findall(regex, sentence, re.DOTALL)
            list_specific_t.append(elements_to_grep)
        return list_specific_t

extract20min = extract_pdf('./echantillons_pdf/')
text_html = extract20min.convert_pdf_to_txt()
title20min = extract20min.extract_specific_text(text_html,'title')
paragraph20min = extract20min.extract_specific_text(text_html,'paragraph')
