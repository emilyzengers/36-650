def show_records(table):
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("SELECT * from employees LIMIT 10")
    conn.commit()
    cur.close()
    conn.close()

show_records(employees)