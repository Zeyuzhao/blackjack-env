import gym
from gym import error, spaces, utils
from gym.utils import seeding

class BlackjackLite(gym.Env):
    cards = [(i + 1) for i in range(13)]

    """
    A simple implementation of Blackjack: Deck with unlimited cards.

    The objective of the game is beat the dealer closer to 21 without going over.
    Cards between 2 - 10 inclusive are worth pip value; J, Q, and K are worth 10.
    The Ace could be worth 1 or 11, the holder of the card determines the value.

    The rewards are:

    -1 if the player loses
    0 if its a stand
    1 if the player wins

    The actions at each stage are either hit or stand.
    Hit retrieves an additional card, while stand terminates the move.

    """

    # metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Discrete()

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pass

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    @staticmethod
    def getScore(deck):
        score = 0
        ace = False
        for card in deck:
            if card <= 10:
                if card == 1:
                    ace = True
                score += card
            else:
                score += 10
        if score >= 21:
            return None
        if ace and score <= 11:
            score += 10
        return score

    @staticmethod
    def isBlackJack(deck):
        return 1 in deck and len(deck) == 2






