import torch
import random
import numpy as np
from snake_game import SnakeGameAI,Direction,Point
from collections import deque

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001