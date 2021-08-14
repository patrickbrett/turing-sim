# turing-sim

Simulating a Turing machine in Python

Work in progress!

## About

Simulating four machines with increasing complexity which can process languages in the four levels of the Chomsky Hierarchy:

1. Finite State Machine / Finite Automaton
2. Pushdown Automaton
3. Linear Bounded Automaton
4. Turing Machine

## Wikipedia version

From [Wikipedia](https://en.wikipedia.org/wiki/Turing_machine):

A Turing machine consists of:

- A tape divided into cells, one next to the other. Each cell contains a symbol from some finite alphabet. The alphabet contains a special blank symbol (here written as '0') and one or more other symbols. The tape is assumed to be arbitrarily extendable to the left and to the right, so that the Turing machine is always supplied with as much tape as it needs for its computation. Cells that have not been written before are assumed to be filled with the blank symbol. In some models the tape has a left end marked with a special symbol; the tape extends or is indefinitely extensible to the right.
- A head that can read and write symbols on the tape and move the tape left and right one (and only one) cell at a time. In some models the head moves and the tape is stationary.
A state register that stores the state of the Turing machine, one of finitely many. Among these is the special start state with which the state register is initialized. These states, writes Turing, replace the "state of mind" a person performing computations would ordinarily be in.
- A finite table of instructions that, given the state(qi) the machine is currently in and the symbol(aj) it is reading on the tape (symbol currently under the head), tells the machine to do the following in sequence (for the 5-tuple models):
1. Either erase or write a symbol (replacing aj with aj1).
2. Move the head (which is described by dk and can have values: 'L' for one step left or 'R' for one step right or 'N' for staying in the same place).
3. Assume the same or a new state as prescribed (go to state qi1).
