import psycopg2

class PostDB():
    '''Class to manage a postgresql database, to create this object the file database.ini is needed'''
    def __init__(self):
        try:
            from config import config
        except Exception as e:
            print('Create a database.ini with the configurations and proper format before continuing...')
            print('Error IMPORTING CONFIG -> ', e)
            exit()

        self.__conn = None
        self.__connected = False

        # read connection parameters (From the database.ini file)
        self.__params = config()
    
    def isConnected(self):
        return self.__connected
    
    def checkDB(self):
        """ Check the connection to the database server"""

        test = False
        try:
            test = self.connectDB()

            cur = self.__conn.cursor()

            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            db_version = cur.fetchone()
            print(db_version)

            cur.close()
        except (Exception, psycopg2.DatabaseError) as e:
            print('Error CHECKING DB -> ', e)
        finally:
            self.closeDB()

            return test
    
    def dropDB(self):
        from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

        try:
            # Drops the database in the database.ini conf
            answer = input('THIS COMMAND WILL DROP THE WHOLE DATABASE AND ALL THE DATA IN IT, ARE YOU SURE WANT TO PROCEED? (TYPE: "I DO" TO DROP)')

            if answer == 'I DO':
                # If the user agreeds to drop the database it will connect to postgres main database and drop the database selected
                print('Dropping '+self.__params['database']+' database...')
                con = psycopg2.connect(dbname='postgres',
                user=self.__params['user'], host='',
                password=self.__params['password'])

                con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

                cur = con.cursor()
                cur.execute("DROP DATABASE %s  ;" % self.__params['database'])

        except (Exception, psycopg2.DatabaseError) as e:
            print('Error DROPPING DB -> ', e)
    
    def createDB(self):
        from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

        try:
            # Creates the database and connects to it in case of success
            print('Creating '+self.__params['database']+' database...')
            con = psycopg2.connect(dbname='postgres',
            user=self.__params['user'], host='',
            password=self.__params['password'])

            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            cur = con.cursor()
            cur.execute("CREATE DATABASE %s  ;" % self.__params['database'])

        except (Exception, psycopg2.DatabaseError) as e:
            print('Error CREATING DB -> ', e)
        finally:
            # returns if the database is connected
            return self.checkDB()

    def connectDB(self):
        try:
            # Connect to the database
            print('Connecting to '+self.__params['database']+' database...')
            self.__conn = psycopg2.connect(**self.__params)

            self.__connected = True
        except (Exception, psycopg2.DatabaseError) as e:
            print('Error OPENNING CONN -> ', e)
        finally:
            return self.isConnected()
    
    def closeDB(self):
        try:
            # Close the connection to database
            if self.__conn is not None:
                self.__conn.close()
                print('Database connection closed.')
            
            self.__connected = False
            self.__conn = None
        except (Exception, psycopg2.DatabaseError) as e:
            print('Error CLOSING CONN -> ', e)
        finally:
            return self.isConnected()

    def importSQL(self, sqlFile, shell = False):
        # Execute sql file
        check = False
        print('Importing sql file...')
        if shell:
            # Runs the sql file directly with psql in shell (Better for some commands like COPY...FROM STDIN)
            import subprocess

            try:
                subprocess.call('psql '+self.__params['database']+' < '+sqlFile, shell=True)
                check = True
            except (Exception, psycopg2.DatabaseError) as e:
                print('Error EXECUTING SQL IN SHELL -> ', e)
            finally:
                return check
        else:
            # If the command don't run in shell mode the autocommit is set to True, for all the changes to take place and the function execute() from the cursor is used to run all the script
            if self.connectDB():
                self.__conn.autocommit = True

                cur = self.__conn.cursor()

                try:
                    with open(sqlFile, "r") as sql:
                        code = sql.read()
                        cur.execute(code)
                        check = True
                except (Exception, psycopg2.DatabaseError) as e:
                    print('Error OPEN SQL FILE -> ', e)
                    sql.close()
                finally:
                    cur.close()
                    self.closeDB()
                    return check
            else:
                print('There was a problem connecting to the database, check it and try again...')
                return check
    
    def select(self, columns, tables, conditions="1", complement=""):
        result = []
        # Execute a simple select query in the database
        try:
            if self.connectDB():
                # The sql is created separately to avoid sql injection
                SQL    = "SELECT {} FROM {} WHERE (%s) {};".format(columns, tables, complement)
                VALUES = (conditions,)

                query = cursor.mogrify(SQL, VALUES)

                cur = self.__conn.cursor()
                cur.execute(query)

                result = cur.fetchall()

                cur.close()
            else:
                print('There was a problem connecting to the database, check it and try again...')
        except (Exception, psycopg2.DatabaseError) as e:
            print('Error SELECT -> ', e)
        finally:
            self.closeDB()

            return result
    
    def insert(self, columns, tables, rows):
        id = 0
        # Simple sql insert query to execute in the database
        try:
            if self.connectDB():
                SQL    = 'INSERT INTO {} {} VALUES %s;'.format(columns, tables)
                VALUES = (rows,)

                query = cursor.mogrify(SQL, VALUES)

                cur = self.__conn.cursor()
                cur.execute(query)

                id = cur.fetchone()[0]

                conn.commit() 
                cur.close()
            else:
                print('There was a problem connecting to the database, check it and try again...')
        except (Exception, psycopg2.DatabaseError) as e:
            print('Error INSERT -> ', e)
        finally:
            self.closeDB()

            return id

