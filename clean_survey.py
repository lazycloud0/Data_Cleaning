def clean_social_media_survey(df):
    """
    Comprehensive cleaning of social media survey data
    """
    # 1. Handle Missing Ages
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    # Option 1: Impute with median age by demographic group
    df['age'] = df.groupby('demographic_group')['age'].transform(
        lambda x: x.fillna(x.median())
    )
    
    # 2. Standardize Country Names
    country_mapping = {
        'USA': 'United States',
        'US': 'United States',
        'America': 'United States',
        # Add more mappings as needed
    }
    df['country'] = df['country'].replace(country_mapping)
    
    # 3. Handle Impossible Values
    df.loc[df['age'] > 120, 'age'] = np.nan
    
    # 4. Remove Duplicates
    df = df.drop_duplicates(subset=['user_id', 'timestamp'])
    
    # 5. Standardize Income
    # Convert all to USD using exchange rates
    exchange_rates = {
        'GBP': 1.25,
        'EUR': 1.1,
        # Add more rates as needed
    }
    
    def standardize_income(row):
        if pd.isna(row['income']) or pd.isna(row['currency']):
            return np.nan
        return row['income'] * exchange_rates.get(row['currency'], 1)
    
    df['income_usd'] = df.apply(standardize_income, axis=1)
    
    return df

# Best practices to mention:
# 1. Document all cleaning steps
# 2. Keep raw data unchanged
# 3. Log all modifications
# 4. Create validation checks
# 5. Consider impact on analysis