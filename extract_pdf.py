import pandas
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter,TextConverter,XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
from io import StringIO
from os import listdir
from os.path import isfile, join
from pathlib import Path


class extract_pdf:
    def __init__(self, path):
        self.path = path
        self.allfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        # print(self.allfiles)

    def convert_pdf_to_txt(self):

        pdf_folder = Path(self.path)
        # print(self.allfiles)
        list_txt = list()
        for files in self.allfiles:
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            codec = 'utf-8'
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
            print(files)
            fp = open(pdf_folder / files, 'rb')
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            password = ""
            maxpages = 0
            caching = True
            pagenos = set()

            for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                          check_extractable=True):
                interpreter.process_page(page)

            text = retstr.getvalue()
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


toto = extract_pdf('./echantillons_pdf')
toto2 = toto.convert_pdf_to_txt()