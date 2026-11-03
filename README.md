# e-portfolio

Portfolio de Maxime DUMAS (FISA 3EA), migré depuis Wix vers **GitHub Pages**.

Adresse une fois GitHub Pages activé : **https://maximedumas46.github.io/e-portfolio/**

## Activer GitHub Pages (une seule fois)

1. Sur GitHub : **Settings → Pages**.
2. *Build and deployment* → **Source : Deploy from a branch**.
3. **Branch : `main`**, dossier **`/ (root)`** → **Save**.
4. Le site est en ligne après 1 à 2 minutes (l'onglet **Actions** montre le déploiement).

GitHub construit le site automatiquement avec Jekyll à chaque modification de `main`.

## Structure

| Page | Fichier |
|---|---|
| Home (accueil, à propos, CV, mentors) | `index.html` |
| Projects | `projects.html` + `_projects/*.md` (un fichier par projet) |
| Engagement | `engagement.md` |
| FutursProches | `futursproches.md` |
| Mobility | `mobility.md` |
| Sports | `sports.md` |
| Contact | `contact.html` |

| Autres fichiers | Rôle |
|---|---|
| `_config.yml` | Nom du site, **menu**, **coordonnées**, **liens vers les CV** |
| `_layouts/` | Gabarits (`default.html` = en-tête/pied de page, `page.html`, `project.html`) |
| `_includes/` | Blocs réutilisables (images, galeries, cartes projet) |
| `assets/css/style.css` | Le style (couleurs, mode sombre automatique) |
| `assets/js/main.js` | Menu mobile, formulaire de contact, visionneuse d'images |

Les textes des pages `.md` s'écrivent en Markdown : modifiez-les directement sur GitHub (bouton ✏️).

Le formulaire de contact ouvre la messagerie du visiteur avec le message pré-rempli
(GitHub Pages ne peut pas envoyer d'e-mails lui-même).

## Ajouter ou modifier un projet

Directement depuis GitHub (bouton ✏️ ou **Add file → Create new file** dans `_projects/`) :

```markdown
---
title: "Nom du projet"
order: 1                 # position dans la grille (1 = en premier)
year: "BUT3 - Semestre 6"
location: "BUT GEII - IUT Paul Sabatier"
type: "SAE"
summary: "Une phrase affichée sur la carte du projet."
cover:
  src: /assets/img/mon-projet.jpg   # image ajoutée au dépôt
  width: 1600
  height: 1200
gallery:
  - src: /assets/img/mon-projet-2.png
    width: 1200
    height: 800
    title: "Légende de l'image"
---

### Project Objective

Texte en Markdown…
```

Pour une image locale, mettez-la dans `assets/img/` et utilisez `src:`. Les images reprises de Wix utilisent `id:` (identifiant Wix Media).

## Copier les médias Wix dans le dépôt (une seule fois)

Les photos, les CV et la vidéo reprises de Wix peuvent être copiés dans le dépôt pour que le site ne dépende plus de Wix :

1. Onglet **Actions** du dépôt → **Import Wix media** (à gauche).
2. Bouton **Run workflow** → **Run workflow**.
3. Après 2 à 3 minutes, le workflow a ajouté un commit « Import media from Wix into the repository » :
   - photos → `assets/media/` (WebP, en 480 / 960 / 1600 px),
   - CV → `assets/cv/`,
   - vidéo → `assets/video/`,
   - et `media_local: true` dans `_config.yml`.

Si l'étape *Commit and push* échoue (erreur 403) : **Settings → Actions → General → Workflow permissions → Read and write permissions**, puis relancer.

Le script (`scripts/import_wix_media.py`) ne modifie rien si un seul téléchargement échoue, et ne retélécharge pas ce qui est déjà copié.

## Tester en local (facultatif)

```bash
gem install jekyll
jekyll serve
```

Puis ouvrir http://localhost:4000/e-portfolio/
