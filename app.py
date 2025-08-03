#!/usr/bin/env python3
"""
Aplicación de ejemplo para Edison New Repository
"""

def main():
    print("¡Hola desde Edison New Repository!")
    print("Este es un proyecto de ejemplo para Docker y GitHub")
    
    # Información del desarrollador
    developer = {
        "nombre": "Ing. Edison Inc",
        "email": "ing.edison.inc@gmail.com",
        "usuario_github": "ing-edison-inc"
    }
    
    print(f"\nDesarrollador: {developer['nombre']}")
    print(f"Email: {developer['email']}")
    print(f"GitHub: {developer['usuario_github']}")

if __name__ == "__main__":
    main() 