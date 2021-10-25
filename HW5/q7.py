import psycopg2
import itertools

def populate_table(employees):
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        INSERT INTO employees(fname, lname) VALUES(%s, %s);
        """)
    conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="114645", 
                        database="postgres")
    try:
        cur = conn.cursor()
        cur.executemany(commands, employees)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
# create 2 arrays with random first and last names
fname = ['jfkdsl', 'jfld', 'jlkj', 'uwiot', 'jjkfdj', 'eot', 'zfljslk','jklsj', 'mxitkl', 'kldjgm', 'eotmkhl', 'jlm', 'intaf', 'jfkslgg',
        'jsdlkfj', 'tihod', 'vmmvld', 'etohfm', 'jfk', 'ehtilh','jkld', 'tioph', 'jkhk', 'dhtk', 'fe']
lname = ['sjglk', 'hiolhk', 'rhgdkgn', 'rotk', 'oymj', 'klj', 'dsagh', 'etyhj', 'bjjgf', 'weyhdsd','yjllr', 'sdgjl', 'ed', 
         'hlfd', 'kljkjllf','vnddkrt', 'yirlfm', 'shgjh', 'wety', 'nfkl']

# create list of the combinations of the first and last names created from above
employees = list(itertools.product(fname, lname))

populate_table(employees)