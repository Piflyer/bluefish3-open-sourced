class School:
    def __init__(self):
        # Sample Main Building
        self.matrixf0 = {
            'pathfinding':
            [
                #0, 1, 2, 3, 4, 5, 6, 7, 8 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], #0
                [1, 1, 1, 1, 1, 1, 1, 1, 1], #1
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #2
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #3
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #4
                [1, 1, 0, 0, 0, 0, 1, 1, 1], #5
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #6
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #7
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #8
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #9
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #10
                [1, 1, 1, 1, 1, 1, 1, 1, 1], #11
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #12
                [0, 1, 1, 1, 1, 1, 1, 1, 0], #13
                [0, 1, 0, 0, 1, 0, 0, 1, 0], #14
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #15
                [0, 0, 0, 0, 0, 0, 0, 0, 0]  #16
            ],
            'weights':
            [
                #0, 1, 2, 3, 4, 5, 6, 7, 8 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], #0
                [1, 1, 1, 1, 1, 1, 1, 1, 1], #1
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #2
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #3
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #4
                [1, 1, 0, 0, 0, 0, 1, 1, 1], #5
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #6
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #7
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #8
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #9
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #10
                [1, 1, 1, 1, 1, 1, 1, 1, 1], #11
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #12
                [0, 1, 1, 1, 1, 1, 1, 1, 0], #13
                [0, 1, 0, 0, 1, 0, 0, 1, 0], #14
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #15
                [0, 0, 0, 0, 0, 0, 0, 0, 0]  #16
            ],
            'sigmoid':
            [
                #0, 1, 2, 3, 4, 5, 6, 7, 8 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], #0
                [1, 1, 1, 1, 1, 1, 1, 1, 1], #1
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #2
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #3
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #4
                [1, 1, 0, 0, 0, 0, 1, 1, 1], #5
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #6
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #7
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #8
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #9
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #10
                [1, 1, 1, 1, 1, 1, 1, 1, 1], #11
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #12
                [0, 1, 1, 1, 1, 1, 1, 1, 0], #13
                [0, 1, 0, 0, 1, 0, 0, 1, 0], #14
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #15
                [0, 0, 0, 0, 0, 0, 0, 0, 0]  #16       
            ],
            'copyable':
            [
                #0, 1, 2, 3, 4, 5, 6, 7, 8 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], #0
                [1, 1, 1, 1, 1, 1, 1, 1, 1], #1
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #2
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #3
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #4
                [1, 1, 0, 0, 0, 0, 1, 1, 1], #5
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #6
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #7
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #8
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #9
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #10
                [1, 1, 1, 1, 1, 1, 1, 1, 1], #11
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #12
                [0, 1, 1, 1, 1, 1, 1, 1, 0], #13
                [0, 1, 0, 0, 1, 0, 0, 1, 0], #14
                [0, 1, 0, 0, 0, 0, 0, 1, 0], #15
                [0, 0, 0, 0, 0, 0, 0, 0, 0]  #16       
            ]
        }
        # Sample extension
        self.matrixe0 = {
            'pathfinding':
            [
                [0, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
            ],
            'weights':
            [
                [0, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
            ],
            'sigmoid':
            [
                [0, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
            ],
            'copyable':
            [
                [0, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0],
            ]
        }