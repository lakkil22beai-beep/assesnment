from collections import Counter

# choose lemmatized tokens for frequency
all_tokens = [w for toks in lemmatized for w in toks]
freq = Counter(all_tokens)
top15 = freq.most_common(15)
print("Top 15 words:", top15)