# social_sentiment_vader.py
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
# nltk.download('vader_lexicon')

comments = [
"Love the new update — UI is so smooth!",
"App crash after the latest patch, please fix.",
"Great customer support! They helped me quickly.",
"This product is a waste of money.",
"Does anyone know how to change the settings?",
"Amazing sound quality, much better than before.",
"I’m returning it — the battery didn't last.",
"Totally worth every rupee. Highly recommended!",
"Lagging on my device, not sure why.",
"Sale price was awesome, grabbed it fast.",
"Customer service was rude to me.",
"This review helped me decide to buy, thanks!",
"Not impressed with the camera in low light.",
"Fast delivery and nice packaging.",
"The update removed my favorite feature :(",
"Five stars — performance is top notch.",
"Is there an international warranty?",
"Had a small scratch on delivery, returned it.",
"Superb battery life after firmware update.",
"I will never buy from this brand again."
]

sia = SentimentIntensityAnalyzer()
rows = []
for i, c in enumerate(comments):
    s = sia.polarity_scores(c)
    comp = s['compound']
    if comp >= 0.05:
        lab = 'positive'
    elif comp <= -0.05:
        lab = 'negative'
    else:
        lab = 'neutral'
    rows.append((i+1, c, lab, comp))

df = pd.DataFrame(rows, columns=['ID','Comment','Sentiment','Score'])
display(df)

# Compute percentages
counts = df['Sentiment'].value_counts(normalize=True) * 100
print("Percent positive:", round(counts.get('positive',0),2))
print("Percent neutral:", round(counts.get('neutral',0),2))
print("Percent negative:", round(counts.get('negative',0),2))

# Save CSV
df.to_csv('social_comments_sentiment.csv', index=False)