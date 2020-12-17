import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import numpy as np
import cv2
import random
from numpy.random import randint
from time import sleep

'''
class QNetwork(nn.Module):
    def __init__(self, obs_size, action_size):
        super(QNetwork, self).__init__()
        self.lstm = nn.LSTM(5000, 100)
        self.fc1 = nn.Linear(100, action_size)

    def forward(self, x):
        x = x.reshape(x.size(0), -1)
        out, _ = self.lstm(x.view(len(x), 1, -1))
        out = self.fc1(out.view(len(x), -1))
        return out
'''

class QNetwork(nn.Module):
    def __init__(self, obs_size, action_size):
        super(QNetwork, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 1, kernel_size=10, stride=10, padding=0),
            nn.ReLU())
        self.layer2 = nn.Sequential(
            nn.Conv2d(1, 1, kernel_size=10, stride=10, padding=0),
            nn.ReLU())
        self.layer3 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=4, stride=2, padding=0),
            nn.ReLU())
        self.layer4 = nn.Sequential(
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=0),
            nn.ReLU())
        self.drop_out = nn.Dropout()
        #self.lstm = torch.nn.LSTM(120, 0, 2)
        self.fc1 = nn.Linear(40, action_size, nn.ReLU())
        self.fc2 = nn.Linear(30, action_size, nn.ReLU())

    def forward(self, x):
        #out = cv2.resize(out, dsize=(8, 5), interpolation=cv2.INTER_CUBIC)
        out = self.layer1(x)
        out = self.layer2(out)
        #out = self.layer3(out)
        #out = self.layer4(out)
        out = out.reshape(out.size(0), -1)
        #out = self.drop_out(out)
        #out, _ = self.lstm(out.view(len(out), 1, -1))
        #out = self.fc1(out.view(len(x), -1))
        out = self.fc1(out)
        #out = self.fc2(out)
        return out