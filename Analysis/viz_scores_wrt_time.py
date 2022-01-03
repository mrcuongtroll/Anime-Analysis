import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import mplcursors

"""
This code will create scatterplots of anime scores with respect to time.
Please note that since the number of data points is huge, the code will run a bit slow, usually takes about
1 ~ 2 minutes for the plots to show up.
"""


def label_point(x, y, val, ax):
    """
    This function will add labels to every data point on a scatterplot.
    Please not that this function runs very slow because the number of data points is huge.
    We just leave this function here but don't use it.
    :param x: x value of data point
    :param y: y value of data point
    :param val: value of the labels. For instance: title
    :param ax: the axe to add point labels.
    :return: None
    """
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        if point['x'] and point['y'] != 'nan':
            ax.text(point['x'], point['y'], str(point['val']))


def on_clicked(dataframe, attrs, selection):
    """
    This function is used to add annotation when the user clicks on the data points
    :param dataframe: The dataframe containing the data to be used as annotation.
    :param attrs: The attributes to be annotated.
    :param selection: The data point selected
    :return: None
    """
    assert [a in dataframe.columns for a in attrs], 'Attributes included must be in the data frame'
    try:
        annot = ''
        for attr in attrs:
            annot += f'{attr}: {dataframe[attr][selection.index]}\n'
        selection.annotation.set_text(annot)
    except KeyError:
        return


def get_quantiles(dataframe, attr):
    """
    This function
    :param dataframe:
    :param attr: The attribute to be quantiled
    :return: quantiles: list
    """
    quantiles = []
    for index, row in dataframe.iterrows():
        if row[attr] < dataframe[attr].quantile(0.25):
            quantiles.append('p<0.25')
        elif row[attr] < dataframe[attr].quantile(0.5):
            quantiles.append('0.25<p<0.5')
        elif row[attr] < dataframe[attr].quantile(0.75):
            quantiles.append('0.5<p<0.75')
        elif row[attr] < dataframe[attr].quantile(0.9):
            quantiles.append('0.75<p<0.9')
        elif row[attr] < dataframe[attr].quantile(0.95):
            quantiles.append('0.9<p<0.95')
        elif row[attr] < dataframe[attr].quantile(0.99):
            quantiles.append('0.95<p<0.99')
        elif row[attr] <= dataframe[attr].quantile(1):
            quantiles.append('0.99<p<=1.0')
    return quantiles


