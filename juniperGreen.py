
import gym
from gym import spaces
from gym.utils.env_checker import check_env
import numpy as np
import random
from tqdm import tqdm
from bucket_env import plot_stats


class JuniperGreenEnv(gym.Env):
    def __init__(self, Nmax=100):
        self.Nmax = Nmax
        self.action_space = gym.spaces.Discrete(self.Nmax + 1)
        #define the observation space with a array of unknown size
        self.observation_space = gym.spaces.Box(low=0, high=self.Nmax, shape=(1,), dtype=np.int32)
        self.current_number = np.random.randint(self.Nmax) + 1
        self.played_numbers = []
        self.reset()

    def reset(self):
        self.current_number = np.random.randint(self.Nmax) + 1
        self.played_numbers = []
        return np.array([self.current_number])

    def isValidAction(self, action):
        return (self.current_number % action == 0 or action % self.current_number == 0) and action not in self.played_numbers

    def step(self, action):
        #Player 1
        if (self.isValidAction(action)):
            self.played_numbers.add(action)
            self.current_number = action
            reward = 1
            done = False
        else:
            reward = 0
            done = True

        #Player 2 with random action
        if not done:
            action = np.random.randint(self.Nmax) + 1
            if (self.isValidAction(action)):
                self.played_numbers.add(action)
                self.current_number = action
                reward = 1
                done = False
            else:
                reward = 0
                done = True


        return np.array([self.current_number]), reward, done, {}
  

    def render(self, mode='human', close=False):
        print("Current number: ", self.current_number)
        print("Current player: ", self.player)


env=JuniperGreenEnv()
check_env(env)
env.reset()
tab = [1,9,11]

done = False
while(not done):
    _, _, done, _ = env.step(np.random.randint(100) + 1)

print("Game over")


