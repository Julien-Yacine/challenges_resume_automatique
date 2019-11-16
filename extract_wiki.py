import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import re
from urllib.parse import unquote
import wikipediaapi
import pandas as pnd

class extract_portal_wikipedia:
    
    def __init__(self, url_portal):
        self.url_portal = url_portal
        
    def scrap_all_url_from_portal(self):
        super_links = []
        regexp = re.compile(r'page suivante')
        url = self.url_portal
        for k in range(0,2):
            print(k)
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "lxml")
            for i in soup.find_all(name='a', href=True):
                if regexp.search(str(i)):
                    #print(re.findall('href="(.*?)#', str(i)))
                    tmp_super_link = re.findall('href="(.*?)#', str(i))

                    tmp_super_link = re.sub('amp;', "", str(tmp_super_link))
                    super_links.append('https://fr.wikipedia.org/'+str(tmp_super_link)[2:-2])
                    break
            url = super_links[k]
            print(url)

        return super_links
        
    

    def extract_url(self,super_link):

        req = requests.get(super_link)
        soup = BeautifulSoup(req.text, "lxml")

        tmp_links = []
        urls = []

        for i in soup.find_all(name='li'):
            for link in i.find_all('a', href=True):
                tmp_links.append(link['href'])
        for i in tmp_links:
            article = re.findall('/wiki/(.*?)$', i)
            if article != []:
                urls.append(unquote(article[0]))
        return urls

    def extract_resumes(self, urls):
        resumes = []
        articles = [] 
        titres = [] 
        wiki_wiki = wikipediaapi.Wikipedia(language='fr', extract_format=wikipediaapi.ExtractFormat.WIKI) 
        for url in urls:
            print(f'je test {url}')
            resume = wiki_wiki.page(url)
            if resume.exists():
                print(f'{url} existe')
                resumes.append(re.sub("\\n", "", resume.summary))
                if resume.text!='' and resume.text != None:
                    article = resume.text
                    #article = re.search("\\n\\n", article).start()
                    article = re.sub('(\\n\\n).*(\\n)', "", article)
                    article = re.sub("\\n", "", article)
                    articles.append(article)
                else:
                    articles.append(resume.text) 
                titres.append(resume.title)
            else:
                print(f"{url} n'existe pas, on essaie donc {url.replace('_', ' ')}")
                resume = wiki_wiki.page(url.replace('_', ' '))

                if not resume.exists():
                    print(f"{url}  & {url.replace('_', ' ')} n'existe pas")
                    resume = None
                else:
                    resumes.append(re.sub("\\n", "", resume.summary))
                    if resume.text!='':
                        article = re.sub('(\\n\\n).*(\\n)', "", article)
                        article = re.sub("\\n", "", article)
                        articles.append(article)
                    else:
                        articles.append(resume.text) 
                    titres.append(resume.title)
            del(url)

        return  titres, resumes, articles



portail_economie = extract_portal_wikipedia('https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Portail:%C3%89conomie/Articles_li%C3%A9s')
print('Extraction des SUPERS URLS')
super_links = portail_economie.scrap_all_url_from_portal()
#print(super_links)
super_df = pnd.DataFrame()
print('Extraction du contenu des SUPERS URLS')
for super_link in super_links:
    print(super_link)
    url_economie = portail_economie.extract_url(super_link)
    resumes = portail_economie.extract_resumes(url_economie[4:])
    df = pnd.DataFrame(resumes)
    df_transpose = df.T
    df_transpose.columns = ['Titre', 'Resume', 'Texte']
    df_transpose['summary_lenght']=df_transpose['Resume'].apply(len)
    text=[]
    for i in enumerate(df_transpose['summary_lenght']):
        #print(i)
        #print(df_transpose.iloc[i[0],2][i[1]:])
        text.append(df_transpose.iloc[i[0],2][i[1]:])
    df_transpose['text']=text
    super_df = super_df.append(df_transpose)