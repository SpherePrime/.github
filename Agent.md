# Agent Guidelines & Project Architecture — SpherePrime .github

## 1. Архитектурный Стандарт и Организация (SpherePrime)
- **Организация:** SpherePrime (`https://github.com/SpherePrime`)
- **Основатели и Соавторы:**
  - **LilKALINOV** (`@LilKALINOV`) — Co-founder, Lead QA Astra, системная архитектура, тестирование ИИ-агентов, Rust / Python / Desktop.
  - **dwertyfa** (`@dwertyfa288`) — Co-founder, Full-stack инженер, Three.js, веб-платформы, PrimeBoost VPN, Astra плагины, Rust.
- **Экосистема проектов:**
  - **Prime CLI** (`SpherePrime/CLI`) — флагманский терминальный ИИ-ассистент на Go с поддержкой MCP, LSP, сессий и голосового ввода.
  - **Prime Desktop** (`SpherePrime/CLI/tree/main/desktop`) — кроссплатформенный рабочий стол на Tauri v2 (Windows) и Electron (Linux).
  - **PrimeBoost** (ранее RoxyBoost / `roxyvpn.ru`) — высокоскоростной VPN-сервис и защищённый сетевой протокол с Rust-ядром.
  - **PrimeAi** (`SpherePrime/PrimeAi`) — интеллектуальный AI-роутер для Astra с динамической маршрутизацией запросов.
  - **PrimeProxy** (`SpherePrime/PrimeProxy`) — локальный MTProto-прокси для Telegram на Rust с WebSocket-транспортом.
  - **Astra-PrimeProxy** (`SpherePrime/Astra-PrimeProxy`) — защищенный прокси-транспорт для голосового ассистента Astra.
  - **PrimeAutoAccept** (`SpherePrime/PrimeAutoAccept`) — Astra-плагин быстрого автопринятия матчей (LoL, Dota 2, CS2).

---

## 2. Структура Репозитория .github
- `profile/README.md` — официальный README профиля организации SpherePrime, отображаемый на странице `https://github.com/SpherePrime`.
- `profile/assets/` — SVG-компоненты, векторные баннеры, интерактивные карточки проектов и бейджи профиля.
- `assets/` — зеркальная директория ассетов для бесшовного разрешения путей при просмотре репозитория из корня.
- `README.md` — корневой README репозитория `.github`.
- `generate_profile_assets.py` — генератор векторной графики в единой темной эстетике SpherePrime.
- `Agent.md` — архитектурный манифест и инструкции для агентов.
- `CHAT.md` — журнал диалогов, история решений и статус задач.

---

## 3. Правила Разработки и Оформления
1. **Единый визуальный язык:**
   - Dark industrial aesthetic (`#121211` фон, `#0e0e0d` подложки, `#2d2c29` разделители, `#ff5b14` фирменный оранжевый акцент, `#ecebe5` текст, `#8d8b85` вторичный текст).
   - Векторные SVG-баннеры с анимациями без растровой деградации.
   - Адаптивность и читаемость на экранах любой ширины (включая мобильные клиенты GitHub).
2. **Git и Авторство:**
   - Автор коммитов: строго **Lil KKALINOV** (`150132236+LilKALINOV@users.noreply.github.com`).
   - Запрещены сторонние соавторы (`Co-authored-by`).
3. **Проверка перед завершением (Completion Check):**
   - Все SVG проверяются на валидность XML.
   - Все ссылки ведут на актуальные репозитории и сайты.

---

## 4. Датасет Предотвращения Ошибок (Error Prevention Rulebook)
1. **GitHub Org Profile Assets:**
   - *Проблема:* GitHub при отображении `profile/README.md` на странице организации может разрешать относительные пути как относительно `profile/`, так и относительно корня.
   - *Правило:* Ассеты сохраняются в обоих каталогах (`profile/assets/` и `assets/`), пути в Markdown указываются как `./assets/...`.
2. **SVG XML валидность:**
   - *Проблема:* Символы `&` или незакрытые теги в тексте SVG ломают XML-парсер браузера.
   - *Правило:* Заменять амперсанды на `&amp;`, проверять парсером `xml.etree.ElementTree` перед коммитом.
3. **Именование RoxyBoost:**
   - *Правило:* Продукт RoxyBoost сохранён и представлен в обновлённом бренде **PrimeBoost** с указанием исторической преемственности (`RoxyBoost → PrimeBoost`).
