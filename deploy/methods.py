import numpy as np
import pandas as pd
import joblib


knn=joblib.load('deploy\knn.pkl')
encoder=joblib.load('deploy\encoder.pkl')
data = pd.read_csv('deploy\movie_data.csv')
def title(x:str):
    try:
        return x.split('.')[1]
    except:
        return x
    
def get_similar_items(q):
    q_mpa_encoded = encoder.transform([[q['MPA']]])
    
    q_year = np.array([[q['Year']]])
    q_duration = np.array([[q['Duration']]])
    q_rating = np.array([[q['Rating']]])
    
    q_vector = np.hstack([q_year, q_duration, q_mpa_encoded, q_rating])
    
    distances, indices = knn.kneighbors(q_vector)
    data['Title']=data['Title'].apply(title)
    similar_items = data.iloc[indices[0]].to_dict(orient='records')
    return similar_items
   