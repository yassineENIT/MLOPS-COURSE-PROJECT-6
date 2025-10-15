import joblib
import os 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,precision_score,recall_score,f1_score
import matplotlib.pyplot as plt
import seaborn as sns
from src.logger import get_logger
from src.custom_exception import CustomException
import numpy as np
from src.custom_exception import CustomException

logger=get_logger(__name__) 

class ModelTraining:
    def __init__(self):
        self.processed_data_path="artifacts/processed"
        self.model_path="artifacts/models"
        os.makedirs(self.model_path, exist_ok=True)
        self.model=DecisionTreeClassifier(criterion="gini",max_depth=30,random_state=42)
        logger.info("ModelTraining Initialized")
    def load_data(self):
        try:
            X_train=joblib.load(os.path.join(self.processed_data_path,"X_train.pkl"))
            X_test=joblib.load(os.path.join(self.processed_data_path,"X_test.pkl"))
            y_train=joblib.load(os.path.join(self.processed_data_path,"y_train.pkl"))
            y_test=joblib.load(os.path.join(self.processed_data_path,"y_test.pkl"))
            logger.info("Processed data loaded successfully")
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logger.error(f"Error loading processed data: {e}")
            raise CustomException('Error loading processed data', e)

    
    def train_model(self, X_train, y_train):
        try:
            self.model.fit(X_train, y_train)
            joblib.dump(self.model, os.path.join(self.model_path, "model.pkl"))
            logger.info("Model trained successfully")
        except Exception as e:
            logger.error(f"Error training model: {e}")
            raise CustomException('Error training model', e)
    
    def evaluate_model(self, X_test, y_test):
        try:
            y_pred=self.model.predict(X_test)
            accuracy=accuracy_score(y_test, y_pred)
            precision=precision_score(y_test, y_pred, average='weighted')
            recall=recall_score(y_test, y_pred, average='weighted')
            f1=f1_score(y_test, y_pred, average='weighted')
            logger.info(f"Model Evaluation - Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1-Score: {f1}")
            cm=confusion_matrix(y_test, y_pred)
            plt.figure(figsize=(8,6))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y_test), yticklabels=np.unique(y_test))
            plt.xlabel('Predicted')
            plt.ylabel('Actual')
            plt.title('Confusion Matrix')
            confusion_matrix_path=os.path.join(self.model_path, "confusion_matrix.png")
            plt.savefig(confusion_matrix_path)
            plt.close()
            logger.info(f"Confusion matrix saved at {confusion_matrix_path}")
        except Exception as e:
            logger.error(f"Error evaluating model: {e}")
            raise CustomException('Error evaluating model', e)
        
    def run(self):
        X_train, X_test, y_train, y_test = self.load_data()
        self.train_model(X_train, y_train)
        self.evaluate_model(X_test, y_test)



if __name__ == "__main__":
    trainer = ModelTraining()
    trainer.run()
