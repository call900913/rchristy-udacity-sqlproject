README

# Logs Analysis
## Project Description


### What This Program Does

Given a mock PostgreSQL database 'news' for a fictional news website, this Python script uses the psycopg2 library to analyze the database and produce a report that answers the following question:

1. What are the 3 most popular articles?
2. Which authors are most popular?
3. Which day has the most 404 errors (over 1% of all requests)?

Running this program gives you the answers to these questions.


### Requirements

You need to have the following installed on your machine:

  * Python 3
  * psycopg2 module
  * PostgreSQL

## Checking for Python 3 installation

To find out whether you have Python 3 installed on your machine, on a mac, open your Terminal application and type:
python3 --version

If it does not reply with something of the form
Python 3.x.y
visit ttps://www.python.org/downloads/ for further instructions.


## Checking psycopg2 module

In your terminal, type `pip3 freeze | grep psycopg2`.

If you don't have it installed, type `pip3 install psycopg2`.


## PostgreSQL installation

To find out whether your machine has PostgreSQL installed, you can type `which psql` into your terminal: if there is no output, you PostgreSQL is not yet installed.


### Prerequisites

This script assumes you have access to the newsdata.sql file and the *news* database.
If you do not have the newsdata.sql file, you can obtain a compressed version here:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

If you do not yet have the news database setup, turn on your PostgreSQL server, and run `createdb news` on your terminal.

Then, connect to the database with `psql -d news`.

Next, import the newsdata.sql file to the database by typing `psql -d news -f newsdata.sql` and hit enter.


### Running the Program

This program runs on the terminal.

Open your Terminal application.

Navigate to folder containing the file newsdata.py .

Type `python3 newsdata.py` into your terminal and hit enter.

It then lists the data in a nicely legible format.

A, 'The 3 most popular articles', lists the names of the articles, each with its number of visits).

B, 'The authors ranked by popularity', lists the names of authors and the number of visits the articles written by each.

C, 'The days on which more than 1% of requests lead to 404 error', lists when more than 1% end up in errors.
(Percentage is calculated as 100.0 * x / y, where x is the number of errors in the day and y is the count of all the requests in that day.)
