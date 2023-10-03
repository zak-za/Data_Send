import pyodbc
import pandas as pd


SERVER = '192.168.0.165,1433'
DATABASE = 'BDMantenimiento_DAT'
USERNAME = 'innova_read'
PASSWORD = 'BVvwSK76'
# Query_Sql = 'from DEXPPLAN d where d.DATEPLAN >= Cast(GETDATE() As Date) and d.DATEPLAN < DATEADD(Day, 1, Cast(GETDATE() as Date)) or d.DATEPLAN >= DATEADD(DAy, -DATEPART(weekday, GETDATE())+1, cast(GETDATE() as DAte)) and d.DATEPLAN <DATEADD(day, 8-DATEPART(weekday, GETDATE()), cast(GETDATE() as date))'


def generate_db_data():
    connection_string = f"DRIVER=ODBC Driver 18 for SQL Server;SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes"
    conn = pyodbc.connect(connection_string)
    pd.read_sql("""select IDJOBPLAN, JOBNAME ,INSTANCIA ,PRIOSALI ,DATEPLAN ,FMINEJEC from DEXPPLAN d 
                where d.DATEPLAN >= Cast('2023-09-21 16:30:36.290' As Date)
                and d.DATEPLAN < DATEADD(Day, 1, Cast('2023-09-21 16:30:36.290' as Date))
                or d.DATEPLAN >= DATEADD(DAy, -DATEPART(weekday, '2023-09-21 16:30:36.290')+1, cast('2023-09-21 16:30:36.290' as DAte))
                and d.DATEPLAN <DATEADD(day, 8-DATEPART(weekday, '2023-09-21 16:30:36.290'), cast('2023-09-21 16:30:36.290' as date))""", conn).to_excel('items.xlsx')
