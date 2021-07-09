# # import pymssql  

# # conn = pymssql.connect(
# #     server='dataplatform-sql.database.windows.net', 
# #     user='application_logging@dataplatform-sql.database.windows.net', 
# #     password='SuperSecret!', 
# #     database='deng_ctrl_db'
# #     )


# # cursor = conn.cursor()  
# # cursor.execute(
# #     """
# #         SELECT TOP (1000) [id]
# #             ,[run_id]
# #             ,[test]
# #             ,[expected]
# #             ,[actual]
# #             ,[executed_at]
# #             ,[result]
# #         FROM [test].[result]    
# #     """)

# # row = cursor.fetchone()  
# # while row:  
# #     msg = str(row[0]) + " " + str(row[1]) + " " + str(row[2])
# #     print(msg)   
# #     row = cursor.fetchone()


# import pyodbc 
# # Some other example server values are
# # server = 'localhost\sqlexpress' # for a named instance
# # server = 'myserver,port' # to specify an alternate port
# server = 'dataplatform-sql.database.windows.net' 
# database = 'deng_ctrl_db' 
# username = 'application_logging' 
# password = 'SuperSecret!' 
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()


# #Sample select query
# cursor.execute("SELECT @@version;") 
# row = cursor.fetchone() 
# while row: 
#     print(row[0])
#     row = cursor.fetchone()



# #Sample insert query
# count = cursor.execute("""
# INSERT INTO SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) 
# VALUES (?,?,?,?,?)""",
# 'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP).rowcount
# cnxn.commit()
# print('Rows inserted: ' + str(count))

