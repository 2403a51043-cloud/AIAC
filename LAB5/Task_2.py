def sentiment_analysis(text):
    positive_words = ['good', 'great', 'excellent', 'happy', 'love', 'wonderful', 'fantastic', 'amazing', 'positive', 'enjoy']
    negative_words = ['bad', 'terrible', 'awful', 'sad', 'hate', 'horrible', 'worst', 'negative', 'angry', 'dislike']

    text_lower = text.lower()
    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)

    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    else:
        return "neutral"

user_input = input("Enter text for sentiment analysis: ")
result = sentiment_analysis(user_input)
print(result)