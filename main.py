from conn_db import generate_db_data
from add_to_excel import generate_excel_data
from add_data_to_mail import generate_html_data
from send_file import send_mail
from dotenv import load_dotenv
import  os


load_dotenv(dotenv_path=f"{os.getcwd()}/config\\.env")


if __name__ == '__main__':
    generate_db_data()
    generate_excel_data(os.environ.get('FINAL_PATH')+'generate_data\\items.xlsx', 'Sheet1')
    html_data = generate_html_data(os.environ.get('FINAL_PATH')+'generate_data\\final_data.xlsx')
    send_mail(html_data)
