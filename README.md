# Covid-19 Dashboard Project
A Dashboard to display information regarding COVID-19

### Table of Contents

 1. [Installation](#installation)
 2. [Project Motivation](#motivation)
 3. [File Descriptions](#files)
 4. [Execution](#execution)
 5. [Licensing, Authors, and Acknowledgements](#licensing)
 

## Installation <a name="installation"></a>

For this project we used Python Libraries(Pandas, Request, Numpy), Web App and Data Visualization(Flask, Plotly)and for the creation of the app JavaScript, Bootstrap.  The code should run with no issues using   Python versions 3.

## Project Motivation<a name="motivation"></a>

The project scope is to build a Data Dashboard wed-site with API to show everyday data for COVID-19. The dataset is an open-source API create and provided by [disease.sh - Open Disease API](https://github.com/disease-sh).

## File Descriptions <a name="files"></a>

There are 2 folders available here with work related to the project.  Both of the folders is a key to run the dashboard.  Markdown cells were used to assist in walking through the thought process for individual steps.
In the covidapp folder are all the needed templates to run the web app. 
In the wrangling_scripts we have the template to get data from the API, clean them and create the charts.

## Execution<a name="execution"></a>

1. You can run the following commands in the project's root directory to set up the database and model.

Uncomment second line in the covid.py file.
2. Run the following command in the app's directory to run your web app.
    `python covid.py`

3. Go to http://0.0.0.0:3001/

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to [disease.sh - Open Disease API]( https://github.com/disease-sh) for providing the data. Also Udacity for giving me the chance to learn Data Science in depth. Otherwise, feel free to use the code here as you would like! 
