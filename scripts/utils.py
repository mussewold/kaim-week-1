import pandas as pd
import talib
#used to read csv files
def read_csv_file(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)
    
    # Remove any 'Unnamed:' columns
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    
    # Get additional info
    column_names = data.columns.tolist()  
    row_count = data.shape[0]  
    
    return {
        'data': data,
        'column_names': column_names,
        'row_count': row_count
    }


def load_multiple_stocks(file_paths, date_column='Date'):

    combined_df = None
    
    for symbol, path in file_paths.items():
        # Read the CSV file
        df = pd.read_csv(path, parse_dates=[date_column])
        # Set the date as index
        df.set_index(date_column, inplace=True)
        
        # Rename columns to include the symbol
        df.columns = [f'{symbol}_{col}' for col in df.columns]
        
        # Merge with existing data
        if combined_df is None:
            combined_df = df
        else:
            # Use inner join to keep only dates that exist in both DataFrames
            combined_df = combined_df.join(df, how='inner')
    
    # Sort by date
    combined_df.sort_index(inplace=True)
    
    return combined_df

def prepare_stock_data(data, tickers):
    """Select relevant columns for technical analysis."""
    columns = []
    for ticker in tickers:
        columns.extend([f'{ticker}_Open', f'{ticker}_High', f'{ticker}_Low', 
                       f'{ticker}_Close', f'{ticker}_Volume'])
    return data[columns]

def calculate_technical_indicators(data, ticker):
    """Calculate technical indicators for a given stock."""
    results = {}
    
    # Moving Averages
    results['SMA50'] = talib.SMA(data[f'{ticker}_Close'], timeperiod=50)
    results['SMA200'] = talib.SMA(data[f'{ticker}_Close'], timeperiod=200)
    
    # RSI
    results['RSI'] = talib.RSI(data[f'{ticker}_Close'], timeperiod=14)
    
    # MACD
    results['MACD'], results['MACD_Signal'], results['MACD_Hist'] = talib.MACD(
        data[f'{ticker}_Close'], fastperiod=12, slowperiod=26, signalperiod=9
    )
    
    return results