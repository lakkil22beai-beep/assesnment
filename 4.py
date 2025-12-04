from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')  # uncommented to fix the error
sia = SentimentIntensityAnalyzer()

sentiments = []
for i, r in enumerate(reviews):
    score = sia.polarity_scores(r)
    compound = score['compound']
    if compound >= 0.05:
        label = 'positive'
    elif compound <= -0.05:
        label = 'negative'
    else:
        label = 'neutral'
    sentiments.append((i+1, r[:80] + ('...' if len(r)>80 else ''), label, compound))

import pandas as pd
df_sent = pd.DataFrame(sentiments, columns=['ID','Comment','Sentiment','Score'])
display(df_sent)