import pandas as pd
class univariate():
    def quanqual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset:
            if(dataset[columnName].dtypes=='O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual
    def descriptive(dataset,quan):                                                
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Variance","Standard Deviation","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5*IQR","Lower_Outlier","Upper_Outlier","Min","Max","Skew","Kurtosis"],columns=quan)
        for columnName in quan:
            descriptive.loc["Mean",columnName]=dataset[columnName].mean()
            descriptive.loc["Median",columnName]=dataset[columnName].median()
            descriptive.loc["Mode",columnName]=dataset[columnName].mode()[0]
            descriptive.loc["Variance",columnName]=dataset[columnName].var()
            descriptive.loc["Standard Deviation",columnName]=dataset[columnName].std()
            descriptive.loc["Q1:25%",columnName]=dataset.describe()[columnName]["25%"]
            descriptive.loc["Q2:50%",columnName]=dataset.describe()[columnName]["50%"]
            descriptive.loc["Q3:75%",columnName]=dataset.describe()[columnName]["75%"]
            descriptive.loc["Q4:100%",columnName]=dataset.describe()[columnName]["max"]
            descriptive.loc["IQR",columnName]=descriptive.loc["Q3:75%",columnName]-descriptive.loc["Q1:25%",columnName]
            descriptive.loc["1.5*IQR",columnName]=1.5*descriptive.loc["IQR",columnName]
            descriptive.loc["Lower_Outlier",columnName]=descriptive.loc["Q1:25%",columnName]-descriptive.loc["1.5*IQR",columnName]
            descriptive.loc["Upper_Outlier",columnName]=descriptive.loc["Q3:75%",columnName]+descriptive.loc["1.5*IQR",columnName]
            descriptive.loc["Min",columnName]=dataset[columnName].min()
            descriptive.loc["Max",columnName]=dataset[columnName].max()
            descriptive.loc["Skew",columnName]=dataset[columnName].skew()
            descriptive.loc["Kurtosis",columnName]=dataset[columnName].kurtosis()
        return descriptive
    def findingoutliers(quan,descriptive):
        lower=[]
        upper=[]
        for columnName in quan:
            if(descriptive.loc["Min",columnName]<descriptive.loc["Lower_Outlier",columnName]):
                lower.append(columnName)
            if(descriptive.loc["Max",columnName]>descriptive.loc["Upper_Outlier",columnName]):
                upper.append(columnName)
        return lower,upper
    def replacingoutliers(lower,upper,descriptive,dataset):
        for columnName in lower:
            dataset.loc[dataset[columnName]<descriptive.loc["Lower_Outlier",columnName],columnName]=descriptive.loc["Lower_Outlier",columnName]
        for columnName in upper:
            dataset.loc[dataset[columnName]>descriptive.loc["Upper_Outlier",columnName],columnName]=descriptive.loc["Upper_Outlier",columnName]
        return dataset
    def frequency(columnName,dataset):
        FreqTable=pd.DataFrame(columns=["Unique_Value","Frequency","Cumulative_Frequency","Relative_Frequency","Cumulative_Relative_Frequency"])
        FreqTable["Unique_Value"]=dataset[columnName].value_counts().index
        FreqTable["Frequency"]=dataset[columnName].value_counts().values
        FreqTable["Cumulative_Frequency"]=FreqTable["Frequency"].cumsum()
        FreqTable["Relative_Frequency"]=(FreqTable["Frequency"]/len(dataset[columnName].value_counts()))
        FreqTable["Cumulative_Relative_Frequency"]=FreqTable["Relative_Frequency"].cumsum()
        return FreqTable