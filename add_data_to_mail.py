import pandas  as pd

df =pd.read_excel('items.xlsx')
table_html = df.to_html(table_id='your_data')

table_html = table_html.replace('class="dataframe" id="your_data">','class="styled-table" id="your_table">')

with open('table style.txt') as file:
    table_style_html = file.read()
    
with open('before table html.txt') as body_file:
    body_html = body_file.read()   

final_html = table_style_html+body_html +table_html  

