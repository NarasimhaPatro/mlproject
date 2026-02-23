from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging
from src.exception import CustomException
import sys

class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            logging.info("Training pipeline started")

            # Step 1: Data Ingestion
            data_ingestion = DataIngestion()
            train_path, test_path = data_ingestion.initiate_data_ingestion()

            # Step 2: Data Transformation
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = (
                data_transformation.initiate_data_transformation(
                    train_path, test_path
                )
            )

            # Step 3: Model Training
            model_trainer = ModelTrainer()
            model_trainer.initiate_model_trainer(
                train_arr, test_arr
            )

            logging.info("Training pipeline completed successfully")

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    TrainPipeline().run_pipeline()