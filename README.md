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


///Для начала мы проверили, установлен ли Git в терминале, чтобы настроить систему контроля версий нашего калькулятора.

![image](https://github.com/user-attachments/assets/e31c97b4-3641-4484-bbf8-f8b888e5f5eb)

Далее мы клонировали репозиторий с GitHub.

![image](https://github.com/user-attachments/assets/dfad34ab-8fff-4d34-a6f3-ae0c7c3dd3b2)

На виртуальной машине появились все файлы нашего репозитория.

![image](https://github.com/user-attachments/assets/ea1ba96a-7502-4e4b-869b-71f73fcef6d4)

Для проверки возможности внесения изменений в репозиторий с помощью Git, мы создали новый файл, добавили его, закоммитили и запушили, используя предварительно созданный токен репозитория.

![image](https://github.com/user-attachments/assets/34d01932-f41d-4990-a76f-994bbe207848)

Проверили, что файл действительно появился.

![image](https://github.com/user-attachments/assets/eeccca54-7a4b-40b3-985f-ccc2ad737704)

Преходим к настройке пайплайна.
Прописали простую конфигурацию пайплайна для обновления версии калькулятора (.gitlab-ci.yml) и запушили его в основную ветку репозитория.

![image](https://github.com/user-attachments/assets/a90abaca-b66a-4ff5-ad6b-c91983637b4f)_






