# semesters required

#notes
# find the longest path. because all others can be done subsequently
# entry point is courses with no prereqs, draw out the graph adajacney list 
# use deafult dict for easier adjancency list creation 


def semesters_required(num_courses, prereqs):
  ## build the graph 
  ## 
  graph = build_graph(num_courses, prereqs)
  distance = {}
  for course in range(num_courses):
    if len(graph[course]) == 0:
      distance[course] = 1
  
  #call recursive on each one 
  for course in range(num_courses):
    traverse_distance(graph, course, distance)

    #finally return the max 
  return max(distance.values())

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
  
  max_distance = 0

  #save max distance of each node, 
  for neighbor in graph[node]:
    neighbor_distance = traverse_distance(graph, neighbor, distance)
    if neighbor_distance > max_distance:
      max_distance = neighbor_distance
    
  distance[node] = 1 + max_distance
  return distance[node]

def build_graph(num_courses, prereqs):
  graph = {}
  
  for course in range(num_courses):
    graph[course] = []
    
  for prereq in prereqs:
    a, b = prereq
    graph[a].append(b)
  
  return graph