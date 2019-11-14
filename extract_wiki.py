import wikipedia
import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import re


class extract_portal_wikipedia:
    
    def __init__(self, url_portal):
        self.url_portal = url_portal

    def extract_url(self):

        req = requests.get(self.url_portal)
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
                resumes.append(resume.summary)
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
                    resumes.append(resume.summary)
                    if resume.text!='':
                        article = re.sub('(\\n\\n).*(\\n)', "", article)
                        article = re.sub("\\n", "", article)
                        articles.append(article)
                    else:
                        articles.append(resume.text) 
                    titres.append(resume.title)
            del(url)

        return  titres, resumes, articles



portail_economie = extract_portal_wikipedia('https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Portail:%C3%89conomie/Articles_li%C3%A9s&from=B')
url_economie = portail_economie.extract_url()
resumes = portail_economie.extract_resumes(url_economie[0:20])