user_words = input("Введите нескольких слов, разделённых пробелами: ").split()
for ind, word in enumerate(user_words):
    print(ind, word[:10])
