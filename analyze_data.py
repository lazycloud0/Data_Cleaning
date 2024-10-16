def analyze_survey_data(survey_responses, user_demographics):
    """
    Join survey responses with user demographics and perform aggregations
    """
    # Merge the dataframes
    merged_data = pd.merge(
        survey_responses,
        user_demographics,
        on='user_id',
        how='left'
    )
    
    # Example aggregations
    analysis = merged_data.groupby(['age_group', 'location']).agg({
        'response_time': 'mean',
        'satisfaction_score': ['mean', 'count'],
        'user_id': 'count'
    }).round(2)
    
    # Calculate response rates
    total_users = len(user_demographics)
    response_rates = (analysis[('user_id', 'count')] / total_users * 100).round(2)
    
    return analysis, response_rates