if __name__ == '__main__':
    # First we load our data
    data_path = '../data/csv/title_single_valued_attrs.csv'
    data = pd.read_csv(data_path)
    data['start_date'] = pd.to_datetime(data['start_date'])     # Convert start_date from string to datetime format
    data['season_year'] = pd.to_datetime(data['season_year'], format='%Y')  # Convert from float to datetime
    # Sort the dataframe based on start_date since we're going to analyse the change in score and popularity
    # with respect to time.
    data.sort_values('start_date', inplace=True)
    data.reset_index(drop=True, inplace=True)

    # Prepare data
    # Since different websites have different user bases and/or different method of grading anime,
    # we will make 4 plots for 4 individual websites.
    data_anilist = data.dropna(subset=['mean_score_anilist', 'start_date', 'popularity_anilist', 'season_season'])
    data_anilist['popularity_quantiles'] = get_quantiles(data_anilist, 'popularity_anilist')
    data_anilist.reset_index(drop=True, inplace=True)
    data_mal = data.dropna(subset=['mean_score_mal', 'start_date', 'popularity_mal', 'season_season'])
    data_mal['popularity_quantiles'] = get_quantiles(data_mal, 'popularity_mal')
    data_mal.reset_index(drop=True, inplace=True)
    data_anisearch = data.dropna(subset=['mean_score_anisearch', 'start_date', 'number_scorer_anisearch',
                                         'season_season'])
    data_anisearch['popularity_quantiles'] = get_quantiles(data_anisearch, 'number_scorer_anisearch')
    data_anisearch.reset_index(drop=True, inplace=True)
    data_kitsu = data.dropna(subset=['mean_score_kitsu', 'start_date', 'user_count_kitsu', 'season_season'])
    data_kitsu['popularity_quantiles'] = get_quantiles(data_kitsu, 'user_count_kitsu')
    data_kitsu.reset_index(drop=True, inplace=True)

    # We'll use the quantiles to define the size of data points (i.e. the dots on the scatterplots)
    size_order = ['0.99<p<=1.0', '0.95<p<0.99', '0.9<p<0.95', '0.75<p<0.9', '0.5<p<0.75', '0.25<p<0.5', 'p<0.25']
    sizes = {'p<0.25': 10,
             '0.25<p<0.5': 20,
             '0.5<p<0.75': 30,
             '0.75<p<0.9': 40,
             '0.9<p<0.95': 75,
             '0.95<p<0.99': 100,
             '0.99<p<=1.0': 125}

    # Plot
    fig, ax = plt.subplots(2, 2)    # Create 4 subplots for 4 websites
    # For each subplot, we create a scatterplot where the y-axis represents time, the x-axis represents the score,
    # the size of the data points represents the popularity (the number of users, by quantiles) and the color
    # of the data points represents the season in which they're released.
    # Besides the scatterplots, we also plot a line representing the mean score and its standard deviation 
    # throughout the years.
    scatter_anilist = sns.scatterplot(data=data_anilist, x='start_date', y='mean_score_anilist',
                                      size='popularity_quantiles', size_order=size_order, sizes=sizes,
                                      hue='season_season', ax=ax[0, 0])
    line_anilist = sns.lineplot(data=data_anilist, x='season_year', y='mean_score_anilist',
                                ci='sd', ax=ax[0, 0], color='black')
    ax[0, 0].set_xlabel('Time')
    ax[0, 0].set_ylabel('Avg Score')
    ax[0, 0].set_title('AniList')
    scatter_mal = sns.scatterplot(data=data_mal, x='start_date', y='mean_score_mal',
                                  size='popularity_quantiles', size_order=size_order, sizes=sizes,
                                  hue='season_season', ax=ax[0, 1])
    line_mal = sns.lineplot(data=data_mal, x='season_year', y='mean_score_mal',
                            ci='sd', ax=ax[0, 1], color='black')
    ax[0, 1].set_xlabel('Time')
    ax[0, 1].set_ylabel('Avg Score')
    ax[0, 1].set_title('My Anime List')
    scatter_anisearch = sns.scatterplot(data=data_anisearch, x='start_date', y='mean_score_anisearch',
                                        size='popularity_quantiles', size_order=size_order, sizes=sizes,
                                        hue='season_season', ax=ax[1, 0])
    line_anisearch = sns.lineplot(data=data_anisearch, x='season_year', y='mean_score_anisearch',
                                  ci='sd', ax=ax[1, 0], color='black')
    ax[1, 0].set_xlabel('Time')
    ax[1, 0].set_ylabel('Avg Score')
    ax[1, 0].set_title('AniSearch')
    scatter_kitsu = sns.scatterplot(data=data_kitsu, x='start_date', y='mean_score_kitsu',
                                    size='popularity_quantiles', size_order=size_order, sizes=sizes,
                                    hue='season_season', ax=ax[1, 1])
    line_kitsu = sns.lineplot(data=data_kitsu, x='season_year', y='mean_score_kitsu',
                              ci='sd', ax=ax[1, 1], color='black')
    ax[1, 1].set_xlabel('Time')
    ax[1, 1].set_ylabel('Avg Score')
    ax[1, 1].set_title('Kitsu')

    # Create interactive cursors
    # We want to make an interactive visualization, where an annotation containing the information about an anime
    # pops up when the user clicks on the data point corresponding to that anime.
    # This is done by connecting the plots to a cursor object, using the on_clicked function created above
    # To show annotation: left-click on data point.
    # To hide annotation: right-click on annotation.
    cursor_anilist = mplcursors.cursor(scatter_anilist)
    cursor_anilist.connect('add', lambda sel: on_clicked(data_anilist,
                                                       ['title',
                                                        'start_date',
                                                        'season_season',
                                                        'mean_score_anilist',
                                                        'popularity_anilist',
                                                        'favorites_anilist'],
                                                       sel))
    cursor_mal = mplcursors.cursor(scatter_mal)
    cursor_mal.connect('add', lambda sel: on_clicked(data_mal,
                                                   ['title',
                                                    'start_date',
                                                    'season_season',
                                                    'mean_score_mal',
                                                    'popularity_mal',
                                                    'favorites_mal'],
                                                   sel))
    cursor_anisearch = mplcursors.cursor(scatter_anisearch)
    cursor_anisearch.connect('add', lambda sel: on_clicked(data_anisearch,
                                                         ['title',
                                                          'start_date',
                                                          'season_season',
                                                          'mean_score_anisearch',
                                                          'number_scorer_anisearch',
                                                          'favorites_anisearch'],
                                                         sel))
    cursor_kitsu = mplcursors.cursor(scatter_kitsu)
    cursor_kitsu.connect('add', lambda sel: on_clicked(data_kitsu,
                                                     ['title',
                                                      'start_date',
                                                      'season_season',
                                                      'mean_score_kitsu',
                                                      'user_count_kitsu',
                                                      'favorite_count_kitsu'],
                                                     sel))

    # Show plots
    plt.subplots_adjust(hspace=0.3)
    plt.show()
