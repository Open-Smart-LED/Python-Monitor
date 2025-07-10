#!/usr/bin/env python3
"""
Script pour générer des secrets sécurisés pour Python-Monitor
Usage: python generate_secrets.py
"""

import secrets
import string

def generate_jwt_secret(length=32):
    """Génère un secret JWT sécurisé"""
    return secrets.token_urlsafe(length)

def generate_password(length=16):
    """Génère un mot de passe sécurisé"""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def main():
    print("🔐 Générateur de Secrets Sécurisés - Python-Monitor")
    print("=" * 50)
    
    # JWT Secret
    jwt_secret = generate_jwt_secret()
    print(f"JWT_SECRET={jwt_secret}")
    
    # Database password (if needed)
    db_password = generate_password()
    print(f"DATABASE_PASSWORD={db_password}")
    
    # Wi-Fi password suggestion
    wifi_password = generate_password(20)
    print(f"WIFI_PASSWORD={wifi_password}")
    
    print("\n📝 Instructions:")
    print("1. Copiez ces valeurs dans votre fichier .env")
    print("2. Ne partagez jamais ces secrets")
    print("3. Utilisez des secrets différents pour chaque environnement")
    print("4. Changez les secrets régulièrement")

if __name__ == "__main__":
    main()