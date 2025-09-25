import pandas as pd  # Data handling
import numpy as np   # Numerical operations
import re            # Regular expressions for text cleaning
import html as html_lib  # HTML unescaping
from sklearn.feature_extraction.text import TfidfVectorizer  # Text vectorization

# File paths for input (raw reviews) and output (processed dataset)
input_file = r"C:\Users\manic\OneDrive\Desktop\AIAC\LAB17\movie_reviews.csv"
output_file = r"LAB17/movie_updated.csv"

# Load input CSV into a DataFrame
df = pd.read_csv(input_file)

# Determine which column contains the review text
if 'review' in df.columns:
    text_col = 'review'
elif 'review_text' in df.columns:
    text_col = 'review_text'
else:
    text_col = None

# --- BEFORE SUMMARY --- (basic diagnostics before processing)
print("=== BEFORE CLEANING ===")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing ratings:", df['rating'].isna().sum() if 'rating' in df.columns else "N/A")
if text_col is not None and len(df) > 0:
    print("Sample review (raw):", df[text_col].iloc[0])

# 1) Standardize text: unescape HTML, strip tags, normalize whitespace, lowercase
def clean_text(text):
    """Clean a review string by unescaping HTML, removing tags, collapsing
    whitespace, and lowercasing. Returns an empty string for NaNs."""
    if pd.isnull(text):
        return ""
    raw = str(text)
    # Unescape HTML entities first (e.g., &amp; -> &)
    unescaped = html_lib.unescape(raw)
    # Remove HTML tags robustly (non-greedy across tags)
    no_tags = re.sub(r"<[^>]+>", " ", unescaped)
    # Normalize whitespace and lowercase
    normalized = re.sub(r"\s+", " ", no_tags).strip().lower()
    return normalized

if text_col is not None:
    df['review_clean'] = df[text_col].apply(clean_text)
else:
    raise ValueError("No 'review' or 'review_text' column found in the input CSV.")

# 2) Tokenize and encode reviews using TF-IDF (top 100 terms, English stopwords)
vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
tfidf_matrix = vectorizer.fit_transform(df['review_clean'])
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=[f"tfidf_{w}" for w in vectorizer.get_feature_names_out()])
df = pd.concat([df.reset_index(drop=True), tfidf_df.reset_index(drop=True)], axis=1)

# 3) Handle missing ratings by imputing the column median
if 'rating' in df.columns:
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    median_rating = df['rating'].median()
    df['rating_filled'] = df['rating'].fillna(median_rating)
else:
    raise ValueError("No 'rating' column found in the input CSV.")

# 4) Normalize ratings from 0–10 to 0–1 scale
df['rating_norm'] = df['rating_filled'] / 10.0

# --- AFTER SUMMARY --- (post-processing diagnostics)
print("\n=== AFTER CLEANING ===")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing ratings (after fill):", df['rating_filled'].isna().sum())
print("Median rating used for fill:", median_rating)
print("Sample review (cleaned):", df['review_clean'].iloc[0])
print("TF-IDF features:", [col for col in df.columns if col.startswith("tfidf_")][:5], "...")

# Save cleaned dataset; if target is locked, write to an alternate filename
try:
    df.to_csv(output_file, index=False)
    print(f"\nCleaned dataset saved to: {output_file}")
except PermissionError:
    alt_output = (
        output_file[:-4] + "_new.csv" if output_file.lower().endswith('.csv') else output_file + "_new"
    )
    df.to_csv(alt_output, index=False)
    print(f"\nOriginal file locked. Cleaned dataset saved to: {alt_output}")

