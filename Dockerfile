FROM python:3.11-slim

# Créer un utilisateur non-root
RUN groupadd -r smartled && useradd -r -g smartled smartled

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Copier et installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Créer le dossier de logs et ajuster les permissions
RUN mkdir -p logs && \
    chown -R smartled:smartled /app

# Passer à l'utilisateur non-root
USER smartled

# Exposer le port
EXPOSE 8000

# Variables d'environnement par défaut (à surcharger en production)
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Commande de démarrage
CMD ["uvicorn", "API_osl:app", "--host", "0.0.0.0", "--port", "8000"]