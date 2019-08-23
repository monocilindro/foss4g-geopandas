ax = boroughs['Gross_Annual_Pay_-_Female_(2016)'].plot.hist(bins=15,figsize=(10,5),alpha=0.5);
ax = boroughs['Gross_Annual_Pay_-_Male_(2016)'].plot.hist(bins=15,figsize=(10,5),alpha=0.5);
ax.legend(['female','male']);

