#notes start
# this is an exhaustive recurison question
# because youre testing all of the possible paths
# why storing in dict? allows for updating 
#terminal nodes dont point to any others - 



# the for loop checks how much deeper each node goes, if a child has depth, add it to the count of the parent in memo
 
# longest path
def longest_path(graph):
  distance = {}
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 0
      
  for node in graph:
    traverse_distance(graph, node, distance)
    
  return max(distance.values())

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]
  
  largest = 0
  for neighbor in graph[node]:
    attempt = traverse_distance(graph, neighbor, distance)
    if attempt > largest:
      largest = attempt
  
  distance[node] = 1 + largest
  return distance[node]