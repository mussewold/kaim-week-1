from nltk.tokenize import word_tokenize
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK data
required_packages = [
    'punkt',
    'stopwords',
    'vader_lexicon',
    'averaged_perceptron_tagger'
]

for package in required_packages:
    try:
        nltk.data.find(f'tokenizers/{package}' if package == 'punkt' 
                      else f'corpora/{package}' if package == 'stopwords'
                      else package)
    except LookupError:
        nltk.download(package)

# Initialize other variables
stop_words = set(stopwords.words('english'))
sia = SentimentIntensityAnalyzer()


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    
    # Lowercase and remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    
    # Tokenize the text
    tokens = word_tokenize(text, language='english')  # Ensure language is set explicitly
    
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    
    return ' '.join(tokens)


def get_sentiment(text):
    scores = sia.polarity_scores(text)
    if scores['compound'] > 0.05:
        return 'positive'
    elif scores['compound'] < -0.05:
        return 'negative'
    else:
        return 'neutral'


def extract_keywords(headlines, n_top=20):
    """
    Extract and count most common meaningful keywords from headlines.
    """
    # Custom stopwords
    stop_words = {
        'stock', 'stocks', 'company', 'companies', 'market', 
        'markets', 'share', 'shares', 'price', 'prices',
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 
        'to', 'for', 'of', 'with', 'by'
    }
    
    words = []
    for headline in headlines:
        # Simple word splitting
        tokens = headline.lower().split()
        words.extend([
            word for word in tokens 
            if word not in stop_words
            and word.isalnum()
            and len(word) > 2
        ])
    
    return Counter(words).most_common(n_top)

def extract_phrases(headlines, n_top=20):
    """
    Extract and count most common bigrams and trigrams from headlines.
    """
    processed_headlines = []
    for headline in headlines:
        # Simple word splitting
        tokens = [token for token in headline.lower().split() if token.isalnum()]
        processed_headlines.append(tokens)
    
    bigrams_list = []
    trigrams_list = []
    for tokens in processed_headlines:
        # Create bigrams
        for i in range(len(tokens) - 1):
            bigrams_list.append((tokens[i], tokens[i + 1]))
        # Create trigrams
        for i in range(len(tokens) - 2):
            trigrams_list.append((tokens[i], tokens[i + 1], tokens[i + 2]))
    
    return {
        'bigrams': Counter(bigrams_list).most_common(n_top),
        'trigrams': Counter(trigrams_list).most_common(n_top)
    }

def find_specific_events(headlines):
    """
    Find and count specific types of events in headlines.
    """
    events = {
        'fda_approval': r'fda\s+approv(al|es|ed)',
        'price_target': r'price\s+target',
        'earnings_report': r'earnings|quarterly\s+results',
        'upgrade_downgrade': r'upgrade|downgrade',
        'merger_acquisition': r'merger|acquisition|acquires'
    }
    
    counts = {event: 0 for event in events}
    for headline in headlines:
        headline = headline.lower()
        for event, pattern in events.items():
            if re.search(pattern, headline):
                counts[event] += 1
    
    return counts