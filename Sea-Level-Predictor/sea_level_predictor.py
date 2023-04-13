import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    df.plot.scatter(x='Year',
                    y='CSIRO Adjusted Sea Level',
                    ax=ax,
                    c='g',
                    label='Original data')
    
    # Create first line of best fit
    first_results = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    first_slope = first_results.slope
    first_y_intercept = first_results.intercept
    # first_x_regr = df['Year']
    # first_x_regr.loc[len(first_x_regr.index)] = 2050
    first_x_regr = pd.DataFrame(list(range(1880, 2050, 1)))
    first_y_regr = first_slope * first_x_regr + first_y_intercept
    # ax.plot(first_x_regr, first_y_regr, c='r', label='First line of best fit')
    ax.plot(first_x_regr[0],
            first_y_regr[0],
            c='r',
            label='First line of best fit')
    
    # Create second line of best fit
    #
    """df_second = pd.DataFrame([[2000, df[df['Year'] == 2000]['CSIRO Adjusted Sea Level'].values[0]],
                             [df['Year'].iloc[-1], df['CSIRO Adjusted Sea Level'].iloc[-1]]],
                             columns=['Year', 'Sea Level'])"""
    idx_2000 = df.loc[df['Year'] == 2000].index
    df_second = df.loc[idx_2000[0]:, ['Year', 'CSIRO Adjusted Sea Level']]
    df_second.rename(columns={'CSIRO Adjusted Sea Level': 'Sea Level'},
                     inplace=True)
    second_results = linregress(x=df_second['Year'], y=df_second['Sea Level'])
    second_slope = second_results.slope
    second_y_intercept = second_results.intercept
    # second_x_regr = df_second['Year']
    # second_x_regr.loc[len(second_x_regr.index)] = 2050
    second_x_regr = pd.DataFrame(list(range(2000, 2050, 1)))
    second_y_regr = second_slope * second_x_regr + second_y_intercept
    # ax.plot(second_x_regr, second_y_regr, c='m', label='Second line of best fit')
    ax.plot(second_x_regr[0],
            second_y_regr[0],
            c='m',
            label='Second line of best fit')
    
    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xticks([
        1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0,
        2075.0
    ])
    ax.set_xlim([1850, 2075])
    
    # Add legend
    ax.legend()
        
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# draw_plot()
