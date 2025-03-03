# Проект по автоматизации тестирования Gismeteo.ru
<a target="_blank" href="https://gismeteo.ru/">Сайт проекта</a>

## 📄 Содержание
- [Технологии и инструменты](#tech_and_ins-технологии-и-инструменты)
- [Примеры UI тестов](#pager-Примеры-UI-тестов)
- [Сборка в Jenkins с параметрами](#-Сборка-в-Jenkins-с-параметрами)
- [Allure отчет](#-Allure-отчет)
- [Отчет в Telegram с помощью бота](#-Отчет-в-Telegram-с-помощью-бота)
- [Видео прохождения тестов на Selenoid](#film_projector-Видео-прохождения-тестов-на-Selenoid)

## :wrench: Технологии и инструменты
<p>
<a href="https://www.python.org/"><img src="resources/python.svg" width="50" height="50"  alt="Python" title="Python"/></a>
<a href="https://www.jetbrains.com/pycharm/"><img src="resources/PyCharm_Icon.svg" width="50" height="50"  alt="Pycharm" title="IntelliJ IDEA"/></a>
<a href="https://github.com/"><img src="resources/Github.svg" width="50" height="50"  alt="Github" title="GitHub"/></a>
<a href="https://www.selenium.dev/"><img src="resources/selenium.svg" width="50" height="50"  alt="Selenium" title="Selenium"/></a>
<a href="https://github.com/yashaka/selene"><img src="resources/selene.png" width="50" height="50"  alt="Selene" title="Selene"/></a>
<a href="https://aerokube.com/selenoid/"><img src="resources/Selenoid.svg" width="50" height="50"  alt="Selenoid" title="Selenoid"/></a>
<a href="https://www.jenkins.io/"><img src="resources/Jenkins.svg" width="50" height="50"  alt="Jenkins" title="Jenkins"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="resources/Allure_Report.svg" width="50" height="50"  
alt="Allure" title="Allure"/></a>
<a href="https://telegram.org/"><img src="resources/Telegram.svg" width="50" height="50"  alt="Telegram" title="Telegram"/></a>
<a href="https://qameta.io/"><img src="resources/Allure_Testops.svg" width="120" height="50"  alt="Allure_Test_Ops" title="Allure_Test_Ops"/></a>



В данном проекте автотесты написаны на <code>Python</code> с использованием <code>Selenium</code>, <code>Selene</code> и <code>Pytest</code> для UI-тестов
>
> <code>Selenoid</code> выполняет запуск браузеров в контейнерах <code>Docker</code>.
>
> <code>Allure Report</code> формирует отчет о запуске тестов.
>
> <code>Jenkins</code> выполняет запуск тестов.
> После завершения прогона отправляются уведомления с помощью бота в <code>Telegram</code>.


## :pager: Примеры UI тестов
- Проверка тайтла страницы
- Проверка работоспособности поиска
- Проверка корректности наименования страниц
- Проверка навигационого бара


## <img src="resources/Jenkins.svg" width="25" height="25"  alt="Jenkins" title="Jenkins"/></a> Сборка в Jenkins с параметрами
>
> В сборке присутствуют настраиваемые параметры.
>
> Например версия запускаемого браузера или платформа тестируемого сайта. Сами тесты запускаются удаленно с помощью <code>Selenoid</code>
<p align="center">
<img title="Сборка в Jenkins с параметрами" src="resources/Jenkins_parametrs.png">
</p>

## <img src="resources/Allure_Report.svg" width="25" height="25"  alt="Allure_Report" title="Allure_Report" title="Allure_Report"/></a> Allure отчет
>
> Allure формирует подробный отчет о прогоне тестов. Кастомные фильтры и листенеры делают отчет максимально понятным
>
> Например в отчет пишутся все селекторы и методы <code>Selene</code>, отчеты формируются по категориям, в конце приложен скриншот, видео запись прогона теста и логи.
<p align="center">
<img title="Allure отчет" src="resources/Allure_Overview.png">
</p>
<p align="center">
<img title="Allure отчет" src="resources/Allure_suites.png">
</p>
<p align="center">
<img title="Allure отчет" src="resources/Allure_graphs.png">
</p>

## <img width="4%" title="Telegram" src="resources/Telegram.svg"> Отчет в Telegram с помощью бота
>
> После прогона всех тестов в <code>Telegram</code> чат автоматически приходит сообщение с полной информацией о прогоне и ссылкой на <code>Allure</code>
>
<p>
<img title="Отчет в Telegram с помощью бота" src="resources/Telegram_results.png">
</p>

## :film_projector: Видео прохождения тестов на Selenoid
>
> <code>Selenoid</code> пишет видео прогона каждого теста и видео прикладывается в отчет <code>Allure</code>
>
<p>
<img title="Selenoid Video" src="resources/video_test.gif" alt="video">
</p>
