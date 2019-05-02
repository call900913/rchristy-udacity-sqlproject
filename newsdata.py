import psycopg2


#open connection to database
db = psycopg2.connect('dbname=news')
cr = db.cursor()



#What are the three most popular articles?
cr.execute("select articles.title, count from articles join (select path, count(*) from log where status = '200 OK' group by path) as something on slug = replace(path, '/article/', '') order by count desc limit 3")
result1 = cr.fetchall()
print('\nA. The 3 most popular articles:')
print()
i = 0
while i < len(result1):
    print(('%s. ' % (i+1)) + result1[i][0] + ' (with %s visits)' % (result1[i][1]))
    i += 1


#Who are the most popular authors?
cr.execute("CREATE VIEW view_01 AS select author, sum(count) from articles join (select path, count(*) from log where status = '200 OK' group by path) as log1 on replace(path, '/article/', '')  = slug group by author")
cr.execute('select authors.id, authors.name, sum from authors join view_01 on authors.id = view_01.author order by sum desc')
result2 = cr.fetchall()
print('\n\nB. The authors ranked by popularity:\n')
i = 0
while i < len(result2):
    print('%s. %s (%s article visits)' % (result2[i][0], result2[i][1], result2[i][2]))
    i += 1


#What are the days on which more than 1% of requests lead to errors?
cr.execute("select date, round(ep, 2) from (select a.date, (100.0 * numOfErroneousRequests / totalRequests) ep from (select date(time) as date, count(status) as numOfErroneousRequests from log where status = '404 NOT FOUND' group by date(time)) as a, (select date(time) as date, count(*) as totalRequests from log group by date(time)) as b where a.date = b.date) as result where ep > 1;")
result3 = cr.fetchall()
print('\n\nThe days on which more than 1% of requests lead to 404 error:')
i = 0
while i < len(result3):
    print('Date: %s; error percentage: %s\n' % (result3[0][0], result3[0][1]))
    i += 1




#close the connection to database
db.close()
