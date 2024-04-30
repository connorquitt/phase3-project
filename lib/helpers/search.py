from models.book import Book

def search():
    while True:
        print('How would you like to search?')
        choice = input('please enter author, title, genre, or back > ')
        if choice.lower() == 'author':
            author = input('Author > ')
            results = Book.find_item_by_author(author)
            if results:
                print(f'Results for "{author}":')
                for item in results:
                    print(f'{item.id}) | {item.title} | {item.author}')
            else:
                print(f'No results for {author}')
                return None
        elif choice.lower() == 'title':
            title = input('title > ')
            results = Book.find_item_by_title(title)
            if results:
                print(f'Results for "{title}":')
                for item in results:
                    print(f'{item.id}) | {item.title} | {item.author}')
            else:
                print(f'No results for "{title}"')
                return None
        elif choice.lower() == 'genre':
            genre = input('genre > ')
            results = Book.find_item_by_genre(genre)
            if results:
                print(f'Results for "{genre}":')
                for item in results:
                    print(f'{item.id}) | {item.title} | {item.author}')
            elif choice.lower() == 'back':
                return None
            else:
                print(f'No results for "{genre}"')
                return None
        else:
            print('Invalid choice, please select from author, title, or genre')