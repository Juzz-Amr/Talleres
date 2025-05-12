import json

JSON_FILE = "data.json.json"

def load_data():
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"Archivo {JSON_FILE} cargado correctamente")
        return data
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {JSON_FILE}")
        print("Asegúrese de que:")
        print(f"1. El archivo {JSON_FILE} existe en el mismo directorio que este script")
        print(f"2. El nombre del archivo es exactamente '{JSON_FILE}'")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo {JSON_FILE} no tiene formato JSON válido")
        return None

def show_all_books(data):
    print("\nTodos los libros disponibles:")
    for book in data['books']:
        print(f"• {book['title']} por {book['author']} ({book['year']})")
        print(f"  Géneros: {', '.join(book['genres'])}")
        print(f"  Ratings: Goodreads {book['ratings']['goodreads']}, Amazon {book['ratings']['amazon']}\n")

def show_books_before_year(data, year):
    print(f"\nLibros publicados antes de {year}:")
    found = False
    for book in data['books']:
        if book['year'] < year:
            found = True
            print(f"- {book['title']} ({book['year']})")
    
    if not found:
        print(f"No hay libros publicados antes de {year}")

def show_highest_rated(data, platform):
    print(f"\nLibro con mejor rating en {platform}:")
    highest = None
    for book in data['books']:
        current_rating = book['ratings'].get(platform.lower())
        if current_rating:
            if highest is None or current_rating > highest[1]:
                highest = (book['title'], current_rating)
    
    if highest:
        print(f"{highest[0]} con rating de {highest[1]}")
    else:
        print(f"No se encontraron ratings para {platform}")

def main():
    biblioteca = load_data()
    if not biblioteca:
        return
    
    show_all_books(biblioteca)
    show_books_before_year(biblioteca, 1950)
    show_highest_rated(biblioteca, "goodreads")
    show_highest_rated(biblioteca, "amazon")
    
    print("\nEstadísticas generales:")
    print(f"Total de libros: {biblioteca['total_books']}")
    print(f"Género más popular: {biblioteca['most_popular_genre']}")

if __name__ == "__main__":
    main()