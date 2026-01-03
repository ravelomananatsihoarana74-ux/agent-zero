# Agent Zéro 🤖

L'Agent Zéro est un agent autonome intelligent conçu pour s'auto-évoluer sous supervision humaine.

## Fonctionnalités

*   **Cerveau Groq** : Utilise LLaMA 3 pour le raisonnement complexe.
*   **Auto-évolution** : Capable de modifier son propre code source et de le pousser sur GitHub.
*   **Contrôle Telegram** : Notifications en temps réel et validation humaine obligatoire pour les actions critiques.
*   **Calcul Kaggle** : Intégration pour l'exécution de tâches de data science à la volée.

## Configuration

L'agent nécessite les variables d'environnement suivantes :

| Variable | Description |
| --- | --- |
| `GITHUB_TOKEN` | Token d'accès personnel GitHub |
| `GROQ_API_KEY` | Clé API Groq |
| `TELEGRAM_TOKEN` | Token du bot Telegram |
| `TELEGRAM_CHAT_ID` | ID de votre chat Telegram |
| `KAGGLE_USERNAME` | Nom d'utilisateur Kaggle |
| `KAGGLE_KEY` | Clé API Kaggle |

## Installation

```bash
git clone https://github.com/ravelomananatsihoarana74-ux/agent-zero.git
cd agent-zero
pip install -r requirements.txt
python main.py
```

## Utilisation

L'agent démarre et attend des ordres via Telegram (nécessite l'implémentation d'un listener Telegram comme `python-telegram-bot`).
