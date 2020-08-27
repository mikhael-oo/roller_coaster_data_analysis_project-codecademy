import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
# this loads the wood roller coaster
gd_tk_w = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')

# this loads the steel roller coaster
gd_tk_s = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

print(gd_tk_w.head(5))
print(gd_tk_s.head(5))


# write function to plot rankings over time for 1 roller coaster here:
def plot_ranking(name, df, park):
    rankings = df.loc[(df.Name == name) & (df.Park == park)]
    plt.plot(range(len(rankings)), rankings['Rank'], 'go--')
    ax = plt.subplot()
    ax.set_xticks(range(len(rankings)))
    ax.set_xticklabels(['2013', '2014', '2015', '2016', '2017', '2018'])
    ax.invert_yaxis()
    plt.axis([-1, 6, 5, 0])
    plt.xlabel('Ranking', fontsize=18)
    plt.ylabel('Year', fontsize=18)
    plt.title(name + ' Rankings', fontsize=18)
    plt.show()


plot_ranking('El Toro', gd_tk_w, 'Six Flags Great Adventure')

plt.clf()


# write function to plot rankings over time for 2 roller coasters here:
def comp_rankings(name1, name2, df, park1, park2):
    rankings1 = df.loc[(df.Name == name1) & (df.Park == park1)]
    rankings2 = df.loc[(df.Name == name2) & (df.Park == park2)]
    plt.plot(range(len(rankings1)), rankings1['Rank'], color='blue', marker='o')
    plt.plot(range(len(rankings2)), rankings2['Rank'], color='red', marker='o')
    ax1 = plt.subplot()
    ax1.set_xticks(range(len(rankings1)))
    ax1.set_xticklabels(['2013', '2014', '2015', '2016', '2017', '2018'])
    ax1.invert_yaxis()
    plt.axis([-1, 6, 5, 0])
    plt.xlabel('Ranking', fontsize=18)
    plt.ylabel('Year', fontsize=18)
    plt.title(name1 + ' vs ' + name2, fontsize=18)
    plt.show()


comp_rankings('El Toro', 'Boulder Dash', gd_tk_w, 'Six Flags Great Adventure', 'Lake Compounce')

plt.clf()


# write function to plot top n rankings over time here:
def top_rankings(n, df):
    rankings = df.loc[(df.Rank <= n)]
    ax = plt.subplot()
    for c in set(rankings.Name):
        indiv_rank = rankings[(rankings.Name == c)]
        ax.plot(indiv_rank['Year of Rank'], indiv_rank.Rank, label=c, )

    ax.invert_yaxis()

    plt.title('Ranking of the top ' + str(n) + ' coasters', fontsize=18)
    plt.xlabel('Year', fontsize=15)
    plt.ylabel('Rank', fontsize=15)
    plt.legend(loc='right', bbox_to_anchor=(1.05, 1))
    plt.show()


top_rankings(5, gd_tk_w)

plt.clf()

# load roller coaster data here:
rc_dt = pd.read_csv('roller_coasters.csv')
print(rc_dt.head(5))


# write function to plot histogram of column values here:

def col_hist(df, name):
    if name == 'height':
        heights = df[df['height'] <= 140]
        value = heights[name].dropna()
    else:
        value = df[name].dropna()

    plt.hist(value, bins=40)
    plt.title("Histogram of Roller Coaster's " + name[0].upper() + name[1:], fontsize=16)
    plt.ylabel('Count', fontsize=14)
    plt.xlabel(name[0].upper() + name[1:], fontsize=14)


plt.figure(figsize=(10, 8))
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.subplot(2, 2, 1)
col_hist(rc_dt, 'speed')
plt.subplot(2, 2, 2)
col_hist(rc_dt, 'height')
plt.subplot(2, 2, 3)
col_hist(rc_dt, 'length')
plt.subplot(2, 2, 4)
col_hist(rc_dt, 'num_inversions')

plt.show()

plt.clf()


# write function to plot inversions by coaster at a park here:
def inv_bar(df, park):
    park_coasters = df[df.park == park].sort_values('num_inversions', ascending=False)
    names = park_coasters.name
    inversions = park_coasters.num_inversions

    ax = plt.subplot()
    plt.bar(range(len(inversions)), inversions)
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=90, fontsize=13)
    plt.title('Number of Inversions per Coaster at ' + park, fontsize=16)
    plt.xlabel('Roller Coaster', fontsize=14)
    plt.ylabel('Number of Inverions', fontsize=14)


inv_bar(rc_dt, 'Six Flags Great Adventure')
plt.show()

plt.clf()


# write function to plot pie chart of operating status here:
def comp_pie(df):
    operating = df[df.status == 'status.operating']
    closed = df[df.status == 'status.closed.definitely']
    status_counts = [len(operating), len(closed)]
    plt.pie(status_counts, labels=['Still_Open', 'Closed'], autopct='%0.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title('Open Roller Coasters v Closed Roller Coasters', fontsize=18)
    plt.show()


comp_pie(rc_dt)

plt.clf()


# write function to create scatter plot of any two numeric columns here:
def scatter_compare(df, col1, col2):
    if col1 != 'height' and col2 != 'height':
        first = df[col1]
        second = df[col2]
    else:
        df = df[df.height < 140]
        first = df[col1]
        second = df[col2]
    plt.scatter(first, second)
    plt.title('Scatter Plot Comparing ' + col1[0].upper() + col1[1:] + ' and ' + col2[0].upper() + col2[1:],
              fontsize=18)
    plt.xlabel(col1[0].upper() + col1[1:], fontsize=14)
    plt.ylabel(col2[0].upper() + col2[1:], fontsize=14)
    plt.show()


scatter_compare(rc_dt, 'speed', 'height')

plt.clf()