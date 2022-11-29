import pandas as pd

csv = "CRM_data_copy.csv"

df = pd.read_csv(csv)

def count_missings() :
    print(df.count()/df.shape[0] * 100)

count_missings()

def count_uniques() :

    for i in df :
        print(f"------------------{i}------------------")
        print(df[i].nunique())
        print(df[i].unique())

#count_uniques()

def str_to_date() :
    df['Subscribe date'] = pd.to_datetime(df['Subscribe date'])
    df['Lost date'] = pd.to_datetime(df['Lost date'])
    #print(df)
    #print(type(df['Subscribe date'][0]))
    #print(type(df['Lost date'][1]))

str_to_date()

def new_column() :

    def from_stagename(x) :
        if x == "Gagné" :
            return 1
        else :
            return 0

    df['Stagename_bin'] = df['Stagename'].apply(from_stagename)

    #print(df)

new_column()

def dummies_stagename() :

    tdf = pd.get_dummies(df['Stagename_bin'])
    df['Stagename_gagne'] = tdf[0]
    df['Stagename_perdu'] = tdf[1]
    #print(df)

dummies_stagename()

#7
def count_win() :
    print(df)
    print(sum(df['Stagename_bin']))

#count_win()

#8
def dummies_project() :

    tdf = pd.get_dummies(df['Project type'])
    df['primary_residence_count'],df['rental_investment_count'],df['secondary_residence_count'] = tdf['primary_residence'],tdf['rental_investment'],tdf['secondary_residence']

dummies_project()

#9

df = df.rename(columns={'Lost reason':'Lost_reason','Source of lead':'Source_of_lead'})



#10

#df = df.groupby(['Source_of_lead'])['Amount'].sum()

#11
df['saucisse'] = df['Stagename_perdu'] + df['Stagename_gagne']

#12
df = df.drop(['saucisse'], axis=1)

#13
df['Lost_reason'] = df['Lost_reason'].str.replace('/','-')

#14
#df['Property kind'] = df['Property kind'].str.replace('Nan','other')
df['Property kind'] = df['Property kind'].fillna('other')

#QUESTIONS

#1
tdf = df.copy()
tdf['Subscribe date'] = tdf['Subscribe date'].apply(lambda x : str(x)[:7])
tdf = tdf.groupby(['Subscribe date'])['Amount'].mean()
#print(tdf)

#2
tdf_2 = df.copy()
#tdf['Subscribe date'] = df['Subscribe date'].apply(lambda x : str(x)[:7])
tdf_2 = tdf_2.groupby(['Subscribe date'])['Amount'].mean()

print(df)
print("===========================")
print(tdf_2)
#print(df)
