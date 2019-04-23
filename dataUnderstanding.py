#  ----------- Data Understanding Phase ----------

# IMDb rating distribution
data.hist(column='imdb_score')


# Movies per year
data.hist(column='title_year')


# Median gross box office per actor
fig = plt.figure(figsize=(8,8))
comparison_df = data.groupby('actor_1_name', as_index=False).mean().sort_values('gross', ascending=False)

name_count_key = data['actor_1_name'].value_counts().to_dict()
comparison_df['films'] = comparison_df['actor_1_name'].map(name_count_key)

comparison_df['actor_1_name'] = comparison_df['actor_1_name'].map(str) + " (" + comparison_df['films'].astype(str) + ")"

comparison_df[comparison_df['films'] >= 5][['actor_1_name', 'gross']][10::-1].set_index('actor_1_name').iloc[:,0].plot(kind='barh')
plt.legend().set_visible(False)
plt.title("Median Gross of Actor_1_name's Films")
plt.ylabel("Actor_1_name (# films)")
plt.xlabel("Gross (in million)")


# title year vs gross
data.plot.scatter(x='title_year', y='gross')


# budget vs gross
data.plot.scatter(x='budget', y='gross')

