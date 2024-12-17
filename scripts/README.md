
# Nova Financial Solutions Predictive Analytics Report

## 1. **Introduction**
   - **Overview**: Analysis of financial news data and its correlation with stock market movements.
   - **Purpose**: 
     - Identify key correlations between news sentiment and stock price movements.
     - Analyze historical stock price data.
     - Classify financial news article sentiments for actionable insights into stock performance.

## 2. **Purpose and Objectives**
   - **Objectives**:
     - Identify key correlations between news sentiment and stock price movements.
     - Analyze historical stock price data for trends and anomalies.
     - Classify financial news article sentiments for actionable insights.

## 3. **Methodology**
   - **Sentiment Analysis**:
     - Utilized NLP techniques for sentiment classification of financial news headlines.
     - Dataset structure: 5 columns - headline, url, publisher, date, stock (ticker).
     - Generated statistical overview of headline lengths and identified common keywords/phrases in headlines.
   - **Quantitative Analysis**:
     - Calculated technical indicators using TA-Lib: 50-day and 200-day Simple Moving Averages (SMAs), RSI, MACD.
     - Analyzed historical stock data for trends and potential trading decisions.
   - **Correlation Analysis**:
     - Aligned news and stock datasets by normalizing dates.
     - Sentiment analysis of headlines to assign sentiment scores.
     - Calculated stock movements as daily returns.
     - Pearson correlation coefficient used to evaluate the relationship between average sentiment scores and stock daily returns.

## 4. **Findings**
   - **Sentiment Analysis**:
     - Distribution of headline lengths.
     - Common keywords and phrases in news headlines.
   - **Publisher Analysis**:
     - Most active publishers and their contributions.
     - Sentiment distribution across top publishers.
   - **Quantitative Analysis**:
     - Technical indicators calculated for various stocks (AAPL, GOOG, MSFT, AMZN, META, TSLA, NVDA).
   - **Correlation Analysis**:
     - Correlation between daily sentiment scores and stock returns for individual stocks.
     - **Observations**:
       - Statistical significance of correlations with varying p-values.
