import pandas as pd
from scipy import stats

class Detector:
    threshold = int(input('Enter the threshold value '))
    def __init__(self):
        self.column = list(pd.read_csv('Intern_data.csv').columns[1:].values)
        self.Data_header=['Cyclone_Inlet_Gas_Temp.csv','Cyclone_Material_Temp.csv','Cyclone_Outlet_Gas_draft.csv','Cyclone_cone_draft.csv','Cyclone_Gas_Outlet_Temp.csv','Cyclone_Inlet_Draft.csv']

    def Methodolody(self):
        try:
            iter=0
            Global_series={}
            while iter<=5:

                data_set=pd.read_csv(self.Data_header[iter],dtype={self.column[iter]:float})
                data_set.drop(columns='Unnamed: 0',axis=1,inplace=True)
                data_set['year'] = [elem.split('/')[2][:4] for elem in data_set[data_set.columns.values[0]]]
                years=['2017','2018','2019','2020']

                series=[]
                for yrs in years:
                    data_set[self.column[iter]+'_scaled']=abs(stats.zscore(data_set[self.column[iter]].to_numpy())) # Applying zscore analysis (Data has been scaled)
                    year_wise_split=data_set[data_set['year']==yrs].index
                    series.append(data_set.loc[year_wise_split,['time',self.column[iter],self.column[iter]+'_scaled','year']])
                Global_series[self.column[iter]]=series
                iter+=1
            return Global_series

        except Exception as e:
            print(e)

    def Abnormality(self):
        try:
            Feature_series=(self.Methodolody().keys())
            abnormality=[]
            for key in Feature_series:
                Data_frame=self.Methodolody()[key]
                for series in Data_frame:
                    for elem in pd.DataFrame(series)[key+'_scaled'].index:
                        if pd.DataFrame(series).loc[elem,key+'_scaled'] > self.threshold:
                            abnormality.append(pd.DataFrame(series).loc[elem,['time',key]])
            return abnormality


        except Exception as e:
            print(e)
    def Output(self):
        with open('Abnormality_thresh{}.txt'.format(self.threshold),'w') as f:
            f.write(str(self.Abnormality()))
