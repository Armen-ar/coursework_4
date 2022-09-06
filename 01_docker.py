"""
Публикация в интернете сайта:
----------------------------
1-ый способ через виртуальный хостинг:
создаём аккаунт в хостинге, заходим в систему администрирования и там есть доступ к некоторой папке,
через которую можем загружать файлы; хостинг поддерживается одним большим web-сервером, который включает
в себя множество таких папок, т.е. делим пространство между всеми остальными участниками хостинга; хостинг
хостинг позволяет одновременно раздавать все эти файлы и опубликованный сайт будет работать; это медленно,
потому что делится пространство между большим количеством участников, но очень низкая стоимость;
2-оы способ это виртуальная машина:
 там есть выделенный сервер там устанавливается специальное ПО,
которая может создавать виртуальные машины; виртуальные машины это отдельные независимые операционные системы,
к которым разработчик получает полный администраторский доступ (создавать, менять любые файлы внутри машины);
3-ий способ с выделенным сервером:
это железный комп, стоящий у провайдера, к которому выдаётся доступ и весь комп принадлежит разработчику;
высокая скорость загрузки, но высокая стоимость;
оптимальный вариант - это виртуальная машина
на сервере устанавливается ПО гипервизор (инструмент, который позволяет запускать и управлять виртуальной машиной)
там их несколько и в каждом из них своя операционная система, набор библиотек;

Заходим в cloud.yandex.ru (Ar_Ar, логин araru) кнопки по очереди: Compute Cloud(первая), Создать ВМ(внизу),
заполняем имя 'armen1' виртуальной машины и выбираем операционную систему Ubuntu и ниже выбираем диск для ВМ
(ТИП самое дешёвое HDD размер выбрать маленький 10) ниже выбираем платформу Intel Cascade Lake, выбираем минимальное
количество ядер 2 и для уменьшения стоимости выбираем 5% и RAM выбираем 1 Гб и ниже в Доступ
Терминал сервера:
в консоли по команде 'ssh-keygen' после 3 Enter ов создадутся папки где будут храниться ключи публичные
C:\Users\armen/.ssh\id_rsa.pub.

"Order Number is: 9987143667"

Терминал сервера:
Дальше вводим (в видеj он вводит 'cat' вместо 'type') 'type .ssh\id_rsa.pub' и получаем содержимое этого файла
публичный ключ 'ssh-rsa AAAAB3N...................7Uhzx4I6ZYhaz838= armen@LAPTOP-H91KOO13', копируем это содержимое
и переходим в cloud.yandex.ru в поле SSH-ключ вставляем и нажимаем создать ВМ, после в графе таблицы 'Публичный адрес'
указан публичный IP адрес, копируем и переходим в консоль(терминал) вводим 'ssh araru@51.250.10.114' далее
'yes' и Enter и поподаем внутрь виртуальной машины. С помощью команды 'ls' можем посмотреть какие файлы существуют,
пока покажет пустоту и командой 'ls -a' покажет скрытые файлы (.  ..  .bash_logout  .bashrc  .cache  .profile  .ssh).
Дальше командой 'ls .ssh' получим 'authorized_keys' и с помощью команды 'cat .ssh/authorized_keys' получим
содержимое того файла: публичный ключ 'ssh-rsa AAAAB3N...................7Uhzx4I6ZYhaz838= armen@LAPTOP-H91KOO13'
КОМАНДЫ:
'ls' - содержимое в папке;
'ls -а' - содержимое в папке, скрытые файлы папки(наименования начинаются с точки);
'type' или 'cat' - содержимое файла;
'ps aux' - выводит все запущенные процессы, как в диспетчере задач;
'top' - всё это в интерактивном режиме;

К виртуальной машине можно подключаться не только через IP адрес, но и через доменное имя (уникальное имя сайта)
Для регистрации доменного имени воспользуемся бесплатным сайтом freenom
в окошке 'Проверить доступность' забиваем наименование домена 'ararutyun.ga' далее нажимаем оформить заказ, там
выбираем период, на который мы регистрируем доменное имя (выбираем max бесплатное время 12 месяцев)
и нужно указать NS адреса, которые будут обрабатывать запросы на этот домен 'Use DNS' и во вкладке 'Use your own DNS'
заполняем Nameserver: ns1.yandexcloud.net и Nameserver: ns2.yandexcloud.net и на кнопку 'Continue'
Заходим в личный кабинет, в корзину(Hello Armen/View cart) и ставим галочку и кнопка 'Complete order'.
Через консоль командой 'nslookup -type=ns arutyunyan.ga' выводим информацию о домене:
ararutyun.ga   nameserver = ns2.yandexcloud.net
ararutyun.ga   nameserver = ns1.yandexcloud.net

Зходим в виртуальную машину и во вкладку 'Все сервисы/Cloud DNS', в правом верхнем углу 'Создать зону',
в окошке зона записываем 'ararutyun.ga.' (в конце точка), выбираем тип 'Публичная',
имя 'arutyunyan' и 'Создать'.
После создания кликаем на имя 'ararutyun' открываются записи и нажимаем 'Создать запись'. Откроется создание записи
Тип A, значение записываем Публичный IPv4 (51.250.10.114) и 'Создать'.
Если в консоли запросим 'nslookup -type=any ararutyun.ga' выводим информацию о домене:
ararutyun.ga text = "51.250.10.114" (т.е. домен под названием arutyunyan.ga это IP 51.250.10.114) или по команде
'host ararutyun.ga' выводит '51.250.10.114 это ararutyun.ga'

Терминал сервера:
Дальше в консоли вводим 'ssh araru@ararutyun.ga' и попадаем внутрь виртуальной машины куда заходили по команде
'ssh araru@51.250.10.114'

Войдя в виртуальную машину и дальше как администратор по команде 'sudo su' выводит 'root@armen:/home/arutyunyan#'
для добавления репозитория (для установки Python) по команда 'add-apt-repository ppa:deadsnakes/ppa' далее вводим
команду 'apt install python3.10'  проверить можно ввести команду 'python3.10 --version' получим 'Python 3.10.4'

=================================================================================================================
'apt install postgresql'
С postgres

Для работы приложения нужно установить базу данных устанавливаем 'apt install postgresql' далее 'Y' установится.
'sudo su postgres' заходим как администратор пользователь postgres выводит 'postgres@armen1:/home/araru$'
'createuser --interactive -P' это команда, что хотим задать пароль
'Enter name of role to add' нас спрашивают какого пользователя хотим создать (например arut_ar)
'Enter password for new role:' ввести пароль '12345' в консоли не видно как вводим
'Shall the new role be a superuser? (y/n)' пользователь будет суперпользователем, отказываем 'n'
'Shall the new role be allowed to create databases? (y/n)' разрешить создавать базы данных? отказываем 'n'
'Shall the new role be allowed to create more new roles? (y/n)' разрешить создавать больше новых ролей?  отказываем 'n'
Пользователь создан.

Создаём БД.
' createdb arut_ar --owner aru_postgres' создаём БД с названием aru_postgres и владелец(owner) пользователь arut_ar
для проверки выполнения команды 'psql -U arut_ar -h 127.0.0.1 aru_postgres' по названию aru_postgres БД
пользователь arut_ar, запросит ввести пароль и попадаем в работающий postgrestsql (aru_postgres=>)
по команде '\l' выводит все записи в БД:

     Name     |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
--------------+----------+----------+-------------+-------------+-----------------------
 aru_postgres | arm_aru  | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 postgres     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
              |          |          |             |             | postgres=CTc/postgres
 template1    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
              |          |          |             |             | postgres=CTc/postgres
=========================================================================================================

Загрузка приложения в виртуальную машину:
----------------------------------------
в терминале PyCharm выходя на верхнюю папку командой 'cd ..' передаём команду
'scp -r deploy araru@ararutyun.ga:flask_application' загружаем приложение на машину в папку flask_application
Перейдя в терминал сервера и заходя в виртуальную машину командой 'ssh araru@ararutyun.ga' и по команде
'ls' убедимся, что появилась папка flask_application, войдя в него 'ls' увидим все папки, которые были в приложении.
Командой 'cd ..' выходим из директории flask_application в верхний уровень. Входим в режим админ. 'sudo su'
'apt install python3.10-venv'
'python3.10 -m venv env' создание виртуального окружения
'. env/bin/activate' активируем его.
Выводит (env) root@armen1:/home/araru#
Дальше устанавливаем библиотеки:
'pip install -r flask_application/requirements.txt'.

Настройка приложения:

1)
Начинаем настраивать приложение:
-------------------------------
Начинаем настраивать приложение: команда 'vim config.py(или другое название)'
открывается текстовый редактор vim и туда записываем содержимое 'SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"'
файла 'default_config' нашего приложения, но вместо sqlite записываем postgrestsql и добавляем имя пользователя
'arm_postgres', через двоеточие пароль '12345' потом '@', а дальше хост, на котором будет запущена postgrestsql
так как та же машина 'localhost' и после слэш название базы данных, у нас это 'postgresdb' получится:
'SQLALCHEMY_DATABASE_URI = "postgrestsql:///arm_postgres:12345@localhost/postgresdb"' и сохраняем файл.
Теперь заходим в директорию командой 'cd flask_app/'
(нолики указываем для того, чтоб смогли извне слать запросы на эту машину)
Переопределяем переменную окружения поэтому командой 'export APP_SETTINGS../config.py' и дальше применяем
миграции: команда 'flask db upgrade' (миграция применяется) и можем запускать приложение: 'flask run -h 0.0.0.0 -p 80'
открываем браузер и забиваем адрес: 'arutyunyan.ga' появится {"total":0,"users":[]} нет пользователей пока.
С помощью Postman создаём пользователя: http://arutyunyan.ga/api/register, в 'Body' формат 'row' 'json'
записываем {"username":"test3","password":"test"} 'Send' увидим {"username": "test3"} и обновляя страничку браузера
увидим {"total":1,"users":[{"username": "test3"}]}
---------------------------------------------------------------------  ИЛИ
'vim config.py' открывается файл и кнопкой 'I' вводим текст:
SQLALCHEMY_DATABASE_URI = "postgresql://arut_ar:12345@localhost/aru_postgres"
                            БД://пользователь:пароль@хост на котором будет развёрнут/название
'cd flask_application' переходим в папку проекта
'export APP_SETTINGS=../config.py'
'flask db upgrade' применяем миграции

Переходим в браузер и по домену ararutyun.ga увидим
{"total":0,"users":[]}
Входим в Postman:
POST адрес 'http:/http://ararutyun.ga/api/register', в Body, raw и json добавляем нового пользователя:
{"username": "test1", "password": "test"} и нажимаем Send
увидим:
{
    "username": "test1"
}
Новый пользователь создан. Переходим в браузер и обновляя страницу увидим нового пользователя
{"total":1,"users":[{"username":"test1"}]}
Если закроем терминал, то сервер (страница в браузере по домену ararutyun.ga) не будет доступен
Создадим ещё одного пользователя: {"username": "test2", "password": "test_first"}
обновив страницу браузера увидим: {"total":2,"users":[{"username":"test1"},{"username":"test2"}]}

Для создания unit файла (работа приложения в фоновом режиме):
-------------------------------------------------------------
'ssh araru@ararutyun.ga' подключаемся к машине
'sudo su' заходим как админ

создание юнит-файла
'vim flask-app.service' открывается файл и кнопкой 'I' вводим текст:
[Unit]
Description=Flask-app
After=network.target

[Service]
WorkingDirectory=/home/arar/insta (уровень папки где находится папка env)
ExecStart=/home/arar/env/bin/python -m flask run -h 0.0.0.0 -p 80
Environment="FLASK_APP=run.py"
Restart=always

[Install]
WantedBy=multi-user.target

для сохранения и выхода из документа 'Ctrl + C', ':' и 'wq'

ИЛИ
2)
в консоли подключаемся к машине команда
'ssh arar@arutyunyan.ga' переходим в режим администратора 'sudo su' и создаём файл команда
'vim /etc/systemd/system/flask-app.service'. 'flask-app.service' это название файла. Открывается этот файл и описываем
секциями файл:
[Unit]
Description=Flask-app(текстовое описание)
After=network.target(значит приложение должно запустится после того, как запустятся все демоны, отвечающие за сеть на
этой виртуальной машине)

[Service]
WorkingDirectory=/home/ararutyun/flask_application/ (папка где код приложения находится)
ExecStart=/home/ararutyun/env/bin/python -m flask run -h 0.0.0.0 -p 80 (команда запускается при старте)
Environment="APP_SETTINGS=/home/ararutyun/config.py" (переменная окружения, путь откуда брать конфиг)
Restart=always (в случае чего приложение будет остановлено это перезапустит)

[Install]
WantedBy=multi-user.target

для сохранения и выхода из документа 'Ctrl + C', ':' и 'wq'

В консоли, как админ команда для загрузки Unit-файл:
'systemctl daemon-reload' команда для того, чтоб systemd загрузил Unit-файл и после мы можем запустить Unit.
'systemctl start flask-app' стартует Unit-файл.
С помощью команды 'systemctl status flask-app' смотрим запущено ли приложение.
Открываем браузер и вводим наш домен увидим работающую страницу. Для отключения от виртуальной машины
вводим команду 'exit', но приложение будет работать в фоновом режиме, страница в браузере будет отвечать.
======================================================================================================================
======================================================================================================================


Зарегистрировать специального пользователя Skyprouser и задать ему пароль в соответствии:
'adduser skypro' дальше запросит ввести пароль, вводим и просит повторно, вводим и Enter ами доходим до 'Y/n' вводим
Y и Enter. Дальше вводим команду 'usermod -aG sudo skypro' Enter.
'vim /etc/ssh/sshd_config' открывается файл и кнопкой 'I' редактируем: проматываем вниз и
PasswordAuthentication вместо 'on' записываем 'yes' и сохраняем ':wq'
Дальше команда 'sudo service ssh restart' Enter. Пользователь создан.
------------------------------------------------------------------------------------------------


'Shift C' - можно отсортировать в порядке потребления процессорного времени;
'Shift M' - можно отсортировать по памяти.
--------------------------------------------------------------------------------------------------



Пароль "nV1Cf@Q@" для пользователя 'skypro' (это для д/з)
"""

