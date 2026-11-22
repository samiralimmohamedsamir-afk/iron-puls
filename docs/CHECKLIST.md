# CHECKLIST — grille de notation IRON PULSE

À cocher par le **reviewer** pour chaque page, puis une dernière fois sur tout le site.
Une case non cochée = retour au développeur.

## A. Consignes obligatoires (site entier)
- [x] HTML + CSS uniquement, aucun framework, aucun fichier ni attribut JavaScript
- [x] 4 pages minimum : Accueil, À propos, Offre (Cours & Tarifs), Contact (+ bonus Coachs)
- [x] Menu identique présent sur toutes les pages
- [x] Pied de page sur toutes les pages : contact, réseaux, mentions
- [x] Au moins 5 images, toutes avec un `alt` pertinent
- [x] Au moins un tableau
- [x] Au moins un formulaire
- [x] Aucun lorem ipsum, aucun texte de remplissage, aucun « TODO »

## B. Code valide (W3C)
- [x] `bash outils/verifier.sh` : 0 erreur HTML sur la page
- [x] 0 erreur CSS sur `css/style.css`
- [x] Aucun lien interne cassé, aucune image manquante

## C. Responsive
- [x] Lisible à 375 px : pas de défilement horizontal, texte ≥ 16 px, boutons cliquables
- [x] Mise en page soignée à 1280 px (colonnes, largeur de lecture maîtrisée)
- [x] Les tableaux restent lisibles sur mobile (défilement interne ou mise en page adaptée)
- [x] Les images s'adaptent (`max-width: 100%`, `height: auto`)

## D. Navigation claire
- [x] Page courante signalée dans le menu (`aria-current="page"` + style visible)
- [x] Bouton « Séance d'essai » accessible depuis chaque page
- [x] Liens explicites (pas de « cliquez ici »), état `:hover` et `:focus-visible` visibles
- [x] `<title>` unique et descriptif par page

## E. Design professionnel
- [x] Charte respectée : noir, orange `#ff5a1f`, gris acier ; Anton en capitales pour les titres, Inter pour le texte
- [x] Cohérence entre les pages (mêmes composants : boutons, cartes, en-têtes de section)
- [x] Contrastes lisibles (texte noir sur boutons orange)
- [x] Espacements réguliers, alignements propres

## F. Code propre
- [x] HTML sémantique (`header`, `nav`, `main`, `section`, `footer`), un seul `h1`, titres sans saut de niveau
- [x] Indentation régulière (2 espaces), commentaires de section lisibles
- [x] Aucun style inline, aucun attribut obsolète
- [x] CSS organisé en sections commentées, variables `:root` utilisées
- [x] Formulaire : chaque champ a un `label` relié, types adaptés (`email`, `tel`), `required` où il faut

## G. Contenu de qualité
- [x] Textes complets, crédibles, en français, sans faute d'orthographe ni de typographie (espaces avant `: ; ! ?` insécables si possible, guillemets « »)
- [x] Informations cohérentes avec `docs/BRIEF.md` (prix, horaires, noms)
- [x] `<meta name="description">` pertinente

## Suivi par page
| Page | Dev | Test | Review | Commit |
|---|---|---|---|---|
| Socle (CSS + images) | ✔ | ✔ | ✔ | ✔ |
| index.html | ✔ | ✔ | ✔ | ✔ |
| a-propos.html | ✔ | ✔ | ✔ | ✔ |
| cours-tarifs.html | ✔ | ✔ | ✔ | ✔ |
| coachs.html | ✔ | ✔ | ✔ | ✔ |
| contact.html | ✔ | ✔ | ✔ | ✔ |
| Passe finale | ✔ | ✔ | ✔ | ✔ |

## Bilan de la passe finale (21/11/2026)
Reviewer : VALIDÉ sur les 5 pages. `bash outils/verifier.sh` : 0 erreur HTML, 0 erreur CSS, 25 images, 0 lien cassé.
Aucun débordement horizontal à 375, 768 et 1280 px. Menu et pied de page identiques sur toutes les pages.
