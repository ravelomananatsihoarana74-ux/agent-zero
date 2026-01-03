import os
import logging
from typing import List, Dict

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AgentZero")

class AgentZero:
    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.telegram_token = os.getenv("TELEGRAM_TOKEN")
        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.kaggle_username = os.getenv("KAGGLE_USERNAME")
        self.kaggle_key = os.getenv("KAGGLE_KEY")
        
        logger.info("Agent Zéro initialisé.")

    def notify_telegram(self, message: str):
        """Envoie une notification sur Telegram."""
        import requests
        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {"chat_id": self.telegram_chat_id, "text": message}
        try:
            requests.post(url, json=payload)
            logger.info(f"Notification Telegram envoyée.")
        except Exception as e:
            logger.error(f"Erreur lors de l'envoi Telegram : {e}")

    def reason(self, prompt: str) -> str:
        """Utilise Groq pour raisonner."""
        from groq import Groq
        client = Groq(api_key=self.groq_api_key)
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
        )
        return completion.choices[0].message.content

    def execute_task(self, task: str):
        """Exécute une tâche spécifique."""
        logger.info(f"Exécution de la tâche : {task}")
        # Logique d'exécution
        self.notify_telegram(f"Tâche terminée : {task}")

    def evolve(self, new_code: str, file_path: str, commit_message: str):
        """Modifie son propre code après validation humaine."""
        logger.info(f"Demande d'évolution pour {file_path}")
        
        # 1. Notification Telegram pour validation
        self.notify_telegram(f"⚠️ DEMANDE D'ÉVOLUTION ⚠️\nFichier: {file_path}\nMessage: {commit_message}\n\nRépondez 'OUI' pour valider.")
        
        # Note: Dans une version déployée, on attendrait un webhook ou un polling Telegram.
        # Ici, nous simulons la validation pour la structure du code.
        
        # 2. Mise à jour du fichier local
        with open(file_path, 'w') as f:
            f.write(new_code)
        
        # 3. Commit et Push sur GitHub
        import subprocess
        try:
            subprocess.run(["git", "add", file_path], check=True)
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            subprocess.run(["git", "push"], check=True)
            self.notify_telegram(f"✅ Évolution terminée et poussée sur GitHub : {commit_message}")
        except Exception as e:
            logger.error(f"Erreur lors de l'évolution GitHub : {e}")
            self.notify_telegram(f"❌ Échec de l'évolution : {e}")

if __name__ == "__main__":
    agent = AgentZero()
    agent.execute_task("Initialisation du système")
