<h1 align="center">Проект по тестированию онлайн-магазина 
<p align="center">
<a href="https://www.chitai-gorod.ru/" target="_blank">
<img src="https://upload.wikimedia.org/wikipedia/commons/3/3a/%D0%A7%D0%B8%D1%82%D0%B0%D0%B9-%D0%B3%D0%BE%D1%80%D0%BE%D0%B4.jpg" 
alt="chitai-gorod" width="340" height="164"> </a> 
</p></h1>

### Список реализованных автотестов
- Добавление товара в корзину
- Очищение корзины
- Переход в нужный раздел каталога
- Изменения города
- Проверка наличия подарочных сертификатов

## Структура проекта
### Проект реализован с использованием
|                                   Python                                    |                                   Pytest                                    |                                  PyCharm                                  |                                Selene                                |                                    Jenkins                                    |                           Allure Report                            |                                Telegram                                |
|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|:--------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|:------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| <img src="/images/python-original.svg" alt="Python" width="45" height="45"> | <img src="/images/pytest-original.svg" alt="Pytest" width="45" height="45"> | <img src="/images/PyCharm_Icon.svg" alt="Pycharm" width="45" height="45"> | <img src="/images/selenoid.png" alt="Selene" width="45" height="45"> | <img src="/images/jenkins-original.svg" alt="Jenkins" width="45" height="45"> | <img src="/images/allure.png" alt="Allure" width="45" height="45"> | <img src="/images/telegram.svg" alt="Telegram" width="45" height="45"> |

## Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C09-dasha_korobok-python_unit15_ui_project_chitai-gorod/">Ссылка на проект в Jenkins</a>

### Для запуска автотестов в Jenkins
1. Открыть проект и выбрать пункт "Собрать с параметрами"
<img src="/images/screenshots/jenkins_step1.png">
2. В случае необходимости изменить параметры и нажать на кнопку "Build"
<img src="/images/screenshots/jenkins_step2.png">
3. Результат запуска сборки можно посмотреть в отчёте Allure
<img src="/images/screenshots/allure_step3.png">

### Локальный запуск автотестов
1. Клонируйте репозиторий
  ```ruby
  git clone https://github.com/DariaSkorobogatova/qa_guru_python_9_15.git
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
<img src="/images/screenshots/test.gif" alt="Test example">

### Настроено автоматическое оповещение о результатах в Telegram
<p align="center">
<img src="/images/screenshots/telegram_alert.png" alt="Telegram alert" width="400" height="350">>
</p>
