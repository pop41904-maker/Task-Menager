import sqlite3 as sq, os
from time import *
from prettytable import *

# All function
def press_enter(table) :
    sleep(0.3)
    if table == '' or table == None :
        sleep(1)
        input('\nPress enter : ')
        sleep(0.3)
        os.system('cls')
    else : 
        print(table)
        sleep(1)
        input('\nPress enter : ')
        sleep(0.3)
        os.system('cls')

# Data Base
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)
db_path = os.path.join(data_dir, 'menager.db')
con = sq.connect(db_path)
cur = con.cursor()

# Create table in database
cur.execute("""CREATE TABLE IF NOT EXISTS Work_List(
    Id INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,
    Work TEXT NOT NULL
)
""")

# Create Table

# Variable Table 
Menu_Table = PrettyTable()
Number_Error = PrettyTable()
Command_Error = PrettyTable()
Id_Not_Found = PrettyTable()
Change_Work_Table = PrettyTable()
Delete_Table = PrettyTable()
Title_Not_Found = PrettyTable()

# Create Title Table
Command_Error.title = 'Error command'
Menu_Table.title = 'Menu'
Number_Error.title = 'Error Number'
Id_Not_Found.title = 'Error Id'
Change_Work_Table.title = 'Change Work'
Delete_Table.title = 'Delete Work'
Title_Not_Found.title = 'Error Title'

# Delete header in table
Command_Error.header = False
Number_Error.header = False
Id_Not_Found.header = False
Title_Not_Found.header = False

# Create rows in Table
Command_Error.add_row(['Unknown command'])
Title_Not_Found.add_row(['Title Not Found Try Again'])
Number_Error.add_row(['Error number write number'])
Id_Not_Found.add_row(['Id not found try again'])
Menu_Table.field_names = ['№', 'Explanation']
Change_Work_Table.field_names = ['№', 'Explanation']
Delete_Table.field_names = ['№', 'Explanation']

# Write in rows Table
Delete_Table.add_rows(
    [
        [1, 'Delete work for id'],
        [2, 'Delete work for title'],
        [3, 'Exit']
    ]
)
Menu_Table.add_rows(
    [
        [1, 'Add work'],
        [2, 'Change work'],
        [3, 'Open all works'],
        [4, 'Open one work'],
        [5, 'Delete work'],
        [6, 'Exit']
    ]
)
Change_Work_Table.add_rows(
    [
        [1, 'For Id'],
        [2, 'For Title'],
        [3, 'Exit']
    ]
)

