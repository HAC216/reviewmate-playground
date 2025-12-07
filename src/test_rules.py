import os

# Violation Règle 3 (Nommage) : Nom de variable pas clair
x = "12345"

def process_data(data):  # Violation Règle 1 (Typage) : Pas de types
    # Violation Règle 1 (Docstring) : Pas de docstring
    
    # Violation Règle 2 (Secrets) : Mot de passe en dur
    db_password = "super_secret_password"
    
    if data == "admin":
        # Violation Règle 1 (Print) : Utilisation de print
        print("Admin access granted")
        return True
    
    return False

def complex_calculation():
    # Violation Règle 3 (Fonction courte) : On simule une fonction trop longue
    # (Imaginez 60 lignes de code ici...)
    result = 0
    for i in range(100):
        result += i
    print(f"Result: {result}") # Encore un print
    return result