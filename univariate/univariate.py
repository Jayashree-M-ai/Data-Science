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
            