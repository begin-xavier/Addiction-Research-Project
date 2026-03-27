import pandas as pd

def load_2024(filepath):
    df2024 = pd.read_csv(filepath, sep="\t", low_memory=False)
    key_cols = ['AGE3', 'STMNMREC', 'SEDNMREC', 'HEALTH', 'SPDPSTYR', 'SEDRSSLEP', 'TRQRSSLEP', 'UDSTWDSLEEP', 'UDSVWDSLEEP', 'IRSEX', 'NEWRACE2', 'IREDUHIGHST2', 'IRFAMIN3']
    df_filtered2024 = df2024[key_cols]
    df_filtered2024 = df_filtered2024[df_filtered2024['AGE3'].between(3, 6)]
    
    return df_filtered2024

def load_2015(filepath):
    df2015 = pd.read_csv(filepath, sep="\t", low_memory=False)
    key_cols_2015 = ['AGE2', 'STMNMREC', 'SEDNMREC', 'HEALTH', 'SEDRSSLEP', 'TRQRSSLEP', 'SPDYR', 'IRSEX', 'NEWRACE2', 'IREDUHIGHST2', 'IRFAMIN3']
    df_filtered2015 = df2015[key_cols_2015]
    df_filtered2015 = df_filtered2015[df_filtered2015['AGE2'].between(5, 12)]
    
    return df_filtered2015

def load_2024_full(filepath):
    df2024 = pd.read_csv(filepath, sep="\t", low_memory=False)
    key_cols = ['AGE3', 'STMNMREC', 'SEDNMREC', 'HEALTH', 'SPDPSTYR', 'SEDRSSLEP', 'TRQRSSLEP', 'UDSTWDSLEEP', 'UDSVWDSLEEP', 'IRSEX', 'NEWRACE2', 'IREDUHIGHST2', 'IRFAMIN3']
    return df2024[key_cols]