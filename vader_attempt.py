import nltk
import glob
import os
import pandas as pd

# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

df = pd.DataFrame(columns=['subreddit', 'negative', 'neutral', 'positive', 'compound', 'size'])


sentiment = SentimentIntensityAnalyzer()

def use_vader():
    path_name = 'subreddits/'
    
    folders = glob.glob(path_name + '*')


    for index,folder in enumerate(folders):
        try:
            files = glob.glob(folder + '/' + '*' + '.txt')

            text_packet = ""
            for file in files:
                fo = open(file, 'r')
                text = fo.readlines()

                for line in text:
                    text_packet += line


                scores = sentiment.polarity_scores(text_packet)

                df.loc[index] = [os.path.basename(file), scores['neg'], scores['neu'], scores['pos'], scores['compound'], os.path.getsize(file)]
                print("file added: " + os.path.basename(file))
        
        except:
            continue


    return df

def main():
    data = use_vader()

    data.to_csv("Subreddit Sentiments")

main()