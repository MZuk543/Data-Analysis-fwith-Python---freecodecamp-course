import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['BMI'] = df['weight'] / ((df['height'] / 100) * (df['height'] / 100))
df['overweight'] = 0
df['overweight'] = df['overweight'].mask(df['BMI'] > 25, 1)
df = df.drop(columns=['BMI'])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    #df_cat['total'] = 1
    #df_cat = df_cat.groupby(['cardio', 'variable', 'value'],
    #                        as_index=False).count()
    # df_cat = df_cat.groupby(['cardio', 'variable', 'value'],
    #                        as_index=False).size().rename(columns={'size': 'total'})

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(data=df_cat,
                      x='variable',
                      hue='value',
                      col='cardio',
                      kind='count').set_axis_labels('variable', 'total')
    fig = g.fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
  '''
  df_heat = df.copy()
    df_heat.drop(df_heat[df_heat.ap_lo < df_heat.ap_hi].index, inplace=True)
    df_heat.drop(
        df_heat[df_heat.height < df_heat.height.quantile(0.0025)].index,
        inplace=True)
    df_heat.drop(
        df_heat[df_heat.height > df_heat.height.quantile(0.975)].index,
        inplace=True)
    df_heat.drop(
        df_heat[df_heat['weight'] < df_heat['weight'].quantile(0.025)].index,
        inplace=True)
    df_heat.drop(
        df_heat[df_heat.weight > df_heat.weight.quantile(0.975)].index,
        inplace=True)
  '''
  df_heat = df[
(df['ap_lo'] <= df['ap_hi']) & 
(df['height'] >= (df['height'].quantile(0.025))) & 
(df['height'] <= (df['height'].quantile(0.975))) & 
(df['weight'] >= (df['weight'].quantile(0.025))) & 
(df['weight'] <= (df['weight'].quantile(0.975)))]
   

  # Calculate the correlation matrix
  corr = df_heat.corr()

  # Generate a mask for the upper triangle
  mask = np.triu(np.ones_like(corr))

  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(11, 9))

  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr,
              mask=mask,
              annot=True,
              vmax=.3,
              center=0,
              linewidths=.5,
              square=True,
              cbar_kws={"shrink": .5},
              fmt='0.1f')

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig
