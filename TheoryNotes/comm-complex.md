# Communication complexity

- used for showing lower bounds
  - some well defined task cannot be achieved in the streaming model in space better than something

- in our example we will use techique to show lower bound on MAJORITY and FREQUENCY-ESTIMATION  
  - MAJORITY - output j if exists j with more than m/2 occurences (m is length of the stream)
    - (otherwise we output none)
  - FREQUENCY-ESTIMATION - we first read the whole stream
    - then we have to answer queries in form j where we then have to output frequency of j

## Scenario

- two players - Alice and Bob
  - each has a fragments of input to function $f$ which they want to evaluate
- GOAL: compute a function $f : \mathcal{X} \times \mathcal{Y} \to \mathcal{Z}$
  
- the players share information about their fragments by a predetermined protocol
  - the protocol runs in rounds

## Cost of a protocol

- for protocol $\Pi$, it is the maximum number of bits that has to be transferred over all possible inputs (when executing the protocol $\Pi$)

## Protocol types

- deterministic protocols
- private-coin randomized protocols
  - the player computes message to send by combining their fragment with a random coin toss which only they can see
- public-coin randomized protocols
  - infinite random string that both players see and can refer to its bits