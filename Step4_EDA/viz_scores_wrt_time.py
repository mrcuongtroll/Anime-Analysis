import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.widgets import Cursor
import seaborn as sns
import mplcursors


def label_point(x, y, val, ax):
    # Very slow
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        if point['x'] and point['y'] != 'nan':
            ax.text(point['x'], point['y'], str(point['val']))


def on_hover(data, attrs, selection):
    # Still slow
    assert [a in data.columns for a in attrs], 'Attributes included must be in the data frame'
    try:
        annot = ''
        for attr in attrs:
            annot += f'{attr}: {data[attr][selection.index]}\n'
        selection.annotation.set_text(annot)
    except KeyError:
        return


if __name__ == '__main__':
    data_path = '../data/csv/title_single_valued_attrs.csv'
    data = pd.read_csv(data_path)
    # print(data.columns)
    data['start_date'] = pd.to_datetime(data['start_date'])
    # data.dropna(subset=['start_date'], inplace=True)
    # data.sort_values('start_date', inplace=True)
    # data.reset_index(drop=True, inplace=True)

    print(data.isnull().sum() / len(data) * 100)
    print(f"Total number of records: {len(data)}")

    # Prepare data
    data_anilist = data.dropna(subset=['mean_score_anilist', 'start_date', 'popularity_anilist', 'season_season'])
    # data_anilist = data1[data1['mean_score_anilist'] >= 0.7]
    data_anilist.reset_index(drop=True, inplace=True)
    data_mal = data.dropna(subset=['mean_score_mal', 'start_date', 'popularity_mal', 'season_season'])
    data_mal.reset_index(drop=True, inplace=True)
    data_anisearch = data.dropna(subset=['mean_score_anisearch', 'start_date', 'number_scorer_anisearch',
                                         'season_season'])
    data_anisearch.reset_index(drop=True, inplace=True)
    data_kitsu = data.dropna(subset=['mean_score_kitsu', 'start_date', 'user_count_kitsu', 'season_season'])
    data_kitsu.reset_index(drop=True, inplace=True)

    # Plot
    fig, ax = plt.subplots(2, 2)
    scatter_anilist = sns.scatterplot(data=data_anilist, x='start_date', y='mean_score_anilist',
                                      size='popularity_anilist', hue='season_season', ax=ax[0, 0])
    ax[0, 0].set_xlabel('Time')
    ax[0, 0].set_ylabel('Avg Score')
    ax[0, 0].set_title('AniList')
    scatter_mal = sns.scatterplot(data=data_mal, x='start_date', y='mean_score_mal',
                                  size='popularity_mal', hue='season_season', ax=ax[0, 1])
    ax[0, 1].set_xlabel('Time')
    ax[0, 1].set_ylabel('Avg Score')
    ax[0, 1].set_title('My Anime List')
    scatter_anisearch = sns.scatterplot(data=data_anisearch, x='start_date', y='mean_score_anisearch',
                                        size='number_scorer_anisearch', hue='season_season', ax=ax[1, 0])
    ax[1, 0].set_xlabel('Time')
    ax[1, 0].set_ylabel('Avg Score')
    ax[1, 0].set_title('AniSearch')
    scatter_kitsu = sns.scatterplot(data=data_kitsu, x='start_date', y='mean_score_kitsu',
                                    size='user_count_kitsu', hue='season_season', ax=ax[1, 1])
    ax[1, 1].set_xlabel('Time')
    ax[1, 1].set_ylabel('Avg Score')
    ax[1, 1].set_title('Kitsu')
    plt.subplots_adjust(hspace=0.3)

    # Create interactive cursors
    cursor_anilist = mplcursors.cursor(scatter_anilist)
    cursor_anilist.connect('add', lambda sel: on_hover(data_anilist,
                                                       ['title',
                                                        'start_date',
                                                        'season_season',
                                                        'mean_score_anilist',
                                                        'popularity_anilist',
                                                        'favorites_anilist'],
                                                       sel))
    cursor_mal = mplcursors.cursor(scatter_mal)
    cursor_mal.connect('add', lambda sel: on_hover(data_mal,
                                                   ['title',
                                                    'start_date',
                                                    'season_season',
                                                    'mean_score_mal',
                                                    'popularity_mal',
                                                    'favorites_mal'],
                                                   sel))
    cursor_anisearch = mplcursors.cursor(scatter_anisearch)
    cursor_anisearch.connect('add', lambda sel: on_hover(data_anisearch,
                                                         ['title',
                                                          'start_date',
                                                          'season_season',
                                                          'mean_score_anisearch',
                                                          'number_scorer_anisearch',
                                                          'favorites_anisearch'],
                                                         sel))
    cursor_kitsu = mplcursors.cursor(scatter_kitsu)
    cursor_kitsu.connect('add', lambda sel: on_hover(data_kitsu,
                                                     ['title',
                                                      'start_date',
                                                      'season_season',
                                                      'mean_score_kitsu',
                                                      'user_count_kitsu',
                                                      'favorite_count_kitsu'],
                                                     sel))

    # Show plots
    plt.show()