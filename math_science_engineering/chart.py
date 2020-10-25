#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# create a list for the periods, this is the "x" axis
labels = ["1", "2", "3", "5", "6"]

# create list of the socres that you want to plot
boyscores = [32, 67, 90, 100, 92]
girlscores = [40, 74, 90, 92, 100]

# %%
width = 0.3

plt.figure(figsize=(10,5))
plt.title('Boys and Girls Scores By Period')
plt.xlabel('Periods')
plt.ylabel('Score')

y_pos = np.arange(len(labels))
plt.xticks(y_pos+0.15, labels)

plt.bar(y_pos, boyscores, width=width, label='boys', color='green', align='center')
plt.bar(y_pos+width, girlscores, width=width, label='girls', color='blue', align='center')

plt.legend(loc='best')
plt.show

# %%
! curl -O https://raw.githubusercontent.com/linuxacademy/content-using-pythons-maths-science-and-engineering-libraries/master/hdi_master.csv

# %%
df = pd.read_csv('hdi_master.csv')

# %%
year_of_interest = 2010

df_year_of_interest = df[df['year']==year_of_interest]
missing_values = df['HDI for year'].isnull()
hdi = df_year_of_interest['HDI for year'][~missing_values]

# %%
plt.figure(figsize=(15, 5))
plt.hist(hdi, facecolor='orange', alpha=0.5)

plt.axvline(hdi.mean(), color='b', linestyle='solid', linewidth=2, label='mean')
plt.axvline(hdi.mean() + hdi.std(), color='b', linestyle='dashed', linewidth=2, label='+1 standard deviation')
plt.axvline(hdi.mean() - hdi.std(), color='b', linestyle='dashed', linewidth=2, label='-1 standard deviation')

plt.title(f'HDI for {year_of_interest}')
plt.xlabel('HDI value')
plt.ylabel('count of specific HDI values')
plt.legend(loc='upper left')
plt.show()

# %%
# create a datafram for male and female
df_male = df[df['sex']=='male'].copy()
df_female = df[df['sex']=='female'].copy()

# Comparison on same graph
suicides_by_male = df_male['suicides/100k pop'].groupby(df['year']).mean().reset_index()
suicides_by_female = df_female['suicides/100k pop'].groupby(df['year']).mean().reset_index()

# %%
plt.figure(figsize=(15, 5))
plt.plot(suicides_by_male['year'], suicides_by_male['suicides/100k pop'], color='red', alpha=0.5, label='male')
plt.plot(suicides_by_female['year'], suicides_by_female['suicides/100k pop'], color='blue', alpha=0.5, label='female')

plt.title(f'Male and Female Suicide Rates')
plt.xlabel('year')
plt.xticks(rotation=90)
plt.ylabel('suicides/100k pop')
plt.legend(loc='best')
plt.show()

# %%
suicides_by_male = df_male['suicides/100k pop'].groupby(df['year']).mean().reset_index()
suicides_by_female = df_female['suicides/100k pop'].groupby(df['year']).mean().reset_index()


plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.plot(suicides_by_male['year'], suicides_by_male['suicides/100k pop'], color='red', alpha=0.5, label='male')
plt.title(f'Male Suicide Rates')
plt.xlabel('year')
plt.xticks(rotation=90)
plt.ylabel('suicides/100k pop')
plt.ylim([0, 30])

plt.subplot(1,2,2)
plt.plot(suicides_by_female['year'], suicides_by_female['suicides/100k pop'], color='blue', alpha=0.5, label='female')
plt.title(f'Female Suicide Rates')
plt.xlabel('year')
plt.xticks(rotation=90)
plt.ylabel('suicides/100k pop')
plt.ylim([0, 30])

plt.show()

# %%
uicides_by_male = df_male['suicides/100k pop'].groupby(df['year']).mean().reset_index()
suicides_by_female = df_female['suicides/100k pop'].groupby(df['year']).mean().reset_index()


plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.scatter(suicides_by_male['year'], suicides_by_male['suicides/100k pop'], color='red', alpha=0.5, label='male')
plt.title(f'Male Suicide Rates')
plt.xlabel('year')
plt.xticks(rotation=90)
plt.ylabel('suicides/100k pop')
plt.ylim([0, 30])

plt.subplot(1,2,2)
plt.scatter(suicides_by_female['year'], suicides_by_female['suicides/100k pop'], color='blue', alpha=0.5, label='female')
plt.title(f'Female Suicide Rates')
plt.xlabel('year')
plt.xticks(rotation=90)
plt.ylabel('suicides/100k pop')
plt.ylim([0, 30])

plt.show()
# %%
