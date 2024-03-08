import tkinter as tk
import mysql.connector
import tkinter.ttk as ttk


# MySQL connection details (replace with your credentials)
db_host = "localhost"
db_user = "root"
db_password = ""
db_name = "primatips"

# Connect to MySQL database
def connect_to_database():
    global connection, cursor
    try:
        connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = connection.cursor()
        print("Connected to MySQL database successfully!")
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL database: {err}")

# Fetch data from MySQL table
def fetch_data():
    global data
    try:
        # Replace "your_table_name" and "your_columns" with your actual table and columns
        cursor.execute("SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,RESULTAT,PM,BUT FROM primatips_table")
        data = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error fetching data from MySQL table: {err}")

# Create the Treeview widget with horizontal scrollbar
def create_treeview():
    global treeview, scrollbar_x

    treeview = tk. ttk.Treeview(window, columns=column_names, show="headings")
    treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar_x = tk.Scrollbar(window, orient=tk.HORIZONTAL, command=treeview.xview)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    treeview.configure(xscrollcommand=scrollbar_x.set)

    # Set column headings (replace with actual column names)
    for column in column_names:
        treeview.heading(column, text=column)

# Populate the Treeview with fetched data
def populate_treeview():
    for row in data:
        treeview.insert("", tk.END, values=row)

# Main program loop
def main():
    connect_to_database()
    fetch_data()
    create_treeview()
    populate_treeview()

    window.mainloop()

# Initialize column names (replace with actual column names from your table)
# column_names = ["PAYS", "TEAMS", "1","X", "2", "SCORE","RESULTAT", "P-M	", "BUT", ...]  # Adjust as needed
column_names = ["PAYS", "TEAMS", "1","X", "2", "SCORE","RESULTAT", "PM", "BUT"]  # Adjust as needed

# Create the main window
window = tk.Tk()
window.title("MySQL Data in Treeview")

if __name__ == "__main__":
    main()
