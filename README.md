# IRON PULSE — site vitrine (devoir HTML & CSS 2026-2027)

Site d'un studio de coaching sportif **fictif** à Lyon : HIIT, musculation, cross training, mobilité et coaching personnalisé.
Réalisé en **HTML + CSS uniquement** (aucun framework, aucun JavaScript).

## Ouvrir le site
1. Télécharger ou cloner le dépôt.
2. Double-cliquer sur `index.html` : il s'ouvre dans le navigateur, sans serveur.
   Dans VS Code, l'extension **Live Server** (clic droit > « Open with Live Server ») recharge la page à chaque modification.

Une connexion Internet sert uniquement à charger les polices Google Fonts (Anton, Inter). Sans connexion, le site reste lisible avec des polices de secours.

## Les pages
| Page | Fichier | Ce qu'on y trouve |
|---|---|---|
| Accueil | `index.html` | Bannière, chiffres clés, 3 disciplines, 4 arguments, témoignages |
| À propos | `a-propos.html` | Histoire du studio, 4 valeurs, présentation des espaces |
| Offre | `cours-tarifs.html` | 5 cours, **tableau du planning** de la semaine, **tableau des tarifs** |
| Coachs (bonus) | `coachs.html` | Les 4 coachs, leur parcours, le déroulé du premier rendez-vous |
| Contact | `contact.html` | **Formulaire** de séance d'essai, coordonnées, horaires, accès, FAQ, mentions légales |

## Structure du dossier
```
index.html, a-propos.html, cours-tarifs.html, coachs.html, contact.html
css/style.css        feuille de style unique, en 14 sections commentées
images/              12 illustrations SVG originales (logo, disciplines, studio, portraits)
docs/BRIEF.md        identité, charte graphique, plan et textes du site
docs/CHECKLIST.md    grille de notation transformée en cases à cocher
outils/              script de vérification (W3C, liens, images)
CLAUDE.md            règles du projet pour Claude Code
.claude/agents/      les 3 agents : développeur, testeur, reviewer
```

## Respect des consignes
| Consigne | Où |
|---|---|
| Menu sur toutes les pages | En-tête identique, page courante soulignée en orange (`aria-current="page"`) |
| Pied de page (contact, réseaux, mentions) | Bas de chaque page ; mentions légales détaillées sur `contact.html#mentions` |
| Au moins 5 images avec `alt` | 25 images au total, chacune avec un texte alternatif qui la décrit |
| Un tableau | Deux : planning et tarifs (`cours-tarifs.html`), avec `caption`, `thead`, `th scope` |
| Un formulaire | Séance d'essai (`contact.html#essai`) : `label` sur chaque champ, `fieldset`, champs obligatoires |
| Pas de lorem ipsum | Tous les textes sont rédigés |
| Code valide W3C | 0 erreur HTML et 0 erreur CSS (moteur du validateur officiel) |
| Responsive | Pensé d'abord pour mobile, puis paliers à 600 px (tablette) et 960 px (ordinateur) |

## Points techniques à expliquer à l'oral
- **Variables CSS** (`:root`) : toutes les couleurs de la charte (noir, orange `#ff5a1f`, gris acier) et les polices sont définies une seule fois.
- **Mobile first** : les styles de base visent le téléphone, les `@media (min-width: …)` ajoutent les colonnes sur grand écran.
- **CSS Grid** pour les grilles de cartes, **Flexbox** pour le menu et les alignements.
- **Tableau du planning sur mobile** : il défile horizontalement dans son cadre, la colonne des horaires reste figée (`position: sticky`).
- **Menu sans JavaScript** : sur mobile, les liens passent simplement à la ligne sous le logo.
- **Formulaire** : validation native du navigateur (`required`, `type="email"`) ; la bordure rouge n'apparaît qu'après une saisie (`:user-invalid`).
- **FAQ** avec `<details>` / `<summary>` : questions dépliables sans JavaScript.
- **Accessibilité** : lien « Aller au contenu principal », focus visible au clavier, un seul `h1` par page, contrastes lisibles (texte noir sur les boutons orange).
- **Images SVG** : illustrations vectorielles créées pour le projet (donc libres de droits), nettes à toutes les tailles et très légères. On peut les remplacer par des photos en gardant le même nom de fichier et en mettant à jour l'extension dans le HTML.

## Vérifier le code
- En ligne : https://validator.w3.org/#validate_by_upload (HTML) et https://jigsaw.w3.org/css-validator/ (CSS).
- En local (Java nécessaire) : `bash outils/verifier.sh` valide HTML et CSS avec `vnu.jar` (moteur du validateur W3C), puis contrôle les liens, les ancres et les images.
  `vnu.jar` s'installe avec `npm install vnu-jar` ; indiquer son chemin avec `VNU_JAR=chemin/vers/vnu.jar bash outils/verifier.sh`.

## Méthode de travail
Le site a été construit avec Claude Code, page par page, par une chaîne de trois agents (`.claude/agents/`) :
1. **développeur** : code la page à partir de `docs/BRIEF.md` ;
2. **testeur** : valide (W3C, liens, responsive à 375, 768 et 1280 px) et corrige ;
3. **reviewer** : relit la page contre `docs/CHECKLIST.md` et renvoie les corrections au développeur.

Un commit par page, une fois la checklist validée.

---
Studio fictif, réalisé dans le cadre d'un projet pédagogique HTML & CSS.
