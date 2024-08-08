# djan_market

Simple example of a supermarket website

![preview](djan_market.gif)

## Used technology
* Python 3.11.0
* Django 4.2.3 (High-level Python web framework)
* Pillow 10.0.0 (Python Imaging Library)

## Installation

Create directory of your choice, let's say `/somedir/example` . Inside in create virtual enviroment 
and copy this repository.

Than download requirements to venv by activating it and running `pip install -r requirements.txt`.

Set new `SECRET_KEY` in `settings.py`. You can generate it by running in interactive shell(in enviroment with installed django) this commands. <br />
`python manage.py shell`, <br />
`from django.core.management.utils import get_random_secret_key`, <br />
`print(get_random_secret_key())`. <br />

Finally, go to the directory with manage.py and start program with `python manage.py runserver` command. 

Or if you have Docker installed you can open project directory from console and run: <br />
`docker build -t site_image .` <br />
`docker run --rm -it -dp 8000:8000 site_image` <br />
And then press Ctrl + C to stop container

### Created for education purpose and misses some serious details such as real DataBase and nginx server.

You need to log in as staff to access the `add_product` page. You can do this by using username `admin` and password `123456`.
This superuser was created by me, but you might create your own.
