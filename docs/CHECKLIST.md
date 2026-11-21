# CHECKLIST — grille de notation IRON PULSE

À cocher par le **reviewer** pour chaque page, puis une dernière fois sur tout le site.
Une case non cochée = retour au développeur.

## A. Consignes obligatoires (site entier)
- [ ] HTML + CSS uniquement, aucun framework, aucun fichier ni attribut JavaScript
- [ ] 4 pages minimum : Accueil, À propos, Offre (Cours & Tarifs), Contact (+ bonus Coachs)
- [ ] Menu identique présent sur toutes les pages
- [ ] Pied de page sur toutes les pages : contact, réseaux, mentions
- [ ] Au moins 5 images, toutes avec un `alt` pertinent
- [ ] Au moins un tableau
- [ ] Au moins un formulaire
- [ ] Aucun lorem ipsum, aucun texte de remplissage, aucun « TODO »

## B. Code valide (W3C)
- [ ] `bash outils/verifier.sh` : 0 erreur HTML sur la page
- [ ] 0 erreur CSS sur `css/style.css`
- [ ] Aucun lien interne cassé, aucune image manquante

## C. Responsive
- [ ] Lisible à 375 px : pas de défilement horizontal, texte ≥ 16 px, boutons cliquables
- [ ] Mise en page soignée à 1280 px (colonnes, largeur de lecture maîtrisée)
- [ ] Les tableaux restent lisibles sur mobile (défilement interne ou mise en page adaptée)
- [ ] Les images s'adaptent (`max-width: 100%`, `height: auto`)

## D. Navigation claire
- [ ] Page courante signalée dans le menu (`aria-current="page"` + style visible)
- [ ] Bouton « Séance d'essai » accessible depuis chaque page
- [ ] Liens explicites (pas de « cliquez ici »), état `:hover` et `:focus-visible` visibles
- [ ] `<title>` unique et descriptif par page

## E. Design professionnel
- [ ] Charte respectée : noir, orange `#ff5a1f`, gris acier ; Anton en capitales pour les titres, Inter pour le texte
- [ ] Cohérence entre les pages (mêmes composants : boutons, cartes, en-têtes de section)
- [ ] Contrastes lisibles (texte noir sur boutons orange)
- [ ] Espacements réguliers, alignements propres

## F. Code propre
- [ ] HTML sémantique (`header`, `nav`, `main`, `section`, `footer`), un seul `h1`, titres sans saut de niveau
- [ ] Indentation régulière (2 espaces), commentaires de section lisibles
- [ ] Aucun style inline, aucun attribut obsolète
- [ ] CSS organisé en sections commentées, variables `:root` utilisées
- [ ] Formulaire : chaque champ a un `label` relié, types adaptés (`email`, `tel`), `required` où il faut

## G. Contenu de qualité
- [ ] Textes complets, crédibles, en français, sans faute d'orthographe ni de typographie (espaces avant `: ; ! ?` insécables si possible, guillemets « »)
- [ ] Informations cohérentes avec `docs/BRIEF.md` (prix, horaires, noms)
- [ ] `<meta name="description">` pertinente

## Suivi par page
| Page | Dev | Test | Review | Commit |
|---|---|---|---|---|
| Socle (CSS + images) | ☐ | ☐ | ☐ | ☐ |
| index.html | ☐ | ☐ | ☐ | ☐ |
| a-propos.html | ☐ | ☐ | ☐ | ☐ |
| cours-tarifs.html | ☐ | ☐ | ☐ | ☐ |
| coachs.html | ☐ | ☐ | ☐ | ☐ |
| contact.html | ☐ | ☐ | ☐ | ☐ |
| Passe finale | ☐ | ☐ | ☐ | ☐ |
