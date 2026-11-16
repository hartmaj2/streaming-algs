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

## Communication complexity

- for function $f$ we define its deterministic communication complexity $D(f)$ as the minimum cost over all protocols $\Pi$ that compute $f$

## Protocol types

- deterministic protocols
- private-coin randomized protocols
  - the player computes message to send by combining their fragment with a random coin toss which only they can see
- public-coin randomized protocols
  - infinite random string that both players see and can refer to its bits

## Randomized protocol

- cost - worst case over all inputs and ALL POSSIBILITIES OF RANDOM STRING
- $\Pi$ computes $f$ with error $\delta$
  - $\forall x,y \in X \times Y : \Pr[\text{out}^{\Pi}(x,y,R) \neq f(x,y)] \leq \delta$
- $R_\delta(f)$ ... minimum worst case cost over all protocols $\Pi$ which compute $f$ with error at most $\delta$

- using the median trick from Unit 2 - we can define $R(f) = R_{1/3}(f)$
  - since if we have constant error, we can use the Chernoff bound and parallel run of the algorithm to get the error below any positive constant

- $D^k(f)$ and $R^k(f)$ are communication complexities for $k$-round protocols (convention - Alice starts)

# Canonical communication games

- EQUALITY
  - goal is to check whether Alice and Bob have same strings or not
- INDEX
  - goal is to find the value (0 or 1) inside Alice's string at index given by Bob's number
- SET-DISJOINTNESS
  - check if Alice's and Bob's strings are disjoint when viewed as characteristic vectors

## Proofs (Deterministic)

### One way index bound

- we define $X = \{0,1\}^N$ Alice's possible words
- alice sends possible messages $\mathcal{M}$
  - computes the message using function $m : X \to \mathcal{M}$
- by correctness of a protocol $\Pi$ we have $\text{out}^\Pi(m(x),y)=x_y$
  - we can use this to calculate $x = (\text{out}(m(x),1),\ldots,\text{out}(m(x),n))$
  - so we can recover the original message using the function $r : \mathcal{M} \to X$ defined as $r(m) = (\text{out}(m,1),\ldots,\text{out}(m,n))$
- so $r$ is inverse of $m$ and thus $m$ is a bijection so $|\mathcal{M}| = |X| = 2^N$
- now if we had a protocol which requires to send only at most $N-1$ bits what would that mean?
  - elements of $\mathcal{M}$ can be strings of zeroes and ones of length at most $N-1$ so $|\mathcal{M}| \leq 2^1 + \ldots + 2^{N-1} = 2^N-2$ which is a contradiction

### Core ideas

- show that we can recover the original $x$ that produced the message $m$ (based on Alice's message function)
- notice, that this tells us, that there is same number of messages as there are possible inputs for Alice
- show a contradiction if we assume protocol has cost $\leq N -1$
  - beause the cost is linked to the size of the set of all possible messages that Alice can send

## Proofs (Randomized)

- TODO

## How it connects to data streaming

- in streaming algs, we have an algorithm $\mathcal{A}$ which processes stream $\sigma$ and uses $S$ bits of memory

- to get a communication game, we split the stream $\sigma$ in $t$ segments arbitrarily and imagine $t$ players
  - the segment $\sigma_i$ can be thought of as the input to the function that the players are trying to compute together

- the players are then communicating together in order to reproduce the correct answer as by $\mathcal{A}$

- we can see that we can use the existence of the algorithm to construct a protocol
  - the players just make the algorithm run on their $\sigma_i$ and then send the state of the memory (at most $S$ bits) to the next player
  - for $t$ players and $p$ rounds, the communication complexity of the protocol is $(tp-1)S$

- in general, we suppose that such algorithm $\mathcal{A}$ exists and that it uses only $S$ memory to achieve something
  - now the players get a communication complexity problem
  - then they create a stream corresponding to their problem, run alg $\mathcal{A}$ on the stream and send the $S$ bits to the next player who continues running $\mathcal{A}$ on his part of the stream which he constructs in order for it, to tell him something about the result, they need to compute