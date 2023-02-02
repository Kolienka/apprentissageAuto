
import gym
from gym import spaces
from gym.utils.env_checker import check_env
import numpy as np
import random
from tqdm import tqdm
from bucket_env import plot_stats

class NimEnv(gym.Env):
    def __init__(self):
        self.player = 1
        self.state = 13
        self.done = False
        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = gym.spaces.Discrete(13)

    def reset(self):
        self.player = 1
        self.state = 13
        self.done = False
        return int(self.state)

    def step(self, action):
        self.player = (self.player % 2) + 1
        self.state -= action + 1
        if self.state == 0:
            self.done = True
        return self.state, self.calculate_reward(), self.done, {}

    def render(self, mode='human'):
        print(self.state)

    def calculate_reward(self):
        if self.done:
            return 1
        else:
            return 0

env = NimEnv()
check_env(env)