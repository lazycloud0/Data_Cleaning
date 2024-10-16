# Original data
data = [
    {'user_id': '001', 'age': '-999', 'income': '50k', 'location': 'LONDON  '},
    {'user_id': '002', 'age': '25', 'income': None, 'location': 'london'},
    {'user_id': '003', 'age': '180', 'income': '60k', 'location': ' London'}
]

# Clean solution
import pandas as pd
import numpy as np

def clean_survey_data(data):
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(data)
    
    # Clean age column
    # Replace invalid ages (-999) with NaN and convert to numeric
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    # Filter out impossible ages (e.g., >120)
    df.loc[df['age'] > 120, 'age'] = np.nan
    
    # Clean income column
    # Remove 'k' and convert to numeric
    df['income'] = df['income'].str.replace('k', '000').fillna('0')
    df['income'] = pd.to_numeric(df['income'])
    
    # Clean location column
    df['location'] = df['location'].str.strip().str.title()
    
    return df

# Usage
cleaned_data = clean_survey_data(data)
print(cleaned_data)

