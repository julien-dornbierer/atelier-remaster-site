# atelier-remaster.ch

Site vitrine d'Atelier Remaster (Julien Dornbierer, Bienne).

- `site/` : les fichiers publiés tels quels (HTML statique, polices auto-hébergées ; les formulaires passent par FormSubmit).
- `.github/workflows/deploy.yml` : à chaque modification de `site/` sur `main`, le site est publié sur GitHub Pages.
- Domaine : `atelier-remaster.ch` (DNS chez Infomaniak, enregistrements A vers GitHub Pages, `www` en CNAME vers `julien-dornbierer.github.io`).
