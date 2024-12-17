import pandas as pd
import matplotlib.pyplot as plt

def plot_publication_frequency(df, date_column='date'):
    """
    Plots the publication frequency of articles over time.
    
    Args:
        df (pd.DataFrame): The input DataFrame containing headlines and their dates.
        date_column (str): The column name for the date information.
    """
    # Ensure the date column is in datetime format
    df[date_column] = pd.to_datetime(df[date_column])
    
    # Count the number of articles published per day
    publication_counts = df.groupby(df[date_column].dt.date).size()
    
    # Plot the publication frequency over time
    plt.figure(figsize=(12, 6))
    plt.plot(publication_counts.index, publication_counts.values, marker='o', color='green', label="Publications per Day")
    plt.title("Publication Frequency Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_top_publishers(publisher_counts, top_n=10):
    
    top_publishers = publisher_counts.head(top_n)
    
    # Plot
    plt.figure(figsize=(10, 6))
    top_publishers.plot(kind='bar', color='skyblue')
    plt.title(f'Top {top_n} Publishers by Number of Articles')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_sentiment_by_publisher(df, publisher_column, sentiment_column, top_n=10):
    
    # Get the top publishers
    top_publishers = df[publisher_column].value_counts().head(top_n).index

    # Filter the DataFrame for only the top publishers
    top_publishers_df = df[df[publisher_column].isin(top_publishers)]

    # Create a pivot table for sentiment counts by publisher
    sentiment_counts = top_publishers_df.pivot_table(
        index=publisher_column,
        columns=sentiment_column,
        aggfunc='size',
        fill_value=0
    )

    # Normalize sentiment counts to percentages
    sentiment_percentages = sentiment_counts.div(sentiment_counts.sum(axis=1), axis=0)

    # Plot
    sentiment_percentages.plot(
        kind='bar',
        stacked=True,
        figsize=(12, 6),
        colormap='tab10'
    )
    plt.title(f"Sentiment Distribution for Top {top_n} Publishers")
    plt.xlabel("Publisher")
    plt.ylabel("Percentage")
    plt.xticks(rotation=45)
    plt.legend(title="Sentiment")
    plt.tight_layout()
    plt.show()


def plot_headline_length_distribution(headline_lengths, figsize=(12, 6)):
    """
    Creates a histogram of headline lengths.

    Args:
        headline_lengths (pd.Series): Series containing the length of headlines
        figsize (tuple): Figure size (width, height)
    """
    plt.figure(figsize=figsize)
    plt.hist(headline_lengths, bins=50, edgecolor='black')
    plt.title('Distribution of Headline Lengths')
    plt.xlabel('Number of Characters')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_keyword_frequencies(keywords, 
                           title: str = "Most Common Keywords",
                           figsize = (12, 6)) -> None:
    words, counts = zip(*keywords)
    plt.figure(figsize=figsize)
    plt.bar(words, counts)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def plot_event_counts(event_counts, 
                     figsize = (10, 6)) -> None:
    events = [event.replace('_', ' ').title() for event in event_counts.keys()]
    counts = list(event_counts.values())
    
    plt.figure(figsize=figsize)
    plt.bar(events, counts)
    plt.title('Frequency of Specific Events in Headlines')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Number of Mentions')
    plt.tight_layout()
    plt.show()


def plot_price_and_ma(data, ticker, indicators):
    """Plot price and moving averages."""
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data[f'{ticker}_Close'], label=f'{ticker} Close Price')
    plt.plot(data.index, indicators['SMA50'], label=f'{ticker} 50-Day SMA')
    plt.plot(data.index, indicators['SMA200'], label=f'{ticker} 200-Day SMA')
    plt.title(f'{ticker} Close Price and Moving Averages')
    plt.legend()
    plt.show()

def plot_rsi(data, ticker, indicators):
    """Plot RSI indicator."""
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, indicators['RSI'], label=f'{ticker} RSI')
    plt.axhline(70, color='r', linestyle='--')
    plt.axhline(30, color='r', linestyle='--')
    plt.title(f'{ticker} Relative Strength Index (RSI)')
    plt.legend()
    plt.show()

def plot_macd(data, ticker, indicators):
    """Plot MACD indicator."""
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, indicators['MACD'], label=f'{ticker} MACD')
    plt.plot(data.index, indicators['MACD_Signal'], label=f'{ticker} MACD Signal')
    plt.bar(data.index, indicators['MACD_Hist'], label=f'{ticker} MACD Hist', alpha=0.3)
    plt.title(f'{ticker} MACD')
    plt.legend()
    plt.show()