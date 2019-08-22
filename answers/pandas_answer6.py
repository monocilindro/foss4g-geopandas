[fig, ax] = plt.subplots(1, figsize=(7,7))
sns.barplot(x="Median_House_Price,_2015", y="Area_name", data=boroughs, ax=ax);

