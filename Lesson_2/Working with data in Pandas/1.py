# Задание 1
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id
# и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:
# [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].

import pandas as pd

authors = pd.DataFrame({'author_id': [1, 2, 3],
                        'author_name': ['Тургенев', 'Чехов', 'Островский']})

book = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                     'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price': [450, 300, 350, 500, 450, 370, 290]})

print(authors)
print(book)
