from search import search_context

if __name__ == "__main__":
    while True:
        query = input("Введите вопрос (или 'exit'): ")
        if query.lower() == "exit":
            break
        print("Ответ:")
        print(search_context(query))
        print("-" * 80)
