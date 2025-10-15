
from src.data_processing import DataProcessing
from src.model_training import ModelTraining


if __name__ == "__main__":
    data_processor = DataProcessing(file_path="artifacts/raw/data.csv")
    data_processor.run()

    trainer = ModelTraining()
    trainer.run()

    

