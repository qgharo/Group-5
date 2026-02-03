import pandas as pd
import matplotlib.pyplot as plt


repo = 'scottyab/rootbeer'
commit_filename = 'data/author_touches_' + repo.split('/')[1] + '.csv'

commit_df = pd.read_csv(commit_filename)
commit_df['Commit_Date'] = pd.to_datetime(commit_df['Commit_Date'])


first_commit = commit_df['Commit_Date'].min()
commit_df['week_diff'] = ((commit_df['Commit_Date'] - first_commit).dt.days // 7)

plt.figure(figsize=(10,8))

authors = commit_df['Author'].unique()
files = commit_df['Filename'].unique()

for i, a in enumerate(authors):
    author_commits = commit_df[commit_df['Author'] == a]
    plt.scatter(author_commits['Filename'], author_commits['week_diff'])


plt.xticks(files, list(range(0, len(files))))
plt.xlabel('file')
plt.ylabel('weeks')

plt.show()
plt.savefig('author_touches.png')
