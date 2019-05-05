#!/usr/bin/env python3


import psycopg2

# open connection to database
db = psycopg2.connect('dbname=news')
cr = db.cursor()


def create_views():
    cr.execute("""CREATE VIEW view_01
    AS select author, sum(count)
       from articles join
        (select path, count(*)
        from log
        where status = '200 OK'
        group by path) as log1
       on replace(path, '/article/', '')  = slug
       group by author
    """)


create_views()


def execute_query():
    cr.execute("""
    SELECT articles.title, count
    FROM articles JOIN
      (select path, count(*) from log where status = '200 OK' group by path)
        as something on slug = replace(path, '/article/', '')
    ORDER BY count
    DESC limit 3
    """)
    query1 = cr.fetchall()

    cr.execute("""
    SELECT authors.id, authors.name, sum
    FROM authors JOIN view_01 ON authors.id = view_01.author
    ORDER BY sum DESC
    """)
    query2 = cr.fetchall()

    cr.execute("""
    SELECT to_char(date, 'Mon DD, YYYY'), round(ep, 2)
    FROM (select a.date, (100.0 * numOfErrors / totalRequests) ep
         from (select date(time) as date, count(status) as numOfErrors
              from log where status = '404 NOT FOUND'
              group by date(time)) AS a,
              (select date(time) as date, count(*) as totalRequests
              from log group by date(time)) AS b
         where a.date = b.date) as result
    WHERE ep > 1
    """)
    query3 = cr.fetchall()

    return query1, query2, query3


results1, results2, results3 = execute_query()


def print_top_articles():
    # print out the top 3 articles in the timespan of the database.
    print('\nA. The 3 most popular articles:\n')
    for i, (title, views) in enumerate(results1, 1):
        print('{}. {} (with {} visits)'.format(i, title, views))


def print_top_authors():
    # print the list of authors ranked by article views.
    print('\n\nB. The authors ranked by popularity:\n')
    for result in results2:
        print('%s. %s (%s article visits)' % (result[0], result[1], result[2]))


def print_errors_over_one():
    # print out the days on which over 1% of logged requests lead to error.
    print('\n\nThe days on which more than 1% of requests lead to 404 error:')
    for result in results3:
        print('Date: %s; error percentage: %s\n' % (result[0], result[1]))


if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()

# close connection to database
db.close()
