[fig, ax] = plt.subplots(1, figsize=(7,7))
ax=sns.scatterplot(y='Median_House_Price,_2015', x='%_of_area_that_is_Greenspace,_2005', data=boroughs,ax=ax);
