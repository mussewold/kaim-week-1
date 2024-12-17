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


def plot_stock_returns(df, stock_columns, figsize=(12, 6)):
    plt.figure(figsize=figsize)

    # Plot returns for each stock
    for column in stock_columns:
        # Extract stock symbol from column name (e.g., 'AAPL_Return' -> 'AAPL')
        stock_symbol = column.split('_')[0]
        plt.plot(df['Date'], df[column], label=stock_symbol, alpha=0.7)

    # Customize the plot
    plt.title('Daily Stock Returns Comparison', fontsize=12)
    plt.xlabel('Date')
    plt.ylabel('Daily Returns (%)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_correlation_analysis(correlations, title='Correlation Analysis'):
    
    stocks = list(correlations.keys())
    correlation_values = [stats['correlation'] for stats in correlations.values()]
    p_values = [stats['p_value'] for stats in correlations.values()]

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Correlation bars
    color = 'tab:blue'
    ax1.set_xlabel('Stocks')
    ax1.set_ylabel('Correlation', color=color)
    ax1.bar(stocks, correlation_values, color=color, alpha=0.6, label='Correlation')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='upper left')

    # P-value line
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('P-value', color=color)
    ax2.plot(stocks, p_values, color=color, marker='o', 
             linestyle='dashed', linewidth=2, markersize=5, label='P-value')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend(loc='upper right')

    fig.tight_layout()
    plt.title(title)
    plt.xticks(rotation=45)
    return fig


