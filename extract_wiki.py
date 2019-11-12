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
                urls.append(article)
        return urls

    def extract_resumes(self, urls):
        resumes = []
        articles = []
        for url in urls:
            print(f'Récupération résumés de {url}')
            try:
                resume = wikipedia.summary(url)
                if resume != '':
                    resumes.append(resume)
                    article = wikipedia.WikipediaPage(url).content
                    articles.append(article)
            except Exception:
                print(f'Je suis INCAPABLE DE RECUPERER {url}')
                pass
        return resumes, articles

portail_economie = extract_portal_wikipedia('https://fr.wikipedia.org/w/index.php?title=Cat%C3%A9gorie:Portail:%C3%89conomie/Articles_li%C3%A9s&from=B')
url_economie = portail_economie.extract_url()
resumes = portail_economie.extract_resumes(url_economie[0:20])