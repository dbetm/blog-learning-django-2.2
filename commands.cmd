-- Activar el entorno virtual:
$ source my_env/bin/activate

-- Crear nuevo proyecto:
$ python manage.py migrate

-- Crear superusuario para interfaz de administrador:
$ python manage.py createsuperuser

-- Correr el servidor
$ python manage.py runserver your_server_ip:8000

-- Entrar a shell python del proyecto:
$ python manage.py shell

-- Iniciar app
$ python manage.py startapp name

-- Crear la migración
$ python manage.py makemigrations

-- Correr la migración
$ python manage.py migrate
