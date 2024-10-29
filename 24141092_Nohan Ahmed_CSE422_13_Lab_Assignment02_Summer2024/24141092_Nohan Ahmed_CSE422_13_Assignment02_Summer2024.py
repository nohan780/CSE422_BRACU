inputs = open("24141092_Nohan Ahmed_CSE422_13_Assignment02_Summer2024_inputFile.txt", "r")
outputs = open("24141092_Nohan Ahmed_CSE422_13_Assignment02_Summer2024_outputFile.txt", "a")
l1 = list((inputs.readline().split()))
n = int(l1[0])
t = int(l1[1])
courses = []
for i in range(int(n)):
  l1 = inputs.readline().split()
  courses.append(l1[0])

#task1

import random

def parent_selection(population, fitness_values):
  total_fit = sum(fitness_values)
  probs = []
  for i in fitness_values:
    probs.append(i/total_fit)
  parents = random.choices(population, weights=probs, k=2)
  return parents


def mutation(chromosome, mutation_rate):
  m = list(chromosome)
  for i in range(len(m)):
    if random.random() < mutation_rate:
      if m[i] != "0":
        m[i] = "0"
      else:
        m[i] = "0"
  return "".join(m)


def crossing(first_parent, second_parent):
  point = random.randint(1, len(first_parent) - 1)
  first = first_parent[:point] + second_parent[point:]
  second = second_parent[:point] + first_parent[point:]
  return first, second


def fitness_check(chromosome, n, t):
  p_overlap = 0
  p_consistency = 0

  for i in range(t):
    timeslot = chromosome[i * n:(i + 1) * n]
    overlap = timeslot.count("1")
    if overlap > 1:
       p_overlap += overlap - 1

  for i in range(n):
    count = 0
    for j in range(t):
      if chromosome[i * n + j] == "1":
        count += 1
    if count != 1:
      p_consistency += abs(count - 1)

  total_penalty = p_overlap + p_consistency
  return -total_penalty


def population_making(pop_size, n, t):
  population = []
  for i in range(pop_size):
    chromosome = ""
    for j in range(n * t):
      chromosome += random.choice(["0", "1"])
    population.append(chromosome)
  return population


def the_genetic_algo(n, t, pop_size = 10, max_generations = 10, mutation_rate = 0.01):
  population = population_making(pop_size, n, t)
  the_solution = None
  the_fitness = float("-inf")
  for generation in range(max_generations):
    fitness_values = []
    for chromosome in population:
      fitness_values.append(fitness_check(chromosome, n, t))

    for chromosome, fit_val in zip(population, fitness_values):
      if fit_val > the_fitness:
        the_fitness = fit_val
        the_solution = chromosome

    new_population = []
    while len(new_population) < pop_size:
      first_parent, second_parent = parent_selection(population, fitness_values)
      first, second = crossing(first_parent, second_parent)
      new_population.extend([mutation(first, mutation_rate), mutation(second, mutation_rate)])

    population = new_population[:pop_size]
  return the_solution, the_fitness




the_solution, the_fitness = the_genetic_algo(n, t)

outputs.write("one pointer:\n")
outputs.write(f"{the_solution}\n")
outputs.write(f"{the_fitness}\n")





#task2

def two_point_crossing(first_parent, second_parent):
  first_pointer = random.randint(1, len(first_parent) - 2)
  second_pointer = random.randint(first_pointer + 1, len(first_parent) - 1)
  first_child = first_parent[:first_pointer] + second_parent[first_pointer:second_pointer] + first_parent[second_pointer:]
  second_child = second_parent[:first_pointer] + first_parent[first_pointer:second_pointer] + second_parent[second_pointer:]

  return first_child, second_child

def the_genetic_algo_2_point(n, t, pop_size = 10, max_generations = 10, mutation_rate = 0.01):
  population = population_making(pop_size, n, t)
  the_solution = None
  the_fitness = float("-inf")
  for generation in range(max_generations):
    fitness_values = []
    for chromosome in population:
      fitness_values.append(fitness_check(chromosome, n, t))

    for chromosome, fit_val in zip(population, fitness_values):
      if fit_val > the_fitness:
        the_fitness = fit_val
        the_solution = chromosome

    new_population = []
    while len(new_population) < pop_size:
      first_parent, second_parent = parent_selection(population, fitness_values)
      first, second = two_point_crossing(first_parent, second_parent)
      new_population.extend([mutation(first, mutation_rate), mutation(second, mutation_rate)])

    population = new_population[:pop_size]
  return the_solution, the_fitness


the_solution_two, the_fitness_of_two = the_genetic_algo_2_point(n, t)

outputs.write("Two pointer:\n")
outputs.write(f"{the_solution_two}\n")
outputs.write(f"{the_fitness_of_two}\n")