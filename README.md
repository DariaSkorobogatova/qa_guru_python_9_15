<h1 align="center">Проект по тестированию онлайн-магазина 
<p align="center">
<a href="https://www.chitai-gorod.ru/" target="_blank">
<img src="https://upload.wikimedia.org/wikipedia/commons/3/3a/%D0%A7%D0%B8%D1%82%D0%B0%D0%B9-%D0%B3%D0%BE%D1%80%D0%BE%D0%B4.jpg" 
alt="chitai-gorod" width="320" height="164"> </a> 
</p></h1>

### Список реализованных автотестов
- Добавление товара в корзину
- Очищение корзины
- Переход в нужный раздел каталога
- Изменения города
- Проверка наличия подарочных сертификатов

## Структура проекта
### Проект реализован с использованием
|                                   Python                                    |                                   Pytest                                    |                                              PyCharm                                              |                                            Selene                                            |                                    Jenkins                                    |                           Allure Report                            |                                Telegram                                 |
|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|:------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| <img src="/Images/python-original.svg" alt="Python" width="45" height="45"> | <img src="/Images/pytest-original.svg" alt="Pytest" width="45" height="45"> |             <img src="/Images/PyCharm_Icon.svg" alt="Pycharm" width="45" height="45"> |             <img src="/Images/selenoid.png" alt="Selene" width="45" height="45"> | <img src="/Images/jenkins-original.svg" alt="Jenkins" width="45" height="45"> | <img src="/Images/allure.png" alt="Allure" width="45" height="45"> | <img src="/Images/telegram.svg" alt="Telegram" width="45" height="45">  |

## Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C09-AlexanderOsipkin-unit15/">Ссылка на проект в Jenkins</a>

### Для запуска автотестов в Jenkins
1. Открыть проект
<img src="/Images/Screenshots/img1.png">
2. Выбрать пункт "Собрать с параметрами"
<img src="/Images/Screenshots/img2.png">
3. В случае необходимости изменить параметры и нажать на кнопку "build"
<img src="/Images/Screenshots/img3.png">
4. Результат запуска сборки можно посмотреть в отчёте Allure
<img src="/Images/Screenshots/new_img4.png">

### Локальный запуск автотестов
1. Клонируйте репозиторий
```ruby
gh repo clone AlexanderOsipkin/qa_guru_python_9_15
```
2. Создайте и активируйте виртуальное окружение
  ```ruby
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установите зависимости с помощью pip
  ```ruby
  pip install -r requirements.txt
  ```
4. Запустите автотесты 
  ```ruby
  pytest -sv
  ```
5. Получите отчёт allure
```ruby
allure serve allure-results
``` 

### Пример видеозаписи прохождения теста
<img src="/Images/Screenshots/test.gif" alt="Test example">

### Настроено автоматическое оповещение о результатах в Telegram
<p align="center">
<img src="/Images/Screenshots/new_img5.png" alt="Telegram allert">
</p>
