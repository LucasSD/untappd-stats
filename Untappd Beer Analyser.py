#Python 3.7.7
#Untappd Beer Analyser 
# Read in csv file from Untappd and output statistics 

import tkinter as tk
from tkinter.filedialog import askopenfilename

import matplotlib.pyplot as plt
import pandas as pd

def analyser(filepath): #BACKEND
    #columns below to delete from raw csv file
    useless_columns = ['beer_name', 'comment', 'venue_lat', 'venue_lng', 'created_at',
                   'checkin_url', 'beer_url', 'brewery_url', 'flavor_profiles', 'purchase_venue',
                   'checkin_id', 'bid', 'brewery_id', 'photo_url', 'tagged_friends',
                   'total_toasts', 'total_comments']

    beers = pd.read_csv(filepath) # read in raw csv
    beers.drop(columns=useless_columns, inplace=True) # delete useless columns from dataframe

    # filter for the columns you want. TODO create loop to get more stats
    beers = beers.filter(['brewery_name', 'rating_score'], axis=1)

    beers=beers.dropna() #remove NaN values

    #obtain the number of entries for each unique column entry
    brewery_counts = beers.groupby(['brewery_name'])[['rating_score']].count() 
                                                                                                                              
    brewery_counts.sort_values(by='rating_score', ascending=True, inplace=True) #sort into ascending

    #TODO: GUI for user to decide their top however many entries by beer count. Number in line below
    #will be user input
    remove_list = list(brewery_counts.index[:-40]) # make a list of the groups with counts too low to include

    brewery_means = beers.groupby(['brewery_name'])[['rating_score']].mean() # obtain means for each group
    brewery_means.drop(remove_list, inplace=True) # remove the groups with counts which are too low
    brewery_means.sort_values(by='rating_score', ascending=True, inplace=True) # ascending order of mean rating
   
    #consider removing median fucntionality below
    brewery_medians = beers.groupby(['brewery_name'])[['rating_score']].median() # obtain medians for each group
    brewery_medians.drop(remove_list, inplace=True) # remove the groups with counts which are too low
    brewery_medians.sort_values(by='rating_score', ascending=True, inplace=True) # ascending order of median rating
    
    output_plotter(brewery_means, brewery_medians)
    
    
    
    #Optional TODO: showing user the beer counts
    #brewery_counts.drop(remove_list, inplace=True) # remove the groups with counts which are too low
    #brewery_counts.to_csv(r'C:\Users\thels\Desktop\New Folder\Beer Stats\Brewery Counts.csv') # write a csv as a
    #record of the counts, for reference

def output_plotter(means, medians):
    means.plot(kind='barh', title='Mean Ratings by Brewery', legend=False) # create horizontal bar charts
    plt.xlabel('Mean Rating out of 5')

    medians.plot(kind='barh', title='Median Ratings by Brewery', legend=False)
    plt.xlabel('Median Rating out of 5')
    
    plt.show()


def open_file(): #GUI
    #Open a CSV file
    global filepath #TODO make work without global variable and add function blocks
    filepath = askopenfilename(filetypes=[("csv Files", "*.csv")])
    if not filepath: return
    analyser(filepath)
    #window.destroy()

#GUI
window = tk.Tk()
window.title('Untappd Beer Statistics')
window.resizable(width=False, height=False)
window.rowconfigure(0, weight=1, minsize=100) 
window.columnconfigure(0, weight=1, minsize=600)

yellow_frm = tk.Frame(window, bg='gold') # make a yellow frame
yellow_frm.grid(row=0, column=0, sticky='nsew')

title_lbl = tk.Label(yellow_frm, text='Untappd Beer Statistics', fg='white', 
                        bg='gold')
title_lbl.grid(row=0, column=3, sticky='n', pady=18)

open_lbl = tk.Label(yellow_frm, 
         text='Select the CSV file you received from Untappd', 
         fg='gold', bg='white')
open_lbl.grid(row=1, column=0, sticky='w')

open_btn = tk.Button(yellow_frm, text='Open', command=open_file)
open_btn.grid(row=1, column=3, sticky='ew')

window.mainloop()