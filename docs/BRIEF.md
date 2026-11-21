# BRIEF — IRON PULSE

Source unique pour l'identité, le plan du site et les textes. Toutes les informations sont fictives
mais doivent rester cohérentes d'une page à l'autre (mêmes prix, mêmes noms, mêmes horaires).

## 1. Identité
- **Nom** : IRON PULSE (toujours en capitales).
- **Activité** : studio de coaching sportif en petits groupes et en individuel : HIIT, musculation, cross training, mobilité, coaching personnalisé.
- **Slogan** : « Entraîne-toi fort. Progresse vite. »
- **Promesse** : des séances intenses, encadrées par de vrais coachs, en petits groupes (12 personnes maximum), pour progresser vite et sans se blesser.
- **Ton** : énergique, direct, motivant, mais professionnel. Tutoiement sur les accroches (« Pousse la porte »), vouvoiement dans les infos pratiques et le formulaire.
- **Création** : 2019, par Karim Benali.
- **Studio** : 450 m² sur deux niveaux : plateau de musculation, zone HIIT avec gazon synthétique, salle de mobilité, vestiaires avec douches.

### Coordonnées (fictives)
- Adresse : 27 rue de la Forge, 69007 Lyon (métro B, arrêt Jean Macé)
- Téléphone : 04 72 18 45 90
- E-mail : contact@ironpulse-studio.fr
- Réseaux : Instagram, Facebook, YouTube (liens vers les sites de ces réseaux, `@ironpulse.lyon`)
- Horaires d'ouverture : lundi au vendredi 6 h 30 – 22 h ; samedi 8 h – 18 h ; dimanche 9 h – 13 h.

### Chiffres clés
- 2019 : année d'ouverture
- 12 : personnes maximum par cours
- 4 coachs diplômés d'État
- 850 membres actifs
- 40 cours par semaine

## 2. Charte graphique
| Rôle | Couleur | Variable CSS |
|---|---|---|
| Fond principal | noir profond `#0b0b0d` | `--noir` |
| Fond secondaire (cartes, bandeaux) | `#16171a` | `--noir-2` |
| Accent (boutons, titres soulignés) | orange vif `#ff5a1f` | `--orange` |
| Accent survol | `#ff7a45` | `--orange-clair` |
| Texte secondaire, bordures | gris acier `#8b939c` | `--acier` |
| Texte principal | `#f2f3f5` | `--blanc` |

- Titres : **Anton** (Google Fonts), en capitales, interlettrage léger.
- Texte : **Inter** (Google Fonts), 400 et 700.
- Boutons orange : **texte noir** sur fond orange (contraste lisible).
- Style : angles nets, bandes diagonales orange, gros chiffres, beaucoup de contraste.

## 3. Plan du site (5 pages)
Menu (dans cet ordre) : Accueil · À propos · Cours & Tarifs · Coachs · Contact. Bouton « Séance d'essai » qui mène à `contact.html#essai`.

