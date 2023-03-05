# Тестовое задание

Реализован интерфейс для доступа к API погоды [https://m3o.com/weather/api](https://m3o.com/weather/api). 

Клонирование репозитория:

```sh
git clone git@github.com:z00k0/m3o-test-task.git
```

Перед запуском необходимо активировать виртуальное окружение и установить зависимости.

```sh
pip install -r requirements.txt`
```

Для работы скрипта необходим `Personal Token`, получаемый на сайте [https://m3o.com](https://m3o.com) при регистрации.

## Работа скрипта
 
```python
# импорт зависимостей
from m3o_weather import Weather

# инициализация 
weather = Weather(api_key=YOUR_API_TOKEN)

# получение текущей погоды
now = weather.now(location="Moscow")

# получение прогноза на три дня
forecast = weather.forecast(location="London", days=3)
```

Пример работы в файле `main.py`. Для запуска необходимо добавить свой апи токен в файл `.env`

