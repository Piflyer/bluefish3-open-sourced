from pathfinding.core.grid import Grid
import copy, json, math, time, sys, threading, os
from pathfinding.finder.a_star import AStarFinder
import floormatrices
from location import roomlocation
from utilities import *

#sigmoid https://www.desmos.com/calculator/kripzqtggh

finder = AStarFinder()
#schedules = json.load(open(sys.argv[1]))
schedules = json.load(open(sys.argv[1]))

schools = [floormatrices.School() for i in range(6)]

# Run singular period on whole school (for thread)
def run_period(period, epochs):
    print(period)
    #0,1,2,3,4,5,6
    print(threading.current_thread().name, 'STARTED')
    
    for epoch in range(epochs):
        counter = 0

        # Iterate through all students
        for student in schedules:
            # Print current student information / state
            #print('NEW STUDENT ------------------------------------------------ \t\t\t THREAD:', threading.current_thread().name)
            #print('STUDENT: ', student, '  PERIOD: ', period + 1, 'to', period + 2)
            print('COUNTER:', counter, '\tSTUDENT:', student, '\tPERIOD:', period + 1, 'to', period + 2, '\t\tEPOCH:', epoch + 1, '\tTHREAD:', threading.current_thread().name)
            counter += 1

            startroom, endroom = schedules[student][period], schedules[student][period + 1]
            floors = ['matrixf0', 'matrixf1', 'matrixf2', 'matrixf3', 'matrixe1', 'matrixe2', 'matrixe3']

            startroute, startfloor, endroute, endfloor, stairs = calc_route(startroom, endroom, period)

            # Test stairs and Add weights to 'weights'
            if not endfloor:
                for i, j in startroute[0]:
                    eval('schools[period].' + str(startfloor))['weights'][j][i] += 1
            elif not stairs:
                for i, j in startroute[0]:
                    eval('schools[period].' + str(startfloor))['weights'][j][i] += 1
                for i, j in endroute[0]:
                    eval('schools[period].' + str(endfloor))['weights'][j][i] += 1
            else:
                for i, j in startroute[0]:
                    eval('schools[period].' + str(startfloor))['weights'][j][i] += 1
                for i, j in endroute[0]:
                    eval('schools[period].' + str(endfloor))['weights'][j][i] +=1
                for (i, j), floor in stairs:
                    eval('schools[period].' + str(floor))['weights'][j][i] += 1

            # Calculate 'sigmoid' from 'weights'
            # COMMENT OUT FOR CONTROL
            for floor in floors:
                for i in range(len(eval('schools[period].' + str(floor))['weights'])):
                    for j in range(len(eval('schools[period].' + str(floor))['weights'][i])):
                        # Old Sigmoid
                        #xyz
                        # New Sigmoid
                        #eval('schools[period].' + str(floor))['sigmoid'][i][j] = 0 if eval('schools[period].' + str(floor))['weights'][i][j] == 0 else (0.24762 / (0.00878772 + 72.4176 * math.e ** (eval('schools[period].' + str(floor))['weights'][i][j] / -14.7055)) + (eval('schools[period].' + str(floor))['weights'][i][j] / 17.3447) + 2)
                        # New Sigmoid V2
                        eval('schools[period].' + str(floor))['sigmoid'][i][j] = 0 if eval('schools[period].' + str(floor))['weights'][i][j] == 0 else (-0.561003 / (-0.0279881 + (-356.934) * math.e ** (eval('schools[period].' + str(floor))['weights'][i][j] / -16.7939)) + (eval('schools[period].' + str(floor))['weights'][i][j] / 10.8063) + 1.1)

                eval('schools[period].' + str(floor))['pathfinding'] = copy.deepcopy(eval('schools[period].' + str(floor))['sigmoid'])
                eval('schools[period].' + str(floor))['sigmoid'] = copy.deepcopy(eval('schools[period].' + str(floor))['copyable'])
            # ENDS HERE

        # Threading / organization
        print('PERIOD', period + 1, 'DONE ------------------------------------------------')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

        # Print matrices when thread is done
        #for i in ['matrixf0', 'matrixf1', 'matrixf2', 'matrixf3', 'matrixe1', 'matrixe2', 'matrixe3']:
        #    print('period:', period + 1)
        #    print('floor:', i)
        #    print_matrix1(eval('schools[period].' + str(i))['weights'])
        #    print('\n')

        
        
        # Output to output folder and create txt file
        for floor in floors:
            try:
                os.mkdir('output')
                os.mkdir('output/pathfinding_matrices/')
                os.mkdir('output/weights_matrices/')
                os.mkdir('output/sigmoid_matrices/')
                os.mkdir('output/copyable_matrices/')
            except FileExistsError:
                pass

            output_pathfinding = open('output/pathfinding_matrices/' + str(floor) + '.txt', 'a')
            output_weights = open('output/weights_matrices/' + str(floor) + '.txt', 'a')
            output_sigmoid = open('output/sigmoid_matrices/' + str(floor) + '.txt', 'a')
            output_copyable = open('output/copyable_matrices/' + str(floor) + '.txt', 'a')

            output_pathfinding.write('PERIOD: ' + str(period + 1) + ' to ' + str(period + 2) + '  EPOCH: ' + str(epoch + 1) + '  FLOOR: ' + str(floor) + '\n')
            for line in eval('schools[period].' + str(floor))['pathfinding']:
                output_pathfinding.write(str(line) + '\n')
            output_pathfinding.write('\n')

            output_weights.write('PERIOD: ' + str(period + 1) + ' to ' + str(period + 2) + '  EPOCH: ' + str(epoch + 1) + '  FLOOR: ' + str(floor) + '\n')
            for line in eval('schools[period].' + str(floor))['weights']:
                output_weights.write(str(line) + '\n')
            output_weights.write('\n')

            output_sigmoid.write('PERIOD: ' + str(period + 1) + ' to ' + str(period + 2) + '  EPOCH: ' + str(epoch + 1) + '  FLOOR: ' + str(floor) + '\n')
            for line in eval('schools[period].' + str(floor))['sigmoid']:
                output_sigmoid.write(str(line) + '\n')
            output_sigmoid.write('\n')

            output_copyable.write('PERIOD: ' + str(period + 1) + ' to ' + str(period + 2) + '  EPOCH: ' + str(epoch + 1) + '  FLOOR: ' + str(floor) + '\n')
            for line in eval('schools[period].' + str(floor))['copyable']:
                output_copyable.write(str(line) + '\n')
            output_copyable.write('\n')

        # Prep for next epoch
        for floor in floors:
            if epoch == epochs - 1:
                pass
            else:
                eval('schools[period].' + str(floor))['weights'] = copy.deepcopy(eval('schools[period].' + str(floor))['copyable'])
        


# Start threads
threads = [threading.Thread(target=run_period, name = 'THREAD' + str(i), args=(i, 5,)) for i in range(6)]
for i in threads:
    print('STARTING THREAD:', i.name)
    i.start()