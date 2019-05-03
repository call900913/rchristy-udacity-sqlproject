#!/usr/bin/env python3


import psycopg2


#open connection to database
db = psycopg2.connect('dbname=news')
cr = db.cursor()



#What are the three most popular articles?
cr.execute("""
SELECT articles.title, count
FROM articles JOIN
  (select path, count(*) from log where status = '200 OK' group by path)
    as something on slug = replace(path, '/article/', '')
ORDER BY count
DESC limit 3
""")

results1 = cr.fetchall()

print('\nA. The 3 most popular articles:\n')
for i (title, views) in enumerate(results1, 1):
    print('{}. {} (with {} visits)'.format(i, title, views))



#Who are the most popular authors?
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
cr.execute("""
SELECT authors.id, authors.name, sum
FROM authors JOIN view_01 ON authors.id = view_01.author
ORDER BY sum DESC
""")

results2 = cr.fetchall()

print('\n\nB. The authors ranked by popularity:\n')
for result in results2:
    print('%s. %s (%s article visits)' % (result[0], result[1], result[2]))



#What are the days on which more than 1% of requests lead to errors?
cr.execute("""
SELECT date, round(ep, 2)
FROM (select a.date, (100.0 * numOfErroneousRequests / totalRequests) ep
     from (select date(time) as date, count(status) as numOfErroneousRequests
          from log where status = '404 NOT FOUND' group by date(time)) AS a,
          (select date(time) as date, count(*) as totalRequests
          from log group by date(time)) AS b
     where a.date = b.date) as result
WHERE ep > 1
""")

results3 = cr.fetchall()

print('\n\nThe days on which more than 1% of requests lead to 404 error:')
for result in results3:
    print('Date: %s; error percentage: %s\n' % (result[0], result[1]))




#close connection to database
db.close()
