const root = document.documentElement;
const themeSwitch = document.querySelector("#theme-switch");
const languageSwitch = document.querySelector("#language-switch");
const search = document.querySelector("#reference-search");
const empty = document.querySelector("#reference-empty");
const announcements = document.querySelector("#announcements");
const fullReference = document.querySelector("#full-reference");
const groups = Array.from(document.querySelectorAll(".api-group"), (section) => ({
    section,
    link: document.querySelector('.topics a[href="#' + section.id + '"]'),
    rows: Array.from(section.querySelectorAll(".api-row")),
}));

let language = "en";
let translations = {};

function loadPreference(name) {
    try {
        return localStorage.getItem(name);
    } catch {
        return null;
    }
}

function savePreference(name, value) {
    try {
        localStorage.setItem(name, value);
    } catch {
        // The control remains usable with storage blocked.
    }
}

function setTheme(theme) {
    root.dataset.theme = theme;
    themeSwitch.setAttribute("aria-pressed", String(theme === "dark"));
}

themeSwitch.hidden = false;
setTheme(root.dataset.theme === "dark" ? "dark" : "light");
themeSwitch.addEventListener("click", () => {
    const theme = root.dataset.theme === "dark" ? "light" : "dark";
    setTheme(theme);
    savePreference("theme", theme);
});

function updateTopics() {
    for (const { link, section } of groups) {
        if (location.hash === "#" + section.id) {
            link.setAttribute("aria-current", "location");
        } else {
            link.removeAttribute("aria-current");
        }
    }
}

function filterReference() {
    const query = search.value.trim().toLocaleLowerCase(language);
    const tokens = query ? query.split(/\s+/) : [];
    let hasResults = false;

    for (const { section, link, rows } of groups) {
        for (const row of rows) {
            const text = row.textContent.toLocaleLowerCase(language);
            row.hidden = !tokens.every((token) => text.includes(token));
        }
        const hasMatch = rows.some((row) => !row.hidden);
        section.hidden = link.hidden = !hasMatch;
        hasResults ||= hasMatch;
    }
    document.querySelector(".topics").hidden = !hasResults;
    empty.hidden = hasResults;
}

search.closest(".search").hidden = false;
search.addEventListener("input", filterReference);
window.addEventListener("hashchange", updateTopics);
updateTopics();

function setLanguage(nextLanguage) {
    language = nextLanguage;
    root.lang = language;
    const labels = translations[language];
    for (const element of document.querySelectorAll("[data-i18n]")) {
        element.textContent = labels[element.dataset.i18n];
    }
    for (const element of document.querySelectorAll("[data-i18n-label]")) {
        element.setAttribute("aria-label", labels[element.dataset.i18nLabel]);
    }
    search.placeholder = labels[search.dataset.i18nPlaceholder];
    languageSwitch.textContent = language.toUpperCase();
    languageSwitch.setAttribute("aria-label", labels.language);
    fullReference.href = language === "ru"
        ? "https://github.com/Artemon0/UsableFunctions/blob/main/README_ru.md#справочник-функций"
        : "https://github.com/Artemon0/UsableFunctions/blob/main/README.md#function-reference";
    filterReference();
}

async function loadTranslations() {
    try {
        const response = await fetch("locales.json");
        if (!response.ok) return;
        translations = await response.json();
        setLanguage(loadPreference("language") === "ru" ? "ru" : "en");
        languageSwitch.hidden = false;
        languageSwitch.addEventListener("click", () => {
            setLanguage(language === "en" ? "ru" : "en");
            savePreference("language", language);
        });
    } catch {
        // Keep the original English markup if the translations are unavailable.
    }
}

loadTranslations();

function announce(message) {
    announcements.textContent = message;
}

for (const button of document.querySelectorAll("[data-copy]")) {
    const source = document.getElementById(button.dataset.copy);
    const label = button.querySelector("[data-i18n]");
    let reset;
    button.hidden = false;
    button.addEventListener("click", async () => {
        try {
            await navigator.clipboard.writeText(source.textContent);
            clearTimeout(reset);
            const copied = translations[language]?.copied || "Copied";
            label.textContent = copied;
            announce(copied);
            reset = setTimeout(() => {
                label.textContent = translations[language]?.copy || "Copy";
            }, 1600);
        } catch {
            const selection = window.getSelection();
            const range = document.createRange();
            range.selectNodeContents(source);
            selection.removeAllRanges();
            selection.addRange(range);
            announce(translations[language]?.["copy-failed"] || "Select and copy the code manually.");
        }
    });
}
