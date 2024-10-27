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
Для начала мы проверили, установлен ли Git в терминале, чтобы настроить систему контроля версий нашего калькулятора.

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

![image](https://github.com/user-attachments/assets/a90abaca-b66a-4ff5-ad6b-c91983637b4f)






