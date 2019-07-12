import torch
import numpy as np
import torch.nn as nn
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    
from utils.lstm import PackedLSTM
from utils.attention import ConditionalAttention
from models.agg_predictor import AggPredictor

class OpPredictor(AggPredictor):
    """
    This module is identical to AggPredictor, so we inherit.
    """
    def __init__(self, num=8, *args, **kwargs):
        super(OpPredictor, self).__init__(*args, **kwargs, num=num)
