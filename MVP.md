## Domain

For this project, I'd like to simulate AlphaGo. This will be a _very_ simplistic simulation. I know how to play the game, not particularly well. In an ideal world, I'd like to make a bot stronger than myself, or more realistically lay the foundation to get there with enough training. If I can get a functioning bot (i.e. one that generates moves non-randomly), that will be a success (and I suppose satisfy the MVP qualifications).


## Data

I'm not so concerned with finding data for this project. I know of public Go repositories that have tens of thousands of professional games which are publicly accessible. In addition, Damien mentioned a website which takes a board position and provides the most common next move, so that could also be helpful. What I am more concerned about is converting board states to something a neural network can interpret.


## Current plan

I see this as a three-step project:

1) Build the necessary architecture / pipeline. I'm still figuring out exactly what this means. I originally thought I'd use the KGS API and set up a bot that can play with other bots (once it's trained). I have a protocol set up that points to another bot (GnuGo) and has that play on KGS, so it could be possible to point it at my bot once it's built. It seems like this might be finicky though, so I'm leaning towards interacting with a bot via the command line (that's my fallback).

2) Compose two CNNs - one to predict the next best move from a given state (although the website Damien mentioned might provide a convenient shortcut or starting point for this), and another to predict the score / winner based on a given state. I need to first convert a game state into something a CNN can interpret though.

3) Use the data I collect to train my models. Once all this is done, I can ideally have my bot log into KGS and play other bots to continue training. I may need to fall back to utilizing the terminal bot. The problem with the fallback is that GnuGo (the terminal bot) isn't very strong, so I worry about contaminating my training data with fodder. This might be an unavoidable problem for this project, though.


## Known unknowns

My current thought is that this project may quickly become overwhelming. It's something I'm highly interested in though, so I'd least like to try. I'm going to see how far I get by this weekend, and pivot if need be. I'm thinking about alternative projects I can do.

For this weekend, if I can make good progress with the API, have some data in a comprehensible format, and get into composing my first CNN (maybe this is premature), I will take that as a good sign. I'm sure there are plenty of unknown unknowns as well.
