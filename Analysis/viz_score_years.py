import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

"""
This code will create box plots of anime scores for each year. Each box corresponds to a year.
"""


if __name__ == '__main__':
    # First we load our data
    data_path = '../data/csv/title_single_valued_attrs.csv'
    data = pd.read_csv(data_path)
    data['start_date'] = pd.to_datetime(data['start_date'])     # Convert start_date from string to datetime format
    data['year'] = data['start_date'].dt.year       # Now we need the year of release to be numeric (float/int)
    # Sort the dataframe based on start_date since we're going to analyse the change in score and popularity
    # with respect to time.
    data.sort_values('start_date', inplace=True)
    data.reset_index(drop=True, inplace=True)

    # Plots
    fig, ax = plt.subplots(2, 2)
    box_anilist = sns.boxplot(data=data, x='year', y='mean_score_anilist', ax=ax[0, 0])
    ax[0, 0].tick_params(axis='x', labelrotation=60)
    ax[0, 0].set_xlabel('Year')
    ax[0, 0].set_ylabel('Avg Score')
    ax[0, 0].set_title('AniList')
    box_mal = sns.boxplot(data=data, x='year', y='mean_score_mal', ax=ax[0, 1])
    ax[0, 1].tick_params(axis='x', labelrotation=60)
    ax[0, 1].set_xlabel('Year')
    ax[0, 1].set_ylabel('Avg Score')
    ax[0, 1].set_title('My Anime List')
    box_anisearch = sns.boxplot(data=data, x='year', y='mean_score_anisearch', ax=ax[1, 0])
    ax[1, 0].tick_params(axis='x', labelrotation=60)
    ax[1, 0].set_xlabel('Year')
    ax[1, 0].set_ylabel('Avg Score')
    ax[1, 0].set_title('AniSearch')
    box_kitsu = sns.boxplot(data=data, x='year', y='mean_score_kitsu', ax=ax[1, 1])
    ax[1, 1].tick_params(axis='x', labelrotation=60)
    ax[1, 1].set_xlabel('Year')
    ax[1, 1].set_ylabel('Avg Score')
    ax[1, 1].set_title('Kitsu')

    # Show plots
    plt.subplots_adjust(hspace=0.5)
    plt.show()
