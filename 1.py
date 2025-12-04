
tokenized = [word_tokenize(t) for t in cleaned]

# Stopword removal
stop = set(stopwords.words('english'))
tokenized_nostop = [[w for w in toks if w not in stop] for toks in tokenized]

# Stemming
ps = PorterStemmer()
stemmed = [[ps.stem(w) for w in toks] for toks in tokenized_nostop]

# Lemmatization
wnl = WordNetLemmatizer()
lemmatized = [[wnl.lemmatize(w) for w in toks] for toks in tokenized_nostop]

# Show samples
for i,orig in enumerate(reviews):
    print(f"Review {i+1} original: {orig}")
    print(f" Cleaned: {cleaned[i]}")
    print(f" Tokenized: {tokenized[i]}")
    print(f" No-stopwords: {tokenized_nostop[i]}")
    print(f" Stemmed: {stemmed[i]}")
    print(f" Lemmatized: {lemmatized[i]}")
    print("="*60)