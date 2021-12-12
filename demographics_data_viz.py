import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('foreveralone.csv')

sns.set_style('darkgrid')

#GENDER
sns.countplot(x ='gender', data = df)
plt.savefig('gender.png')

#FRIENDS & DEPRESSED BY GENDER
sns.catplot(data=df, kind="bar", x="depressed", y="friends", hue="gender")
plt.savefig('depressed.png')

#FRIENDS & SOCIAL FEAR BY GENDER
plt.figure()
sns.catplot(data=df, kind="bar", x="social_fear", y="friends", hue="gender")
plt.savefig('social_fear.png')