# CLAUDE.md — Projet IRON PULSE (devoir HTML & CSS)

Ce fichier donne les règles à tout agent Claude Code qui travaille sur ce dépôt.
Lire aussi : `docs/BRIEF.md` (contenu, identité) et `docs/CHECKLIST.md` (grille de notation).

## Le projet
Site vitrine d'**IRON PULSE**, studio de coaching sportif fictif à Lyon (HIIT, musculation, coaching personnalisé).
Devoir de fin de cours HTML & CSS (2026-2027), rendu le **lundi 23/11/2026**.

## Règles non négociables (consignes du professeur)
1. **HTML + CSS uniquement.** Aucun framework (pas de Bootstrap, Tailwind…), **aucun JavaScript**.
2. **4 pages minimum** : Accueil, À propos, Offre (Cours & Tarifs), Contact. Bonus : Coachs.
3. **Menu identique sur toutes les pages**, avec la page courante signalée (`aria-current="page"`).
4. **Pied de page** sur toutes les pages : contact, réseaux sociaux, mentions.
5. **Au moins 5 images**, chacune avec un `alt` pertinent (décrit l'image, pas « image1 »).
6. **Au moins un tableau** (`<table>` avec `<caption>`, `<thead>`, `<th scope>`).
7. **Au moins un formulaire** (chaque champ a un `<label for>` relié).
8. **Pas de lorem ipsum.** Textes réels, crédibles, en français, sans fautes.

## Critères de notation
Code valide W3C · Responsive (mobile + ordinateur) · Navigation claire · Design pro cohérent ·
Code propre et commenté · Contenu de qualité.

## Conventions de code
- Encodage UTF-8, `<!DOCTYPE html>`, `<html lang="fr">`, `<meta name="viewport">`, `<title>` unique par page,
  `<meta name="description">` par page.
- HTML5 sémantique : `header`, `nav`, `main`, `section`, `article`, `footer`. Un seul `<h1>` par page,
  hiérarchie de titres sans saut.
- Indentation 2 espaces. Noms de classes en minuscules avec tirets (`carte-cours`, `btn-primaire`).
- **Une seule feuille de style** : `css/style.css`, organisée en sections commentées
  (`/* === 1. Variables === */`, etc.). Couleurs et polices via variables CSS (`:root`).
- Pas de style inline (`style="..."`), pas d'attributs obsolètes (`align`, `bgcolor`, `border`…).
- Mobile first : styles de base pour mobile, puis `@media (min-width: …)` pour tablette/ordinateur.
- Images dans `images/`, noms en minuscules sans accents ni espaces ; `width` et `height` renseignés.
- Liens internes relatifs (`cours-tarifs.html`), jamais de chemin absolu local (`C:\…`).
- Commentaires HTML courts pour délimiter les grandes zones (`<!-- ===== EN-TÊTE ===== -->`).

## Fichiers
| Fichier | Rôle |
|---|---|
| `index.html` | Accueil |
| `a-propos.html` | À propos (histoire, valeurs, studio) |
| `cours-tarifs.html` | Offre : cours, planning (tableau), tarifs |
| `coachs.html` | Bonus : l'équipe de coachs |
| `contact.html` | Formulaire de séance d'essai, adresse, horaires, FAQ |
| `css/style.css` | Feuille de style unique |
| `images/` | Illustrations SVG originales du studio |
| `outils/verifier.sh` | Vérification automatique (W3C + liens + images) |

## Vérifier son travail
```bash
bash outils/verifier.sh          # valide HTML + CSS (moteur W3C Nu), liens internes, alt des images
```
Le script utilise `vnu.jar` (le moteur du validateur officiel https://validator.w3.org/nu/).
Sans Java, valider à la main sur https://validator.w3.org/#validate_by_upload et
https://jigsaw.w3.org/css-validator/.

## Workflow des agents (`.claude/agents/`)
Chaîne séquentielle, **page par page** :
1. `developpeur` code la page selon `docs/BRIEF.md`.
2. `testeur` lance `outils/verifier.sh`, contrôle le responsive (captures 375 px et 1280 px), corrige.
3. `reviewer` relit la page contre `docs/CHECKLIST.md` ; s'il trouve un écart, il renvoie au développeur.
4. On reboucle jusqu'à ce que la checklist de la page soit verte, puis commit + push (un commit par page).
