Quick Demo

![](https://github.com/LucasSD/Untappd-Stats/blob/master/Beer%20Analyser%20Gif.gif)

My aim is to continue to improve and add to this project, which combines my love of craft beer with my love of programming! I'm putting this into a GitHub repository so that I can learn about work flow and version control. The current code works and produces a number of horizontal bar charts (see PNG images in repository). They provide statistics which are not available directly via the app (even if you pay the subscription) and would take a lot of time to obtain using a basic spreadsheet. I am focussing on statistics such as mean beer rating by beer style, country, brewery, and so on. My code only includes entries with the highest frequencies, to ensure that a beer with one high rating cannot elevate a brewery to the top of the graph, for example. 

Read more about Untappd here https://untappd.com/home

To install using windows:

1 - download this repo as a zip file and unzip it to your working directory.  
2 - install Python 3.9 to your working directory  
3 - open Windows command prompt for the steps below  
4 - if you would like to create a virtual environment at any stage, type ```$ py -m virtual env```, where env is the name of your virtual environment  
5 - install numpy by typing ```$ py -m pip install numpy==1.19.3``` into the cmd terminal. Version 1.19.4 produces a RunTime error in Windows at the time of writing (16/12/2020).  
6 - install pandas by typing ```$ py -m pip install pandas``` into the cmd terminal.  
7 - install matplotlib by typing ```$ py -m pip install matplotlib``` into the cmd terminal.  
8 - run by typing ```$ py -m Untappd_Beer_Analyser``` into the cmd teminal. Alternatively, type ```$ exec(open('Untappd_Beer_Analyser.py').read())``` into an interactive session.   

To use:   
  
Click on open and select the file called "Untappd beers.csv". Browse the bar charts. 


