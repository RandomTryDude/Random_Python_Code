import argparse
import sqlite3
import sys

class SQLi:
    def __init__(self, database):
        self.database = database
            
        
    def see_content(self , table):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        result = cursor.execute (f'''
                        SELECT * from {table};
                        ''')
        return result
        
def main():
    print("==========\n Main \n==========")
    
    database = input("Database to work on : ")
    SQL = SQLi(database)
    result = SQL.see_content("MaTable")
    
    for row in result:
        print(row)

if __name__ == "__main__":
    droptable = 'Usual command to drop table (SQL):\nDROP TABLE nom_table'
                  
    parser = argparse.ArgumentParser(
        description='SQL Tool - Execute simple SQL Queries',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Example usage:\n'
               '  SQLPython.py -D [Coded later]\n'
               '  SQLPython.py -a for help',
    )
    
    parser.add_argument('-a', '--aide', action='store_true', help='Random Help Section')
    parser.add_argument('-d', '--drop', action='store_true', help='Help to DROP TABLE ')
    
    print(f'{parser.description}\n\n{parser.epilog}')
    args = parser.parse_args()

    if args.aide:
        print(args.aide)
    elif args.drop:
        print(droptable)
    else:
        main()