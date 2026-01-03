# Architecture de l'Agent Zéro

L'**Agent Zéro** est conçu comme un système modulaire capable d'exécuter des tâches, de raisonner via Groq, et de s'auto-modifier sous supervision humaine.

## Composants Principaux

1.  **Cerveau (Groq Integration)** : Utilise les modèles LLaMA via l'API Groq pour le raisonnement, la génération de code et la prise de décision.
2.  **Interface de Communication (Telegram Bot)** :
    *   Envoi de notifications de fin de tâche.
    *   Réception d'ordres d'évolution.
    *   Validation humaine pour les actions critiques.
3.  **Moteur d'Exécution (Kaggle/Local)** : Capacité à exécuter des scripts Python pour le traitement de données ou des calculs intensifs.
4.  **Gestionnaire d'Évolution (GitHub Integration)** :
    *   Capacité à lire son propre code source.
    *   Capacité à proposer des modifications.
    *   Application des modifications après validation via Git (commit/push).

## Flux de Travail

1.  **Réception d'ordre** : L'utilisateur envoie une commande via Telegram.
2.  **Raisonnement** : Groq analyse la commande et détermine les étapes nécessaires.
3.  **Action** : L'agent exécute du code ou effectue des recherches.
4.  **Validation** : Si l'action est critique (ex: modification de code), l'agent demande l'autorisation sur Telegram.
5.  **Évolution** : Après validation, l'agent met à jour son dépôt GitHub.
6.  **Notification** : L'agent confirme la réussite de l'opération sur Telegram.

## Sécurité

*   Toutes les clés API sont gérées via des variables d'environnement.
*   Validation humaine obligatoire pour toute modification du `core`.
