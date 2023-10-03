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
#df_jobs[['JOBNAME', 'Proceso']] = df_jobs['Cargas de datos'].str.split(r'-|\s-\s|-\s|-\s|\s', expand=True)
df_jobs['Proceso'] = df_jobs['Cargas de datos'].str.split(r'-|\s-\s|-\s|-\s', expand=True)[1]
df_jobs['JOBNAME'] = df_jobs['Cargas de datos'].str.split(r'-|\s-\s|-\s|-\s', expand=True)[0]
                        #Manupilation Dataframe by week 
#today_data=df[df['DATEPLAN'].dt.date == today]
#df = df[(df['DATEPLAN'].dt.date >= start_date) & (df['DATEPLAN'].dt.date <= end_date)]
print(df)
                         #Filtere Dataframe 
print(df_jobs)
filtered_jobs_diarios = df_jobs_diarios[df_jobs_diarios['Nombre'].isin(df['JOBNAME'])]
print(filtered_jobs_diarios)
filtered_data = df[df['JOBNAME'].isin(df_jobs['JOBNAME'])]
print("Filtered data")
print(filtered_data)
missing_jobs_data = df[~df['JOBNAME'].isin(filtered_data['JOBNAME'])]
print("Missing data")
print(missing_jobs_data)
final_data = pd.concat([filtered_data, missing_jobs_data], ignore_index=True)
print("Final Data")

def get_proceso(jobname):   
  if jobname in df_jobs_diarios['Nombre'].values:       
    return jobname +' - '+df_jobs_diarios[df_jobs_diarios['Nombre'] == jobname]['Proceso'].iloc[0]  
  elif   jobname in df_jobs.values:       
    return jobname +' - '+ df_jobs[df_jobs['JOBNAME'] == jobname]['Proceso'].iloc[0]  
  return jobname

#final_data['JOBNAME'] = final_data['JOBNAME']+' - '+final_data['JOBNAME'].apply(get_proceso)
final_data['JOBNAME'] = final_data['JOBNAME'].apply(get_proceso)
print(final_data)
 
#final_data.to_excel('final_data.xlsx')
#print(result_df)