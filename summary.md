### Project Design

The design of this project was straight-forward:

1) acquire data, 
2) get board state at move k, 
3) generate training data for:
   A) policy network (train: board state at move k, test: board state at move k+1) and 
   B) value network (train: board state at move k, test: winner), 
4) compose CNN architecture,
5) train / iterate


Acquiring data was easy. Generating a board state was more complicated, mostly because I needed to figure out a robust-enough method to remove a stone from a board once dead -- I used a floodfill algorithm for this. The main issue was account for seki and complicated life and death patterns here. The data also needed to be cleaned up a bit for my requirements -- some games were handicap games, others had "pass moves" added in at the end, so my train/test pairs for the policy network were identical (read: useless), and a few games had only a couple moves, which took longer to diagnose than account for. These were the main hurdles. Composing a CNN structure was reasonable (similar to the MNIST handwriting example), and iterating was reasonable once I had a GPU set up.


### Tools

I didn't use any exciting tools for this project. I managed to set up the architecture to get a Go engine to log into KGS and challenge other computers in the Computer Go room, but this was premature given that I wasn't able to finish building my own bot (missing MCTS), so this was for naught.


### Data

I used the JGDP database, which had ~500k games in raw SGF format. Find it here: https://pjreddie.com/projects/jgdb/


### Algorithms

I wrote utility code to convert raw SGF files into a usable format. I wrote a floodfill algorithm to remove dead stones from a board as I was playing out the moves (the more robust solution would've been implementing a union-find algorithm). I also composed a CNN architecture for both my value and policy networks.


### What I'd do differently next time

I'm glad I got to focus on an interesting project with plenty of room to learn. It was humbling. I wish I hadn't wasted so much time setting up that Go bot to play on KGS, because I could've used that time to work on modeling and getting closer to building a model / engine which could play instead. I feel less regretful, but still slightly so, for wasting as much time as I did figuring out the GPU setup. This was a good learning experience though.
