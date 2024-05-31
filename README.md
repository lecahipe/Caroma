# Caroma

This is my solution for the description provided, I hope you like it :)

I am using ```Django 5.0.6``` and ``Django Rest Framework`` and default Django database and some of the sample data create.

Dependencies can be seen in the file: ```requirements.txt```

## Endpoints

I created the following endpoints:
1. ``/api/restaurants/``
you can use filters for postalcode, exclude restaurant type, and filter by min and max rating
2. ``/api/restaurants/?postal_codes=XXX,ZZZ&exclude_types=a&min_rating=&max_rating=``


## Running Tests 
I use ```pytest``` and ```factory_boy``` for generated random the testing data. To run the tests use:

```bash
  pytest 
```

## Create env and run it locally 

```python3 -m venv env``` 
```source env/bin/activate```
```pip install --no-cache-dir -r requirements.txt```

Don't forget the to create the database and see below how to add some data with a command
```python manage.py makemigrations```
```python manage.py migrate``

Run it:
```python manage.py runserver```


## Create some data

I created a command that uou can use, import data

```python manage.py insert_data /your_path/sample-data.json```

## What's missing?

0. Better Indexing
1. Definetly more tests and documentation
2. data validation in import, admin models
3. Improvements on database Level: Even I tried to make the model as extensible with the data on Utilization and Property ( I would do it in some other modles) as possible but I feel is a lot of room to extend and make the model more flexible to add such things as kind of food (bio, halal) that is sold for the items and the menu items in order to get super specific with the queries as well for the properties.
