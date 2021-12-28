import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


if __name__ == '__main__':
    data_path = '../data/csv/title_single_valued_attrs.csv'
    data = pd.read_csv(data_path)
    data['start_date'] = pd.to_datetime(data['start_date'])
    data['year'] = data['start_date'].dt.year
    data.sort_values('start_date', inplace=True)
    data.reset_index(drop=True, inplace=True)

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

    plt.subplots_adjust(hspace=0.5)
    plt.show()
