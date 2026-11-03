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

| Fichier / dossier | Rôle |
|---|---|
| `_config.yml` | Nom, description, URL du site, liens vers les CV |
| `index.html` | Page d'accueil (présentation, grille des projets, CV) |
| `_projects/*.md` | **Un fichier par projet** (texte + infos + images) |
| `_layouts/` | Gabarits des pages (`default.html`, `project.html`) |
| `_includes/image.html` | Génère les images responsives |
| `assets/css/style.css` | Le style (couleurs, mode sombre automatique) |
| `assets/js/main.js` | Visionneuse d'images (lightbox) |

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

Pour une image locale, mettez-la dans `assets/img/` et utilisez `src:`. Les images reprises de Wix utilisent `id:` (identifiant Wix Media) et sont servies par le CDN de Wix (`static.wixstatic.com`).

## Tester en local (facultatif)

```bash
gem install jekyll
jekyll serve
```

Puis ouvrir http://localhost:4000/e-portfolio/
