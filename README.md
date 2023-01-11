# ghw-sort

This program, written in Python, implements the Merge Sort algorithm to sort an input list. This divide-and-conquer sorting method is *very powerful*, with a run-time complexity of O(nlog(n)).

This implementation of merge sort uses one list to serve as a space for the sorting to occur in several recursive steps. Hence, it uses up less space than if it were to create a new sorted list in each step. The program nonetheless creates two partitions of the original list in each recursive stack, thus there are still space limitations that can be enhanced.
