#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: chaqra

"""

### Exemple de struture pour la definition d'une fonction 
### que j'avais decouverte dans ce mooc:
### https://fr.coursera.org/learn/program-code

# def nom_fonction(variable en entree):
#     """ (type(s) de variable(s) en entree) -> type de variables en sorties
# 
#     Condition prealable: condition sur les variables
# 
#     Description de la fonction 
# 
#     >>> nom_fonction(variable en entree)
#     resultat attendu
# 
#     """



def extraction_pdf(chemin_du_fichier):
    """ (string) -> list

    Cette fonction prend en entree la localisation d'un fichier pdf 
    et retourne en sortie une liste contenant les differentes parties
    textuelle du pdf. 

    >>>extraction_pdf("/home/chaqra/Dropbox/TEEEEEEEEEXTMINING/Journaux/20190830_PAR.pdf")

    """

import PyPDF2

chemin_du_fichier = "/home/chaqra/Dropbox/TEEEEEEEEEXTMINING/Journaux/20190830_PAR.pdf"

# https://automatetheboringstuff.com/chapter13/
pdfFileObj = open(chemin_du_fichier, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(3)
pageObj.extractText()


import subprocess
import os
import uuid

def document_to_html(file_path):
    tmp = "/tmp"
    guid = str(uuid.uuid1())
    # convert the file, using a temporary file w/ a random name
    command = "abiword -t %(tmp)s/%(guid)s.html %(file_path)s; cat %(tmp)s/%(guid)s.html" % locals()
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=os.path.join(settings.PROJECT_DIR, "website/templates"))
    error = p.stderr.readlines()
    if error:
        raise Exception("".join(error))
    html = p.stdout.readlines()
    return "".join(html)

document_to_html(chemin_du_fichier)


