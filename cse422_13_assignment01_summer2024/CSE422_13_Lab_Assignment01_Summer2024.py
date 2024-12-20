from collections import deque

inputs = open("Input file.txt", "r")
outputs = open("output.txt", "a")
all_paths = {}
h = {}
for i in range(20):
    l1 = list((inputs.readline().split()))
    j = 0
    while j < len(l1):
        if j == 0:
            h[l1[j]] = int(l1[j + 1])
            all_paths[l1[j]] = []
            j += 2
        else:
            all_paths[l1[0]].append((l1[j], int(l1[j + 1])))
            j += 2
                


class start:
    def __init__(self, all_paths, h):
        self.hu = h
        self.all_paths = all_paths

 
    def h(self, n):
        Heu = self.hu
        return Heu[n]

    
    def neighbor_city(self, v):
        return self.all_paths[v]


    
    def the_algo(self, strt, stp):

        opened_l = set([strt])
        closed_l = set([])


        cur_dis = {}

        cur_dis[strt] = 0


        parents = {}
        
        parents[strt] = strt

        while len(opened_l) > 0:
            n = None

   
            for v in opened_l:
                if n == None or cur_dis[v] + self.h(v) < cur_dis[n] + self.h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

  
            if n == stp:
                final_paths = []

                while parents[n] != n:
                    final_paths.append(n)
                    n = parents[n]

                final_paths.append(strt)

                final_paths.reverse()

                sum = 0
                x = 0
                
                while x < (len(final_paths) - 1):
                    for y,z in self.all_paths.items():
                        if y == final_paths[x]:
                            for a,b in z:
                                
                                if a == final_paths[x+1]:
                                    sum += b
                                    x += 1
                                    break
                            break
                the_path = "Paths: "
                for i in final_paths:
                    if i != final_paths[-1]:
                        the_path = the_path + i + " -> "
                    else:
                        the_path = the_path + i

                outputs.write(f"{the_path}\nTotal distance: {sum} km\n\n")
                    
                return final_paths

    
            for (m, weight) in self.neighbor_city(n):
       
                if m not in opened_l and m not in closed_l:
                    opened_l.add(m)
                    parents[m] = n
                    cur_dis[m] = cur_dis[n] + weight

                else:
                    if cur_dis[m] > cur_dis[n] + weight:
                        cur_dis[m] = cur_dis[n] + weight
                        parents[m] = n

                        if m in closed_l:
                            closed_l.remove(m)
                            opened_l.add(m)

            opened_l.remove(n)
            closed_l.add(n)

        outputs.write("Path does not exist!")
        return None


start1 = start(all_paths,h)
st = input("Start Node: ")
des = input("Dest Node: ")
start1.the_algo(st,des)