# conatains all the code that is related to reading thed data 

import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


from src.components.data_transformation import DataTransformation , DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv') ## used to store the all the training data in this folder
    test_data_path: str = os.path.join('artifacts', 'test.csv') ## used to store the all the testing data in this folder
    raw_data_path: str = os.path.join('artifacts', 'raw.csv') ## used to store the all the raw data in this folder
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  # three paths will get saved inside this particular class variables 
    
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component.")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Exported the dataset as dataframe.")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            # if the folder exist and keep it otherwise create it 
            
            # saving the raw data here
            df.to_csv(self.ingestion_config.raw_data_path, index= False, header= True)
            
            
            logging.info("Train Test split is initiated.")
            train_set , test_set = train_test_split(df, test_size= 0.2, random_state= 42)
            
            # let's save the train and test data file
            train_set.to_csv(self.ingestion_config.train_data_path, index= False, header= True)
            test_set.to_csv(self.ingestion_config.test_data_path, index= False, header= True)
            logging.info("Ingestion of the data is completed.")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
            
            
             
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":  
    obj = DataIngestion()     # this will sucessfully create a folder containing the train, test and raw file.
    train_data , test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    # data_transformation.initiate_data_transformation(train_data, test_data)
    
    # changing this after the model trainer file is completed 
    train_arr , test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
    
    
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))

    
