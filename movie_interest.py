import sqlite3
import time

conn=sqlite3.connect('moviesdb.sqlite')
cur=conn.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS Movies(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    actor TEXT,
    actress TEXT,
    director TEXT,
    year_of_release INTEGER
);''')

while True:
    response=input('''\n\nEnter your choice:
    1-->Add
    2-->Search
    3-->View all
    4-->Quit\n''')

    if response=='1':
        print('Enter the movie details\n')
        title_name=input('Enter the movie title : ')
        actor_name=input('Enter the actor name : ')
        actress_name=input('Enter the actress name : ')
        dir_name=input('Enter the director name : ')
        yor=input('Enter the year of realease : ')
        cur.execute('INSERT INTO Movies (title,actor,actress,director,year_of_release) VALUES (?,?,?,?,?)',(title_name,actor_name,actress_name,dir_name,yor))

    elif response=='2':
        ch=input('''\nChoose  1-->Search by actor name
        2-->Search by actress name
        3-->Search by director name
        4-->Search by year of release\n''')

        if ch=='1':
            actor_search=input("\nEnter the actor name: ")
            print('\nMovies starring '+actor_search+' are: \n' )
            print("{:<25}{:<25}{:<25}{:<25}\n".format('Title','Actress','Director','Year of Release'))
            for row in cur.execute('SELECT title,actress,director,year_of_release FROM Movies WHERE actor= ?',(actor_search,)):
                title,actress,director,year_of_release=row
                print("{:<25}{:<25}{:<25}{:<25}".format(title,actress,director,year_of_release))
        elif ch=='2':
            actress_earch=input("\nEnter the actress name: ")
            print('\nMovies starring '+actress_earch+' are: \n' )
            print("{:<25}{:<25}{:<25}{:<25}\n".format('Title','Actress','Director','Year of Release'))
            for row in cur.execute('SELECT title,actor,director,year_of_release FROM Movies WHERE actress= ?',(actress_earch,)):
                title,actor,director,year_of_release=row
                print("{:<25}{:<25}{:<25}{:<25}".format(title,actor,director,year_of_release))
        elif ch=='3':
            director_search=input("\nEnter the director name: ")
            print('\nMovies directed by '+director_search+' are: \n' )
            print("{:<25}{:<25}{:<25}{:<25}\n".format('Title','Actor','Actress','Year of Release'))
            for row in cur.execute('SELECT title,actor,actress,year_of_release FROM Movies WHERE director= ?',(director_search,)):
                title,actor,actress,year_of_release=row
                print("{:<25}{:<25}{:<25}{:<25}".format(title,actor,actress,year_of_release))
        elif ch=='4':
            yor_search=input("\nEnter the year of release ")
            print('\nMovies released in year '+yor_search+' are: \n' )
            print("{:<25}{:<25}{:<25}{:<25}\n".format('Title','Actor','Actress','Direactor'))
            for row in cur.execute('SELECT title,actor,actress,director FROM Movies WHERE year_of_release= ?',(yor_search,)):
                title,actor,actress,director=row
                print("{:<25}{:<25}{:<25}{:<25}".format(title,actor,actress,director))
        else:
            pass

    elif response=='3':
        sql_all = 'SELECT * FROM Movies'
        print ("\n{:<5}{:<25}{:<25}{:<25}{:<25}{:<25}\n".format('Id','Title','Actor','Actress','Director','Year Of Release'))
        for row in cur.execute(sql_all):
            id,title,actor,actress,director,year_of_release=row
            print ("{:<5}{:<25}{:<25}{:<25}{:<25}{:<25}".format(id,title,actor,actress,director,year_of_release))
    else:
        print('\nQuitting...')
        conn.commit()
        time.sleep(1)
        quit()

conn.commit()
