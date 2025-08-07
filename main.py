import pandas as pd

# Загружаем данные
df = pd.read_csv("IMDB-Movie-Data.csv")

# Удаляем строки с пропущенными значениями в Genre и Year
df = df.dropna(subset=["Genre", "Year"])

# Сортируем по жанру (по алфавиту) и по году (по убыванию)
df_sorted = df.sort_values(by=["Genre", "Year"], ascending=[True, False])

# Устанавливаем параметры pandas для отображения всех строк
pd.set_option('display.max_rows', None)       # Показывает все строки
pd.set_option('display.max_columns', None)    # Показывает все столбцы
pd.set_option('display.width', None)          # Не обрезает по ширине
pd.set_option('display.max_colwidth', None)   # Не обрезает содержимое ячеек

# Выводим все 1000 фильмов в терминал
print(df_sorted[["Title", "Genre", "Year"]].to_string(index=False))
