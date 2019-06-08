from collections import defaultdict
import sys

#Assumptions:
#1. The paths aren't too large. This is because I'm using recursion to find all the paths (would ideally write an iterative algorithm 
#   but was pressed for time).
#2. The paths mentioned in input.txt are unidirectional. This is assumed because in practice, 
#   the path from a source city to a destination city is not always the same as a path from the destination city to the source city.
#3  The input.txt is completely valid and contains no errors. Didn't have enough time to add validation for the input.txt.


#README:
# Input and Output file will have to be in the same folder as the program.
# Program written in Python3.

INPUT_FILENAME = 'input.txt'
OUTPUT_FILENAME = 'output.txt'


class DFS:

    def __init__(self,vertices):
        '''
        init():
        Initializes the class by setting number of vertices and initializing an empty defaultdict for our graph.
        Returns nothing.
        '''
        self.number_of_vertices = vertices
        self.graph = defaultdict(dict)

    def add_edge(self,information_list):
        '''
        add_edge():
        Adds an edge to the 'graph' by appending to the dictionary item of the source city.
        Returns nothing.
        '''
        self.graph[information_list[0]][information_list[1]] = information_list[-1]

    def calculate_paths(self,source,destination,visited,path,all_paths):
        '''
        calculate_paths():
        Recursively uses DFS to calculate every possible path from source to destination. When a path is found, it's formatted properly and 
        appended to a list containing all paths. 
        Returns list of all possible paths.
        '''
        visited[source] = True
        path.append(source)

        if source == destination:
            path_str = []
            for each_city in path:
                path_str.append(each_city)
            path_str.append(str(self.calculate_distance(path)))
            all_paths.append(path_str)
        else:
            for each_city in self.graph[source]:
                if visited[each_city] == False:
                    self.calculate_paths(each_city, destination, visited, path,all_paths)
        path.pop() 
        visited[source]= False
        return all_paths

    def calculate_distance(self,path):
        '''
        calculate_distance():
        Given a path, finds the distance from the source to the destination using self.graph. Since self.graph is a dictionary,
        lookup is quick. 
        Returns distance from source to destination in given path.
        '''
        total_distance = 0
        for i in range(0,len(path)-1):
            total_distance += self.graph[path[i]][path[i+1]]
        return total_distance

    def sort_paths(self,paths):
        '''
        sort_paths():
        Given a list of lists that contains all paths and total distances, sorts the list of lists by the total distances.
        Returns nothing.
        '''
        paths.sort(key= lambda x: int(x[-1]))
        return paths

    def find_all_paths(self,source,destination,visited):
        '''
        find_all_paths():
        Driver function that calls other functions in the class to calculate all paths and sort them according to distance. Writes
        final output to OUTPUT_FILENAME appropriately.
        Returns nothing.
        '''
        path = []
        all_paths = []
        all_paths = self.calculate_paths(source, destination, visited, path,all_paths)
        if(len(all_paths)==0):
            print('No paths found!')
            return

        sorted_paths = self.sort_paths(all_paths)
        with open(OUTPUT_FILENAME,'w') as open_file:
            for each_element in sorted_paths:
                open_file.write('-'.join(each_element))
                open_file.write('\n')

def read_file(filename):
    '''
    read_file():
    Given a filename, reads the file one line at a time, splits it on the -, strips it of the newline, and then appends it to a list.
    Returns the cleaned input list.
    '''
    cleaned_list = []
    try:
        with open(filename,'r') as open_file:
            file_contents = open_file.readline()
            while file_contents != '':
                split_file_line = file_contents.split("-")
                split_file_line[-1] = int(split_file_line[-1].rstrip('\n')) #Removing newline and converting distance to int
                cleaned_list.append(split_file_line)
                file_contents = open_file.readline()
    except FileNotFoundError:
        print('Input file does not exist. Try again!')
        sys.exit(0)
    return cleaned_list
    
def unique_vertices(graph):
    '''
    unique_vertices():
    Given the graph_information, finds all the unique vertices(in this case, the cities).
    Returns the set of all unique vertices.
    '''
    unique_cities = set()
    for each_element in graph:
        unique_cities.add(each_element[0])
        unique_cities.add(each_element[1])
    return unique_cities

def initialize_visited(unique_cities):
    '''
    initialize_visited():
    Given a set of unique vertices, initializes the visited dictionary that we will use to make sure we don't go in cycles.
    Returns a dictionary of keys being the vertices and all the values being False.
    '''
    return dict.fromkeys(unique_cities, False) 


graph_information= read_file(INPUT_FILENAME)

#Basic checks
if(len(graph_information)==0):
    print('Input.txt is empty. Please enter some data.')
    sys.exit(0)

all_vertices = unique_vertices(graph_information)
number_of_vertices = len(all_vertices)
visited_dict = initialize_visited(all_vertices)

new_graph = DFS(number_of_vertices)
for each_vertex in graph_information:
    new_graph.add_edge(each_vertex)

source_city = input('Enter a source city : ').lower().capitalize() #Basic cleaning of input
destination_city = input('Enter a destination city : ').lower().capitalize()


if(source_city in all_vertices and destination_city in all_vertices):
    new_graph.find_all_paths(source_city,destination_city,visited_dict)
else:
    print('One or both the cities you have mentioned are not in the input file. Please try again!')
