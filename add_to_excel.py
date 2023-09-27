import os
import datetime
import pandas as pd


os.chdir('C:\\Users\\Administrator\\Documents\\Data_send')
excel_file = 'items.xlsx'
sheet_name = 'Sheet1'
today = datetime.date.today()
#today = datetime.datetime(2023,9,14).date()
extract_nombre = []
get_valueof_data=[]
today_weekday = today.weekday()
start_date = today - datetime.timedelta(days=today_weekday)
end_date = today+datetime.timedelta(days=(6-today_weekday))

                                 #All Dataframe 
df_jobs = pd.read_excel('ManualJobsNuevoTestamentoV4.xlsx' ,sheet_name='Jobs',skiprows=[0] , usecols=[0,1])
df_jobs_diarios = pd.read_excel('ManualJobsNuevoTestamentoV4.xlsx' , 
                                sheet_name='Jobs Diarios' ,
                                skiprows=1,usecols=['Nombre', 'Proceso'])
df = pd.read_excel(excel_file, sheet_name=sheet_name)

                        #Manupilation Dataframe by week 
#today_data=df[df['DATEPLAN'].dt.date == today]
#df = df[(df['DATEPLAN'].dt.date >= start_date) & (df['DATEPLAN'].dt.date <= end_date)]
print(df)
                         #Filtere Dataframe 
print(df_jobs['Cargas de datos'])
filtered_jobs_diarios = df_jobs_diarios[df_jobs_diarios['Nombre'].isin(df['JOBNAME'])]
print(filtered_jobs_diarios)
filtered_data = df[df['JOBNAME'].isin(df_jobs['Cargas de datos'])]
print("Filtered data")
print(filtered_data)
missing_jobs_data = df[~df['JOBNAME'].isin(filtered_data['JOBNAME'])]
print("Missing data")
print(missing_jobs_data)
final_data = pd.concat([filtered_data, missing_jobs_data], ignore_index=True)
print("Final Data")

def get_proceso(jobname):   
  if jobname in df_jobs_diarios['Nombre'].values:       
    return df_jobs_diarios[df_jobs_diarios['Nombre'] == jobname]['Proceso'].iloc[0] 
  elif   jobname in df_jobs.values:       
    return df_jobs[df_jobs == jobname]['Proceso'].iloc[0]  
  return None

final_data['Proceso'] = final_data['JOBNAME'].apply(get_proceso)
print(final_data)

#print(result_df)