### Accueil — `index.html`
1. Bannière (hero) : titre « Entraîne-toi fort. Progresse vite. », sous-titre sur la promesse, bouton « Réserver ma séance d'essai » + lien « Voir les cours ».
2. Bandeau chiffres clés (2019, 12, 4, 850).
3. « Nos disciplines » : 3 cartes avec image (HIIT, Musculation, Coaching personnalisé).
4. « Pourquoi IRON PULSE » : 4 arguments (petits groupes, coachs diplômés, suivi de progression, horaires larges).
5. Témoignages : 2 ou 3 avis de membres (prénom + initiale, durée d'adhésion).
6. Appel à l'action final : « Ta première séance est offerte ».

### À propos — `a-propos.html`
1. Titre de page + introduction.
2. Notre histoire : Karim Benali, ancien sprinteur de niveau national, devenu préparateur physique, ouvre IRON PULSE en 2019 dans un ancien atelier de métallurgie du 7e arrondissement (d'où le nom « Iron »). Image du studio.
3. Nos valeurs : Exigence, Bienveillance, Progression, Collectif (un court texte chacune).
4. Le studio : description des espaces (liste) + image.
5. Lien vers la page Coachs.

### Cours & Tarifs — `cours-tarifs.html` (page « Offre »)
1. Les cours (cartes) :
   - **HIIT Burn** — 45 min, intensité 4/5 : intervalles courts, cardio et poids du corps.
   - **Force & Muscu** — 60 min, intensité 3/5 : technique des mouvements de base (squat, soulevé de terre, développé couché), charges progressives.
   - **Cross Circuit** — 50 min, intensité 4/5 : circuits variés, kettlebells, rameur, corde.
   - **Mobility Reset** — 45 min, intensité 1/5 : mobilité, gainage, récupération.
   - **Coaching personnalisé** — 60 min, en individuel : programme sur mesure, bilan initial.
2. **Tableau planning** de la semaine (lundi → samedi, créneaux 7 h 00, 12 h 15, 18 h 30, 19 h 45). Exemple de répartition cohérente :
   - Lundi : 7 h HIIT Burn · 12 h 15 Force & Muscu · 18 h 30 Cross Circuit · 19 h 45 Mobility Reset
   - Mardi : 7 h Force & Muscu · 12 h 15 HIIT Burn · 18 h 30 Force & Muscu · 19 h 45 HIIT Burn
   - Mercredi : 7 h Cross Circuit · 12 h 15 Mobility Reset · 18 h 30 HIIT Burn · 19 h 45 Force & Muscu
   - Jeudi : 7 h HIIT Burn · 12 h 15 Cross Circuit · 18 h 30 Force & Muscu · 19 h 45 Cross Circuit
   - Vendredi : 7 h Force & Muscu · 12 h 15 HIIT Burn · 18 h 30 Cross Circuit · 19 h 45 Mobility Reset
   - Samedi : 9 h 00 HIIT Burn · 10 h 15 Force & Muscu · 11 h 30 Mobility Reset (créneaux du samedi indiqués dans une ligne ou une note à part)
3. **Tableau tarifs** (formules) :
   | Formule | Contenu | Prix |
   |---|---|---|
   | Séance d'essai | 1 cours collectif au choix + bilan | Offerte |
   | Carte 10 séances | 10 cours collectifs, valable 4 mois | 150 € |
   | Abonnement Pulse | 2 cours collectifs par semaine, sans engagement | 59 € / mois |
   | Abonnement Iron | Cours collectifs illimités + 1 bilan par trimestre, sans engagement | 89 € / mois |
   | Coaching perso — séance | 1 h en individuel | 60 € |
   | Coaching perso — pack 10 | 10 h en individuel + programme écrit | 520 € |
   Note : -15 % étudiants et demandeurs d'emploi sur les abonnements, sur justificatif.
4. Appel à l'action vers la séance d'essai.

### Coachs — `coachs.html` (bonus)
4 cartes avec portrait illustré, spécialité, diplôme, citation courte :
- **Karim Benali** — fondateur, Force & Muscu. BPJEPS AF, licence STAPS. Ancien sprinteur (100 m).
- **Léa Moreau** — HIIT & cardio. BPJEPS AF, 8 ans d'expérience, ancienne handballeuse.
- **Thomas Diallo** — coaching personnalisé et préparation physique. Master STAPS, prépare des sportifs amateurs aux compétitions.
- **Inès Garcia** — Mobility Reset et remise en forme. BPJEPS AF, formation en yoga, spécialiste de la reprise après blessure.

### Contact — `contact.html`
1. **Formulaire** « Réserver ma séance d'essai » (id `essai`) : nom, prénom, e-mail, téléphone (facultatif), cours souhaité (select), créneau préféré (radios matin / midi / soir), objectif (textarea), case « J'accepte d'être recontacté » (required), bouton Envoyer. `action` vers une adresse fictive ou `#` avec `method="post"`.
2. Coordonnées + horaires d'ouverture (liste ou `<dl>`).
3. Accès : métro, vélo'v, parking (texte).
4. FAQ (bonus) avec `<details>`/`<summary>` : faut-il être sportif ? que faut-il apporter ? peut-on résilier ? y a-t-il des douches ?

## 4. Pied de page (toutes les pages)
- Logo + slogan
- Coordonnées (adresse, téléphone, e-mail)
- Horaires résumés
- Réseaux sociaux (Instagram, Facebook, YouTube)
- Mentions : « © 2026 IRON PULSE — Site réalisé dans le cadre d'un projet pédagogique HTML & CSS. Studio fictif. » + lien « Mentions légales » vers `contact.html#mentions` (court paragraphe de mentions sur la page Contact).

## 5. Images (dossier `images/`)
Illustrations SVG originales (créées pour le projet, donc libres de droits), dans la charte noir / orange / acier.
| Fichier | Sujet | Utilisée sur |
|---|---|---|
| `logo.svg` | logo IRON PULSE (haltère + pulsation) | toutes (en-tête) |
| `hero.svg` | athlète en mouvement, scène dynamique | Accueil |
| `hiit.svg` | sprint / chronomètre | Accueil, Cours |
| `musculation.svg` | barre chargée de disques | Accueil, Cours |
| `coaching.svg` | coach et élève, presse-papier | Accueil, Cours |
| `cross.svg` | kettlebell et corde | Cours |
| `mobilite.svg` | étirement / tapis | Cours |
| `studio.svg` | vue du plateau du studio | À propos |
| `coach-karim.svg`, `coach-lea.svg`, `coach-thomas.svg`, `coach-ines.svg` | portraits stylisés | Coachs |
