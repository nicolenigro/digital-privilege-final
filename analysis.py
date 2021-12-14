import csv

class subReddit:
    def __init__(self, name, negative, neutral, positive, compound, size):
        self.name = name
        self.negative = float(negative)
        self.neutral = float(neutral)
        self.positive = float(positive)
        self.compound = float(compound)
        self.size = int(size)
    
    def __repr__(self):
        return self.name[:-4]

filename = 'subreddit_sentiments.csv'

with open(filename, 'r') as f:
    csvReader = csv.reader(f)
    fields = next(csvReader)
    subReddits = []
    for row in csvReader:
        subReddits.append(subReddit(*row[1:]))
    neg = [s for s in subReddits if s.compound <= -0.05]
    pos = [s for s in subReddits if s.compound >= 0.05]
    neutral = [s for s in subReddits if s.compound <= 0.05 and s.compound >= -.05]
    print('Number of subreddits with a negative sentiment =', len(neg))
    print('Number of subreddits with a positive sentiment =', len(pos))
    print('Number of subreddits with a neutral sentiment =', len(neutral))
    compounds = [float(s.compound) for s in subReddits]
    maxSubs = [s for s in subReddits if s.compound == max(compounds)]    # subs with most positive sentiment
    minSubs = [s for s in subReddits if s.compound == min(compounds)]      # subs with most negative sentiment
    print('\nSubreddits with the most positive sentiment =', maxSubs)
    print('\nSubreddits with the most negative sentiment =', minSubs)
