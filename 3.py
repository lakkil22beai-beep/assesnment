from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

# Use cleaned texts
cv = CountVectorizer()
Xcv = cv.fit_transform(cleaned)
tdm_cv = pd.DataFrame(Xcv.toarray(), columns=cv.get_feature_names_out())
print("TDM (CountVectorizer) shape:", tdm_cv.shape)
display(tdm_cv.head())

tfidf = TfidfVectorizer()
Xtf = tfidf.fit_transform(cleaned)
tdm_tfidf = pd.DataFrame(Xtf.toarray(), columns=tfidf.get_feature_names_out())
print("TDM (TF-IDF) shape:", tdm_tfidf.shape)
display(tdm_tfidf.head())