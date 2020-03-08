import seaborn as sns

titanic = sns.load_dataset("titanic")

print(titanic.head(3).append(titanic.tail(3)))
