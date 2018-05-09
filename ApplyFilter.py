import pandas as pd 
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import preprocessor as p

class ApplyFilter():

    def ApplyFilter(df):

        # filter variables
        min_tweets = 5
        max_tweets = 10000
        max_followers = 2500
        max_following = 2500
        lang = "en"

        # grab only the rows that meet the criteria
        df = df[df.followers < max_followers]
        df = df[df.status_count > min_tweets]
        df = df[df.status_count < max_tweets]
        df = df[df.friends_count < max_following]

        return df


    def filterSentiment(filtered_df, words_df):

        key_phrases = []
        frames = []

        for row in words_df["phrases"]:
            
            key_phrases.append(row)
            
            for key_phrase in key_phrases:
                
                data_to_add = filtered_df[filtered_df['Tweet_text'].str.contains(key_phrase, na = False)]
                frames.append(data_to_add)

        frames_df = pd.concat(frames)
        frames_df_drop = frames_df.drop_duplicates(subset='Tweet_text', keep="first")
        #frames_df_drop.head()

        #VaderSentiment on filtered data (by humanFilter & keyPhrases)

        
        analyzer = SentimentIntensityAnalyzer()

        i=0 #counter

        compval1 = []  #empty list to hold compound VADER scores

        while (i<len(frames_df_drop)):
            
            k = analyzer.polarity_scores(frames_df_drop.iloc[i]['Tweet_text'])
            compval1.append(k["compound"])
            
            i = i + 1

        compval1 = np.array(compval1)
        frames_df_drop['VADER score'] = compval1

        return frames_df_drop

    def sentAnalyzer(df):
        
        analyzer = SentimentIntensityAnalyzer()

        i=0 #counter
        textBlob_list = []
        clean_text = []
        
        
        compval1 = []  #empty list to hold compound VADER scores

        while (i<len(df)):
            
            k = analyzer.polarity_scores(df.iloc[i]['Tweet_text'])
            compval1.append(k["compound"])
            
            b = TextBlob(tweets_df.iloc[i]['Tweet_text'])
            c = b.sentiment.polarity
            textBlob_list.append(c)
    
            d = p.clean(tweets_df.iloc[i]['Tweet_text'])
            clean_text.append(d)
            
            i = i + 1

        compval1 = np.array(compval1)
        df['VADER score'] = compval1
        
        df["TextBlob Score"] = textBlob_list

        df["Clean_Text_data "] = clean_text
        
        
        return df