while True :
    os.system('cls')
    print(Menu_Table)
    try :
        Menu_Choise_Action = int(input('Choise : '))
        sleep(0.2)
        os.system('cls')
    except ValueError :
        os.system('cls')
        press_enter(Number_Error)
    else :
        if Menu_Choise_Action == 1 :
            print('== Add Work ==')
            Title_For_Work = input('Title : ').strip()
            Work_In_Table = input('Work : ').strip()
            sleep(1)
            cur.execute("""INSERT INTO Work_List(Title, Work)
            VALUES(?, ?)
            """, (Title_For_Work, Work_In_Table))
            con.commit()
            sleep(0.2)
            os.system('cls')
            print('= Work add =')
            press_enter('')
        elif Menu_Choise_Action == 2:
            while True :
                print(Change_Work_Table)
                try :
                    Choise_How_Change_Work = int(input('Choise : '))
                    sleep(0.5)
                except ValueError :
                    os.system('cls')
                    press_enter(Number_Error)
                else :
                    if Choise_How_Change_Work == 1 :
                        os.system('cls')
                        Write_Id = int(input('Write id : '))
                        sleep(0.2)
                        cur.execute("""SELECT Id 
                        FROM Work_List
                        WHERE Id = ?
                        """, (Write_Id,))
                        Check = cur.fetchone()
                        if Check :
                            cur.execute("""DELETE FROM Work_List
                            Where Title = ?
                            """, (Write_Id,))
                            con.commit()
                            os.system('cls')
                            Change_Title_Work = input('New Title : ').strip()
                            sleep(0.4)
                            Change_Work = input('New Work : ').strip()
                            sleep(0.3)
                            cur.execute("""UPDATE Work_List 
                            SET Title = ?, Work = ? 
                            WHERE Id = ?""", (Change_Title_Work, Change_Work, Write_Id))
                            os.system('cls')
                            con.commit()
                            print('= Work Change for new =')
                            press_enter('')
                        else :
                            press_enter(Title_Not_Found)
                    elif Choise_How_Change_Work == 2:
                        os.system('cls')
                        Write_Title = input('Write Title : ').strip()
                        sleep(0.2)
                        cur.execute("""SELECT Title
                        FROM Work_List
                        WHERE Title = ?
                        """, (Write_Title,))
                        Check = cur.fetchone()
                        if Check :
                            cur.execute("""DELETE FROM Work_List
                            Where Title = ?
                            """, (Write_Title,))
                            con.commit()
                            os.system('cls')
                            Change_Title_Work = input('New Title : ').strip()
                            sleep(0.4)
                            Change_Work = input('New Work : ').strip()
                            sleep(0.3)
                            cur.execute("""UPDATE Work_List 
                            SET Title = ?, Work = ? 
                            WHERE Id = ?""", (Change_Title_Work, Change_Work, Write_Title))
                            con.commit()
                            os.system('cls')
                            print('= Work Change for new =')
                            press_enter('')
                        else :
                            press_enter(Title_Not_Found)
                    elif Choise_How_Change_Work == 3 :
                        os.system('cls')
                        break
        elif Menu_Choise_Action == 3 : 
            cur.execute("""SELECT Id, Title, Work 
            FROM Work_List
            """)
            Check = cur.fetchall()
            for row in Check :
                print(f'\n{row}\n')
                sleep(0.3)
            sleep(2)
            press_enter('')
        elif Menu_Choise_Action == 4 :
            while True :
                os.system('cls')
                Change_Work_Table.title = 'Open Work'
                print(Change_Work_Table)
                try :
                    Choise_How_Change_Work = int(input('Choise : '))
                    sleep(0.3)
                    os.system('cls')
                except ValueError :
                    os.system('cls')
                    press_enter(Number_Error)
                else :
                    if Choise_How_Change_Work == 1 :
                        try : 
                            Id_For_Found_Work = int(input('Id : '))
                        except ValueError :
                            os.system('cls')
                            press_enter()
                        else :
                            cur.execute("""SELECT Id, Title, Work FROM Work_List WHERE Id = ?""", (Id_For_Found_Work,))
                            Check = cur.fetchone()
                            if Check :
                                print(Check)
                                press_enter('')
                            else :
                                press_enter(Id_Not_Found)
                    elif Choise_How_Change_Work == 2:
                        Title_For_Found_Work = input('Title : ').strip()
                        cur.execute("""SELECT Id, Title, Work FROM Work_List WHERE Title = ?""", (Title_For_Found_Work,))
                        Check = cur.fetchone()
                        if Check :
                            print(Check)
                            press_enter('')
                        else :
                            press_enter(Title_Not_Found)
                    elif Choise_How_Change_Work == 3:
                        break
                    else :
                        press_enter(Command_Error)
        elif Menu_Choise_Action == 5 :
            while True :
                print(Delete_Table)
                try :
                    Choise_How_Delete_Work = int(input('Choise : '))
                    sleep(0.3)
                    os.system('cls')
                except ValueError :
                    os.system('cls')
                    press_enter(Number_Error)
                else :
                    if Choise_How_Delete_Work == 1:
                        try :
                            Id_For_Delete_Work = int(input('Id : '))
                            sleep(0.3)
                        except ValueError :
                            os.system('cls')
                            press_enter(Number_Error)
                        else :
                            cur.execute("""SELECT Id FROM Work_List WHERE Id = ?""", (Id_For_Delete_Work,))
                            Check = cur.fetchone()
                            if Check :
                                cur.execute("""DELETE FROM Work_List WHERE Id = ?""", (Id_For_Delete_Work,))
                                con.commit()
                                os.system('cls')
                                print('== Work Delete ==')
                                sleep(0.5)
                                press_enter('')
                            else :
                                press_enter(Id_Not_Found)
                    elif Choise_How_Delete_Work == 2:
                        try :
                            Title_For_Delete_Work = input('Title : ').strip()
                            sleep(0.3)
                        except ValueError :
                            os.system('cls')
                            press_enter(Number_Error)
                        else :
                            cur.execute("""SELECT Title FROM Work_List WHERE Title = ?""", (Title_For_Delete_Work,))
                            Check = cur.fetchone()
                            if Check :
                                cur.execute("""DELETE FROM Work_List WHERE Title = ?""", (Title_For_Delete_Work,))
                                con.commit()
                                os.system('cls')
                                print('== Work Delete ==')
                                sleep(0.5)
                                press_enter('')
                            else :
                                press_enter(Title_Not_Found)
                    elif Choise_How_Delete_Work == 3:
                        break
                    else :
                        press_enter(Command_Error)
        elif Menu_Choise_Action == 6 :
            con.close()
            break
        else :
            press_enter(Command_Error)