import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
df= pd.read_csv("vine.csv")
df.columns
isinstance(df["fixed acidity"],(pd.core.series.Series,np.ndarray))

class StandardScaler2:
    def __init__(self):
        self.data = None

    def fit(self,data_to_fit):
        if isinstance(data_to_fit,(pd.core.series.Series,np.ndarray))==True:
          self.data_to_fit=data_to_fit
          self.mean = np.mean(self.data_to_fit)
          self.std = np.std(self.data_to_fit)
          self.params_ = {"Mean" : self.mean, "Std" : self.std}
          return self.mean, self.std, self.params_

        elif isinstance(data_to_fit,pd.DataFrame)==True:
          self.data_to_fit=data_to_fit
          self.means = []
          self.stds = []
          self.params_ = {}
          for column in data_to_fit.columns:
            self.means.append(np.mean(data_to_fit[column]))
            self.stds.append(np.std(data_to_fit[column]))
            self.params_[column] = {"Mean" : np.mean(data_to_fit[column]), "Std":np.std(data_to_fit[column])}
          return self.means, self.stds, self.params_
        else:
          print("Error, StandardScaler.fit only accepts numpy array or dataframe as inputs")

    def transform(self,data_to_transform):
        if isinstance(data_to_transform,(pd.core.series.Series,np.ndarray))==True:
          try:
            return (data_to_transform-self.mean)/self.std
          except AttributeError:
            print("Can't transform since scaler hasn't been fitted yet!")
        
        elif isinstance(data_to_transform,pd.DataFrame)==True:
          try:
            df_scaled = pd.DataFrame()
            for index in range(len(data_to_transform.columns)):
              df_scaled[data_to_transform.columns[index]] = (data_to_transform.iloc[:,index]-self.means[index])/self.stds[index]
            return df_scaled
          except AttributeError:
            print("Can't transform since scaler hasn't been fitted yet!")

    def fit_transform(self, data_to_fit_transform):
        self.fit(data_to_fit_transform)
        return self.transform(data_to_fit_transform)

df2 = df[["fixed acidity", "volatile acidity"]]
# sc2 = StandardScaler2()
# print(sc2.fit_transform(df2))
# print(sc2.params_)

sc = StandardScaler()
print(sc.fit_transform(df2))