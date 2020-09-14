import mysql.connector
import getpass
from mysql.connector import errorcode

db=input("Enter the Name of the Database ")
usr=input("Enter User ")
pswd=getpass.getpass(prompt='Enter Your Password ') 

def show_info(db):
    try:
        cnx = mysql.connector.connect(user=usr, password=pswd,host='localhost',database=db)
        cursor = cnx.cursor()
        query=("SHOW TABLES")
        cursor.execute(query)
        tables=cursor.fetchall()
        query_1="SELECT count(*) FROM "
        list1=[]
        count_row={}
        for table in tables:
            list1.append(table)
        list2 = [item for t in list1 for item in t]   
        for x in list2:
            var=query_1+str(x)
            cursor.execute(var)
            count_row[x]=list(cursor.fetchone())      
        print(count_row)
    except:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


show_info(db)

    
    
