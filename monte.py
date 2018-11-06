
# This is a the first and most simple function related to implementing
# the Monte Carlo algorithm within the GYM Blackjack environment.

import gym
env = gym.make('Blackjack-v0')

print(env.observation_space)
print(env.action_space)
print(env.action_space.n)

for i_episode in range(100):

    state = env.reset()
    while True:
        print(state)
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        print(state, reward, done, info, action)
        if done:
            print('End game! Reward: ', reward)
            if reward > 0:
                print('You won :)\n')
            elif reward < 0:
                print('You lost :(\n')
            else:
                print('Draw')
            break

def generate_episode_from_limit(bj_env):
    episode = []
    state = bj_env.reset()
    while True:
        action = 0 if state[0] > 18 else 1
        next_state, reward, done, info = bj_env.step(action)
        episode.append((state, action, reward))
        state = next_state
        if done:
            break
    return episode

    for i in range(3):
        print(generate_episode_from_limit(env))
