import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=[0], index_col=[0])

# Clean data
df = df.loc[(df['value'] > (df['value'].quantile(0.025)))
            & (df['value'] < (df['value'].quantile(0.975)))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 5))
    df.plot(kind='line', ax=ax, legend=False, x_compat=True, color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.autofmt_xdate()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    months = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ]
    df_bar = df.copy()
    df_bar = df_bar.groupby([df_bar.index.year, df_bar.index.month
                             ]).agg(avg_page_viewers=('value',
                                                      'mean')).round(0)
    # idx=df_bar.index
    # idx = idx.set_levels(months, level=1)
    df_bar.index = df_bar.index.set_levels(months, level=1)

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(16, 8))
    df_bar.unstack().plot(kind='bar', ax=ax)
    ax.set_xlabel('Years', fontsize='x-large')
    ax.set_ylabel('Average Page Views', fontsize='x-large')
    ax.legend(labels=months, title="Months", title_fontsize='large')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    sns.set_theme(style='ticks')
    fig, (ax1, ax2) = plt.subplots(1,
                                   2,
                                   figsize=(16, 5),
                                   gridspec_kw=dict(width_ratios=[1, 1]))

    sns.boxplot(data=df_box, x='year', y='value', orient='v', ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', order=months, orient='v', ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
