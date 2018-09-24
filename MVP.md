## Domain

For this project, I'd like to a replication study of Google DeepMind's AlphaGo. This will be a _very_ simplistic replication, given that my timeframe is less than three weeks. I know how to play the game, but not particularly well. Eventually, I'd like to make a bot stronger than myself, or more realistically lay the foundation to get there with enough training -- time is the likely bottleneck. If I can get a functioning bot (i.e. one that generates moves non-randomly), that will be good enough.


## Data

There are many datasets for a project of this nature. I know of public Go repositories that have tens of thousands of professional games which are publicly accessible. In addition, there are websites which provide a heuristic which spits out a winner or next move based on a current board state - for purposes of comparison.


## Current plan

I see this as a three-step project:

1) Build the necessary architecture / pipeline. I'm still figuring out exactly what this means. My original thought was to use the KGS API to set up a bot that can play with other bots (once trained). I have a protocol set up that points to another engine (GnuGo) which plays on KGS, so my goal is to point it at my bot once built. This might be finicky though, so my fallback for now involves interacting with a bot via the command line.

2) Compose two CNNs: a policy network to predict the next best move from a given state, and a value network to predict the score / winner based on a given state.

3) Use the data I collect to train my models. Once all this is done, I can hopefully have my bot log into KGS and play other bots to continue training. The problem with the fallback option is that GnuGo (the terminal bot) isn't very strong, so I worry about contaminating my training data with fodder. This might be an unavoidable problem for this project, given that I have less than three weeks.


## Known unknowns

My current thought is that this project may quickly become overwhelming and time prohibitive; in other words, I don't have millions of dollars lying around on my dresser for training. It's something I'm interested in though, so I'd at least like to try. I'm going to see how far I get in five days, and pivot if need be.

For this weekend, if I can make substantial progress with the API, have some data in a comprehensible format, and get into composing my first CNN (perhaps premature), I'll take that as a sign from the go gods.
