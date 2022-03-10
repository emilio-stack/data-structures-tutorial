# Queues

Queues are everywhere in everyday life! 
Here are some examples:
* The line at the store
* A customer service queue
* Your music playlist
* The order of turns in a game of Uno

## Efficiency
The overall efficiency of a queue is 

## Basic Structure
Queues are a first in first out structure meaning 
that the first entitiy to enter the queue is also the first to exit.
Depending on the type of queue there can be some exceptions to this rule.
See an example of an implementation of a <a href="basic.py">Basic Queue</a>

## Types of Queues
### Priority
One exception to the basic queue structure is the Priority Queue.
In a priority queue the entity with the highest priority exits first, not necessarily the first entity to
enter.
This is to say that if entity 1 in the queue has a lower priority than entity 2, then entity 2 will exit the queue before entity 1. 
A good example of this kind of queue is a customer service call center where different needs have different priorities.

### Turns
Another variation to the basic queue structure is the turn queue where entities take turns in the queue. 
The entity that exits first is the one with the least number of turns and the entity that exits last is the
one with the most number of turns.
A good example of this kind of queue is a game of Uno where the number of cards in your hand is the number of turns you have left. The goal is to exit the queue first by getting rid of your number of turns.
See an example of an implementation of a <a href="basic.py">Turns Queue</a>
