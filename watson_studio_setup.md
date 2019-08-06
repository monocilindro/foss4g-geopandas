# IBM Cloud

# Watson Studio

## Add data to Cloud Object Store (COS)
The data for this workshop needs to be added to your project. Go to the GitHub repo and download the files in the [data folder](https://github.com/IBMDeveloperUK/foss4g-geopandas/tree/master/data) to your machine. 

Go to Watson Studio and add the files in the data menu on the right of the notebook (click the 1010 button  at the top right if you do not see this) into COS:

- boundaries.zip
- 2018-1-metropolitan-street.zip
- 2018-2-metropolitan-street.zip
- 2018-metropolitan-stop-and-search.zip

## Create notebook

## Project Access token

As the data files are not simple csv files, we need a little trick to load the data. The first thing you need is a project access token to programmatically access COS.

Click the 3 dots at the top of the notebook to insert the project token that you created earlier. This will create a new cell in the notebook that you will need to run first before continuing with the rest of the notebook. If you are sharing this notebook you should remove this cell, else anyone can use you Cloud Object Storage from this project.

> If you cannot find the new cell it is probably at the top of this notebook. Scroll up, run the cell and continue with section 3.3
