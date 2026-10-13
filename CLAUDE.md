# Atelier Remaster : site atelier-remaster.ch

Site vitrine d'Atelier Remaster, activité indépendante de Julien Dornbierer (Bienne),
spécialiste en marketing avec brevet fédéral. Ce dépôt est **public** : n'y mets jamais
de données de prospects, de stratégie interne ou d'informations personnelles.

Si le dossier `private/` existe (il est ignoré par git), lis d'abord `private/CONTEXTE.md` :
il contient tout le contexte business, les décisions et la liste des tâches ouvertes.

## Publication
- `site/` est publié tel quel sur GitHub Pages par `.github/workflows/deploy.yml` à chaque push sur `main`
  (environ 1 minute). Pas de build, pas de dépendances.
- Domaine : DNS chez Infomaniak (A → 185.199.108/109/111.153, `www` CNAME → julien-dornbierer.github.io).
  E-mails : Google Workspace (MX/SPF/DKIM/DMARC dans la même zone : ne pas toucher).
- Après modification : vérifier le rendu (desktop 1280 px + mobile 390 px, FR, DE et EN, aucun scroll horizontal),
  puis commit + push. Rappeler à Julien de recharger avec Ctrl+F5.

## Structure de `site/index.html`
- Page unique, HTML/CSS/JS inline. Polices auto-hébergées dans `site/fonts/` (Bricolage Grotesque pour les titres,
  Source Serif 4 pour le texte). Aucun appel à Google Fonts (cohérence avec la déclaration de protection des données).
- Couleurs en variables CSS (`--paper`, `--ink`, `--amber`, …) avec mode sombre automatique.
- **Trilingue FR/DE/EN** (sélecteur à 3 onglets) : chaque texte traduisible porte `data-i="clé"`. Le français est dans le HTML ;
  l'allemand dans l'objet JS `DE` (plus des `Object.assign(DE, {...})` successifs : la dernière valeur gagne),
  l'anglais dans l'objet JS `EN`.
  Toute modification de texte FR doit avoir son équivalent DE et EN.
- Formulaires (bilan + contact) : envoyés via FormSubmit (AJAX) vers julien@atelier-remaster.ch.
- `site/mentions-legales.html` : impressum + protection des données FR/DE/EN. À tenir à jour si l'hébergement,
  les outils ou les traitements de données changent.
- `tools/` : scripts Python de modifications ponctuelles (historique, ne pas relancer).

## Règles de rédaction (validées par Julien)
- **« Je », jamais « nous »** : Julien travaille seul. Pareil en allemand (ich, pas wir).
- Ton humble, clair, concret ; pas de jargon ni de terminologie musicale.
- **Ne jamais mettre en avant l'IA** sur le site.
- Réseaux sociaux : Julien **met en place le système** (profils, modèles, planning, outils) ; il ne publie pas à la place du client.
- Multilingue : français, allemand, anglais (pas seulement FR/DE).
- Avis Google / fiche Google : détail secondaire, pas un argument principal.
- Aucun faux avis, aucune fausse référence : les réalisations n'apparaissent qu'avec l'accord des clients.

## Offre et prix affichés (CHF, hors TVA)
- Bilan d'image + plan chiffré : gratuit (pour l'instant).
- Pack S « Rafraîchir » 1'800–3'000 · Pack M « Remettre à niveau » 4'000–7'000 · Pack L « Refondre » dès 8'000.
- Entretien 79.– / mois (6 mois minimum, puis résiliable chaque mois).
- À la pièce : heure 110.– (au quart d'heure), document graphique 90, modèle de publication 60,
  annonce d'emploi 180, campagne sponsorisée 250 (hors budget pub).
