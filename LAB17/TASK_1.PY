# Core libraries for data handling and text processing
import pandas as pd
import string
import re

# Define input and output file paths
# Input: raw social media posts
# Output: cleaned dataset saved back into the LAB17 folder
input_file = r"C:\Users\manic\OneDrive\Desktop\AIAC\LAB17\social_media.csv"
output_file = r"LAB17/social_updated.csv"

# Load the dataset into a DataFrame
df = pd.read_csv(input_file)

# 1) Text cleaning setup: stopwords used to filter out non-informative words
#    This list removes common pronouns, articles, and auxiliaries
stopwords = set([
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
    'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
    'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
    'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
    'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
    'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
    'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out',
    'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why',
    'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
    'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should',
    "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't",
    'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't",
    'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't",
    'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
])

def clean_text(text):
    """Clean a single text string by removing HTML, punctuation, special symbols,
    converting to lowercase, and dropping stopwords."""
    # Handle missing values as empty strings
    if pd.isnull(text):
        return ""
    # Remove any HTML/XML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove punctuation characters
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove any remaining non-alphanumeric symbols
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    # Normalize to lowercase
    text = text.lower()
    # Split into tokens
    words = text.split()
    # Drop stopwords
    words = [word for word in words if word not in stopwords]
    # Reconstruct the cleaned text
    return ' '.join(words)

# Apply text cleaning to the original post text
df['post_text_clean'] = df['post_text'].apply(clean_text)

# 2) Numeric cleanup: coerce, fill, and type-cast likes and shares
df['likes'] = pd.to_numeric(df['likes'], errors='coerce')
df['shares'] = pd.to_numeric(df['shares'], errors='coerce')
df['likes'] = df['likes'].fillna(0).astype(int)
df['shares'] = df['shares'].fillna(0).astype(int)

# 3) Time features: parse timestamp and extract hour and weekday name
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d-%m-%Y %H:%M', errors='coerce')
df['hour'] = df['timestamp'].dt.hour
df['weekday'] = df['timestamp'].dt.day_name()

# 4) Remove duplicate posts based on the cleaned text
df = df.drop_duplicates(subset=['post_text_clean'])

# Save the cleaned DataFrame to CSV in LAB17 folder
df.to_csv(output_file, index=False)





