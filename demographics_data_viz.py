import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('foreveralone.csv')
df.replace(to_replace="No", value=0)
df.replace(to_replace="Yes", value=1)

print(df)

sns.set_style('darkgrid')

sns.countplot(x ='gender', data = df)
plt.savefig('gender.png')

plt.figure()
sns.stripplot(x ='gender', y ='friends', data = df, jitter = True, dodge = True)
plt.savefig('friends.png')

plt.figure()
sns.stripplot(x ='friends', y ='depressed', data = df, jitter = True, dodge = True, hue='gender')
plt.savefig('depressed.png')