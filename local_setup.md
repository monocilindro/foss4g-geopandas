# Local installation

## Python and Jupyter notebooks

Install these from [Anaconda](https://docs.anaconda.com/anaconda/install/).

> As we only have a Mac to test this one these instructions might be slighlty different for Windows or Linux, but instructions for all systems can be found here: https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html

## Environments

Detailed instructions: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Best practice is to create a separate environment for each of your projects. This you can do with the following command, which creates an environment called `foss4g` that uses the `environment.yml` file to add additional packages and Python version 3.6:

Open the terminal and go to the directory of the downloaded workshop repo:

`cd ..../foss4g-geopandas`

Then create the new environment with the following command:

`conda env create --name foss4g --file environment.yml python=3.6`

## Run the notebook

Activate the new custom environment:

`source activate foss4g`

Create a jupyter kernel from the new environment:

`python -m ipykernel install --user --name foss4g --display-name "Python (foss4g)"`

Then start the notebook environment, which will open a web browser:

`jupyter notebook`

Go to the 'notebooks' folder and click on the workshop notebook `1-pandas-workshop.ipynb`. This will open a new browser window and start the notebook. Make sure you select the right kernel and then you can run the cells in the notebook. 
