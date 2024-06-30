import sys, os
from cellSegmentation.pipeline.training_pipeline import TrainPipeline
from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException


obj = TrainPipeline()
obj.run_pipeline()
print("Training done")
    