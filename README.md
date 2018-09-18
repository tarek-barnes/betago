In code directory:
generate_policy_states.py -- Takes raw games as input and generates a pickle file which is a list of training examples for the policy network.
generate_value_states.py -- Takes raw games as input and generates a pickle file which is a list of training examples for the value network.
get_game_record.py -- Takes a raw Go game file and extract useful information from it (list of moves, winner).
get_game_state.py -- Takes a game record and generates game states for training. This includes a floodfill algorithm to remove dead stones.
partition_training_data.py -- Takes a large pickle file and splits it into partitions (since my training data was consuming absurd amounts of RAM).

In models directory:
policy_model.py -- Policy network take 1 (not good results).
policy_model2.py -- Policy network take 2 (ok results).
value_model.py -- Value network, same structure as policy_model2.
policy_hyperparam_tuning_results.txt -- Brief network stints to establish hyperparamaters.
