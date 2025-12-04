# web_mining_ait.py
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')

url = "https://ait.ac.in"
resp = requests.get(url, timeout=15)
html = resp.text

# Save raw html for screenshot:
with open("ait_homepage_raw.html", "w", encoding="utf-8") as f:
    f.write(html)

soup = BeautifulSoup(html, "html.parser")

# Count headings H1 - H6
h_counts = {f"h{i}": len(soup.find_all(f"h{i}")) for i in range(1,7)}

# Count hyperlinks
a_tags = soup.find_all('a')
hyperlink_count = len(a_tags)

# Extract visible text
for script in soup(["script","style"]):
    script.decompose()
text = soup.get_text(separator=" ")
text = re.sub(r'\s+', ' ', text).strip()

# Preprocess for top words
text_clean = text.lower()
text_clean = re.sub(r'[^a-z0-9\s]', ' ', text_clean)
tokens = text_clean.split()
stop = set(stopwords.words('english'))
tokens_nostop = [t for t in tokens if t not in stop and len(t)>2]
freq = Counter(tokens_nostop)
top10 = freq.most_common(10)

# Save outputs
print("Heading counts H1-H6:", h_counts)
print("Total hyperlinks (a tags):", hyperlink_count)
print("Top 10 frequent words (post-preprocessing):", top10)

# Save small CSV for report
import pandas as pd
pd.DataFrame(top10, columns=['word','freq']).to_csv('ait_top10_words.csv', index=False)