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

// Localization
// Translation strings live in locales.json, keyed by language code ("en", "ru", ...).
// Adding a new language only requires adding a new key there - no JS changes needed
// beyond wiring up a switch option if one isn't already exposed in the UI.
let translations = null;

async function loadTranslations() {
    if (translations) return translations;
    try {
        const response = await fetch('locales.json');
        translations = await response.json();
    } catch (err) {
        console.error('Failed to load locales.json, falling back to English only.', err);
        translations = { en: {} };
    }
    return translations;
}

function applyTranslations(lang) {
    const dict = (translations && translations[lang]) || {};

    document.querySelectorAll('*:not(script):not(style)').forEach(element => {
        if (element.tagName === 'P' || (element.childNodes.length === 1 && element.childNodes[0].nodeType === 3)) {
            const text = element.textContent.trim();
            if (dict[text]) {
                element.textContent = dict[text];
            }
        }

        if (element.title && dict[element.title.trim()]) {
            element.title = dict[element.title.trim()];
        }
    });
}

// Language Management
async function initializeLanguage() {
    const langSwitch = document.getElementById('langSwitch');
    const langText = document.querySelector('.lang-text');
    const savedLang = localStorage.getItem('language') || 'en';

    await loadTranslations();

    if (savedLang === 'ru') {
        langSwitch.checked = true;
        langText.textContent = 'RU';
        document.documentElement.setAttribute('lang', 'ru');
        applyTranslations('ru');
    }

    langSwitch.addEventListener('change', async function (e) {
        if (e.target.checked) {
            langText.textContent = 'RU';
            localStorage.setItem('language', 'ru');
            document.documentElement.setAttribute('lang', 'ru');
            await loadTranslations();
            applyTranslations('ru');
        } else {
            // Reload to cleanly restore the original English text nodes.
            langText.textContent = 'EN';
            localStorage.setItem('language', 'en');
            document.documentElement.setAttribute('lang', 'en');
            window.location.reload();
        }
    });
}

// Initialize everything when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
    initializeTheme();
    initializeSmoothScroll();
    initializeLanguage();
    Prism.highlightAll();
});
