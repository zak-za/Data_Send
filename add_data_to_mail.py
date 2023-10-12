import pandas as pd
import os

def generate_html_data(file_name):
    df = pd.read_excel(file_name)
    table_html = df.to_html(table_id='my_data')

    table_html = table_html.replace(
        'class="dataframe" id="my_data">', 'class="styled-table" id="my_table">')

    with open(os.environ.get('FINAL_PATH')+r'template\\table_style.txt') as file:
        table_style_html = file.read()

    with open(os.environ.get('FINAL_PATH')+r'template\\before_table_html.txt') as body_file:
        body_html = body_file.read()

    final_html = table_style_html + body_html + table_html
    return final_html
