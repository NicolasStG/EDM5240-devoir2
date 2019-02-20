# coding: utf-8

### Bravo pour ce script bien documenté!
### Et qui fonctionne parfaitement bien!

#import json #J'ai remarqué qu'il n'était pas nécessaire, parce que la fonction get permet de lire le json déjà.
import csv
import requests

fichier = "banq.csv"

### Wow! Bravo pour cette utilisation d'une fonction «custom»! :)
def lien_url(banq):
        mon_dict = banq["bitstreams"]["racine"]["fils"][0]["formats"][0]
        if "url" in mon_dict:
            return(mon_dict["url"])
        else:
            return("")

entete = {
    "User-Agent":"Nicolas St-Germain - 438/492-2926",
    "From":"niikostg@gmail.com"
}

h = 999
with open(fichier,"w") as f2:
    creation_fichier = csv.writer(f2,)
    for i in range(1000,2001):
        url = "http://collections.banq.qc.ca/api/service-notice?handle=52327/" + str(i)
        req = requests.get(url,headers=entete)
        if req.status_code == 200:
#Le fait d'ajouter .status_code fait en sorte que ce que vous tentiez de faire dans le cours fonctionne désormais.
### Ha ha! En effet! Il y a tant de détails dont il faut se souvenir, que mon pauvre cerveau n'y arrive plus!
            banq = req.json()
            h += 1 ### Imprimer «i» aurait fait la même chose :)
            print(h, "="*80)
            if banq["type"] == "audio":
                #print(clip)
                infos = []
                infos.append(banq["titre"].split(" /")[0])
                infos.append(banq["createurs"][0])
                infos.append(banq["dateCreation"])
                infos.append(banq["descriptionMat"])
                infos.append(lien_url(banq))
                print(banq["titre"].split(" /")[0])
                print(banq["createurs"][0])
                print(banq["dateCreation"])
                print(banq["descriptionMat"])
                print(lien_url(banq))
                creation_fichier.writerow(infos)
            else:
                print("Ce n'est pas un fichier audio")
        elif req.status_code == 500:
            print("problème de serveur")
        else:
            print("Ça marche pas.. :/")