# =====================================================================================================================
"""
Докер это система контейнеризации, позволяющая изолировать приложение на одной машине друг от друга. Контейнер это
запущенное приложение, которое изолировано от всех остальных. Это делается с помощью двух механизмов в ядре
операционной системы (namespaces и cgroups).
Для установки Docker на компьютер: в браузере, в командной строке docker.com и на странице 'Get Started'.
После установки заходим в консоль и командой 'docker' видим что докер установлен, командой 'ps' увидим какие сейчас
запущены контейнеры.
Для просмотра образа команда 'docker images', скачать - 'docker pull <образ>', удалить - 'docker rm <образ>'


Команды:

'docker -p' запуск контейнера;

'docker ps' запущенные контейнеры;

'docker -d' запуск контейнера в режиме демона;

'docker logs' выводит логи контейнера;

'docker rm -f' и указываем (id контейнера) удаляет контейнер;

'docker ps -a' запущенные и остановленные контейнеры(все);

'docker system prune' удалить все остановленные контейнеры;

'docker exec (id контейнера) ls' выполняет команду внутри контейнера;

В терминале сервера:
'docker run -p 8080:80 nginx' в браузере по адресу localhost:8080 увидим приветствие сайта nginx
'docker run -p 80:80 docker/getting-started' в браузере по адресу localhost откроется обучающая страничка nginx
Контейнеры можно остановить через Docker Desktop нажав на кнопку стоп (квадратик)
Для того, чтоб не зависнуть в консоли при запуске контейнера, нужно контейнер запускать в режиме демона (-d)
'docker run -p 8080:80 -d nginx' нам возвращается id контейнера и можем дальше работать в терминале.
'docker ps' увидим все запущенные контейнеры
'docker logs 75dfcb8229d2(id контейнера)' получим логи
'docker rm -f 75dfcb8229d2(id контейнера)' удалим работающий контейнер
'docker ps' увидим нет запущенных контейнеров
'docker ps -a' увидим контейнеры, сети, которые когда-то работали и работающие тоже
'docker system prune' система предупредит, спросит да или нет удалить всё
'docker ps -a' увидим нет запущенных контейнеров, сетей
'docker run -d nginx' запускам в режиме демона nginx
'docker ps' выводим id
'docker exec 42dccb5c6f7d(id контейнера) ls' выводит всю корневую директорию контейнера 

'docker exec -it 42dccb5c6f7d(id контейнера) /bin/bash' в интерактивном режиме можем попасть внутрь контейнера и
внутри как в виртуальной машине работать командами (видим root@42dccb5c6f7d:/#):
командой 'ls' выводит все директории,
командой 'pwd' выводит в какой директории находимся ('/' означает, что находимся в корне),
команда 'apt' установка команд
команда 'apt update' обновляет базу репозитория,
команда 'apt install procps' устанавливает пакет,
команда 'ps' выводит название всех запущенных контейнеров, сетей
команда 'ps aux' выводит аля, диспетчер задач все запущенные процессы;
команда 'kill (PID[порядковый номер] из таблицы)' убивает(останавливает) процесс, но пересоздаёт под другим PID;
команда 'kill 1' выкидывает из контейнера (останавливает все процессы в этом контейнере) (C:\Users\armen>)
командой 'docker ps -a' увидим, что этот контейнер был запущен и остановлен;
команда 'docker start (id контейнера)' перезапускает контейнер

----------------------------------------------------------------------------------------------------------------------
В PyCharm создаём файл Dockerfile
--------------------------------
1)
FROM ubuntu:20.04 (образ с операционной системой)

RUN apt update && apt install -y nginx (устанавливает в ubuntu nginx, а '-y' это без вопросов установить,
предварительно обновив базу пакетов)
CMD nginx -g 'daemon off;' (указываем, какую команду должен запустить этот образ при запуске)

В терминале PyCharm: docker build -t (название образа) my_custom_nginx . (директория, откуда будут браться
файлы для сборки, точка-это текущая директория)
'docker run -p 80:80 -d my_custom_nginx' запускается контейнер и выводит id
команда 'ps' выводит название всех запущенных контейнеров, сетей
Запустить два контейнера:
-------------------------
команда 'docker kill (id контейнера)' убиваем запущенный контейнер
'docker run nginx:1.19' запускаем контейнер nginx версии 1.19
'docker run nginx:1.20' запускаем контейнер nginx версии 1.20
команда 'docker exec -it (id контейнера) /bin/bash' вход внутрь одного из контейнеров;
командой 'curl localhost:80' позволяет посылать запросы http (увидим html страничка nginx);
командой 'curl -I localhost:80' получить заголовки;
команда 'exit' выход из контейнера не убивая его;

Для обращения из одного контейнера в другой:
--------------------------------------------
командой 'ifconfig', но предварительно обновив и установив пакет 'apt update' и 'apt install net-tools' выводит
конфигурацию данного контейнера, в том числе 'inet 172.17.0.3' IP адрес(оба контейнера), после по команде
'curl -I 172.17.0.2' обращаемся к конфигурации другого контейнера 'Server: nginx/1.19.10', а по команде
'curl -I localhost' выведет информацию о текущем контейнере 'Server: nginx/1.20.2';

Для создания сети:
------------------
Удаляем все контейнеры командой 'docker kill (id)' заранее определив id по команде 'docker ps'
команда 'docker network create my_nginxes' создаём сеть;
для каждого контейнера отправляем команду:
'docker run -d --name=nginx_1_20 --network=my_nginxes --network-alias=nginx_1_20 nginx:1.20' и
'docker run -d --name=nginx_1_19 --network=my_nginxes --network-alias=nginx_1_19 nginx:1.19' дальше входим в любой
из них (уже можно не по id 'd33bf57e5d05', а по имени 'nginx_1_19')

команда 'apt install dnsutils' предварительно обновив пакеты 'apt update'
и по команде 'host nginx_1_19' можем проверить IP адрес выводит (nginx_1_20 has address 172.18.0.3)
---------------------------------------------------------
2) для flask приложения
-----------------------
FROM python:3.10-slim (образ с операционной системой, весит меньше и меньше библиотек)

WORKDIR /code (весь код будет лежать в отдельной директории /code)
COPY requirements.txt . (копируем файл библиотек)
RUN pip install -r requirements.txt (выполняем команду установки библиотек)
COPY app.py . (копируем файл приложения)
COPY migrations migrations (копируем файл для миграций)
COPY docker_config.py default_config.py(копируем конфигурацию приложения, заранее создав отдельный такой файл
docker_config.py, в котором будет настройка для config и его подменим, вместо стандартного config положим нужный нам)

CMD flask run -h 0.0.0.0 -p 80(команда запуска приложения, host 0.0.0.0, для того чтоб извне можно было достучаться до
контейнера и указываем порт '80')

В терминале PyCharm:
'docker build -t flask_app .' создаём контейнер с названием flask_app (загружается приложение)
для создания контейнера с postgres нужно создать сеть командой 'docker network create flask_app'
'docker run -d --network=flask_app --network-alias pg -e POSTGRES_USER=flask_app_user
-e POSTGRES_PASSWORD=flask_app_password -e POSTGRES_DB=flask_app_db --name=pg postgres' создаём контейнер postgres
с названием pg
'docker build -t flask_app .' создаём контейнер с flask приложением
'docker run --network=flask_app -d flask_app' создаём контейнер с приложением
'docker run --network=flask_app -d -p 80:80 --name=flask_app flask_app' создаём контейнер с приложением и прокидываем
порты и название контейнера
'docker exec -it (id контейн.) /bin/bash' входим в контейнер
и там запускаем команду 'flask db upgrade' для применения миграций
В браузере по адресу localhost увидим: {"total":0,"users":[]}
===================================================================================================================
"""


