import pickle
import pandas as pd

class predObj:
    def pred_log(self , dict_pred):
        with open('modelForPrediction.pickle' , "rb") as f:
            model = pickle.load(f)

        data_df = pd.DataFrame(dict_pred , index=[1,])

        predict = model.predict(data_df)

        if predict[0] == 1:
            result = 'has an affair'
        else:
            result = 'doesnt have an affair'



        return result
