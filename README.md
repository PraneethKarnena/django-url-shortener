## Django URL Shortener
A simple Django project to implement an URL Shortnening service.
An API service for shortening links programmatically.

**Tools:**

 - Django
 - Django Rest Framework
 - Ajax

**Demo:** [https://url-shortener-drf.herokuapp.com/](https://url-shortener-drf.herokuapp.com/)

**API:**
URL: `https://url-shortener-drf.herokuapp.comapi/shorten-url/`
Method: `POST`
Body:

```json
{
url: 'https://www.google.com/'
}
```

**Run:**

 - Clone the project
 - Do `pip install requirements.txt` and `cd <project-folder>`
 - Run `python manage.py makemigrations` and `python manage.py migrate`
 - Deploy test server: `python manage.py runserver` 
