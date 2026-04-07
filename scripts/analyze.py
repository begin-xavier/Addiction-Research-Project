import pandas as pd


def misuse_counts(df, misuse_cols, misuse_values=[1, 2]):
    return {col: df[col].isin(misuse_values).sum() for col in misuse_cols}


def distress_correlation(df, misuse_cols, distress_col, misuse_values=[1, 2]):
    results = {}
    for col in misuse_cols:
        misusers = df[df[col].isin(misuse_values)].dropna(subset=[distress_col])
        distressed = (misusers[distress_col] == 1).sum()
        not_distressed = (misusers[distress_col] == 0).sum()
        results[col] = {'distressed': distressed, 'not_distressed': not_distressed}
    return results


def health_breakdown(df, misuse_cols, health_col='HEALTH', misuse_values=[1, 2]):
    results = {}
    for col in misuse_cols:
        misusers = df[df[col].isin(misuse_values)]
        results[col] = misusers[health_col].value_counts().sort_index().to_dict()
    return results


def demographic_breakdown(df, misuse_cols, demographic_cols, misuse_values=[1, 2]):
    results = {}
    for misuse_col in misuse_cols:
        misusers = df[df[misuse_col].isin(misuse_values)]
        results[misuse_col] = {}
        for demo_col in demographic_cols:
            if demo_col in df.columns:
                results[misuse_col][demo_col] = misusers[demo_col].value_counts().to_dict()
    return results


def age_group_comparison(df, misuse_cols, age_col, age_range, misuse_values=[1, 2]):
    age_min, age_max = age_range
    age_group_df = df[df[age_col].between(age_min, age_max)]
    return misuse_counts(age_group_df, misuse_cols, misuse_values)
