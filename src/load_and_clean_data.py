import pandas as pd

def load_and_clean_data(filepath, output_cleaned_data):
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    df.dropna(subset=['CustomerID'], inplace=True)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%y %H:%M', errors='coerce')
    df.dropna(subset=['InvoiceDate'], inplace=True)
    df.to_csv(output_cleaned_data, index=False)
    return df

