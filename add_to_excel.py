import os
import datetime
import numpy as np
import pandas as pd

os.chdir('C:\\Users\\Administrator\\Documents\\Data_send')
excel_file = 'foo.xlsx'
sheet_name = 'Sheet1'
#today = datetime.date.today()
today = datetime.datetime(2023,9,14).date()
extract_nombre = []
get_valueof_data=[]
today_weekday = today.weekday()
start_date = today - datetime.timedelta(days=today_weekday)
end_date = today+datetime.timedelta(days=(6-today_weekday))

df_jobs = pd.read_excel('ManualJobsNuevoTestamentoV4.xlsx' ,sheet_name='Jobs',skiprows=[0,1],usecols=[1])
df_jobs_diarios = pd.read_excel('ManualJobsNuevoTestamentoV4.xlsx' , 
                                sheet_name='Jobs Diarios' ,
                                skiprows=1,usecols=['Nombre', 'Proceso'])
df = pd.read_excel(excel_file, sheet_name=sheet_name)
today_data=df[df['DATEPLAN'].dt.date == today]
week_data = df[(df['DATEPLAN'].dt.date >= start_date) & (df['DATEPLAN'].dt.date <= end_date)]
       

#df_jobs.drop_duplicates(keep = 'first', inplace=True)
#print(df_jobs)

filtered_jobs_diarios = df_jobs_diarios[df_jobs_diarios['Nombre'].isin(week_data['JOBNAME'])]
print(filtered_jobs_diarios)
filtered_data = week_data[week_data['JOBNAME'].isin(df_jobs)]
print("Filtered data")
print(filtered_data)
missing_jobs_data = week_data[~week_data['JOBNAME'].isin(filtered_data['JOBNAME'])]
print("Missing data")
print(missing_jobs_data)
final_data = pd.concat([filtered_data, missing_jobs_data], ignore_index=True)
print("Final Data")
print(final_data)
def get_proceso(jobname):   
  if jobname in df_jobs_diarios['Nombre'].values:       
    return df_jobs_diarios[df_jobs_diarios['Nombre'] == jobname]['Proceso'].iloc[0]    
  return None
final_data['Proceso'] = final_data['JOBNAME'].apply(get_proceso(df_jobs_diarios))


#print(result_df)
'''
missing_jobs = week_data[~week_data['JOBNAME'].isin(filtered_jobs_diarios['Nombre'])]
new = df_jobs['Cargas de datos'].str.split("-", n = 1, expand = True)
df_jobs['Nombre']=new[0]
df_jobs.drop(columns =["Cargas de datos"], inplace = True)
missing_jobs_data = df_jobs[df_jobs['Nombre'].isin(missing_jobs['JOBNAME'])]
result_df = pd.concat([filtered_jobs_diarios, missing_jobs_data], ignore_index=True)
print(result_df)'''
  
'''for j in range(0,len(df_1)):
   
   for i in range(0,len(week_data)):
    if (week_data.iloc[i, 2] == df_1.iloc[j, 0])  :
        week_data.iloc[j,2] = week_data.iloc[i, 2] +' - '+ df_1.iloc[j, 1]
        #print(week_data.iloc[j,2])
         
 
for j in range(0,len(df_2)):
     get_valueof_data = df_2.iloc[j,1]
     extract_nombre =re.split("-",get_valueof_data)
     #print(get_valueof_data)
     
     for i in range(0,len(week_data)):
         
         if ( week_data.iloc[i, 2] == extract_nombre[0].strip() ):  
           list_Data  =   get_valueof_data 
           #list_Data = list(set(list_Data))
           #print('pass: ')
           #print(list_Data)
# saving the destination excel file
#week_data.to_excel('filee.xlsx')
#print(get_valueof_data)
# cell = sheet_1['C'+i]
#print(list_of_Data)'''

