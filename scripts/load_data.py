import pandas as pd
import os

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

def load_nsduh(filepath, age_col, age_range, key_cols):
    df = pd.read_csv(filepath, sep="\t", low_memory=False)
    df_filtered = df[key_cols]
    df_filtered = df_filtered[df_filtered[age_col].between(age_range[0], age_range[1])]
    return df_filtered

def load_all_years(data_dir):
    datasets = {}
    filenames = {
        2015: 'NSDUH_2015_Tab.tsv',
        2016: 'NSDUH_2016_Tab.tsv',
        2018: 'NSDUH_2018_Tab.tsv',
        2020: 'NSDUH_2020_Tab.txt',
        2022: 'NSDUH_2022_Tab.txt',
        2024: 'NSDUH_2024_Tab.txt'
    }
    
    for year, filename in filenames.items():
        config = YEAR_CONFIGS[year]
        filepath = os.path.join(data_dir, filename)
        datasets[year] = load_nsduh(filepath, config['age_col'], config['age_range'], config['key_cols'])
        print(f"{year}: {datasets[year].shape}")
    
    return datasets

YEAR_CONFIGS = {
    2015: {
        'age_col': 'AGE2',
        'age_range': (5, 12),
        'distress_col': 'SPDYR',
        'key_cols': ['AGE2', 'STMNMREC', 'SEDNMREC', 'HEALTH', 'SPDYR', 'SEDRSSLEP', 'TRQRSSLEP', 'IRSEX', 'NEWRACE2', 'IREDUHIGHST2', 'IRFAMIN3']
    },
    2016: {
        'age_col': 'AGE2',
        'age_range': (5, 12),
        'distress_col': 'SPDYR',
        'key_cols': ['AGE2', 'STMNMREC', 'SEDNMREC', 'HEALTH', 'SPDYR', 'SEDRSSLEP', 'TRQRSSLEP', 'IRSEX', 'NEWRACE2', 'IREDUHIGHST2', 'IRFAMIN3']
    },
    2018: {
        'age_col': 'AGE2',
        'age_range': (5, 12),
        'distress_col': 'SPDYR',
        'key_cols': ['AGE2', 'STMNMREC', 'SEDNMREC', 'HEALTH', 'SPDYR', 'SEDRSSLEP', 'TRQRSSLEP', 'IRSEX', 'NEWRACE2', 'IREDUHIGHST2', 'IRFAMIN3']
    },
    2020: {
        'age_col': 'AGE2',
        'age_range': (5, 12),
        'distress_col': 'SPDYR',
        'key_cols': ['AGE2', 'STMNMREC', 'SEDNMREC', 'HEALTH', 'SPDYR', 'SEDRSSLEP', 'TRQRSSLEP', 'IRSEX', 'NEWRACE2', 'IREDUHIGHST2', 'IRFAMIN3']
    },
    2022: {
        'age_col': 'AGE3',
        'age_range': (3, 6),
        'distress_col': 'SPDPSTYR',
        'key_cols': ['AGE3', 'STMNMREC', 'SEDNMREC', 'HEALTH', 'SPDPSTYR', 'SEDRSSLEP', 'TRQRSSLEP', 'IRSEX', 'NEWRACE2', 'IREDUHIGHST2', 'IRFAMIN3']
    },
    2024: {
        'age_col': 'AGE3',
        'age_range': (3, 6),
        'distress_col': 'SPDPSTYR',
        'key_cols': ['AGE3', 'STMNMREC', 'SEDNMREC', 'HEALTH', 'SPDPSTYR', 'SEDRSSLEP', 'TRQRSSLEP', 'UDSTWDSLEEP', 'UDSVWDSLEEP', 'IRSEX', 'NEWRACE2', 'IREDUHIGHST2', 'IRFAMIN3']
    }
}