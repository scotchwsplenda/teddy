import pandas as pd 



url = 'https://www.pro-football-reference.com/teams/sea/2021.htm'
table = pd.read_html(url, match='Game Results Table')
df = table[0]
print(df.index)
scores = df.iloc[:, 10:12]

scores.columns = scores.columns.to_flat_index()
scores.columns=(['Tm', 'Opp'])
scores['Diffy']  =scores['Tm']-scores['Opp']
print(scores)

    # merge actual and predited spreads
    # dd = get_df_panda().reset_index(drop = True)
    # dd = dd.loc[:16,['Title','Differenchy']]
    # df_predictions = pd.read_sql('SELECT * FROM vPredicted_Score_Dif', sqlite3.connect('db.sqlite3'))
    # df_predictions = df_predictions.T
    # new_header = df_predictions.iloc[0] #grab the first row for the header
    # df_predictions = df_predictions[1:] #take the data less the header row
    # df_predictions.columns = new_header #set the header row as the df header
    # df_predictions = df_predictions.reset_index(drop = True)
    # bigdata = pd.merge(dd, df_predictions, left_index=True, right_index=True)
    # bigdata = bigdata.fillna(0)
    # bigdata['Differenchy'] = bigdata['Differenchy'].astype(int)
    # bigdata = bigdata.rename(columns={'Differenchy' : 'Actual Spread'})
    # bigdatahtml = bigdata.to_html(classes="table table-striped table-bordered table-hover", index=False)
    # # show accuracy of predictions
    # dumb=[]
    # for index, row in bigdata.iterrows():
    #     zz = np.where((row[1] * row[2:]) > 0, (row[1] - row[2:]).abs(), None).tolist()
    #     zz.insert(0,row[1]) 
    #     zz.insert(0,row[0])
    #     dumb.append(zz)
    # dumb = np.array(dumb)
    # df_accurate_wl = pd.DataFrame(dumb, columns=bigdata.columns.to_list()).fillna('X')
    # df_accurate_wlhtml = df_accurate_wl.style.applymap(highlight_max).hide_index().set_table_attributes('border="1" class="dataframe table table-hover table-bordered table-striped"').render()
    # # prediction grade
    # df_accurate_wl_funk = df_accurate_wl
    # cut_conditions = [-1, 0, 3.5, 7.5, 10.5, 14.5, 21.5,22]
    # cut_scores =     [    1, .95,  .9,  .85,   .8, .75, 0]
    # df_predictions_accuracy = pd.DataFrame()
    # df_predictions_accuracy['name'] = df_accurate_wl.iloc[:,0]
    # df_predictions_accuracy['WEEK1'] = pd.cut(df_accurate_wl_funk['WEEK1'],bins = cut_conditions, labels = cut_scores, include_lowest=True, right=True)
    # return render(request, "seahawks_2022_predictions/accuracy.html", {'df_accurate_wl': df_accurate_wlhtml, 'df_predictions': df_predictions.to_html(), 'bigdata' : bigdatahtml })
