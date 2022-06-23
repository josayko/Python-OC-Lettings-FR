---
marp: true
theme: gaia
class: invert
footer: Jonny Saykosy - 2022
---

# OC-Lettings

---

## Projet

- Application de location de biens immobiliers
- Profils d'utilisateurs (profiles)
- Addresses de locations (lettings)
- Dashboard admin
- Base de données

---

## Réduction de la dette technique

- Application unique monolithique -> application modulaire
  - 2 applications: `lettings` et `profiles`
  - urls nommées et `namespace`
  - références des vues
  - migrations base de données vers nouvelles tables
- Pluralisation nom de modèle `Address` -> `Addresses` (Meta)
- Code linting
- Suite de tests unitaires

---

## Pipeline CI/CD

- Application déployé sur `https://<nom-app>.herokuapp.com`
- Variables d'environnement
- Configurations CircleCI, Dockerfile et Heroku
- Travail de construction et tests pour toute les branches
- Conteneurisation uniquement sur branche principale
- Déploiement sur Heroku uniquement sur branche principale
- Monitoring avec Sentry

---

## Questions et axes d'amélioration
