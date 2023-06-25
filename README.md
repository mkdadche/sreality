# Project Setup

This project requires the following steps to set up and run:

## 1. Setting up the PostgreSQL Database

- Create a table in PostgreSQL with the following configuration:

  - Table Name: `offers`
  - Columns:
    - `id` (datatype: `int`, not null, primary key)
    - `title` (datatype: `text`, not null)
    - `locality` (datatype: `text`, not null)
    - `images` (datatype: `text[]`, not null)

- Configure the database connection with the following parameters:

  ```plaintext
  hostname = 'localhost'
  port = '5432'
  database = 'sreality'
  username = 'postgres'
  password = ''

## 2- create a virtual environment in python : 
          python -m venv env

## 3-activate the env : 
        env\Scripts\activate
  
## 4- download the packages specified in a requirements.txt file : 
          pip install -r requirements.txt

## 5- execute the following command :
          flask run