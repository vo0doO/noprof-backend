Демонстрационный проект трясогузки
=======================

Это демонстрационный проект для удивительной [Wagtail CMS](https://github.com/wagtail/wagtail).

Демонстрационный сайт предназначен для предоставления примеров общих особенностей и рецептов, чтобы познакомить вас с разработкой трясогузки. Помимо кода, он также позволит вам изучить интерфейс администрирования / редактирования CMS.

Примечание. мы не рекомендуем использовать этот проект для запуска собственного сайта-демонстрация предназначена для того, чтобы стать трамплином для начала работы. Не стесняйтесь копировать код из демо-версии в свой собственный проект.

### Особенности трясогузки, продемонстрированные в этой демонстрации

Эта демонстрация предназначена в первую очередь для разработчиков, желающих узнать больше о внутренних частях Wagtail, и предполагает, что вы будете читать его исходный код. После просмотра функций обратите особое внимание на код, который мы использовали для:

- Разделение проекта на несколько приложений
- Пользовательские модели контента и "контексты" в приложениях "хлеб" и "местоположения"
- Типичный веб-блог в приложении "блог" 
- Пример использования" базового " приложения, содержащего разные дополнительные функции (например, контактную форму, информацию и т. д.)
- Модель "StandardPage" с использованием миксинов, заимствованных из других приложений
- Пример настройки администратора Wagtail через _wagtail_hooks_
- Пример использования системы Wagtail "snippets" для представления категорий хлеба, стран и ингредиентов
- Пример пользовательской функции "галереи", которая вытягивает изображения, используемые в других типах контента в системе
- Пример создания множества отношений с помощью функции Ингредиенты на странице хлеб
- Намного больше

**Содержание документа**

- [Установка](#Установка)
- [Следующие шаги](#next-steps)
- [Вклад](#вклад)
- [Другие заметки](#другие заметки)

# Установка

- [Бродяга](#setup-with-vagrant)
- [Docker](#setup-with-docker)
- [Virtualenv](#setup-with-virtualenv)
- [Heroku](#deploy-to-heroku)

Если вы новичок в Python и / или Django, мы предлагаем вам запустить этот проект на виртуальной машине с помощью Vagrant или Docker (в зависимости от того, что вам удобнее). И Vagrant, и Docker помогут решить распространенные проблемы зависимости программного обеспечения. Разработчиков, знакомых с
virtualenv и традиционные инструкции по настройке приложения Django должны перейти к [Setup with virtualenv] (#setup-with-virtualenv).

# Установка с Бродягой
------------------

#### Зависимости
* [Бродяга](https://www.vagrantup.com/)
* [Мужской голос](https://www.virtualbox.org/)

#### Установка
После установки необходимых зависимостей выполните следующие команды:

```удар
клон git https://github.com/wagtail/portfolio.git
компакт-портфель
бродяга вверх
бродяга ssh
# затем, в течение сеанса SSH:
./manage.py runserver 0.0.0.0: 8000
```

Демо-сайт теперь будет доступен по адресу [http://localhost:8000/](http://localhost:8000/) и трясогузка админ
интерфейс на [http://localhost:8000/admin/](http://localhost:8000/admin/).

Войдите в режим администрирования с полномочиями `администратора / changeme`.

Используйте "Ctrl+c", чтобы остановить локальный сервер. Чтобы остановить бродячую среду, выполните команду "выход", а затем "остановка бродяги".

Настройки с Настройки
-----------------

#### Зависимости
* [Докер](https://docs.docker.com/engine/installation/)
* [Докер сочинять](https://docs.docker.com/compose/install/)

### Установка
Выполните следующие команды:

```удар
клон git https://github.com/wagtail/portfolio.git
компакт-портфель
docker-compose up-build-d
docker-compose run app / venv / bin / python manage.py load_initial_data
докер-сочиняй
```

Демо-сайт теперь будет доступен по адресу [http://localhost:8000/](http://localhost:8000/) и трясогузка админ
интерфейс на [http://localhost:8000/admin/](http://localhost:8000/admin/).

Войдите в режим администрирования с полномочиями `администратора / changeme`.

** Важно: * * этот ' докер-сочиняй.yml ' настроен только для локального тестирования и не предназначен для производственного использования.

### Отладка
Чтобы отслеживать журналы из контейнеров Docker в реальном времени, выполните:

```удар
docker-составление журналов-f
```

Настройка с помощью Virtualenv
---------------------
Вы можете запустить демонстрационную версию Wagtail локально без настройки Vagrant или Docker и просто использовать Virtualenv, что является [рекомендуемым подходом к установке](https://docs.djangoproject.com/en/1.10/topics/install/#install-the-django-code) для самого Джанго.

#### Зависимости
* Python 3.4, 3.5 или 3.6
* [О virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [VirtualenvWrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) (необязательно)

### Установка

С [Пипом](https://github.com/pypa/pip) и [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
установлен, запущен:

    mkvirtualenv wagtailportfolio
    версия Python

Убедитесь, что это показывает совместимую версию Python 3.x. если нет, и у вас есть несколько версий Python, установленных в вашей системе, вам может потребоваться указать соответствующую версию при создании virtualenv:

    дезактивировать
    rmvirtualenv wagtailportfolio
    mkvirtualenv wagtailportfolio -- python=python3. 6
    версия Python

Теперь мы готовы создать демонстрационный проект пекарни.:

    cd ~ / dev [или ваш предпочтительный каталог dev]
    клон git https://github.com/wagtail/portfolio.git
    компакт-портфель
    pip install-r требования / база.формат txt

Далее мы настроим наши локальные переменные окружения. Мы используем [django-dotenv](https://github.com/jpadilla/django-dotenv)
чтобы помочь в этом. Он считывает переменные окружения, расположенные в имени файла `.env ' в директории верхнего уровня проекта. Единственная переменная, которую нам нужно запустить - это ' DJANGO_SETTINGS_MODULE`:

    $ CP portfolio / settings / local.py. example portfolio/settings/local.py
    $ echo " DJANGO_SETTINGS_MODULE=портфель.настройки.местный" > .ОКР

Чтобы настроить базу данных и загрузить исходные данные, выполните следующие команды:

    ./manage.py мигрировать
    ./manage.py load_initial_data
    ./manage.py runserver

Войдите в режим администрирования с полномочиями `администратора / changeme`.

Развертывание на Heroku
----------------

Если вы не хотите тестировать локально, вы можете развернуть демонстрационный сайт на общедоступном сервере с помощью [Heroku](https://heroku.com)
решение для развертывания в один клик на их бесплатном уровне "хобби":

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/wagtail/portfolio)

Если у вас нет учетной записи Heroku, нажав на кнопку выше, вы пройдете через следующие шаги
чтобы создать его.  На этом этапе вам будет представлен экран для настройки вашего приложения. Для наших целей,
мы примем все значения по умолчанию и нажмем кнопку "развернуть".  Состояние развертывания будет динамически изменяться.
обновление в браузере. После завершения нажмите кнопку "Просмотр", чтобы увидеть общедоступный сайт.

Войдите в режим администрирования с полномочиями `администратора / changeme`.

Чтобы демо-сайт не восстанавливал новый Django " SECRET_KEY` каждый раз, когда Heroku перезапускает ваш сайт, вы должны установить
переменная окружения 'DJANGO_SECRET_KEY` в Heroku, использующая веб-интерфейс или [CLI](https://devcenter.heroku.com/articles/heroku-cli). при использовании CLI, вы можете установить "SECRET_KEY", как так:

    Heroku config: set DJANGO_SECRET_KEY=changeme

Чтобы узнать больше о Heroku, прочитайте [развертывание приложений Python и Django на Heroku](https://devcenter.heroku.com/articles/deploying-python).

### Хранение медиафайлов Wagtail на AWS S3

Если вы развернули демонстрационный сайт на Heroku или через Docker, возможно, потребуется выполнить дополнительную настройку.  Хероку использует
[эфемерная файловая система](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem), и хостинг на базе Docker
среды обычно работают таким же образом.  С точки зрения непрофессионалов, это означает, что загруженные изображения исчезнут в
минимум один раз в день и при каждом развертывании приложения. Чтобы смягчить это, вы можете разместить свой носитель на S3.

В этой документации предполагается, что у вас есть учетная запись AWS, пользователь IAM и правильно настроенная корзина S3. Эта тема
выходят за рамки данной документации; следующее [сообщение в блоге](https://wagtail.io/blog/amazon-s3-for-media-files/)
я проведу вас по этим ступеням.

Этот демонстрационный сайт поставляется с предварительно настроенным файлом производственных настроек, который позволит использовать S3 для хранения загруженных носителей, если
"AWS_STORAGE_BUCKET_NAME" определяется в среде оболочки. Все, что вам нужно сделать, это установить следующую среду
переменные. Если вы используете Heroku, вам сначала нужно установить и настроить [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli затем выполните следующие команды для установки вышеупомянутых переменных среды:

    Heroku config: set AWS_STORAGE_BUCKET_NAME=changeme
    Heroku config: set AWS_ACCESS_KEY_ID=changeme
    Heroku config: set AWS_SECRET_ACCESS_KEY=changeme

Не забудьте заменить "changeme" на фактические значения для вашего аккаунта AWS. Если вы используете другой хостинг
среда, установите там те же переменные среды, используя метод, соответствующий вашей среде.

После того, как Heroku перезапустит ваше приложение или ваш контейнер Docker будет обновлен, у вас должно быть постоянное хранилище мультимедиа!

Бег". /manage.py load_initial_data ' будет копировать локальные изображения в S3, но если вы настроили S3 после запуска его первым
время, которое вам может понадобиться, чтобы запустить его снова.

# Дальнейшие действия

Надеюсь, после того, как вы поэкспериментируете с демо, вы захотите создать свой собственный сайт. Для этого вам нужно будет запустить команду "wagtail start" в выбранной вами среде. Вы можете найти дополнительную информацию в [начало работы Wagtail CMS docs](http://wagtail.readthedocs.io/en/latest/getting_started/index.html).


# Способствующий

Если вы разработчик Python или Django, раскошелитесь на репо и застрянете! Если вы хотите принять участие, вы можете найти наши [руководящие принципы по содействию] (https://github.com/wagtail/portfolio/blob/master/contributing.md) полезное чтение.

### Подготовка этого архива к распространению

Если вы изменили содержимое или изображения в этом РЕПО и вам нужно подготовить новый файл фикстуры для экспорта, выполните следующие действия в ветке:

`./manage.py данные дампа --природно-иностранные отступ 2 -е авт.разрешение-e contenttypes-e wagtailcore.GroupCollectionPermission - e wagtailimages.фильтр-e wagtailcore.pagerevision-e wagtailimages.исполнение-e сессии > портфолио / база / светильники / портфолио.формат JSON`

Пожалуйста, оптимизируйте все включенные изображения до 1200px в ширину со сжатием JPEG на 60%. Обратите внимание, что` media/images `игнорируется в репо по'.gitignore", но "media / original_images" - нет. Локальные "представления" образа трясогузки исключены в приведенном выше рецепте приспособления.

Сделайте запрос на вытягивание, чтобы https://github.com/wagtail/portfolio

# Другие заметки

### Примечание по демо-поиску

Поскольку мы не можем (легко) использовать ElasticSearch для этой демонстрации, мы используем собственный поиск по БД wagtail.
Однако собственный поиск в БД не может выполнять поиск определенных полей в наших моделях по обобщенному запросу "страница".
Поэтому только для демонстрационных целей мы жестко кодируем имена моделей, которые мы хотим искать в " search.взгляды`, который является
не идеальный. В производственной среде используйте ElasticSearch и упрощенный поисковый запрос.
[http://docs.wagtail.io/en/v1.13.1/topics/search/searching.html](http://docs.wagtail.io/en/v1.13.1/topics/search/searching.html).

### Отправка электронной почты из контактной формы

Следующая настройка в `base.py-и `production.py " гарантирует, что живая электронная почта не отправляется с помощью демонстрационной контактной формы.

'EMAIL_BACKEND = "Джанго.ядро.почта.базовая программа.приставка.EmailBackend"`

В производстве на вашем собственном сайте вам нужно будет изменить это на:

'EMAIL_BACKEND = "Джанго.ядро.почта.базовая программа.протокол SMTP.EmailBackend"`

и настроить [настройки SMTP](https://docs.djangoproject.com/en/1.10/topics/email/#smtp-backend) подходит для вашего провайдера электронной почты.

### Владение демонстрационным контентом

Все содержимое демо является общественным достоянием. Текстовый контент в этом проекте либо взят из Википедии, либо является lorem ipsum. Все изображения взяты либо из Викисклада, либо из других источников, не защищенных авторским правом.
