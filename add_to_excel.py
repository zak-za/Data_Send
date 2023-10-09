import pandas as pd
import os


def get_proceso(jobname, df_jobs, df_jobs_diarios):
    if jobname in df_jobs_diarios['Nombre'].values:
        return jobname + ' - ' + df_jobs_diarios[df_jobs_diarios['Nombre'] == jobname]['Proceso'].iloc[0]
    elif jobname in df_jobs.values:
        return jobname + ' - ' + df_jobs[df_jobs['JOBNAME'] == jobname]['Proceso'].iloc[0]
    return jobname


def generate_excel_data(excel_file, sheet_name):
    df_jobs = pd.read_excel(os.environ.get('FINAL_PATH')+'ManualJobsNuevoTestamentoV4.xlsx', sheet_name='Jobs', skiprows=[0], usecols=[1])
    df_jobs_diarios = pd.read_excel(os.environ.get('FINAL_PATH')+'ManualJobsNuevoTestamentoV4.xlsx', sheet_name='Jobs Diarios', skiprows=1, usecols=['Nombre', 'Proceso'])
    df = pd.read_excel(excel_file, sheet_name=sheet_name) 
    df_jobs['Proceso'] = df_jobs['Cargas de datos'].str.split(
        r'-|\s-\s|-\s|-\s', expand=True)[1]
    df_jobs['JOBNAME'] = df_jobs['Cargas de datos'].str.split(
        r'-|\s-\s|-\s|-\s', expand=True)[0]

    # Filtere Dataframe
    print(df_jobs)
    filtered_jobs_diarios = df_jobs_diarios[df_jobs_diarios['Nombre'].isin(
        df['JOBNAME'])]
    print(filtered_jobs_diarios)

    filtered_data = df[df['JOBNAME'].isin(df_jobs['JOBNAME'])]
    print("Filtered data")
    print(filtered_data)

    missing_jobs_data = df[~df['JOBNAME'].isin(filtered_data['JOBNAME'])]
    print("Missing data")
    print(missing_jobs_data)

    final_data = pd.concat(
        [filtered_data, missing_jobs_data], ignore_index=True)
    print("Final Data")

    final_data['JOBNAME'] = final_data['JOBNAME'].apply(lambda x: get_proceso(x, df_jobs, df_jobs_diarios))
    print(final_data)
    
    final_data.to_excel(os.environ.get('FINAL_PATH')+'final_data.xlsx')
