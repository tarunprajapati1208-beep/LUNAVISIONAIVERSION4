import numpy as np
import heapq

# A* Autonomous Rover Navigation System
# Lead Architect: Bhaumik Nandha

class RoverPathPlanner:
    def __init__(self):
        pass

    def heuristic(self, a, b):
        """
        Manhattan distance metric for precise grid movement approximation.
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def plan_path(self, start, goal, hazard_map):
        """
        A* Heuristic Search Algorithm.
        Routes the rover from the landing zone to the ice deposit while strictly avoiding hazards.
        """
        # All 8 possible directional vectors (horizontal, vertical, diagonal)
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        close_set = set()
        came_from = {}
        gscore = {start: 0}
        fscore = {start: self.heuristic(start, goal)}
        oheap = []
        heapq.heappush(oheap, (fscore[start], start))
        
        while oheap:
            current = heapq.heappop(oheap)[1]
            
            # If target reached, reconstruct the path trace
            if current == goal:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                data.append(start)
                return data[::-1] # Reverse to get Start -> Goal order
                
            close_set.add(current)
            
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                
                # Dynamic Grid Bounds Checking
                if 0 <= neighbor[0] < hazard_map.shape[1]:
                    if 0 <= neighbor[1] < hazard_map.shape[0]:
                        # Hazard Enforcement: 1 = Obstacle, Skip this node
                        if hazard_map[neighbor[1]][neighbor[0]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue
                    
                tentative_g_score = gscore[current] + self.heuristic(current, neighbor)
                
                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue
                    
                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(oheap, (fscore[neighbor], neighbor))
                    
        # Return False if rover is completely blocked by hazards
        return False