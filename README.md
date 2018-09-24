In code directory:

1) generate_policy_states.py -- Take raw games as input and generate a pickle file which is a list of training examples for the policy network.
2) generate_value_states.py -- Take raw games as input and generate a pickle file which is a list of training examples for the value network.
3) get_game_record.py -- Take a raw Go game file (SGF) and extract useful information from it (list of moves, winner).
4) get_game_state.py -- Take a game record and generate game states for training. This includes a floodfill algorithm to remove dead stones.
5) partition_training_data.py -- Take a large pickle file and split it into partitions (since my training data consumes _absurd_ amounts of RAM).

In models directory:

1) policy_model.py -- Policy network take 1 (mediocre results).
2) policy_model2.py -- Policy network take 2 (OK results).
3) value_model.py -- Value network, same structure as policy_model2.
4) policy_hyperparam_tuning_results.txt -- Network policy stints to establish decent hyperparamaters.
