![](https://github.com/LucasSD/Untappd-Stats/blob/master/beer_cover.jpg)
# Introduction

This project combines my love of craft beer with my love of programming! The current code produces a number of horizontal bar charts (see PDF document in the "user_output" directory). They provide statistics which are not available directly via the app (even if you pay the subscription) and would take a lot of time to obtain using a basic spreadsheet. I am focussing on statistics such as mean beer rating by beer style, country, brewery, and so on. My code only includes entries with the highest frequencies, to ensure that a beer with one high rating cannot elevate a brewery to the top of the graph, for example. 

Read more about Untappd here https://untappd.com/home

## To run using Windows:

1 - download this repo as a zip file and unzip it to your working directory.  
2 - install Python 3.9.5 to your working directory  
3 - open Windows command prompt for the steps below and change directory as needed  
4 - if you would like to create a virtual environment at any stage, type ```py -m venv env```, where ```env``` is the name of your virtual environment. Activate the virtual environment by typing ```env\Scripts\activate.bat```.    
5 - install dependencies by typing ```py -m pip install -r requirements.txt``` into the cmd terminal.  
6 - run by typing ```py -m beer_analyser``` into the cmd terminal. Alternatively, type ```exec(open('beer_analyser.py').read())``` into an interactive session.  

## To run using UNIX:  

1 - download this repo as a zip file and unzip it to your working directory.  
2 - install Python 3.9.5 to your working directory  
3 - go to the Terminal for the steps below and change directory as needed  
4 - if you would like to create a virtual environment at any stage, type ```python venv env```, where ```env``` is the name of your virtual environment. Activate the virtual environment by typing ```source env/bin/activate```   
5 - If you’re on Linux and installed Python using your OS package manager, you may have to install pip separately for the steps below; see https://packaging.python.org/guides/installing-using-linux-tools/    
6 - Due to the way most Linux distributions are handling the Python 3 migration, Linux users using Python without creating a virtual environment first should replace the ```python``` commands below with ```python3``` and the ```pip``` commands below with ```pip3 --user```.   
7 - install dependencies by typing ```pip install -r requirements.txt```.

8 - run by typing ```python beer_analyser.py``` into the UNIX terminal.  

## To use:   
  
Click on open and select the file called "untappd_beers_raw.csv". A PDF document of multiple bar charts will appear in the same directory as your CSV file. If you are an Untappd user and have your own CSV file from Untappd, use that to check out your own stats!

## Quick Demo (to be updated)

![](demo.gif)

## Technologies

Python 3.9.5, NumPy 1.19.3, Pandas 1.2.5, Matplotlib 3.4.2

## Known Issues

There are some font and clipping issues with y-axis labels.

## Project Status

On hold. 
###### To do:
- fix known y-axis label issue
- rewrite in modules
- add other stats such as mean alcohol content, worst rated beers/breweries/cities..., correlations between alcohol content and rating, and so on
- deploy the application online




