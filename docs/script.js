// Theme Management
function initializeTheme() {
    const themeSwitch = document.getElementById('themeSwitch');
    // Default to light theme if no theme is saved
    const savedTheme = localStorage.getItem('theme') || 'light';

    // Apply the saved theme or default to light
    document.documentElement.setAttribute('data-theme', savedTheme);
    themeSwitch.checked = savedTheme === 'dark';

    themeSwitch.addEventListener('change', function (e) {
        if (e.target.checked) {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
        }
    });
}

// Smooth Scroll
function initializeSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}

// Language Management
function initializeLanguage() {
    const langSwitch = document.getElementById('langSwitch');
    const langText = document.querySelector('.lang-text');
    const savedLang = localStorage.getItem('language') || 'en';

    if (savedLang === 'ru') {
        langSwitch.checked = true;
        langText.textContent = 'RU';
        document.documentElement.setAttribute('lang', 'ru');
        translateToRussian();
    }

    langSwitch.addEventListener('change', function (e) {
        if (e.target.checked) {
            langText.textContent = 'RU';
            localStorage.setItem('language', 'ru');
            document.documentElement.setAttribute('lang', 'ru');
            translateToRussian();
        } else {
            langText.textContent = 'EN';
            localStorage.setItem('language', 'en');
            document.documentElement.setAttribute('lang', 'en');
            translateToEnglish();
        }
    });
}

// Initialize everything when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeTheme();
    initializeSmoothScroll();
    initializeLanguage();
    Prism.highlightAll();
});

// Russian Translations
function translateToRussian() {
    const translations = {
        'A powerful Python utility library for everyday tasks': 'Мощная библиотека Python для повседневных задач',
        'View on GitHub': 'Смотреть на GitHub',
        'Get Started': 'Начать работу',
        'Installation': 'Установка',
        'Choose your preferred installation method:': 'Выберите предпочтительный способ установки:',
        'From ZIP': 'Из ZIP-архива',
        'Download ZIP': 'Скачать ZIP',
        'As a Package (Recommended)': 'Как пакет (Рекомендуется)',
        'Quick Start': 'Быстрый старт',
        'Get started with this simple example:': 'Начните с этого простого примера:',
        'Available Functions': 'Доступные функции',
        'Features': 'Особенности',
        'Easy to Use': 'Простота использования',
        'Simple and intuitive API design': 'Простой и интуитивный дизайн API',
        'Comprehensive': 'Комплексность',
        'Wide range of utility functions for common tasks': 'Широкий спектр утилит для повседневных задач',
        'Well Documented': 'Хорошая документация',
        'Clear documentation and examples for each function': 'Понятная документация и примеры для каждой функции',
        'Actively Maintained': 'Активная поддержка',
        'Regular updates and improvements': 'Регулярные обновления и улучшения',
        'About Me': 'Обо мне',
        'Python Developer': 'Python Разработчик',
        '12 y.o. Opensource Python developer focused on creating useful tools and libraries for the community. Creator of UsableFunctions and UsableFunctionsJava': '12-летний Python разработчик с открытым исходным кодом, создающий полезные инструменты и библиотеки для сообщества. Создатель UsableFunctions и UsableFunctionsJava',
        'Current Version': 'Текущая версия',
        'License': 'Лицензия',
        'Email Me': 'Написать',
        'GitHub Profile': 'Профиль GitHub',
        'Telegram Channel': 'Канал Telegram',
        'All rights reserved.': 'Все права защищены.',
        'Perform basic arithmetic operations': 'Выполнение базовых арифметических операций',
        'Interactive math quiz game with difficulty levels 1-3': 'Интерактивная математическая игра-викторина с уровнями сложности 1-3',
        'Convert Python scripts to standalone executables': 'Конвертация Python-скриптов в автономные исполняемые файлы',
        'Generate secure random passwords': 'Генерация безопасных случайных паролей',
        'Calculate factorial of a number': 'Вычисление факториала числа',
        'Check if a specific key is pressed': 'Проверка нажатия определенной клавиши',
        'Install Python packages from Git repositories': 'Установка пакетов Python из репозиториев Git',
        'Create and write content to new files': 'Создание и запись содержимого в новые файлы',
        'Read content from existing files': 'Чтение содержимого из существующих файлов',
        'Delete a file from the system': 'Удаление файла из системы',
        'Rename an existing file': 'Переименование существующего файла',
        'Move a file to a new location': 'Перемещение файла в новое местоположение',
        'Class for circular motion calculations (velocity, period, frequency)': 'Класс для расчетов кругового движения (скорость, период, частота)',
        'Get the IP address of the current machine': 'Получение IP-адреса текущего компьютера',
        'Get MAC address of the current machine': 'Получение MAC-адреса текущего компьютера',
        'Get information about the current machine(hostname, ip address, mac address, platform, python version)': 'Получение информации о текущем компьютере (hostname, ip address, mac address, platform, python version)',
        'Get memory usage information': 'Получение информации о использовании памяти',
        'Optimize system performance by clearing memory cache. WARNING: Use with caution! This may affect system stability and you need to reload the internet': 'Оптимизация производительности системы путем очистки кэша памяти. ВНИМАНИЕ: Используйте с осторожностью! Это может повлиять на стабильность системы и потребуется перезагрузить интернет',
        'Get disk usage information': 'Получение информации о использовании диска',
        'Get CPU usage information': 'Получение информации о использовании CPU',
        'System information panel': 'Панель информации о системе',
        'In this class, you can convert files from one format to another(png -> jpg, jpg -> png, etc.)': 'В этом классе вы можете конвертировать файлы из одного формата в другой (png -> jpg, jpg -> png, и т.д.)',
    };

    document.querySelectorAll('*:not(script):not(style)').forEach(element => {
        // if (element.tagName === 'STRONG') return;

        if (element.tagName === 'P' || (element.childNodes.length === 1 && element.childNodes[0].nodeType === 3)) {
            const text = element.textContent.trim();
            if (translations[text]) {
                element.textContent = translations[text];
            }
        }

        if (element.title && translations[element.title.trim()]) {
            element.title = translations[element.title.trim()];
        }
    });
}

// Return to English
function translateToEnglish() {
    window.location.reload();
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', function () {
    initializeTheme();
    initializeLanguage();
    initializeSmoothScroll();
});
