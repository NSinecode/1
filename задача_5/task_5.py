import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('library_books.csv')
f = df.nsmallest(3, 'Количество выданных за последний год')

print('Топ-3 популярных книг:')
for idx, row in f.iterrows():
    print(f'{idx}. "{row["Название книги"]}" ({row["Автор"]}) - количество выданных экземпляров: {row["Количество выданных за последний год"]}')

df.groupby('Жанр')['Количество выданных за последний год'].mean().plot(kind='bar')
plt.xlabel('Жанр')
plt.ylabel('Среднее количество проданых книг')
plt.show()
plt.savefig('задача_5_2.png')