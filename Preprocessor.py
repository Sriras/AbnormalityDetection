import pandas as pd

class Preprocessing():

    def __init__(self,data_set='Intern_data.csv'):
        self.raw_data=data_set

    def Handling_Unobsevables(self):
        try:
            data_frame=pd.read_csv(self.raw_data)
            Final_series=[]
            removables=[]
            Heading=list(data_frame.columns)[1:]
            for column in data_frame.columns[1:]:
                current_subcolumn=data_frame[column]
                for elem in current_subcolumn:
                    if elem[0].isalpha():
                        removables.append(elem)
                removals=list(pd.Series(removables).unique())
                for items in removals:
                    Unobserved_vals = current_subcolumn[current_subcolumn == items].index
                    current_subcolumn.drop(Unobserved_vals,inplace=True)
                removables=[]
                Final_series.append(data_frame.loc[current_subcolumn.index,['time',column]])
        except Exception as e:
            print(e)
        else:
            index=0
            for series in Final_series:
                pd.DataFrame(series).to_csv(Heading[index]+'.csv')
                index+=1

