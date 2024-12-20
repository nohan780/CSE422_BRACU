inputs = open("24141092_Nohan Ahmed_CSE422_13_Assignment03_Summer2024_inputFile.txt", "r")
l1 = list((inputs.readline().split()))
n = int(l1[0])
l1 = list((inputs.readline().split()))
t = int(l1[0])



#task1
print("Task:1")
import random

class the_game_tree:
  def __init__(self, depth, player, maimum_depth, value = None):
    self.depth = depth
    self.player = player
    self.maximum_depth = maimum_depth
    self.value = value
    self.child = []

  def make_tree(self):
    if self.depth < self.maximum_depth:
      for j in range(2):
        next_player = 1 - self.player
        child = the_game_tree(self.depth + 1, next_player, self.maximum_depth)
        self.child.append(child)
        child.make_tree()

  def set_leaf_value(self, value):
    self.value = value

def get_tree_leaves(node):
  if not node.child:
    return [node]
  all_leaves = []
  for k in node.child:
    leaves_from_child = get_tree_leaves(k)
    for l in leaves_from_child:
      all_leaves.append(l)
  return all_leaves



def alpha_beta_pruning(node, alpha, beta, check):
  if node.depth == node.maximum_depth or not node.child:
     return node.value

  if check == True:
    max_evaluation = float('-inf')
    for x in node.child:
      evaluation = alpha_beta_pruning(x, alpha, beta, False)
      if evaluation is not None:
        max_evaluation = max(max_evaluation, evaluation)
        alpha = max(alpha, evaluation)
      if beta <= alpha:
        break
    return max_evaluation
  else:
    min_evaluation = float('inf')
    for y in node.child:
      evaluation = alpha_beta_pruning(y, alpha, beta, True)
      if evaluation is not None:
        min_evaluation = min(min_evaluation, evaluation)
        beta = min(beta, evaluation)
      if beta <= alpha:
        break
    return min_evaluation




def mortal_kombat_game(start_player):
  maximum_depth = 5
  total_rounds = 3
  every_round_results = []

  for i in range(total_rounds):
    main = the_game_tree(0, start_player, maximum_depth)
    main.make_tree()
    leaves = get_tree_leaves(main)
    num = len(leaves)
    leaf_values = []
    for m in range(num):
      leaf_values.append(random.choice([-1, 1]))
    for i in range(num):
      leaves[i].set_leaf_value(leaf_values[i])

    round_winner_value = alpha_beta_pruning(main, float('-inf'), float('inf'), start_player == 0)
    if round_winner_value == -1:
      round_winner = "Scorpion"
    else:
      round_winner = "Sub-Zero"
    every_round_results.append(round_winner)
    start_player = 1 - start_player
  scorpion_wins = every_round_results.count("Scorpion")
  sub_zero_wins = every_round_results.count("Sub-Zero")
  if scorpion_wins > sub_zero_wins:
    game_winner = "Scorpion"
  else:
    game_winner = "Sub-Zero"
  print(f"Game Winner: {game_winner}")
  print(f"Total Rounds Played: {total_rounds}")
  for i in range(len(every_round_results)):
    winner = every_round_results[i]
    print(f"Winner of Round {i + 1}: {winner}")



mortal_kombat_game(n)










#task2
print("\n")
print("Task:2")
def the_pacman_game(cost):
  leaf_values = [3, 6, 2, 3, 7, 1, 2, 0]


  final = minimax(0, 0, True, leaf_values, float('-inf'), float('inf'))

  left_with_dark_magic = leaf_values[1] - cost
  right_with_dark_magic = leaf_values[4] - cost
  best_with_dark_magic = max(left_with_dark_magic, right_with_dark_magic)
  if best_with_dark_magic > final:
    if left_with_dark_magic> right_with_dark_magic:
      print(f"The new minimax value is {best_with_dark_magic}. Pacman goes left and uses dark magic")
    else:
      print(f"The new minimax value is {best_with_dark_magic}. Pacman goes right and uses dark magic")
  else:
    print(f"The minimax value is {final}. Pacman does not use dark magic")

def minimax(depth, index, check, leaf_values, alpha, beta):
  if depth == 3:
    return leaf_values[index]
  if check == True:
    max_evaluation = float('-inf')
    for i in range(2):
      evaluation = minimax(depth + 1, index * 2 + i, False, leaf_values, alpha, beta)
      if evaluation is not None:
        max_evaluation = max(max_evaluation, evaluation)
        alpha = max(alpha, evaluation)
      if beta <= alpha:
        break
    return max_evaluation
  else:
    min_evaluation = float('inf')
    for i in range(2):
      evaluation = minimax(depth + 1, index * 2 + i, True, leaf_values, alpha, beta)
      if evaluation is not None:
        min_evaluation = min(min_evaluation, evaluation)
        beta = min(beta, evaluation)
      if beta <= alpha:
        break
    return min_evaluation

the_pacman_game(t)