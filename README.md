# atelier-remaster.ch

Site vitrine d'Atelier Remaster (Julien Dornbierer, Bienne).

- `site/` : les fichiers publiés tels quels (HTML statique, polices auto-hébergées, aucune dépendance externe hormis l'envoi des formulaires via FormSubmit).
- `.github/workflows/deploy.yml` : à chaque modification de `site/` sur `main`, le site est envoyé chez Infomaniak par SFTP (lftp, sans suppression de fichiers distants).

## Activer la publication automatique

Dans *Settings › Secrets and variables › Actions*, créer :

| Secret | Valeur |
|---|---|
| `FTP_SERVER` | serveur FTP affiché par Infomaniak (hébergement › FTP) |
| `FTP_USERNAME` | utilisateur FTP créé pour le déploiement |
| `FTP_PASSWORD` | son mot de passe |

Tant que ces secrets n'existent pas, le workflow s'exécute mais ne publie rien.
