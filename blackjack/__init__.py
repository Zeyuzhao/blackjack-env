from gym.envs.registration import register

register(
    id='blackjack-v0',
    entry_point='blackjack.envs:BlackJack',
)