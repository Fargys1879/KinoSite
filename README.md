# KinoSite
Site with Films
Arhitecture
Таблицы и поля
 
1-Категории
имя - Char
описание - Text
url - Slug
2-Фильмы
название - Char
слоган - Char
описание - Text
постер - Image
год - Date
страна - Char
режиссер - M2M
актеры - M2M
жанр - M2M
премьера в мире - Char
бюджет - Char
сборы в США - Char
сборы в мире - Char
категория - FK 
url - Slug
черновик - Bool
3-Кадры из фильма
название - Char
описание - Text
изображение - Image
фильм - FK
4-Режиссеры\Актеры
имя - Char
возраст - Int
описание - Text
изображение - Image
5-Звезды рейтинга
значение - Int
6-Рейтинг
ip - IP
звезда - FK
фильм - FK
7-Отзывы
email - Email
name - Char
text - Text
родитель (кому ответили)
фильм - FK
8-Жанры
имя - Char
описание - Text
url - Slug
