## IBM Cloud

- [Sign up](https://ibm.biz/BdzfFJ) for an IBM Cloud account

- When you are signed up click `Create Resource` at the top of the Resources page. You can find the resources under the hamburger menu at the top left:

 ![](https://github.com/IBMDeveloperUK/pandas-workshop/blob/master/images/resources.png)
 
- Search for Watson Studio and click on the tile:

![](https://github.com/IBMDeveloperUK/jupyter-notebooks-101/blob/master/images/studio.png)

- Select the Lite plan and click `Create`.
- Go back to the Resources list and click on your Watson Studio service that you find under `Services` and then click `Get Started`. 

![](https://github.com/IBMDeveloperUK/jupyter-notebooks-101/blob/master/images/launch.png)

## IBM Watson Studio

### 1. Create a new Project

- You should now be in Watson Studio.
- Create a new project by clicking on `Get Started` and `New Project`, or `Create Project`
- Give your Project a name.
- Select an Object Storage from the drop-down menu or create a new one for free. This is used to store the notebooks and data. **Do not forget to click refresh when returning to the Project page.**
- Click `Create`.  

### 2. Create a Project Access token

To load data into a notebook you need an Access Token. 

- Go the Settings tab at the top of the Project and scroll down to `Access tokens`. 
- Click `New token`
- Give the new token a name, select `Editor` and click `Create`

![](https://github.com/IBMDeveloperUK/geopandas-workshop/blob/master/images/token.png)

- You will need this later in the notebook

### 3. Create a custom Python environment

As geopandas is not installed in the default Python environments you need to create a customized environment. This uses `conda create`. But as the environment is running in the Cloud there are a few steps to go through:

- Go to the environments tab at the top of your project
- Click on `new environment definition`

![](https://github.com/IBMDeveloperUK/geopandas-workshop/blob/master/images/new_env.png)

- Give your new environment a name
- Keep the default, select the free hardware configuration `Free - 1 vCPU and 4 GB RAM`, `Default Python 3.6` and click `Create`

![](https://github.com/IBMDeveloperUK/geopandas-workshop/blob/master/images/customize.png)

- In the next screen you can customize the new environment. Scroll down and click on the `Create` link under Customization

![](https://github.com/IBMDeveloperUK/geopandas-workshop/blob/master/images/customize_env.png)

- A textfield appears that you can edit. Delete all text and copy and paste the below into the textfield:

```
channels:
- defaults
- conda-forge

# Please add conda packages here
dependencies:
- geopandas=0.4.1
- geoplot=0.2.4
- pysal=2.0.0
- folium=0.9.1
- python=3.6.8

# Please add pip packages here
# To add pip packages, please comment out the next line
#- pip:
```
- Click `Apply`

- Now you can use this new environment to run notebooks

## 4. Load and run a notebook

-  Add a new notebook. Click `Add to project` and choose `Notebook`:

![](https://github.com/IBMDeveloperUK/pandas-workshop/blob/master/images/addnotebook.png)

- Choose new notebook `From URL`. Give your notebook a name and copy the URL `https://github.com/IBMDeveloperUK/foss4g-geopandas/blob/master/notebooks/1-pandas-workshop.ipynb`
- Select the **custom runtime enviroment** that you created and click `Create Notebook`. 
-  The notebook will load.
- Go back to the project page and repeat this for the other 2 notebooks that we will use in this workshop. Make sure you select your **custom runtime enviroment** for both :
 - `https://github.com/IBMDeveloperUK/foss4g-geopandas/blob/master/notebooks/2-geopandas-workshop.ipynb`
 - `https://github.com/IBMDeveloperUK/foss4g-geopandas/blob/master/notebooks/3-crime-data-workshop.ipynb`

 
You are now ready to follow along with the workshop in the notebook!
