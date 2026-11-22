"""Contrôle des liens internes, des ancres, des images et des règles du devoir.

Usage : python3 outils/controle_liens.py page1.html page2.html ...
"""
import os
import re
import sys
from html.parser import HTMLParser


class Analyseur(HTMLParser):
    """Collecte liens, images, identifiants et éléments interdits d'une page."""

    def __init__(self):
        super().__init__()
        self.liens, self.images, self.ids, self.problemes = [], [], set(), []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "href" in a:
            self.liens.append(a["href"])
        if tag == "img":
            self.images.append(a)
        if tag == "script":
            self.problemes.append("balise <script> interdite (pas de JavaScript)")
        if "style" in a:
            self.problemes.append(f"style inline interdit sur <{tag}>")
        for nom in a:
            if nom.startswith("on"):
                self.problemes.append(f"attribut JavaScript {nom} interdit")


def analyser(fichier):
    p = Analyseur()
    with open(fichier, encoding="utf-8") as f:
        texte = f.read()
    p.feed(texte)
    if re.search(r"lorem|ipsum|TODO|à compléter", texte, re.I):
        p.problemes.append("texte de remplissage détecté (lorem / TODO)")
    return p


def main(pages):
    cache, erreurs, nb_images = {}, 0, 0
    for page in pages:
        cache[page] = cache.get(page) or analyser(page)
        p = cache[page]
        for pb in p.problemes:
            print(f"{page} : {pb}"); erreurs += 1
        for img in p.images:
            nb_images += 1
            src = img.get("src", "")
            if not os.path.isfile(src):
                print(f"{page} : image introuvable {src}"); erreurs += 1
            if not img.get("alt", "").strip() and img.get("alt") != "":
                print(f"{page} : image sans alt {src}"); erreurs += 1
            elif img.get("alt") == "" and "logo" not in src:
                print(f"{page} : alt vide sur une image de contenu {src}"); erreurs += 1
            if "width" not in img or "height" not in img:
                print(f"{page} : width/height manquants sur {src}"); erreurs += 1
        for href in p.liens:
            if re.match(r"(https?:|mailto:|tel:)", href):
                continue
            cible, _, ancre = href.partition("#")
            cible = cible or page
            if not os.path.isfile(cible):
                print(f"{page} : lien cassé {href}"); erreurs += 1
                continue
            if ancre and cible.endswith(".html"):
                cache[cible] = cache.get(cible) or analyser(cible)
                if ancre not in cache[cible].ids:
                    print(f"{page} : ancre introuvable {href}"); erreurs += 1
    print(f"{len(pages)} page(s), {nb_images} image(s) contrôlée(s), {erreurs} problème(s)")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
