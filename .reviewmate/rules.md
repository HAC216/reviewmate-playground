# Règles de Qualité du Projet ReviewMate

Ces règles sont prioritaires et doivent être respectées par l'IA lors de l'analyse.

## 1. Règles de Style Python
- **Interdiction formelle des `print()`** : Tout code de production doit utiliser le module `logging`. Les `print()` sont réservés au débogage local et doivent être retirés avant le merge.
- **Typage Fort** : Toutes les signatures de fonctions doivent avoir des annotations de type (Type Hints). Ex: `def my_func(a: int) -> str:`.
- **Docstrings** : Chaque module, classe et fonction publique doit avoir une docstring explicative.

## 2. Règles de Sécurité
- **Pas de secrets en dur** : Aucune clé API, mot de passe ou token ne doit apparaître dans le code. Utilisez `os.getenv()`.
- **Validation des entrées** : Toute donnée venant de l'extérieur (API, User Input) doit être validée (Pydantic, regex, etc.).

## 3. Règles d'Architecture
- **Fonctions courtes** : Une fonction ne devrait pas dépasser 50 lignes.
- **Nommage explicite** : Les variables comme `x`, `data`, `temp` sont interdites. Utilisez des noms descriptifs (`user_data`, `temporary_file_path`).