import pandas as pd 

class getWordsDF():
    
    # this method is designed to take a very specific
    # file (triggerWords.csv) and convert/return a dataframe
    def getWordsDF(filepath):

        keywords_df = pd.read_csv(filepath, header=None, encoding = "ISO-8859-1")
        keywords_df.columns = ['phrases']

        return keywords_df

    def getDFFromCSV(filepath):

        df = pd.read_csv(filepath, delimiter="|", header=None, error_bad_lines=False, encoding="ISO-8859-1")
        df.columns = ['ID', 'DateTime', 'Username', 
                        'Tweet_text', 'retweet count', 
                        'Tweet Name', 'followers', 
                        'friends_count', 'status_count', 
                        'Search Coordinates']
        return df

    def getDFTest(filepath):

        col = ['Polarity', 'Tweet_ID', 'Date', 'Query', 'Username', 'Tweet_text']
        df = pd.read_csv(filepath, names=col, header=None, error_bad_lines=False, encoding="ISO-8859-1")

        return df
    
    def getFilteredDFCSV(filepath):

        df = pd.read_csv(filepath, encoding = "ISO-8859-1")

        return df

    def getVaderPosNegNeuScores(pyTest):

        posCtr = 0
        negCtr = 0
        neutralCtr = 0

        for row in pyTest['VADER score']:
            if row > 0:
                posCtr += 1
            elif row < 0:
                negCtr += 1
            else:
                neutralCtr += 1

        data = {'Category': ['Positive', 'Neutral', 'Negative'], 
                'Score': [posCtr, neutralCtr, negCtr]}
        df = pd.DataFrame(data)
        df = df.set_index('Category')
        

        return df  

        
        