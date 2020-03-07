#[[1,1,1,1],
# [0,1,1,0],
# [0,1,0,1],
# [0,1,9,1],
# [1,1,1,1]]

# --------------------------------------------------------------------------------------
# Variables & Constants
# --------------------------------------------------------------------------------------

matrix = [[1,1,1,1], [0,1,1,0], [0,1,0,1], [0,1,9,1], [1,1,1,1]]
size_x = len(matrix)
size_y = len(matrix[0])
visited = []
solutions = []

best_path = -1
position_x = 0
position_y = 0

# --------------------------------------------------------------------------------------
# Functions
# --------------------------------------------------------------------------------------

def build_node(x, y, previous):
  return { 'x': x, 'y': y, 'value': matrix[x][y], 'previous': previous }

def key_value(x, y):
  return str(x) + "-" + str(y), matrix[x][y]

# Explore left
def check_left(node):
    target_x = node["x"]
    target_y = node["y"] - 1

    if target_y > 0:
      return build_node(target_x, target_y, node)
    else:
      return None  

# Explore right
def check_right(node):
    target_x = node["x"]
    target_y = node["y"] + 1

    if target_y < size_y:
      return build_node(target_x, target_y, node)
    else:
      return None

# Explore top
def check_top(node):
    target_x = node["x"] - 1
    target_y = node["y"]

    if target_x > 0:
      return build_node(target_x, target_y, node)
    else:
      return None

# Explore bottom
def check_bottom(node):
    target_x = node["x"] + 1
    target_y = node["y"]

    if target_x < size_x:
      return build_node(target_x, target_y, node)
    else:
      return None

def explore(node):
  nodes = []

  key, value = key_value(node['x'], node['y'])
  if value is 0:
    print("--- Node ", key, " - value = 0")
    return []

  if value is 9:
    print("--- Node ", key, " - value = 9")
    solutions.append(node)
    return []

  if key in visited:
    print("--- Node ", key, " - visited")
    return []

  visited.append(key)

  right = check_right(node)
  if right is not None:
    nodes.append(right)
      
  left = check_left(node)
  if left is not None:
    nodes.append(left)
  
  bottom = check_bottom(node)
  if bottom is not None:
    nodes.append(bottom)

  top = check_top(node)
  if top is not None:
    nodes.append(top)

  keys = ''
  for temp in nodes:
    keys = keys + str(temp['x']) + '-' + str(temp['y']) + ', '
  print("-- Node:", key, ", sub-nodes: [ " + keys + "]")

  return nodes

def explore_nodes(nodes):
  keys = ''
  for temp in nodes:
    keys = keys + str(temp['x']) + '-' + str(temp['y']) + ', '
  print("\n- Explore nodes: [ " + keys + "]")

  new_nodes = []
  for node in nodes:
    if len(solutions) == 0:
      sub_nodes = explore(node)
      new_nodes.extend(sub_nodes)
  
  if len(new_nodes) != 0:
    explore_nodes(new_nodes)

# --------------------------------------------------------------------------------------
#  Execution
# --------------------------------------------------------------------------------------      

for row in matrix:
    print(row)

print("\n - \n")

position = matrix[position_x][position_y]
print("Initial position:", position)

print("")

root = build_node(0, 0, None)
nodes = [root]
explore_nodes(nodes)

print("\nResult: ")

for solution in solutions:
  path = ' '
  while solution['previous'] is not None:
    path = " -> " + str(solution['x']) + "," + str(solution['y']) + path 
    solution = solution['previous']
  print('0,0' + path)
