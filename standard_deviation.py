import os
import numpy as np

path = 'output_without_brackets/'

day_1 = []
day_1 = np.array(day_1)
day_2 = []
day_2 = np.array(day_2)
day_3 = []
day_3 = np.array(day_3)
day_4 = []
day_4 = np.array(day_4)
day_5 = []
day_5 = np.array(day_5)
day_6 = []
day_6 = np.array(day_6)

day_1_sig = []
day_1_sig = np.array(day_1_sig)
day_2_sig = []
day_2_sig = np.array(day_2_sig)
day_3_sig = []
day_3_sig = np.array(day_3_sig)
day_4_sig = []
day_4_sig = np.array(day_4_sig)
day_5_sig = []
day_5_sig = np.array(day_5_sig)
day_6_sig = []
day_6_sig = np.array(day_6_sig)

print('stated iterating')
for folder in os.listdir(path):
    print('folder:', folder)
    for subfolder in os.listdir(path + folder):
        if 'weights' in subfolder:
            print('subfolder:', subfolder)
            print(os.listdir(path + folder + '/' + subfolder))
            for file in os.listdir(path + folder + '/' + subfolder)[6:7]:
                current = open(path + folder + '/' + subfolder + '/' + file, 'r')
                for char in current.read():
                    if not char.isdigit() or char == '0':
                        continue
                    else:
                        if folder == 'output_control_day_1':
                            day_1 = np.append(day_1, float(char))
                        elif folder == 'output_control_day_2':
                            day_2 = np.append(day_2, float(char))
                        elif folder == 'output_control_day_3':
                            day_3 = np.append(day_3, float(char))
                        elif folder == 'output_control_day_4':
                            day_4 = np.append(day_4, float(char))
                        elif folder == 'output_control_day_5':
                            day_5 = np.append(day_5, float(char))
                        elif folder == 'output_control_day_6':
                            day_6 = np.append(day_6, float(char))
                        elif folder == 'output_new_sigmoid_V2_5_epochs_day_1':
                            day_1_sig = np.append(day_1_sig, float(char))
                        elif folder == 'output_new_sigmoid_V2_5_epochs_day_2':
                            day_2_sig = np.append(day_2_sig, float(char))
                        elif folder == 'output_new_sigmoid_V2_5_epochs_day_3':
                            day_3_sig = np.append(day_3_sig, float(char))
                        elif folder == 'output_new_sigmoid_V2_5_epochs_day_4':
                            day_4_sig = np.append(day_4_sig, float(char))
                        elif folder == 'output_new_sigmoid_V2_5_epochs_day_5':
                            day_5_sig = np.append(day_5_sig, float(char))
                        elif folder == 'output_new_sigmoid_V2_5_epochs_day_6':
                            day_6_sig = np.append(day_6_sig, float(char))


print('finished iterating')
print('started calculating standard deviation')

print('Day 1 control: ' + str(np.std(day_1)))
print('Day 2 control: ' + str(np.std(day_2)))
print('Day 3 control: ' + str(np.std(day_3)))
print('Day 4 control: ' + str(np.std(day_4)))
print('Day 5 control: ' + str(np.std(day_5)))
print('Day 6 control: ' + str(np.std(day_6)))
print('Day 1 sigmoid: ' + str(np.std(day_1_sig)))
print('Day 2 sigmoid: ' + str(np.std(day_2_sig)))
print('Day 3 sigmoid: ' + str(np.std(day_3_sig)))
print('Day 4 sigmoid: ' + str(np.std(day_4_sig)))
print('Day 5 sigmoid: ' + str(np.std(day_5_sig)))
print('Day 6 sigmoid: ' + str(np.std(day_6_sig)))