"""
Docker volumes
--------------
Добавим пользователя через Postman.
по адресу 'localhost/api/register'  {"username": "test1", "password": "test_first"} и
{"username": "test2", "password": "test_second"} на браузере обновив увидим:
{"total":2,"users":[{"username":"test1"},{"username":"test2"}]}
Командой 'docker rm -f pg' удалим контейнер с postgres
И создадим контейнер заново командой: 
'docker run -d --network=flask_app --network-alias pg -e POSTGRES_USER=flask_app_user
-e POSTGRES_PASSWORD=flask_app_password -e POSTGRES_DB=flask_app_db --name=pg postgres'
Увидим, что все файлы были стёрты. Поэтому удаляем контейнер postgres в Docker Desktop и содаём контейнер, но
уже с созданием папки для сохранения данных.
'docker run -d --network=flask_app --network-alias pg -e POSTGRES_USER=flask_app_user
-e POSTGRES_PASSWORD=flask_app_password -e POSTGRES_DB=flask_app_db --name=pg
-v ${pwd}/pd_data:/var/lib/postgresql/data postgres' создаём контейнер postgres с названием pg и для создания
директории(pd_data:/var/lib/postgresql/data), куда будет сохранятся данные
В корне приложения создастся папка pd_data
Внутри папки создаём текстовый файл 'test_file' с текстом 'test' 
'docker exec -it pg /bin/bash' входим в контейнер pg, 'cd /var/lib/postgresql/data/' заходим в нужную директорию
и командой 'ls' видим файл 'test_file'. Командой 'cat test_file' можем посмотреть содержимое файла.
С помощью команды 'rm test_file' удаляем этот файл и видим, что из папки тоже удалиться.
Теперь применяем миграции:
'docker exec -it flask_app /bin/bash' заходим в контейнер flask_app
'flask db upgrade' применим миграции
обновляя браузер по адресу localhost видим страницу с нуля: {"total":0,"users":[]}
Через Postman добавляем пользователей и снова обновляем страницу браузера, увидим:
{"total":2,"users":[{"username":"test1"},{"username":"test2"}]}
Теперь удаляем контейнер с postgres 'docker rm -f pg' при этом папка pg_data не удаляется, что позволяет сохранить
данные. Поэтому если снова создадим контейнер postgres:
'docker run -d --network=flask_app --network-alias pg -e POSTGRES_USER=fla
sk_app_user -e POSTGRES_PASSWORD=flask_app_password -e POSTGRES_DB=flask_app_db --name=pg
-v ${pwd}/pg_data:/var/lib/postgresql/data/ postgres' обновляя страницу браузера заметим, что все записи сохранились.
====================================================================================================================

Docker Compose
--------------
Создаём файл: docker-compose.yaml
docker-compose.yaml

version: "3.9"

services:
  api:
    build:
        context: .
    ports:
      - 80:80
    volumes:
      - ./docker_config.py:/code/default_config.py  
  pg:
    image: postgres:latest
    environment:
      POSTGRES_USER: flask_app_user
      POSTGRES_PASSWORD: flask_app_password
      POSTGRES_DB: flask_app_db
    volumes:
      - ./pg_data/var/lib/postgresql/data

И после заполнения этого файла уже вводим команду:
'docker-compose down' останавливаем докер компос 
'docker-compose up --build -d' 
По команде 'docker ps' видим два запущенных контейнера 'deploy_pg_1' и 'deploy_api_1'
Открывая и обновляя страницу браузера увидим, что нет изменений:


Удаляем папку pd_data и запустим приложение заново:
'docker-compose up --build -d' напишет, что миграции не выполнены
сначала 'docker-compose exec -it deploy_api_1 /bin/bash' для применения миграции попадаем внутрь контейнера,
вводим команду 'flask db update'
заново создаст директорию pd_data в корне приложения

Развёртывание приложения на сервере:
------------------------------------
Для этого можем скопировать весь код проекта, залить в машину и запустить с помощью docker-compose,
но обычно так не делают. Процесс сборки достаточно нагруженный и не надо нагружать сервера постоянной сборкой.
Поэтому заранее можно собрать образ и отправить в Docker Hub и далее на сервере использовать только файлик
docker-compose.yaml с конфигурацией без кода приложения и запускать оттуда через docker-compose приложение.
Для этого нужен аккаунт в Docker Hub создать репозиторий новый, например с названием 'insta'

Теперь для сборки образа в терминале PyCharm пишем команду 'docker-compose build'
для отправки образа в Docker Hub пишем команду 'docker login' выводит запись:
Username: (записываем имя при регистрации)
Password: (записываем пароль, которую ввели при регистрации)
и после успешного входа вводим команду 'docker-compose push'

Для запуска приложения на сервере в терминале пишем команду 'ssh araru@ararutyun.ga'
чтоб установить docker-compos на сервер переходим в режим админ 'sudo su' и с помощью команды 'curl' скачиваем
специальный репозиторий, после этого запускаем команду 'echo \', дальше обновляем 'apt-get update',
после команда 'apt install dosker-ce dosker-ce-cli containerd.io' дальше Y

Заходим в терминал PyCharm и пишем команду
'ssh araru@ararutyun.ga' создаём директорию для файла docker_config.py
'mkdir insta_docker' - создание папки и 'logout' - ??????
'scp docker_config.py araru@ararutyun.ga:insta/docker_config.py' скопируем во вновь созданную директорию файл
'scp docker-compose.yaml araru@ararutyun.ga:insta' скопируем во вновь созданную директорию файл

Возвращаемся в терминал сервера:
в контейнере вводим 'docker ps' видим пустой докер
===================================================================================================================
"""


