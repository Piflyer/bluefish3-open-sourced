from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.grid import Grid
import json, main
from floormatrices import *
from location import roomlocation, stairlocation

totalschedules = json.load(open("wholeschool.json"))

def calc_route(startroom, endroom, period):
    finder = AStarFinder()


    startloc, startfloor = (roomlocation[startroom][0], roomlocation[startroom][1]), roomlocation[startroom][2]
    endloc, endfloor = (roomlocation[endroom][0], roomlocation[endroom][1]), roomlocation[endroom][2]

    # Order floors by name in order
    # Here floorf0 would be 'below' extensione0
    hierarchyext = ['matrixf0', 'matrixe0',]
    # Order floors by name in order without the extensions
    hierarchyreg = ['matrixf0',]

    if startfloor == endfloor:
        grid = Grid(matrix = eval('test.schools[period].' + str(startfloor))['pathfinding'])

        start = grid.node(startloc[0], startloc[1])
        end = grid.node(endloc[0], endloc[1])
        
        route = finder.find_path(start, end, grid)

        return route, startfloor, None, None, None
    
    if startfloor != endfloor:
        gridstart = Grid(matrix = eval('test.schools[period].' + str(startfloor))['pathfinding'])
        gridend = Grid(matrix = eval('test.schools[period].' + str(endfloor))['pathfinding'])
        
        if 'e' in startfloor or 'e' in endfloor:
            possible = [(0, 1), (0, 5)]
        else:
            possible = list(set(stairlocation[startfloor[-2:]]) & set(stairlocation[endfloor[-2:]]))
        
        possibilities = {}
        totals = []
        
        for stairwell in possible:
            if 'e' in startfloor and 'e' not in endfloor:
                startstart = gridstart.node(startloc[0], startloc[1])
                startend = gridend.node(stairwell[0], stairwell[1])

                endstart = gridend.node(stairwell[0] + 8, stairwell[1])
                endend = gridend.node(endloc[0], endloc[1])
            
                routestart = finder.find_path(startstart, startend, gridstart)
                routeend = finder.find_path(endstart, endend, gridend)
            
            elif 'e' in endfloor and 'e' not in startfloor:
                startstart = gridstart.node(stairwell[0], stairwell[1])
                startend = gridstart.node(stairwell[0] + 8, stairwell[1])

                endstart = gridend.node(stairwell[0], stairwell[1])
                endend = gridend.node(endloc[0], endloc[1])
            
                routestart = finder.find_path(startstart, startend, gridstart)
                routeend = finder.find_path(endstart, endend, gridend)
            
            else:
                startstart = gridstart.node(startloc[0], startloc[1])
                startend =  gridstart.node(stairwell[0], stairwell[1])
        
                endstart = gridend.node(stairwell[0], stairwell[1])
                endend = gridend.node(endloc[0], endloc[1])

                routestart = finder.find_path(startstart, startend, gridstart)
                routeend = finder.find_path(endstart, endend, gridend)
                
            total = len(routestart[0]) + len(routeend[0])
            
            if 'e' in startfloor and not endfloor: 
                total += abs(int(startfloor[-1]) * 2 - int(endfloor[-1]) - 1)
            if 'e' in endfloor and not startfloor:
                total += abs(int(endfloor[-1]) * 2 - int(startfloor[-1]) - 1)
            else:
                total += abs(int(startfloor[-1]) - int(endfloor[-1])) * 2
            
            
            gridstart.cleanup()
            gridend.cleanup()

            possibilities[total] = stairwell
            totals.append(total)

        minimum = (possibilities[min(totals)], startfloor)

        startstart, startend = gridstart.node(startloc[0], startloc[1]), gridstart.node(minimum[0][0], minimum[0][1])
        endstart, endend = gridend.node(minimum[0][0], minimum[0][1]), gridend.node(endloc[0], endloc[1])

        routestart, routeend = finder.find_path(startstart, startend, gridstart), finder.find_path(endstart, endend, gridend)

        if abs(int(startfloor[-1]) - int(endfloor[-1])) == 1:
            return routestart, startfloor, routeend, endfloor, None
        else:
            stairs = [minimum]

        if (0, 1) in stairs[0] or (0, 5) in stairs[0]:
            if int(startfloor[-1]) < int(endfloor[-1]):
                lower, higher = hierarchyext.index(startfloor[-2:]), hierarchyext.index(endfloor[-2:])
            else:
                lower, higher = hierarchyext.index(endfloor[-2:]), hierarchyext.index(startfloor[-2:])
            for i in hierarchyext[lower + 1:higher]:
                if 'f' in i:
                    stairs.append(((minimum[0][0] + 8, minimum[0][1]), 'matrix' + i))
                elif 'e' in i:
                    stairs.append((minimum[0], 'matrix' + i))
        else:
            if int(startfloor[-1]) < int(endfloor[-1]):
                lower, higher = hierarchyreg.index(startfloor[-2:]), hierarchyreg.index(endfloor[-2:])
            else:
                lower, higher = hierarchyreg.index(endfloor[-2:]), hierarchyreg.index(startfloor[-2:])
            for i in hierarchyreg[lower + 1:higher]:
                stairs.append((minimum[0], 'matrix' + i))

        return routestart, startfloor, routeend, endfloor, stairs