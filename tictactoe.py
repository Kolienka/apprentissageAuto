import gym
from gym import spaces
from gym.utils.env_checker import check_env
import numpy as np
import random
from tqdm import tqdm
from bucket_env import plot_stats

class TicTacToeEnv(gym.Env):
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.player = 1
        
        self.observation_space = gym.spaces.Box(
            low=0, high=2, shape=(3, 3), dtype=np.int32
        )
        self.action_space = gym.spaces.Discrete(9)

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.player = 1
        return self.board

    def step(self, action):
        x, y = action // 3, action % 3
        self.board[x, y] = self.player
        self.player = (self.player % 2) + 1

        if self.is_game_over():
            self.done = True

        reward = self.calculate_reward()

        return self.board, reward, self.done, {}

    def render(self, mode='human'):
        print('-' * 9)
        for row in self.board:
            row_str = '| '
            for cell in row:
                if cell == 0:
                    row_str += '  | '
                elif cell == 1:
                    row_str += 'X | '
                else:
                    row_str += 'O | '
            print(row_str)
            print('-' * 9)

    def is_game_over(self):
        for i in range(3):
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2] and self.board[i, 0] != 0:
                return True
            if self.board[0, i] == self.board[1, i] == self.board[2, i] and self.board[0, i] != 0:
                return True

        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] and self.board[0, 0] != 0:
            return True
        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] and self.board[0, 2] != 0:
            return True

        return False

    def calculate_reward(self):
        if self.done:
            if self.player == 1:
                return -1
            else:
                return 1
        return 0


def random_run(episodes=300):
    print(f'Random run')
    env = TicTacToeEnv()
    stats = {"Rewards" : []}
    for e in range(1, episodes + 1):
        done = False
        total_reward = 0
        state = env.reset()
        while not done:
            action = env.action_space.sample()
            state, reward, done, _ = env.step(action)
            total_reward += reward
            if done:
                #print(f'Got ${total_reward} at the end the month')
                break
            env.close()
        stats['Rewards'].append(total_reward/(30*7))
    return stats






plot_stats(random_run())