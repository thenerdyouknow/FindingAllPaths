# Recursive DFS

Given an input.txt with the following format,

```
Guwahati-Dharmanagar-10
Guwahati-Agartala-30
Dharmanagar-Udaipur-20
Dharmanagar-Agartala-15
Agartala-Udaipur-8

```
where the last value is the distance between the two cities.

And given two cities, find all paths from source city to destination city. Write these paths to another file output.txt, in ascending order of
total distance between the cities in the same format.

So if someone were to choose source city to be 'Guwahati' and destination city to be 'Udaipur', the sample output should look something like this:

```
Guwahati-Dharmanagar-Udaipur-30
Guwahati-Dharmanagar-Agartala-Udaipur-33
Guwahati-Agartala-Udaipur-38

```

Some notes:

1. Since the algorithm is recursive, having paths that are too long will probably not work very well.
2. The paths are assumed to be unidirectional. That means, 'Guwahati' to 'Dharmanagar' != 'Dharmanagar' to 'Guwahati'.

Program written using Python3.

More documentation is mentioned inside the .py file.