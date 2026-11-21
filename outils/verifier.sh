#!/usr/bin/env bash
# =====================================================================
# verifier.sh — contrôle qualité automatique du site IRON PULSE
# 1. Validation HTML et CSS avec vnu.jar (moteur du validateur W3C Nu)
# 2. Liens internes, ancres et images (fichiers présents, attribut alt)
# 3. Règles du devoir : pas de JavaScript, pas de style inline, pas de lorem
# Usage : bash outils/verifier.sh [page.html ...]   (toutes les pages par défaut)
# =====================================================================
cd "$(dirname "$0")/.." || exit 1

pages=("$@")
[ ${#pages[@]} -eq 0 ] && pages=(*.html)

# --- Localiser vnu.jar -----------------------------------------------
VNU="${VNU_JAR:-}"
for candidat in "$VNU" outils/vnu.jar "$HOME/tools/node_modules/vnu-jar/build/dist/vnu.jar" \
                /home/user/tools/node_modules/vnu-jar/build/dist/vnu.jar; do
  [ -n "$candidat" ] && [ -f "$candidat" ] && VNU="$candidat" && break
done

statut=0
echo "=== 1. Validation W3C (HTML + CSS) ==="
if [ -n "$VNU" ] && command -v java >/dev/null; then
  if java -jar "$VNU" --errors-only --format text "${pages[@]}" 2>&1 | grep -v '^Picked up'; then
    statut=1
  else
    echo "HTML : 0 erreur"
  fi
  if java -jar "$VNU" --css --errors-only --format text css/*.css 2>&1 | grep -v '^Picked up'; then
    statut=1
  else
    echo "CSS : 0 erreur"
  fi
else
  echo "vnu.jar introuvable : valider sur https://validator.w3.org/nu/ et https://jigsaw.w3.org/css-validator/"
fi

echo "=== 2. Liens, images, règles du devoir ==="
python3 outils/controle_liens.py "${pages[@]}" || statut=1

[ $statut -eq 0 ] && echo "RÉSULTAT : OK" || echo "RÉSULTAT : des erreurs sont à corriger"
exit $statut
