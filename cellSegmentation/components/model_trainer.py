import os,sys
import yaml
from cellSegmentation.utils.main_utils import read_yaml_file
from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
from cellSegmentation.entity.config_entity import ModelTrainerConfig
from cellSegmentation.entity.artifacts_entity import ModelTrainerArtifact



# class ModelTrainer:
#     def __init__(
#         self,
#         model_trainer_config: ModelTrainerConfig,
#     ):
#         self.model_trainer_config = model_trainer_config


    

#     def initiate_model_trainer(self,) -> ModelTrainerArtifact:
#         logging.info("Entered initiate_model_trainer method of ModelTrainer class")

#         try:
#             logging.info("Unzipping data")
#             os.system("unzip data.zip")
#             os.system("rm data.zip")
           
#             os.system(f"yolo task=segment mode=train model={self.model_trainer_config.weight_name} data=data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true")


#             os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
#             os.system(f"cp runs/segment/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
           
#             os.system("rm -rf yolov8s-seg.pt")
#             os.system("rm -rf train")
#             os.system("rm -rf valid")
#             os.system("rm -rf test")
#             os.system("rm -rf data.yaml")
#             os.system("rm -rf runs")

#             model_trainer_artifact = ModelTrainerArtifact(
#                 trained_model_file_path="artifacts/model_trainer/best.pt",
#             )

#             logging.info("Exited initiate_model_trainer method of ModelTrainer class")
#             logging.info(f"Model trainer artifact: {model_trainer_artifact}")

#             return model_trainer_artifact


#         except Exception as e:
#             raise AppException(e, sys)

import logging
import zipfile
import shutil


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def unzip_file(self, source_file: str, dest_dir: str):
        with zipfile.ZipFile(source_file, 'r') as zip_ref:
            zip_ref.extractall(dest_dir)

    def remove_file(self, file_path: str):
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

    def copy_file(self, src: str, dest: str):
        shutil.copy(src, dest)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            self.unzip_file('data.zip', '.')
            self.remove_file('data.zip')

            os.system(f"yolo task=segment mode=train model={self.model_trainer_config.weight_name} data=data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true")

            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            self.copy_file('runs/segment/train/weights/best.pt', f"{self.model_trainer_config.model_trainer_dir}/best.pt")

            self.remove_file('yolov8s-seg.pt')
            self.remove_file('train')
            self.remove_file('valid')
            self.remove_file('test')
            self.remove_file('data.yaml')
            self.remove_file('runs')

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=f"{self.model_trainer_config.model_trainer_dir}/best.pt"
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise AppException(e, sys)