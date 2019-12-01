import pickle 
import pandas as pnd

pnd.set_option('display.expand_frame_repr', False)

fichier = '/home/chaqra/Dropbox/TEEEEEEEEEXTMINING/jyc_summarize/super_df4.pkl'

df = pickle.load(open( fichier, "rb" ))

df.columns

df[['Resume', 'text']]

# https://github.com/summanlp/textrank


text = df.text.values[2]
from summa import summarizer
resume = summarizer.summarize(text, language='french', ratio = 0.1)


len(text)
len(resume)
len(df.Resume.values[2])

print(df.Titre.values[2])
print(resume)

from summa import keywords
print(keywords.keywords(text, language='french', ratio = 0.01))



# texte issue de 20190903_PAR.pdf

# traitement: on vire les traits d'unions
text = """
La privatisation de la Française des Jeux (FDJ) est en marche. Dimanche, le mi- nistre de l’Economie, Bruno Le Maire, a annoncé qu’elle pourrait débuter « d’ici à la fin de l’année, sans doute avant la fois du mois de novembre ». L’Etat, qui détient aujourd’hui 72 % du capital de la FDJ, compte en effet réduire sa partici- pation à 20 % au sein de l’organisation de loteries. Un retrait qui va réduire à proportion les dividendes qu’il en perçoit en tant qu’actionnaire, et qui ont atteint 90 millions d’euros en 2017. Les actions qui seront cédées à des in- vestisseurs, mais aussi à des particu- liers, pourraient rapporter à l’Etat jusqu’à 1,5 milliard d’euros. Une somme qui doit alimenter le fonds consacré à l’innova- tion et l’industrie lancé par le ministère de l’Economie en 2018, doté de 10 mil- liards d’euros. Mais, à l’image d’Aéroports de Paris, dont la privatisation annoncée fait polémique au point d’avoir suscité un projet de référendum d’initiative parta- gée, le retrait partiel de l’Etat de la FDJ peut intriguer. Encore en 2019, le groupe annonçait un chiffre d’affaires en pro- gression, à 1,8 milliard d’euros. Pour Régis Juanico, député socialiste de la Loire, dommage, donc, de « brader un patrimoine national » au profit d’inves- tisseurs privés. Une valeur sûre L’Etat, lui, met en avant la nécessité de se désendetter et rappelle que la taxe sur les jeux d’argent, qui continue (et devrait continuer) de s’appliquer à la FDJ, rap- porte bien davantage que les dividendes (3,3 milliards d’euros l’an passé). Selon Mathieu Plane, économiste à l’Ob- servatoire français des conjonctures éco- nomiques, au lieu de conserver son ca- pital dans une valeur sûre telle que la FDJ, l’Etat décide de l’investir dans un fonds pour l’innovation dont les rende- ments – 200 à 300 millions d’euros, selon le gouvernement – devront être démon- trés. Alors que l’Etat souligne que les pri- vatisations aident au désendettement, Mathieu Plane estime qu’il « aurait mieux valu lever les 10 milliards d’euros sur les marchés » plutôt que de céder son capital à la FDJ, pour atteindre le même objec- tif. Grâce aux taux d’intérêt actuellement négatifs, « cela lui coûterait moins cher ». Autre risque mis en avant : la dérégu- lation d’une activité jusqu’ici encadrée par l’Etat pour surveiller, notamment, les phénomènes d’addiction au jeu. Un faux procès, d’après le gouvernement, qui rappelle que la FDJ sera régulée par l’Autorité des jeux en ligne. Mais pour l’économiste Christian Chavagneux, la loi du marché pourrait reprendre le des- sus. Les nouveaux investisseurs « ne se- ront intéressés que si les perspectives de profits sont croissantes », souligne-t-il sur le site Xerfi. A terme, poursuit-il, « deux voies sont offertes au gouver- nement pour les rassurer : augmenter le taux de retour aux joueurs pour les inciter à miser plus, avec des risques accrus d’addiction. Ou bien réduire les prélèvements fiscaux sur les mises, accroissant les bénéfices et poussant à la hausse le cours de l’action, mais au prix de recettes fiscales moindres pour l’Etat. » L’Etat pourrait perdre sur les deux tableaux
"""
text = text.replace('- ', '').replace('\n','')
resume = summarizer.summarize(text, language='french', ratio = 0.2)

len(text)
len(resume)
resume
