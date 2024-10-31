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

Для создания пайплайна мы проверили наличие git с помощью команды **git --version**, которая показала, что на данном компьютере установлена версия Git 2.20.1.

![image](https://github.com/user-attachments/assets/32ffce49-b4e7-4054-9615-20227769065c)

Затем мы клонировали репозиторий с GitHub на локальный компьютер. 

![image](https://github.com/user-attachments/assets/f7c70945-7f4e-41ef-a3f4-2dc2e8d10128)

Процесс клонирования прошел успешно, и репозиторий был успешно скачан и распакован в локальный каталог api-calculator.

![image](https://github.com/user-attachments/assets/c8b04aae-ebd9-4eef-b7d2-e352d310cb40)

Вследствие чего файл в репозитории действительно появился.

![image](https://github.com/user-attachments/assets/5527127b-9690-4bc1-9ff0-a05df4b326d4)

Проверка настройки системы контроля версий

![image](https://github.com/user-attachments/assets/eaeb398e-d5db-4fda-8a72-2b81bc3e0f2a)


Изначально мы пробовали настроить CI/CD с помощью GitLab, но сайт работал некорректно. Затем мы приняли решение настроить непрерывную интеграцию с помощью Jenkins, но эксперимент, очевидно, неудачный... Пробуем настроить с помощью GitHub actions.

Переходим во вкладку Actions нашего репозитория и используем рекомендованные пайплайны для нашего кода.

![image](https://github.com/user-attachments/assets/b785f3b8-ed87-4ee2-8d48-5fd095a5237b)

Изменили калькулятор. После проверки всё работает!

![image](https://github.com/user-attachments/assets/8adc5218-4bd8-47e4-9947-e62742ac0fa7)







