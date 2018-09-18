### Project Design

The design of this project was pretty straight-forward: 1) acquire data, 2) get board state at move k, 3) generate training data for policy network (train: board state at move k, test: board state at move k+1) and value network (train: board state at move k, test: winner), 4) compose CNN architecture, 5) train / iterate.

Acquiring data was easy. Generating a board state was a little complicated, mostly because I needed to figure out how to remove a stone from a board once it was dead. The data also needed to be cleaned up a bit -- some games were handicap games, others had "pass moves" added in at the end, so my train/test pairs for the policy network were identical, and a few games only had a couple moves, which took me forever to diagnose. That was the main hurdle. Composing a CNN was reasonable (similar to the MNIST handwriting example), and iterating was reasonable once I had a GPU set up properly.


### Tools

I didn't really use any exciting tools for this project. I did manage to set up the architecture to get a Go bot to log into KGS and challenge other computers in the Computer Go room, but this was premature given that I wasn't able to finish building my own bot (missing MCTS), so this was for naught.


### Data

I used the JGDP database, which had ~500k raw games in SGF format. Find them here: https://pjreddie.com/projects/jgdb/


### Algorithms

I wrote some "filler code" to get the raw SGF files into a usable format. Nothing difficult. I did write a floodfill algorithm to remove dead stones from a board as I was playing out the moves, which is something reasonably easy I had to figure out (the more robust solution would've been implementing a union-find algorithm). I also composed a CNN for both my value and policy networks.


### What I'd do differently next time

I'm glad I got to focus on an interesting project with plenty of room to learn. I wish I hadn't wasted so much time setting up that Go bot to play on KGS, because I could've used that time to work on modeling and getting closer to building a model / engine which could play instead. I feel less regretful, but still slightly so, for wasting as much time as I did figuring out the GPU setup -- at first, I assumed the GPU would be automatically detected, and then once I realized that wasn't the case, I spent _much_ too long trying to get it to work. This was a good learning experience, though.