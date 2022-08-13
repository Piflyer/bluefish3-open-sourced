# Project Bluefish 3
[Report PDF](https://www.scribd.com/document/582148255/Bluefish-3-Report)
## Project Abstract
Traffic is becoming an increasingly dangerous issue, especially during the time of Covid-19. During times of a pandemic, social distancing is a critical component in containing the spread of Covid-19. Boston Latin School suffers these exact problems. Four minutes are given between classes for transitioning, and students are often in very crowded and congested areas where social distancing cannot be kept. However, other parts of the campus are often empty, creating the need of trying to distribute the traffic within the school for a safer and faster transition for students. After deciding to use Python along with 2D matrices representing our school’s different floor plans it was necessary to gather data that was needed. Acquiring the anonymous student schedules from the school's registrar in the format of a large Google Sheet then led to creating a method to manage this data efficiently and format it in a way that is straightforward to use. Following this, matrices were created for simulation to run on and the required relations between room numbers (to which the student will go) and their corresponding locations within the matrices. Subsequently, running a control model with no optimizations as a control model allowed comparison to future iterations. Preliminary results were created by running a smaller test size with a simpler algorithm to gauge whether or not our plan is feasible. These preliminary results showed that it is possible to spread the traffic within the school campus more evenly. Specifically, the average number of students within a given area was reduced by about 7.2%. The fastest path was found to oftentimes not be the shortest path. To get the final results, all that was needed to do was to scale the preliminary code to all 7 periods on all 6 days of the rotating schedule, and the number of students in a specific area was reduced up to 20.7%. This project gave reasoning to back the assumption that humans cannot perfectly predict and assess what the most efficient route between places is, and that creating an external tool that can help improve the efficiency of students' movement significantly during the times of a pandemic when safety and speed are crucial.

## Usage:
### Dependencies:
* Python 3.7+
* Unix OS (MacOS, Linux, etc.)
    * If using Windows, command line arguments and file system will be different. Change all necessary references manually.
* Schedule formatted in a CSV

## Install Libraries
`pip3 install pathfinding csv copy json threading numpy`

## Edit files to suit your circumstances
* Create CSV for `extraction.py` with the sample format below
* Configure `extraction.py` to necessary options
* Create 2D floor matrices in `floormatrices.py`
* Create room references in `location.py`
* If using automation change arguments in `automate.sh`
* Specify `output_folder` and complete necessary revisions when needed in `main.py`
* Complete `hierarchyext` and `hierarchyreg` in `utilities.py` 

### Sample CSV format:
```
Student ID,Grade,Periods,Subject,Homeroom,Classroom
5,7,3(3) ,Study,235,216
...
5,7,6(3) ,Study,235,032
6,7,3(3) ,Study,231,034
6,7,1(7) 2(1) 3(2) 4(3) 5(4) 6(6) ,English Language Arts 7,231,235
...
6,7,4(4) 6(7) ,Fundamentals Of Music 1 MS,231,421
12,7,4(7) ,Study,227,228
...
```
## Running Bluefish 3:
```
# Extract schedules
$ python3 extraction.py

# For automation:
$ automate.sh

# For manual execution:
$ python3 main.py <json_file_from_extraction>

# Rerun for each "day" of the rotating schedule as needed
```
## Issues
Any issues with the code or questions can be reported through the [issue-tracker](https://github.com/Piflyer/bluefish3-open-sourced/issues)

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Any help or feedback will greatly be appreciated.

## License
[MIT](LICENSE)

## Credits
[Tim Nguyen](https://thisistim.dev)

[Phineas Scovel](https://github.com/pitfall24)

[Python-Pathfinding](https://pypi.org/project/pathfinding/)
