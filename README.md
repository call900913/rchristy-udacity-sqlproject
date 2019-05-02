README



What This Program Does



Perusing the data in the 'news' database, this program answers the following question:

1. What are the 3 most popular articles?
2. Which authors are most popular? 
3. Which day has the most 404 errors (over 1% of all requests)? 

If you'd like to obtain the answer to this question, you can run this program and obtain the answers displayed



How It Works

You need to have Python 3 installed on your machine. 

To find out whether you have Python 3 installed on your machine, on a mac, open your Terminal application and type:
python3 --version

If it does not reply with something of the form 
Python 3.x.y
visit ttps://www.python.org/downloads/ for further instructions.



Running the Program

This program runs on the terminal.

Hence, first, open your Terminal application.

Navigate to folder containing the file. 

Make sure the database server is running locally.

Find the file with the following name:
newsdata.py

Type
python3 newsdata.py
into the terminal.

Hit enter.

It then lists the data in a nicely legible format.

A, 'The 3 most popular articles', lists the names of the articles, each with its number of visits).

B, 'The authors ranked by popularity', lists the names of authors and the number of visits the articles written by each.

C, 'The days on which more than 1% of requests lead to 404 error', lists when more than 1% end up in errors. 
(Percentage is calculated as 100.0 * x / y, where x is the number of errors in the day and y is the count of all the requests in that day.)


