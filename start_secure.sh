# Script pour démarrer l'application en mode sécurisé
#!/bin/bash

# Vérifier que les variables d'environnement sont définies
if [ -z "$JWT_SECRET" ]; then
    echo "ERREUR: JWT_SECRET n'est pas défini"
    exit 1
fi

if [ -z "$API_METEO" ]; then
    echo "ERREUR: API_METEO n'est pas défini"
    exit 1
fi

# Créer le dossier de logs
mkdir -p logs

# Démarrer l'application
echo "Démarrage de Python-Monitor..."
uvicorn API_osl:app --host 0.0.0.0 --port 8000 --log-level info