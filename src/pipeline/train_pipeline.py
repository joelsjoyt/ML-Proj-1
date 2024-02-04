from src.components.data_ingesion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging

data_ingestion = DataIngestion()
train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
logging.info("Data ingestion completed...")

data_transformation = DataTransformation()
train_array, test_array, preporcessor_file_path = data_transformation(train_data_path, test_data_path)
logging.info("Data transformation completed...")

model_trainer = ModelTrainer()
trained_best_model = model_trainer.initate_model_trainer(train_array, test_array)
logging.info("Model training completed...")