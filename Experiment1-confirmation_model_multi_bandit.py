
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import random
import math
import seaborn as sns

def softmax(values, temperature):
    exp_values = np.exp(np.array(values) / temperature)
    probabilities = exp_values / sum(exp_values)
    action = np.random.choice([0, 1], p=probabilities)
    return action

def update_value_estimates(values, action, rewards, alpha_confirmatory, alpha_disconfirmatory):
    prediction_errors = rewards - values
    values[action] += alpha_confirmatory * prediction_errors[action]
    values[1 - action] += alpha_disconfirmatory * prediction_errors[1 - action]
    return values

def simulate_confirmation_model(p1, p2, alpha_confirmatory, alpha_disconfirmatory, temperature, trials):
    values = np.zeros(2)  
    total_reward = 0  

    for _ in range(trials):
        action = softmax(values, temperature)  
        reward1 = np.random.binomial(1, p1)  
        reward2 = np.random.binomial(1, p2)  
        rewards = np.array([reward1, reward2])  
        total_reward += rewards[action]  
        values = update_value_estimates(values, action, rewards, alpha_confirmatory, alpha_disconfirmatory)  

    average_reward = total_reward / trials  
    return average_reward

# Environment parameters
p1, p2 = 0.4, 0.6 
alpha_confirmatory = 0.1  
alpha_disconfirmatory = 0.05  
temperature = 0.1  
trials = 1024  

# test the functions
average_reward = simulate_confirmation_model(p1, p2, alpha_confirmatory, alpha_disconfirmatory, temperature, trials)
print(f"Average reward: {average_reward}")

# %%
# Experiment
alpha_C_list = np.linspace(0.05, 0.95, 19)
alpha_D_list = np.linspace(0.05, 0.95, 19)
print(alpha_D_list)
result=[]
for alpha_C in alpha_C_list:
    for alpha_D in alpha_D_list:
        average_reward = simulate_confirmation_model(p1, p2, alpha_C, alpha_D, temperature, trials)
        # print(f"Average reward for alpha_C={alpha_C}, alpha_D={alpha_D}: {average_reward}")
        result.append((alpha_C, alpha_D, average_reward))
df=pd.DataFrame(result, columns=['alpha_C', 'alpha_D', 'reward'])
print(df)
df.to_csv('ex1.csv', index=False)

df=pd.read_csv('ex1.csv')

alpha_D_unique = df['alpha_D'].unique()
alpha_C_unique = df['alpha_C'].unique()
reward_matrix = np.zeros((len(alpha_D_unique), len(alpha_C_unique)))

# 填充矩阵
for i, alpha_D in enumerate(alpha_D_unique):
    for j, alpha_C in enumerate(alpha_C_unique):
        reward_matrix[i, j] = df[(df['alpha_D'] == alpha_D) & (df['alpha_C'] == alpha_C)]['update reward'].values[0]

# 创建热图
plt.figure(figsize=(10, 6))
sns.heatmap(reward_matrix, fmt=".2f", xticklabels=alpha_D_unique, yticklabels=alpha_C_unique, cmap='YlOrBr')

# 显示图形
plt.title('Reward Heatmap for Different alpha_C and alpha_D')
plt.xlabel('alpha_D')
plt.ylabel('alpha_C')
plt.show()


