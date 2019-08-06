# Local installation

## Python and Jupyter notebooks

Install these from [Anaconda](https://www.anaconda.com/distribution/).

## Environments

Detailed instructions: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Best practice is to create a separate environment for each of your projects. This you can do with the following command, which creates an environment called `foss4g` that uses the `environment.yml` file to add additional packages and Python version 3.6:

First go to the directory of the downloaded workshop repo:

`cd ..../crime-data-workshop`

Then open the terminal to create the new environment with the following command:

`conda env create --name foss4g --file environment.yml python=3.6`

## Run the notebook

Activate the new custom environment:

`source activate foss4g`

Create a jupyter kernel from the new environment:

`python -m ipykernel install --user --name foss4g --display-name "Python (foss4g)`

Then start the notebook environment, which will open a web browser:

`jupyter notebook`

Go to the 'notebooks' folder and click on the workshop notebook `***`. This will open a new browser window and start the notebook. Make sure you select the right kernel and then can run the cells in the notebook. 
