# CM-DQN: A Value-Based Deep Reinforcement Learning Model to Simulate Confirmation Bias
## NYU DS-GA 1016 Computational Cognitive Modelling Final Project
In human decision-making tasks, individuals learn through trials and prediction errors. When individuals learn the task, some are more influenced by good outcomes, while others weigh bad outcomes more heavily. Such confirmation bias can lead to different learning effects. In this study, we propose a new algorithm in Deep Reinforcement Learning, CM-DQN, which applies the idea of varying update strategies for positive or negative prediction errors, to simulate the human decision-making process when the task's states are continuous while the actions are discrete. We test CM-DQN in a Lunar Lander environment with confirmatory, disconfirmatory, and non-biased bias to observe the learning effects. Moreover, we apply the confirmation model in a multi-armed bandit problem (environment in discrete states and discrete actions), which utilizes the same idea as our proposed algorithm, as a contrast experiment to algorithmically simulate the impact of different confirmation biases in the decision-making process. In both experiments, confirmatory bias indicates better learning effects.


## How to start
fork the repo by
```
git clone https://github.com/Patrickhshs/CM-DQN
```
change the root path and run the experiment files like the following way:
```
python ccm_comfirmation_bias_rl.py
```
Below is the result running on seed 2024:

![image](https://github.com/Patrickhshs/CM-DQN/assets/103577592/8e73d1aa-39f3-4ebd-9027-26658f122229)
## Contributor
- Jiacheng Shen (shen.patrick.jiacheng@nyu.edu)
- Lihan Feng (lf2383@nyu.edu)
## If you used our work or code, please cite us in your work by 
```
@misc{shen2024cmdqnvaluebaseddeepreinforcement,
      title={CM-DQN: A Value-Based Deep Reinforcement Learning Model to Simulate Confirmation Bias}, 
      author={Jiacheng Shen and Lihan Feng},
      year={2024},
      eprint={2407.07454},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2407.07454}, 
}
```
