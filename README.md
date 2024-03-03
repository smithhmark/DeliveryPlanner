# Introduction
DeliveryPlanner takes a CSV file of coordinates pairs that represents the origin and destination of shipments and uses it to compute an estimate of the minimal delivery cost to move all the shipments in a period.

# Goal And Approach
The initial goal of this project is to demonstrate clean, professional coding. Therefore I am not making a serious attempt at producing a highly performant general solution to the Pickup Drop Off Vehicle Routing Problem.

To address the VRP I am using the heuristic that the overall cost is minimized by minimizing the number of drivers. Therefore I am using a greedy algorithm to iteratively find the best route for a driver of the remaining loads to be shipped. In this case, "best" means that they are handling the most shipments first, and secondarily traversing the lowest distance.

Greedily finding the "best" route for a driver, then repeating for the next driver seems like it might miss a globally optimal solution. Also, the greedy method is not able to result much work from prior runs, so runtime is probably not great eatier.

## Approaches discarded
- building a constraint solver. This would be super fun, but would be a lot of work and be very difficult.
- using a genetic algorithm. This would also be very fun, but identifying a functional genetic encoding that would allow for crossover would be very challenging in the time allotted.
- using an iterative relaxation approach. By starting with assigning a single driver to each shipment, then merging routes to eliminate drivers we can build up an ever more cost efficient solution. Could probably use something like simulated annealling to select the merges. This might sill not find the globably optimal assignment of routes, but should do. (this was kind of my first idea as I started thinking of this as a Dynamic Programming problem and the merging reuses previous work)
- use someone else's solution. fast, probably easy. Discarded for being unethicaland no fun.
- use an open source library. In a professional setting this is what I would do. Spending a few days to learn how to use the library and delivering a decent solution nearly immediately is clearly the right approach. If the results aren't what are needed, having a working solution in hand should allow us to pursue other options.

# Resources consulted
- [https://towardsdatascience.com/the-vehicle-routing-problem-exact-and-heuristic-solutions-c411c0f4d734] provides a fairly complete solution in Python and therefore feels like cheating
- [https://vrpy.readthedocs.io/en/latest/] is a python library for solving VRP problems. Again, this seems like cheating
- Wikipedia has a background article, but since the point of this isn't to build a constraint solver from scratch, isn't super useful.





