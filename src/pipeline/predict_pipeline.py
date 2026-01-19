# this code is being written here when model have started working and now i am trying to build flask website 
# to predict the results
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object



class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            
            data_scaled = preprocessor.transform(features)
            
            predictions = model.predict(data_scaled)
            
            return predictions
        
        
        except Exception as e:
            raise CustomException(e, sys)
    

# i can also do this in the app.py 
# trying to avoid it so that i can create the file with more understading here.

class CustomData:
    def __init__(
        self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int
    ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_dataframe(self):
        """
        Returns input data as a pandas DataFrame
        compatible with the preprocessing pipeline
        """
        try:
            return pd.DataFrame({
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            })
            
        except Exception as e:
            raise CustomException(e, sys)

        