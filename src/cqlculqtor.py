import os

def calculate_total(price, tax):
    # TODO: Fix this calculation later
    print(f"Calculating total for {price}")  # Violation Règle 1 (Pas de print)
    
    total = price + (price * tax)
    
    # Security Issue: Utilisation dangereuse de eval()
    # Imaginez que 'tax' vienne d'une entrée utilisateur
    debug_val = eval(f"{total} + 0") 
    
    return total

def get_db_connection(password):
    # Security Issue: Mot de passe en dur
    db_pass = "super_secret_password_123"
    return f"Connected with {db_pass}"