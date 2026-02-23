import os
import sys

import numpy as np
import pandas as pd
import dill

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logger

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok = True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as ex:
        raise CustomException(ex, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        trained_models = {}

        for model_name, model in models.items():
            param = params.get(model_name, {})

            # CatBoost WITHOUT GridSearchCV
            if model_name == "CatBoosting Regressor":
                logger.info("Training CatBoost without GridSearchCV")
                model.fit(X_train, y_train)
            else:
                gs = GridSearchCV(model, param, cv=3)
                gs.fit(X_train, y_train)

                model.set_params(**gs.best_params_)
                model.fit(X_train, y_train)

            # Predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # R2_Scores
            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_score
            trained_models[model_name] = model

        return report, trained_models

    except Exception as ex:
        raise CustomException(ex, sys)
    
    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as ex:
        raise CustomException(ex, sys)
