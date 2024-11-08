# Описание
Данная программа собирает данные с сайта "Flashscore" с использованием библиотеки Selenium и сохраняет результаты матчей в таблицу Excel. Программа находит все матчи на странице, фильтрует только завершенные матчи и сохраняет информацию о командах, статусе и счете в файл "Results.xlsx".

# Установка и требования
Для работы программы необходимы следующие библиотеки и компоненты:
- Python 3
- Selenium
- Pandas
- Chromedriver

### Установка необходимых библиотек
Для установки необходимых библиотек выполните следующие команды в терминале:

```sh
pip install selenium
pip install pandas
```

# Установка ChromeDriver
Для запуска данной программы вам потребуется драйвер ChromeDriver. Скачайте его с официального сайта и поместите в папку, доступную для системы. Убедитесь, что путь к драйверу совпадает с указанием в программе (`chromedriver.app`).

# Настройка и запуск
1. Убедитесь, что драйвер ChromeDriver установлен и доступен в системе.
2. Откройте код и проверьте, что путь к драйверу (`chromedriver.app`) корректен. При необходимости измените его.
3. Запустите программу с помощью Python:
   ```sh
   python имя_файла.py
   ```

# Как работает программа
1. **Импорт библиотек**: Программа импортирует библиотеки Selenium, Pandas и дополнительные модули, необходимые для работы драйвера.
2. **Настройка веб-драйвера**: Используется Chrome с опцией открытия в максимальном размере окна.
3. **Переход на сайт**: Программа переходит на сайт "https://www.flashscore.com.ua/", где будут собраны данные матчей.
4. **Сбор данных о матчах**: Найдены все элементы с классом "event__match--twoLine", которые содержат информацию о матчах.
5. **Обработка данных**: Список матчей фильтруется для извлечения только завершенных матчей.
6. **Экспорт данных**: Данные сохраняются в файл Excel "Results.xlsx".

# Колонки в итоговой таблице
- **status**: Статус матча ("Завершен", если матч уже сыгран).
- **team 1**: Название первой команды.
- **team 2**: Название второй команды.
- **goals 1**: Количество голов первой команды.
- **goals 2**: Количество голов второй команды.

# Примечания
- Убедитесь, что версия ChromeDriver соответствует версии установленного браузера Google Chrome.
- Сайт "Flashscore" может изменять верстку, что может повлиять на корректную работу программы. В таком случае нужно будет обновить селекторы для поиска элементов.
- Программа собирает только те матчи, которые имеют статус "Завершен".

# Потенциальные улучшения
- Добавление обработки ошибок для случаев, когда страница недоступна или данные не загружаются.
- Поддержка других браузеров (Firefox, Edge и т.д.).
- Более гибкая фильтрация матчей, например, по типу турнира или дате.

# Лицензия
Эта программа предоставляется без каких-либо гарантий. Используйте на свой страх и риск.
