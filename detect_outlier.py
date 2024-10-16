def detect_outliers(data, column, threshold=1.5):
    """
    Detect outliers using IQR method
    
    Parameters:
    data: pandas DataFrame or Series
    column: string, column name to check for outliers
    threshold: float, IQR multiplier for outlier detection
    
    Returns:
    tuple: (outlier_indices, outlier_values)
    """
    # Calculate Q1, Q3, and IQR
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    
    # Define bounds
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    
    # Find outliers
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    
    # Return both indices and values
    return outliers.index, outliers[column]

# Example usage:
# outlier_idx, outlier_vals = detect_outliers(df, 'age')