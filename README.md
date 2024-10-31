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

Для создания пайплайна мы проверили наличие git с помощью команды **git --version**, которая показала, что на данной ВМ установлена версия Git 2.20.1.

![image](https://github.com/user-attachments/assets/32ffce49-b4e7-4054-9615-20227769065c)

Затем мы клонировали репозиторий с GitHub на локальный компьютер. 

![image](https://github.com/user-attachments/assets/f7c70945-7f4e-41ef-a3f4-2dc2e8d10128)

Процесс клонирования прошел успешно, и репозиторий был скачан и распакован в локальный каталог api-calculator.

![image](https://github.com/user-attachments/assets/c8b04aae-ebd9-4eef-b7d2-e352d310cb40)

Проверка настройки системы контроля версий. Создали новый файл, добавили его в папку с удаленным репозиторием на ВМ, закоммитили и запушили его на GitHub.

![image](https://github.com/user-attachments/assets/eaeb398e-d5db-4fda-8a72-2b81bc3e0f2a)

Вследствие чего файл в репозитории действительно появился.

![image](https://github.com/user-attachments/assets/5527127b-9690-4bc1-9ff0-a05df4b326d4)

Далее мы пробовали настроить CI/CD с помощью GitLab, но сайт работал некорректно. Затем мы приняли решение настроить непрерывную интеграцию с помощью Jenkins, но эксперимент, очевидно, неудачный... Пробуем настроить с помощью GitHub actions.

Переходим во вкладку Actions нашего репозитория и используем рекомендованные пайплайны для нашего кода. Данный пайплайн как раз при каждом пуше кода пересобирает Docker-контейнер нашего калькулятора.

![image](https://github.com/user-attachments/assets/b785f3b8-ed87-4ee2-8d48-5fd095a5237b)

Изменили калькулятор. После проверки всё работает!

![image](https://github.com/user-attachments/assets/8adc5218-4bd8-47e4-9947-e62742ac0fa7)

## 3. Внедрение открытых инструментов безопасности в пайплайн

Мы выбрали добавление сканирования кода с помощью Grype и Semgrep. Semgrep будет использоваться для статического анализа кода, а Grype будет использоваться для анализа уязвимостей контейнеров и файлов. Для этого обновили наш пайплайн.

```
name: our-pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Build the Docker image
      id: build_image
      run: |
        IMAGE_TAG="my-image-name:$(date +%s)"
        docker build . --file Dockerfile --tag $IMAGE_TAG
        echo "IMAGE_TAG=$IMAGE_TAG" >> $GITHUB_ENV

    - name: Install Semgrep
      run: |
        python3 -m pip install semgrep

    - name: Scan with Semgrep
      uses: returntocorp/semgrep-action@v1
      with:
        config: auto
      continue-on-error: false

    - name: Check Semgrep results
      run: |
        semgrep --config auto --json --output scanning-with-semgrep.json $CI_PROJECT_DIR
        if grep -q '"severity": "CRITICAL"' scanning-with-semgrep.json; then
          echo "CRITICAL vulnerabilities found!"
          exit 1
        else
          echo "No CRITICAL vulnerabilities found."
        fi

    - name: Upload Semgrep report
      uses: actions/upload-artifact@v4
      with:
        name: semgrep-report
        path: scanning-with-semgrep.json

    - name: Install Grype
      run: |
        curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin

    - name: Scan with Grype
      run: |
        docker save ${{ env.IMAGE_TAG }} -o image.tar
        grype image.tar -o json > grype-scan-results.json

    - name: Check Grype results
      run: |
        if grep -q '"severity": "Critical"' grype-scan-results.json; then
          echo "CRITICAL vulnerabilities found in Docker image!"
          exit 1
        else
          echo "No CRITICAL vulnerabilities found in Docker image."
        fi

    - name: Upload Grype report
      uses: actions/upload-artifact@v4
      with:
        name: grype-report
        path: grype-scan-results.json

```

При пуше обновленного пайплайна Semgrep сразу обнаружил критическую уязвимость в нашем коде. Чтобы избежать этой ошибки, мы исправили код (изменили параметр host='127.0.0.1').

![image](https://github.com/user-attachments/assets/ac587c5c-0d97-44b1-914e-4351deebaca1)

После успешного запуска пайплайна, у нас появились артефакты.

![image](https://github.com/user-attachments/assets/e37ff8b0-c9fe-4415-b6d3-7ae0a35ef678)

## 4. Анализ работы инструментов безопасности

Semgrep обнаружил уязвимость в Dockerfile, связанную с отсутствием указания пользователя перед выполнением команды CMD. Это может привести к тому, что программа в контейнере будет запущена от имени пользователя root, что является потенциальной уязвимостью.

![image](https://github.com/user-attachments/assets/10e916fa-daa9-4f9b-86c3-6f8cbc57e92f)

**РЕШЕНИЕ:** чтобы исправить данную ошибку, в Docker-файле нужно перед командой CMD прописать юзера (или создать его), от имени которого будет запускаться команда в контейнере. 

Grype нашел две некритичные уязвимости. Первая уязвимость связана с тем, как OpenSSL обрабатывает определенные криптографические операции с эллиптическими кривыми. В частности, если злоумышленник сможет контролировать входные данные для этих операций, он может вызвать ошибку, которая приведет к выходу за пределы памяти. Это может привести к сбою программы или даже к выполнению вредоносного кода.

![image](https://github.com/user-attachments/assets/b55332d5-3189-456c-8b6e-22a1db8307a8)

**РЕШЕНИЕ:** исправление заключается в обновлении OpenSSL до версии 3.1.7-r1 или более поздней. Но в нашем случае, уязвимость была исправлена автоматически.

Вторая уязвимость была обнаружена в модуле venv и CLI (интерфейсе командной строки) Python. Эта уязвимость связана с тем, как Python обрабатывает имена путей при создании виртуальных сред. Проблема в том, что имена путей, передаваемые в эту команду, не были заключены в кавычки. Это означает, что если злоумышленник сможет контролировать имя пути, он может вставить в него вредоносные команды. Когда виртуальная среда активируется, эти команды будут выполнены.

![image](https://github.com/user-attachments/assets/5378bef3-4dd5-41f5-924a-2eac2b805e14)

**РЕШЕНИЕ:** исправление заключается в обновлении (отслеживаниями обновлений) Python до версии, в которой эта уязвимость уже исправлена. На момент написания этого ответа, точная версия с исправлением не указана. То есть по сути, проблема не в нашем коде, а в самом Python.


