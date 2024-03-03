# Introduction
DeliveryPlanner takes a CSV file of coordinates pairs that represents the origin and destination of shipments and uses it to compute an estimate of the minimal delivery cost to move all the shipments in a period.

# Goal And Approach
The initial goal of this project is to demonstrate clean, professional coding. Therefore I am not making a serious attempt at producing a highly performant general solution to the Pickup Drop Off Vehicle Routing Problem.

To address the VRP I am using the heuristic that the overall cost is minimized by minimizing the number of drivers. Therefore I am using a greedy algorithm to iteratively find the best route for a driver of the remaining loads to be shipped. In this case, "best" means that they are handling the most shipments first, and secondarily traversing the lowest distance.

# Resources consulted
- [https://towardsdatascience.com/the-vehicle-routing-problem-exact-and-heuristic-solutions-c411c0f4d734] provides a fairly complete solution in Python and therefore feels like cheating
- [https://vrpy.readthedocs.io/en/latest/] is a python library for solving VRP problems. Again, this seems like cheating
- Wikipedia has a background article, but since the point of this isn't to build a constraint solver from scratch, isn't super useful.





