# Data_Cleaning

## Overview

This project provides tools for cleaning and analyzing survey data. It includes scripts for detecting outliers, cleaning data, and performing various analyses.

## Project Structure

### Files

- **analyze_data.py**: Contains functions and scripts for analyzing cleaned data.
- **clean_survey.py**: Contains functions for cleaning survey data.
- **data_cleaning.py**: Main script to orchestrate the data cleaning process.
- **detect_outlier.py**: Contains functions for detecting outliers in the data.
- **README.md**: Project documentation.

## detect_outlier.py

This module provides functionality to detect outliers in a dataset using the Interquartile Range (IQR) method.

### Function: `detect_outliers`

```python
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
```

###Parameters:

- data: pandas.DataFrame or pandas.Series - The dataset to check for outliers.
- column: str - The column name to check for outliers.
- threshold: float - The IQR multiplier for outlier detection (default is 1.5).

###Returns:

- tuple: A tuple containing the indices and values of the detected outliers.

Installation
To install the required dependencies, run:

pip install -r requirements.txt

Running the Scripts
To run the main data cleaning script, execute:

```python
python [data_cleaning.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fwinnielau%2FDesktop%2FSite%2FData_Cleaning%2Fdata_cleaning.py%22%2C%22path%22%3A%22%2FUsers%2Fwinnielau%2FDesktop%2FSite%2FData_Cleaning%2Fdata_cleaning.py%22%2C%22scheme%22%3A%22file%22%7D%7D)

Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

License
This project is licensed under the MIT License.

Feel free to expand on this documentation based on the specific details and requirements of your project.
```
