# API-calculator (РИ-411001, Матова, Коновалова, Моисеенко, Дейнега)
## 1. Создание API-калькулятора
Написание калькулятора происходило на языке Python с помощью Flask. Flask - это легкий и мощный веб-фреймворк для Python, который можно легко установить и настроить.

В первую очередь напишем сам API-калькулятор (our-api-cal.py).

После этого создадим Docker-образ, в котором назначаем базовый образ, указываем рабочую директорию, копирование калькулятора в рабочую директорю, устанавливаем Flask и запускаем сам калькулятор.

![image](https://github.com/user-attachments/assets/25ef447f-f347-4c94-9431-730eef5936f5)


Поместим файл калькулятора и Dockerfile в одну директорию.

![image](https://github.com/user-attachments/assets/d912c398-0877-4d13-ab90-f58c85689f56)

Проверим установку докера.

![image](https://github.com/user-attachments/assets/35beb161-0232-401c-8bd9-775769a77995)

Соберем Docker-образ.

![image](https://github.com/user-attachments/assets/2e0ba375-54e3-4d9e-a320-4225f7b47c28)

Запускаем контейнер и проверяем список запущенных контейнеров. 

![image](https://github.com/user-attachments/assets/e46b9c95-b62a-4a1b-bbcf-b7486726888f)

Проверяем работоспособность нашего API-калькулятора.

![image](https://github.com/user-attachments/assets/b089cb8a-9ed2-469e-87e8-bc613c520399)

## 2. Создание пайплайна для обновления версии калькулятора

Первым этапом стала установка Jenkins на Ubuntu.

Перед началом установки проверим, есть ли в системе пакет Java — без него Jenkins не будет работать.

![image](https://github.com/user-attachments/assets/6b81f658-affc-43ce-a13e-f4af44a221c0)

Сначала получаем ключ шифрования GPG с помощью команды **curl**. Ключ нужен для проверки подлинности пакетов, загружаемых из репозитория Jenkins. Чтобы два раза не вставать, установим ключ в систему командой **sudo tee**.
После этого добавим репозиторий Jenkins в список пакетов Ubuntu.

![image](https://github.com/user-attachments/assets/5f50ef5e-e504-4e94-8dfe-4027ac3c3fef)

Обновляем список пакетов и устанавливаем Jenkins. 

![image](https://github.com/user-attachments/assets/2f25235b-1579-4bb4-b052-16a7a6899c98)

Установили ssh и проверили статус работы Jenkins.

![image](https://github.com/user-attachments/assets/13a0cedf-7eaa-4684-afe7-04caf86710b2)

Для нормальной работы Jenkins необходимо было открыть сетевой порт в брандмауре. Для этого открыли SSH, запустили брандмауэр, открыли сетевой порт 8080 и проверили статус.

![image](https://github.com/user-attachments/assets/a6c16476-8d6e-4322-9731-7c948330a4dd)

В интернете открыли окно разблокировки Jenkins по адресу http://10.0.2.15:8080, где 10.0.2.15 - IP сервера.

![image](https://github.com/user-attachments/assets/1db1de4c-1531-4251-a637-42df112c421c)

После этого устанавливаем дефолтный набор плагинов для Jenkins.

![image](https://github.com/user-attachments/assets/f81c2eec-3088-4925-b41e-8267073f56bd)

Далее создаем пайплайн.

![image](https://github.com/user-attachments/assets/bc132ced-3318-4ed0-bed6-bf1d64c31a36)

Скрипт для обновления пайплайна.

![image](https://github.com/user-attachments/assets/7781be99-941a-4c0d-a084-4476bc8dfec3)

Автоматический запуск пайплайна при изменении кода в репозитории.

![image](https://github.com/user-attachments/assets/fb476c92-6655-4c39-97d0-59c4dfc6b94c)

В настройках добавили ссылку на наш репозиторий GitHub.

![image](https://github.com/user-attachments/assets/b808b556-2d0e-46a4-b628-1430da8d9708)







