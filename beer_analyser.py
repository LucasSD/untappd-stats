import re, os
import tkinter as tk
from tkinter.filedialog import askopenfilename

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd


def analyser(filepath):  # BACKEND
    pp = PdfPages(os.path.dirname(filepath) + "/Your_Beer_Statistics.pdf")

    interesting_fields = [
        "brewery_country",
        "brewery_name",
        "beer_type",
        "venue_name",
        "venue_city",
        "venue_country",
        "brewery_city",
        "purchase_venue",
        "serving_type",
    ]
    titles = []
    raw_beers = pd.read_csv(filepath)  # read in raw csv

    for i, field in enumerate(interesting_fields):
        title = field.capitalize().replace("_", " ")
        mo = re.search(" .", title)
        title = re.sub(" .", mo.group().upper(), title)
        titles.append(title)

        beers = raw_beers.filter([field, "rating_score"], axis=1)

        beers = beers.dropna()  # remove NaN values

        # obtain the number of entries for each unique column entry
        brewery_counts = beers.groupby([field])[["rating_score"]].count()

        brewery_counts.sort_values(
            by="rating_score", ascending=True, inplace=True
        )  # sort into ascending

        remove_list = list(
            brewery_counts.index[:-20]
        )  # make a list of the groups with counts too low to include

        brewery_means = beers.groupby([field])[
            ["rating_score"]
        ].mean()  # obtain means for each group
        brewery_means.drop(
            remove_list, inplace=True
        )  # remove the groups with counts which are too low
        brewery_means.sort_values(
            by="rating_score", ascending=True, inplace=True
        )  # ascending order of mean rating

        # consider removing median fucntionality below
        brewery_medians = beers.groupby([field])[
            ["rating_score"]
        ].median()  # obtain medians for each group
        brewery_medians.drop(
            remove_list, inplace=True
        )  # remove the groups with counts which are too low
        brewery_medians.sort_values(
            by="rating_score", ascending=True, inplace=True
        )  # ascending order of median rating

        output_plotter(brewery_means, brewery_medians, titles[i], pp)

    pp.close()
    window.destroy()
    # brewery_counts.to_csv(r'C:\Users\thels\Desktop\New Folder\Beer Stats\Brewery Counts.csv') # write a csv as a
    # record of the counts, for reference


def output_plotter(means, medians, title, pp):

    means.plot(
        kind="barh", title=f"Mean Ratings by {title}", legend=False, figsize=(10, 6)
    )  # create horizontal bar charts
    plt.xlabel("Mean Rating out of 5")
    plt.ylabel("Country")
    pp.savefig()

    medians.plot(
        kind="barh", title=f"Median Ratings by {title}", legend=False, figsize=(10, 6)
    )
    plt.xlabel("Median Rating out of 5")
    plt.ylabel("Country")
    pp.savefig()


def open_file():  # GUI
    # Open a CSV file
    global filepath  # TODO make work without global variable and add function blocks
    filepath = askopenfilename(filetypes=[("csv Files", "*.csv")])
    if not filepath:
        return
    analyser(filepath)


# GUI
window = tk.Tk()
window.title("Untappd Beer Statistics")
window.resizable(width=False, height=False)
window.rowconfigure(0, weight=1, minsize=100)
window.columnconfigure(0, weight=1, minsize=600)

yellow_frm = tk.Frame(window, bg="gold")  # make a yellow frame
yellow_frm.grid(row=0, column=0, sticky="nsew")

title_lbl = tk.Label(yellow_frm, text="Untappd Beer Statistics", fg="white", bg="gold")
title_lbl.grid(row=0, column=3, sticky="n", pady=18)

open_lbl = tk.Label(
    yellow_frm,
    text="Select the CSV file you received from Untappd",
    fg="gold",
    bg="white",
)
open_lbl.grid(row=1, column=0, sticky="w")

open_btn = tk.Button(yellow_frm, text="Open", command=open_file)
open_btn.grid(row=1, column=3, sticky="ew")

window.mainloop()


