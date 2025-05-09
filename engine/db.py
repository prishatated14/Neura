import csv
import sqlite3
con = sqlite3.connect("neura.db")
cursor = con.cursor()

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO sys_command VALUES(null, 'Excel','C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe')"
#cursor.execute(query)
#con.commit() # save database         


##Create a table web_command

## query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
## cursor.execute(query)

## query = "INSERT INTO web_command VALUES (null,'nykka', 'https://www.nykaa.com/?utm_content=ads&utm_source=GooglePaid&utm_medium=search&utm_campaign=Search_Nykaa&gad_source=1&gclid=CjwKCAjwzMi_BhACEiwAX4YZUPgjVbVx_5iPiTRjTxkXXLqF9gL3yf_rZpsM7midhfh0LAobDV5s1BoC-dsQAvD_BwE')"
## cursor.execute(query)#
## con.commit()

# This keeps the first entry and deletes duplicates
#cursor.execute('''
#    DELETE FROM sys_command 
 #   WHERE id NOT IN (
#        SELECT MIN(id) 
#        FROM sys_command 
#        WHERE name = "Excel" 
#        GROUP BY name, path
#    ) AND name = "Excel"
#''')
#con.commit()

# testing module
#app_name = "android studio"#
#cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
#results = cursor.fetchall()
#print(results[0][0])



# Create a table with the desired columns
#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')





# # Create table with combined name column
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts 
#                  (id INTEGER PRIMARY KEY, 
#                  name VARCHAR(200), 
#                  mobile_no VARCHAR(255), 
#                  email VARCHAR(255) NULL)''')

# # Specify the column indices for first name, last name, and mobile number
# # Replace these numbers with the correct indices from your CSV
# first_name_idx = 0  # index for first name
# last_name_idx = 2   # index for last name
# mobile_no_idx = 22  # index for mobile number

# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     next(csvreader)  # Skip header row if exists
#     for row in csvreader:
#         # Extract and combine names
#         name = f"{row[first_name_idx]} {row[last_name_idx]}"
#         mobile_no = row[mobile_no_idx]
        
#         # Insert into database
#         cursor.execute('''INSERT INTO contacts 
#                         (name, mobile_no) 
#                         VALUES (?, ?)''', 
#                      (name, mobile_no))

# # Commit changes and close connection
# con.commit()
# con.close()




# #Search Contacts from database
# query = 'Papa 1'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])




# #Insert Single contacts (Optional)
# query = "INSERT INTO contacts VALUES (null,'Papa 1', '+919370933330', 'null')"
# cursor.execute(query)
# con.commit()

