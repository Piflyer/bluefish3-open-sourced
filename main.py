import copy, json, math, sys, threading, os, floormatrices
from location import roomlocation
from utilities import *
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.grid import Grid

output_folder = ''

finder = AStarFinder()
if len(sys.argv) != 2 or type(sys.argv[1]) != 'str':
    print('Usage: python3 main.py <json_file>')
    sys.exit()
# System Arguments: schedule.json
schedules = json.load(open(sys.argv[1]))

schools = [floormatrices.School() for i in range(6)]

# Run singular period on whole school (for thread)
def run_period(period, epochs):
    print(period)
    print(threading.current_thread().name, 'STARTED')
    
    for epoch in range(epochs):
        counter = 0

        # Iterate through all students
        for student in schedules:
            # Print current student information / state
            print('COUNTER:', counter, '\tSTUDENT:', student, '\tPERIOD:', period + 1, 'to', period + 2, '\t\tEPOCH:', epoch + 1, '\tTHREAD:', threading.current_thread().name)
            counter += 1

            startroom, endroom = schedules[student][period], schedules[student][period + 1]
            floors = ['floorf0',]

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
            # Comment for loop to run control
            for floor in floors:
                for i in range(len(eval('schools[period].' + str(floor))['weights'])):
                    for j in range(len(eval('schools[period].' + str(floor))['weights'][i])):
                        # Sigmoid
                        eval('schools[period].' + str(floor))['sigmoid'][i][j] = 0 if eval('schools[period].' + str(floor))['weights'][i][j] == 0 else (-0.561003 / (-0.0279881 + (-356.934) * math.e ** (eval('schools[period].' + str(floor))['weights'][i][j] / -16.7939)) + (eval('schools[period].' + str(floor))['weights'][i][j] / 10.8063) + 1.1)

                eval('schools[period].' + str(floor))['pathfinding'] = copy.deepcopy(eval('schools[period].' + str(floor))['sigmoid'])
                eval('schools[period].' + str(floor))['sigmoid'] = copy.deepcopy(eval('schools[period].' + str(floor))['copyable'])
        
        # Output to output folder and create txt file
        for floor in floors:
            try:
                os.mkdir(output_folder)
                os.mkdir(output_folder + '/pathfinding_matrices/')
                os.mkdir(output_folder + '/weights_matrices/')
                os.mkdir(output_folder + '/sigmoid_matrices/')
                os.mkdir(output_folder + '/copyable_matrices/')
            except FileExistsError:
                pass

            output_pathfinding = open(output_folder + '/pathfinding_matrices/' + str(floor) + '.txt', 'a')
            output_weights = open(output_folder + '/weights_matrices/' + str(floor) + '.txt', 'a')
            output_sigmoid = open(output_folder + '/sigmoid_matrices/' + str(floor) + '.txt', 'a')
            output_copyable = open(output_folder + '/copyable_matrices/' + str(floor) + '.txt', 'a')

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

        # Threading / organization
        print('PERIOD', period + 1, 'DONE ------------------------------------------------')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

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