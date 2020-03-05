
def printSameStepsDown(same_steps): 

    steps = ['LR LL'] * int(same_steps)
    print(len(steps)*2)
    steps = (' ').join(steps)
    print('%s'%(steps))

def printSameStepsUp(same_steps): 

    steps = ['UR UL'] * int(same_steps)
    print(len(steps)*2)
    steps = (' ').join(steps)
    print('%s'%(steps))

def printShortestPath(n, i_start, j_start, i_end, j_end):

    d_row = (i_start - i_end)
    d_column = (j_start - j_end)

    if d_row%2 != 0:
        print('Impossible')
    else: 
        if d_row > 0:
            # Upper Side
            steps_upper_side = int(d_row/2)
            if abs(d_column) > steps_upper_side: 
                # 
                if (abs(d_column)-steps_upper_side)%2 == 0:
                    if d_column > 0 :
                        steps = ['UL'] * int(steps_upper_side)
                        left_steps = int((abs(d_column)-steps_upper_side)/2)
                        [(steps.append('L')) for i in range(left_steps) ]
                        print(len(steps))
                        steps = (' ').join(steps)
                        print('%s'%(steps))
                    elif d_column < 0:
                        steps = ['UR'] * int(steps_upper_side)
                        right_steps = int((abs(d_column)-steps_upper_side)/2)
                        [ (steps.append('R')) for i in range(right_steps) ]
                        print(len(steps))
                        steps = (' ').join(steps)
                        print('%s'%(steps))
                    else:
                        same_steps = int((abs(steps_upper_side))/2)
                        printSameStepsUp(same_steps)
                else:
                    print('Impossible')

            elif abs(d_column) < steps_upper_side :
                if d_column == 0: 
                    same_steps = int((abs(steps_upper_side))/2)
                    printSameStepsUp(same_steps)
                else: 
                    ur_steps = int((steps_upper_side - d_column)/2)
                    ur_steps = steps_upper_side-ur_steps

                    steps = ['UR'] * ur_steps
                    [ (steps.append('UL')) for i in range(ur_steps) ]
                    print(len(steps))
                    steps = (' ').join(steps)
                    print('%s'%(steps))
            else:
                if d_column > 0:
                    steps = ['UL'] * int(steps_upper_side)
                    print(len(steps))
                    steps = (' ').join(steps)
                    print('%s'%(steps))
                elif d_column < 0: 
                    steps = ['UR'] * int(steps_upper_side)
                    print(len(steps))
                    steps = (' ').join(steps)
                    print('%s'%(steps))
                else: 
                    same_steps = int((abs(steps_upper_side))/2)
                    printSameStepsUp(same_steps)
        else: 
            # Lower Side
            steps_down_side = abs(int(d_row/2))
            
            if abs(d_column) > steps_down_side:

                if (abs(d_column)-steps_down_side)%2 == 0:
                    if d_column > 0 :
                        steps = ['LL'] * steps_down_side
                        left_steps = int((abs(d_column)-steps_down_side)/2)
                        [ (steps.append('L')) for i in range(left_steps) ]
                        print(len(steps))
                        steps = (' ').join(steps)
                        print('%s'%(steps))
                    elif d_column < 0 :
                        
                        right_steps = int((abs(d_column)-steps_down_side)/2)
                        steps = ['R'] * right_steps
                        [ (steps.append('LR')) for i in range(steps_down_side) ]
                        print(len(steps))
                        steps = (' ').join(steps)
                        print('%s'%(steps))
                    else: 
                        print('Impossible 1 : d_column == 0')
                else:
                    print('Impossible') 
                
            elif abs(d_column) < steps_down_side:

                if d_column == 0: 
                    same_steps = int(steps_down_side/2)
                    printSameStepsDown(same_steps)
                else: 
                    lr_steps = int((steps_down_side - d_column)/2)
                    ll_steps = steps_down_side-lr_steps

                    steps = ['LR'] * lr_steps
                    [ (steps.append('LL')) for i in range(ll_steps) ]
                    print(len(steps))
                    steps = (' ').join(steps)
                    print('%s'%(steps))

            else: 
                if d_column > 0:
                    steps = ['LL'] * steps_down_side
                    print(len(steps))
                    steps = (' ').join(steps)
                    print('%s'%(steps))
                elif d_column < 0 :
                    steps = ['LR'] * steps_down_side
                    print(len(steps))
                    steps = (' ').join(steps)
                    print('%s'%(steps))
                else: 
                    same_steps = int((abs(d_column)-steps_down_side)/2)
                    printSameStepsDown(same_steps)



# printShortestPath(100, 2, 24, 92, 45)

printShortestPath(70, 7, 15, 67, 3)

# printShortestPath(150, 24, 15, 46, 102)

# printShortestPath(7, 0, 3, 4, 3)