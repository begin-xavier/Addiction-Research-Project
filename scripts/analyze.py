import pandas as pd

def misuse_counts(filtered_df):
    stim = filtered_df['STMNMREC'].isin([1, 2]).sum()
    sed = filtered_df['SEDNMREC'].isin([1, 2]).sum()
    return {'stimulant_misuse': stim, 'sedative_misuse': sed}
    
    
def distress_correlation(filtered_df):
    filtered_df = filtered_df.dropna(subset=['SPDPSTYR']) #dropping empty rows so that correlation can be calculated
    stress = filtered_df['SPDPSTYR'] == 1
    print("Stress sum", stress.sum()) #checking how many stressed individuals are in the dataset
    
    stim_misuse = filtered_df['STMNMREC'].isin([1, 2]) #creating a boolean series for stimulant misuse
    sed_misuse = filtered_df['SEDNMREC'].isin([1, 2]) #creating a boolean series for sedative misuse
    stim_corr = stress.corr(stim_misuse) #calculating correlation between stress and stimulant misuse
    sed_corr = stress.corr(sed_misuse) #calculating correlation between stress and sedative misuse
    return {'stimulant_correlation': stim_corr, 'sedative_correlation': sed_corr}

def health_breakdown(filtered_df):
    #stimulant misusers
    stim_users = filtered_df[filtered_df['STMNMREC'].isin([1, 2])]
    #sedative misusers
    sed_users = filtered_df[filtered_df['SEDNMREC'].isin([1, 2])]
    #health distribution for stimulant misusers
    stim_health = stim_users['HEALTH'].value_counts().sort_index()
    #health distribution for sedative misusers
    sed_health = sed_users['HEALTH'].value_counts().sort_index()
    return {'stimulant_health_distribution': stim_health.to_dict(), 'sedative_health_distribution': sed_health.to_dict()}
