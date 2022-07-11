roomlocation = {  
        # string:list[int, int, string]
        # room_number:[x, y, floor_matrix(z)]
        '007':[1, 1, 'matrixf0'],
        '004':[1, 2, 'matrixf0'],
        '003':[1, 3, 'matrixf0'],      

}

stairlocation = {
        # string:list[tuple(int, int)]
        # floor_matrix_reference(z):[(stair_1_x, stair_1_y), (stair_2_x, stair_2_y)...]
        'f0':[(0, 1), (0, 5), (0, 11), (1, 15), (7, 15), (8, 1), (8, 5), (8, 11), (3, 13), (5, 13)],
        'e0':[(0, 1), (0, 5)]
}