"""
Создание CI приложения
----------------------
I стадия:
создаём папку .github в корне проекта
внутри этой папки создаём папку workflows
внутри этой папки создаём файла с расширением .yaml

action.yaml
name: Build and deploy workflow  # название workflow
on: [push]  # событие, по которому будет запускаться workflow
jobs: # перечисляем массив
  build_and_push:  # часть CI
    run_on: ubuntu_latest  # указываем, на каком run-ере запускать наши job-ы
    steps:  # скрипты, которые будут запущены на run-ере
      - name: list dir # описание команды для первого
        run: ls -la  # распечатать текущую директорию
      - name: clone code # описание команды
        uses: actions/checkout@v2  # используем готовый action
      - name: list dir 2 # описание команды
        run: ls -la  # ещё раз распечатать текущую директорию
        
В терминале PyCharm
находясь в папке проекта
'git add .'
'git commit -m "start use actions"'
Открываем GitHub и в репо проекта входим во вкладку Actions там есть workflow и можем зайти в него и посмотреть
образ

шаг docker build
----------------

action.yaml
name: Build and deploy workflow  # название workflow
on: [push]  # событие, по которому будет запускаться workflow
jobs: # перечисляем массив
  build_and_push:  # часть CI
    run_on: ubuntu_latest  # указываем, на каком run-ере запускать наши job-ы
    steps:  # скрипты, которые будут запущены на run-ере
      - name: clone cod # описание команды
        uses: actions/checkout@v2  # используем готовый action
      - name: docker build
        run: docker build -t armenar/insta:$GITHUB_REF_NAME-$GITHUB_RUN_ID .  # команда для сборки образа на
                                                                               локальном компьютере
        
        armenar/insta - адрес из Docker Hub (по логину armenar наименование образа insta)
        Специальные переменные из GitHub Actions:
        GITHUB_REF_NAME - при изменении кода нужно сообщить серверам о новой версии образа, переменная содержит в себе
        либо название ветки, которую отправили на GitHub, либо название тэга
        GITHUB_RUN_ID - с каждым запуском будет увеличиваться и не нужно будет дополнительной логики (каждый
        последующий запуск workflow приводил к сборке нового образа)

В терминале PyCharm
находясь в папке проекта
'git add .'
'git commit -m "docker build stop"'
'git push'
Открываем GitHub и в репо проекта входим во вкладку Actions там появился второй workflow и можем зайти в него
и посмотреть образ

после записываем шаг для отправки в DockerHub дописываем верхний кодЖ
      
      - name: docker login # описание команды допуск к репозиторию
        run: echo ${{ secrets.DOCKER_TOKEN }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
        # для получения скрытого пароля переходим в DockerHub (Account Settings левый верх, Security вкладка слева,
        создаём новый Access Token, называем его как хотим и генерируем) заходим в GitHub (в раздел Settings вверху,
        вкладка Secrets слева, вкладка Actions и на верху New repository secret вводим в NAME 'DOCKER_USERNAME',
        а в VALUE пользователь в DockerHub 'armenar' и нажимаем Add secret. Снова New repository secret вводим в
        NAME 'DOCKER_TOKEN', а в VALUE скопированный токен. Для того, чтоб docker login считывал пароль --password-stdin
      - name: docker push # описание команды пушим докер
        run: docker push armenar/insta:$GITHUB_REF_NAME-$GITHUB_RUN_ID .  # пушим вновь созданный образ

В терминале PyCharm
находясь в папке проекта
'git add .'
'git commit -m "docker login and push"'
'git push'
Открываем GitHub и в репо проекта входим во вкладку Actions там появился третий workflow и можем зайти в него
и посмотреть образ

Теперь открываем DockerHub, переходим в репо 'insta' и видим, что появился тэг с ID

Создание CD приложения
----------------------
Для того чтоб разложить приложение на сервере потребуется 2 файла: конфигурация docker-compose и конфигурация
самого приложения. Копируем файл docker-compose.yaml и сохраняем в корне проекта ci версию docker-compose-ci.yaml.
Ключевое отличие в том, что собирать образы не придётся, т.е. убираем секции build и образ имеет конкретную версию,
которую нужно передать из файла .github/worcflows/action.yaml (образ тегировали в секции docker build) теги в этом
файле и api и migrations. И для того, чтоб не показывать параметры POSTGRES_USER, POSTGRES_PASSWORD и POSTGRES_DB
заменяем их значения на $DB_USER, $DB_PASSWORD и $DB_NAME(или DB_DB) 
-------------------------
docker-compose-ci.yaml

version: "3.9"

services:
  api:
    image: armenar/insta:$GITHUB_REF_NAME-$GITHUB_RUN_ID
    ports:
      - 80:80
    volumes:
      - ./docker_config.py:/code/default_config.py
    depends_on:
      pg:
        condition: service_healthy
      migrations:
        condition: service_completed_successfully
  migrations:
    image: armenar/insta:$GITHUB_REF_NAME-$GITHUB_RUN_ID
    volumes:
      - ./docker_config.py:/code/default_config.py
    depends_on:
       pg:
        condition: service_healthy
    command: flask db upgrade
  pg:
    image: postgres:latest
    environment:
      POSTGRES_USER: $DB_USER
      POSTGRES_PASSWORD: $DB_PASSWORD
      POSTGRES_DB: $DB_NAME
    volumes:
      - ./pg_data/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isredy -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
--------------------------------------------------
для локального запуска команды envsubst
в терминале PyCharm вводим команду 'type docker-compose-ci.yaml | envsubst > docker-compose-test.yaml'  # открываем
файл docker-compose-ci.yaml и отправляем его в команду envsubst и результат вывода перевести в файл
docker-compose-test.yaml, который создастся в корне проекта.
---------------------------
docker-compose-test.yaml

version: "3.9"

services:
  api:
    image: armenar/insta:-
    ports:
      - 80:80
    volumes:
      - ./docker_config.py:/code/default_config.py
    depends_on:
      pg:
        condition: service_healthy
      migrations:
        condition: service_completed_successfully
  migrations:
    image: armenar/insta:-
    volumes:
      - ./docker_config.py:/code/default_config.py
    depends_on:
       pg:
        condition: service_healthy
    command: flask db upgrade
  pg:
    image: postgres:latest
    environment:
      POSTGRES_USER:
      POSTGRES_PASSWORD:
      POSTGRES_DB:
    volumes:
      - ./pg_data/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isredy -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
--------------------------------------------------
Заметим, что значения image: и для api и для migrations отсутствуют и значения POSTGRES_USER:, POSTGRES_PASSWORD и 
POSTGRES_DB также отсутствуют.  
"""

