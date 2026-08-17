# UsableFunctions

[![Version](https://img.shields.io/badge/version-1.7.0-blue.svg)](https://github.com/Artemon0/UsableFunctions)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)

Python-библиотека, которую нужно импортировать один раз — и получить набор функций, которые обычно переписываешь в каждом новом проекте: математика, работа с файлами, управление пакетами, системная и сетевая информация, конвертация файлов и пара небольших игр.

**[📚 Полная документация и интерактивные примеры](https://artemon0.github.io/UsableFunctions/)** — тёмная/светлая тема, EN/RU

---

## Содержание

- [Установка](#установка)
- [Быстрый старт](#быстрый-старт)
- [Справочник функций](#справочник-функций)
  - [Математика](#математика)
  - [Игры](#игры)
  - [Файлы](#файлы)
  - [Конвертация файлов](#конвертация-файлов)
  - [Пакеты и скрипты](#пакеты-и-скрипты)
  - [Хелперы авторизации](#хелперы-авторизации)
  - [Система и сеть](#система-и-сеть)
  - [Circle](#circle-вспомогательный-класс)
- [Известные проблемы](#известные-проблемы)
- [Идеи для новых функций](#идеи-для-новых-функций)
- [Об авторе](#об-авторе)

---

## Установка

### С GitHub (рекомендуется)

```bash
pip install --upgrade git+https://github.com/Artemon0/UsableFunctions.git
```

### Из исходников

```bash
git clone https://github.com/Artemon0/UsableFunctions.git
cd UsableFunctions
pip install -e .
```

### Настройка для разработки

```bash
pip install -r requirements.txt
python build.py all
```

---

## Быстрый старт

```python
from UsableFunctions.UF import UsableFunctions as u

# Калькулятор
result = u.calculator(5, 7, '+')          # 12

# Генерация случайного пароля
password = u.get_random_password(12)

# Проверка числа на чётность
print(u.even_odd(42))                     # "Even"

# Мини-игра quest
u.quest("Player1", difficulty=2)
```

---

## Справочник функций

### Математика

| Функция | Описание |
|---|---|
| `calculator(a, b, op) -> float \| str` | Базовая арифметика: `+ - * / % **` |
| `even_odd(number) -> str` | Возвращает `"Even"` или `"Odd"` |
| `factorial(n) -> int \| str` | Собственная реализация факториала |
| `math_factorial(n) -> int` | Факториал через `math.factorial` |
| `while_calculator() -> None` | Интерактивный калькулятор в цикле (работает до выхода) |
| `Circle` | Класс для расчётов кругового движения — [см. ниже](#circle-вспомогательный-класс) |

### Игры

| Функция | Описание |
|---|---|
| `quest(player="Unnamed", difficulty=1) -> str` | Текстовая математическая викторина, сложность `1–3` |
| `game() -> str` | Игра «угадай число» |
| `say_hello(name) -> str` | Возвращает приветствие |
| `say_goodbye(name) -> str` | Возвращает прощание |

### Файлы

| Функция | Описание |
|---|---|
| `write_in_new_file(filename, content) -> str` | Создать файл и записать в него содержимое |
| `read_from_file(filename) -> str` | Прочитать содержимое файла |
| `delete_file(filename) -> str` | Удалить файл |
| `rename_file(old_name, new_name) -> str` | Переименовать файл |
| `move_file(source, destination) -> str` | Переместить файл |
| `create_new_file(filename, content="", filepath=".") -> str` | Новая версия `write_in_new_file` с указанием директории |
| `read_file_content(filepath) -> str` | Новая версия `read_from_file` |
| `download_file(url, file_path) -> str` | Потоковая загрузка файла по URL |
| `compress_folder(folder_path, archive_file_path, password="") -> None` | Заархивировать папку |
| `extract_archive(archive_path, extract_to=".") -> str` | Распаковать `.zip`-архив |
| `get_file_hash(filepath, algorithm="sha256") -> str` | Хеш файла (`sha256`, `md5` и др.) |
| `get_folder_size(folder_path) -> str` | Суммарный размер папки в МБ ⚠️ *см. [Известные проблемы](#известные-проблемы)* |

### Конвертация файлов

Всё в классе `UsableFunctions.FileConverter`:

| Функция | Описание |
|---|---|
| `png_to_jpg(png_file, jpg_file) -> str` | Конвертация PNG → JPG |
| `jpg_to_png(jpg_file, png_file) -> str` | Конвертация JPG → PNG |
| `txt_to_pdf(txt_file, pdf_file) -> str` | Конвертация TXT → PDF |
| `pdf_to_txt(pdf_file, txt_file) -> str` | Конвертация PDF → TXT |
| `jpgs_to_pdf(*jpg_files, pdf_file) -> str` | Объединить несколько JPG в один PDF |
| `FileConverter.gui.gui()` | Универсальный GUI-лаунчер (Tkinter) для конвертеров выше |
| `FileConverter.gui.converter(mode="png_to_jpg")` | Открыть GUI конкретного конвертера напрямую |

> Примечание: `pdf_to_jpgs` (PDF → несколько JPG) упоминается в старой документации, но пока не реализован — см. [Идеи для новых функций](#идеи-для-новых-функций).

### Пакеты и скрипты

| Функция | Описание |
|---|---|
| `install_package(package) -> str` | `pip install <package>` |
| `uninstall_package(package) -> str` | `pip uninstall <package>` |
| `install_package_git(full_git_url="", creator_name="Artemon0", repo_name="UsableFunctions") -> dict` | Установка пакета прямо из Git-репозитория с прогресс-баром |
| `update_this_program() -> str` | Обновить UsableFunctions до последней версии |
| `update_this_program_visual() -> str` | То же самое, но с прогресс-баром `tqdm` |
| `py_to_exe(file="main.py") -> str` | Собрать `.py`-скрипт в отдельный `.exe` через PyInstaller |
| `run_py_file(filepath="") -> str` | Запустить Python-файл в подпроцессе |
| `run_py_file_with_args(filepath="", args=[]) -> str` | То же самое, но с аргументами командной строки |
| `run_python_code(code) -> str` | Выполнить строку с Python-кодом |
| `get_progress_bar(iterable, desc="Processing", ncols=60)` | Обернуть итерируемый объект в прогресс-бар `tqdm` |
| `is_pressed(key) -> bool` | Проверить, нажата ли клавиша сейчас (через `pygame`) |
| `function_time(function) -> float` | Измерить время выполнения функции |

### Хелперы авторизации

> Это простые хелперы для прототипов и учебных проектов, а **не** замена полноценной системы авторизации (нет хеширования, нет соли — не используйте их для хранения реальных паролей пользователей).

| Функция | Описание |
|---|---|
| `token(token, valid_token=...) -> dict` | Сравнить токен с ожидаемым значением |
| `users(users, user) -> dict` | Проверить, есть ли пользователь в списке |
| `register(users, new_user) -> list` | Добавить нового пользователя, автоматически увеличивая `id` при коллизии |
| `check_password(username, password, correct_username, correct_password, password_min_length=0) -> bool` | Проверить учётные данные, с опциональной проверкой минимальной длины пароля |

### Система и сеть

| Функция | Описание |
|---|---|
| `get_ip_address() -> str` | Локальный IP-адрес |
| `get_external_ip() -> str` | Публичный IP-адрес (через ipify) |
| `get_mac_address() -> str` | MAC-адрес |
| `get_machine_info() -> dict` | Hostname, IP, MAC, платформа, версия Python |
| `get_memory_info() -> dict` | Всего/доступно/использовано ОЗУ и процент использования |
| `get_disk_info() -> dict` | Статистика использования диска |
| `get_cpu_info() -> dict` | Число ядер, частота, загрузка CPU |
| `ping_host(host="8.8.8.8") -> bool` | Пинг хоста, возвращает доступность |
| `optimize_system() -> dict` | ⚠️ Очищает кэш памяти, DNS-кэш и временные файлы. **Использовать осторожно** — может повлиять на стабильность системы и ненадолго обрывает сетевое соединение. |
| `system_panel()` | GUI-панель (Tkinter) с системной информацией в реальном времени и кнопкой «оптимизировать» |

### Circle (вспомогательный класс)

`UsableFunctions.Circle(radius=0, T=0, N=0, t=0)` — расчёты кругового движения для физических задач.

| Метод | Описание |
|---|---|
| `calculate_v(radius, T) -> float` | Скорость (длина окружности) |
| `calculate_T(t=0, N=0, n=0) -> float` | Период |
| `calculate_n(N, t) -> float` | Частота |
| `calculate_N(n, t) -> float` | Число оборотов |
| `calculate_t(N, t) -> float` | Время |

---

## Известные проблемы

- **`get_folder_size`** сейчас обращается к неинициализированной переменной `total_size` вместо заведённого аккумулятора `size`, из-за чего функция падает с `NameError` вместо возврата значения. Стоит поправить перед следующим релизом.
- **`pdf_to_jpgs`** упоминается в некоторых местах документации, но не реализован в `UF.py` — либо реализовать, либо убрать из документации во избежание путаницы.
- **Хелперы авторизации** (`token`, `users`, `register`, `check_password`) хранят и сравнивают учётные данные в открытом виде без хеширования — нормально для демо, рискованно для реальных аккаунтов. Стоит везде, где они упоминаются, добавить короткое предупреждение (уже добавлено выше).

---

## Идеи для новых функций

Несколько направлений, которые органично впишутся в стиль библиотеки:

**Файлы и данные**
- `read_json` / `write_json` — загрузка/сохранение JSON одной функцией вместо шаблонного `open()` + `json.load`/`dump`
- `read_csv` / `write_csv` — тонкая обёртка над `csv`/`pandas` для быстрой работы с таблицами
- `merge_files(files, output)` — объединить несколько текстовых файлов в один
- `watch_folder(path, callback)` — вызывать функцию при изменении содержимого папки

**Текст и строки**
- `slugify(text) -> str` — превратить строку в URL-совместимый slug
- `generate_lorem(paragraphs=1) -> str` — генератор текста-заглушки
- `count_words(text) -> dict` — подсчёт частоты слов

**Сеть**
- `is_port_open(host, port) -> bool` — быстрая проверка TCP-порта, дополняет `ping_host`
- `get_weather(city) -> dict` — обёртка над публичным API погоды
- `shorten_url(url) -> str` — сокращение ссылок через публичный API

**Безопасность и валидация**
- `validate_email(email) -> bool`
- `hash_password(password) -> str` / `verify_password(password, hashed) -> bool` — нормальное хеширование с солью (например, через `bcrypt`), чтобы ответственно заменить текущий проверяющий пароли в открытом виде `check_password` для реального использования

**Инструменты разработчика**
- `benchmark(function, runs=1) -> dict` — запустить `function_time` несколько раз и вернуть min/max/среднее
- `retry(function, attempts=3, delay=1)` — декоратор/обёртка для повторных попыток при нестабильных вызовах
- `env(key, default=None)` — типизированное чтение `.env` / переменных окружения

**Развлечения / игры**
- `rock_paper_scissors(player_choice) -> str`
- `tic_tac_toe()` — консольные крестики-нолики для двух игроков, в духе `quest`/`game`

---

## Об авторе

Я Артём, Python-разработчик, работаю над open-source инструментами и библиотеками.

- **Telegram:** [@Artemon0000](https://t.me/Artemon0000)
- **Канал:** [Telegram](https://t.me/AOGames888)
- **GitHub:** [Artemon0](https://github.com/Artemon0)

English version of this documentation: [README.md](README.md)
