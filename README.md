# YPdiplom
# API-тесты для сервиса заказов 

Этот проект содержит автоматизированные тесты для API сервиса заказов самокатов.  
Тесты написаны на **Python** с использованием `pytest` и библиотеки `requests`.

##  **Шаг 1: Клонируем репозиторий**
git clone https://github.com/ТВОЙ_ЛОГИН/YPdiplom.git
cd YPdiplom
### **Шаг 2: Создаём и активируем виртуальное окружение**
python3 -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
#### **Шаг 3: Устанавливаем зависимости**
pip install pytest requests
и затем сгенерируй requirements.txt:
pip freeze > requirements.txt
После установки запусти тест:
pytest -v
**Структура проекта**
📂 YPdiplom ├── 📄 configuration.py # Конфигурация API (URL и эндпоинты) ├── 📄 data.py # Тестовые данные (JSON для заказов) ├── 📄 stand.py # Функции взаимодействия с API ├── 📄 test_order.py # Автоматические тесты (pytest) ├── 📄 .gitignore # Исключения для Git └── 📄 README.md # Документация проекта
