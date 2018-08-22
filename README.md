# Django-Forum
A simple Django forum

[PT-BR]

Um simples fórum feito com Django.

## Instrucions || Instruções

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

[PT-BR]

As instruções permitirem rodar este projeto na sua máquina

### Prerequisites || Pré-requisitos

0) [Python >= 3.6](https://www.python.org/downloads/)


1) [Pip](https://pip.pypa.io/en/stable/installing/)


2) [Django](https://www.djangoproject.com/download/)

```
pip install Django 
```

3) [Ckeditor](https://github.com/django-ckeditor/django-ckeditor)

```
pip install django-ckeditor
```

4) [Pillow](https://python-pillow.org/)

```
pip install Pillow
```

## Deployment || Rodando

```bash
# migrate the db || migre o banco

python manage.py migrate --run-syncdb

# you must create a superuser || é necessário criar um superusuário

python manage.py createsuperuser

# running the server || rodando o servidor

python manage.py runserver
```

## Help || Ajuda

1) Only the admin can create discussions.

###### Navigate to /admin and create the discussions from there.

[PT-BR]

1) Somente o administrador pode criar discussões.

###### Vá em /admin e crie as discussões a partir de lá.


## Author || Autor 

* **Enzo Robaina** -  - [GitHub](https://github.com/EnzoRobaina)

## License || Licença

This project is licensed under Apache 2.0 License - see [Opensource.org](https://opensource.org/licenses/Apache-2.0) page for details

[PT-BR]

Este projeto está licenciado sob a licença Apache 2.0 - veja [Opensource.org](https://opensource.org/licenses/Apache-2.0) para mais detalhes
