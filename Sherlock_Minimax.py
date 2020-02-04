
def getMinDistance(arr, p, idx):
    
    if len(arr) == 1:
        return(arr[0], idx)
    elif len(arr) == 2:
        if abs(arr[0] - p ) > abs(arr[1]-p):
            return arr[1], idx+1
        else:
            return arr[0], idx
    else :

        if arr[len(arr)-1] <= p:
            return(arr[len(arr)-1], idx+len(arr)-1)
        elif arr[0] >= p:
            return(arr[0], idx)
        else :
            
            length = len(arr)
            mid = int(length/2)

            if arr[mid] < p :
                return getMinDistance(arr[mid:length],p, idx+mid)
            elif arr[mid] > p :
                return getMinDistance(arr[0:mid+1],p, idx)
            else: 
                return arr[mid], idx+mid



def sherlockAndMinimax(arr, p, q):
    
    sortedArr = sorted(arr)

    nearest_element_f = -1
    minIdx_f = 0

    nearest_element_l = -1
    minIdx_l = 0

    nearest_element_f, minIdx_f = getMinDistance(sortedArr, p, minIdx_f)
    nearest_element_l, minIdx_l = getMinDistance(sortedArr, q, minIdx_l)

    rangeArr = sortedArr[minIdx_f: minIdx_l+1]

    print('New Array: ', rangeArr)
    
    diffDiffArray = []

    if p < rangeArr[0]:
        diffDiffArray.append(2*abs(p-rangeArr[0]))
    
    for j in range(len(rangeArr)-1):
        diffDiffArray.append(abs(rangeArr[j]-rangeArr[j+1]))

    if q > rangeArr[len(rangeArr)-1]:
        diffDiffArray.append(2*abs(q-rangeArr[len(rangeArr)-1]))


    print('Difference Array: ', diffDiffArray)

    max_dist = max(diffDiffArray)
    maxpos = diffDiffArray.index(max_dist)
    

    if maxpos == 0 :
        if p < rangeArr[0]:
            return rangeArr[0] - int(max_dist/2)
        else: 
            return rangeArr[0] + int(max_dist/2)

    elif maxpos == len(diffDiffArray)-1:
        if q > max(rangeArr):
            print('a3')
            return max(rangeArr) + int(max_dist/2)
        else:
            print('a4')
            return max(rangeArr) - int(max_dist/2)
    else:
        if p < rangeArr[0]: 
            return rangeArr[maxpos-1] + int(max_dist/2)
        else :
            return rangeArr[maxpos] + int(max_dist/2)


#x = [3,24,35,6,7,45]

# print(sherlockAndMinimax(x, 15,20)) 

#print(getMinDistance(x, 45, 0))

#print(sherlockAndMinimax([38, 50, 60, 30, 48], 23, 69))

#print(sherlockAndMinimax([3, 5, 7, 9], 6, 8))

#print(sherlockAndMinimax([5,8,14], 4, 9))

#print(sherlockAndMinimax([12, 10, 50, 24, 40], 9, 16))

#print(sherlockAndMinimax([46, 64, 26, 82, 18, 106, 60, 138, 194, 22], 82, 182))

#print(sherlockAndMinimax([7362,772,4354, 5462, 4924, 5224, 284, 5996, 2402, 2540, 6088, 7764, 4552, 7230, 6672, 3444, 2330, 7616, 7414, 6738, 3268, 7268, 7436, 5812, 6132, 124, 5068, 7184 ,4922, 3576, 368, 4224, 58, 7180, 1014, 1542, 3018, 1662, 4160, 1700 ,604, 2666, 4292, 2416, 5528, 300, 3746, 6468, 4404, 626], 2518, 4111))

#print(sherlockAndMinimax([114, 48, 86, 180, 176, 66, 126, 194, 50, 198, 140, 192, 186, 4, 136, 138, 130, 178, 36, 14], 43, 110))

#print(sherlockAndMinimax([3, 24, 35, 6, 7, 45], 15, 20))

#print(sherlockAndMinimax([7518, 4798 ,5528, 3806, 7798, 3396, 6294, 790, 6724, 3582, 2336, 4372, 4746, 7328, 6822, 1996, 2004, 5098, 7376, 7118, 3478, 2416, 5310, 3082, 3288, 2582, 824, 2832, 4818, 3508, 1134, 6640, 5834, 4068, 3622, 192, 940, 2564, 5026, 4708, 4504, 4828, 2332, 3948, 5948, 5676, 2196, 4206, 7766, 3710, 4938, 5688, 3650, 5824, 4360, 3786, 6712,2856, 5768, 1826, 2452, 5874, 964, 1988, 10, 3226, 2956], 6449, 7347))

#print(sherlockAndMinimax([114, 48, 86, 180, 176, 66, 126, 194, 50, 198, 140, 192, 186, 4, 136, 138, 130, 178, 36, 14], 43, 110))


def intVal(n): 
    return int(n)

x = '263044060 323471968 60083128 764550014 209332334 735326740 558683912 626871620 232673588 428805364 221674872 261029278 139767646 146996700 200921412 121542678 96223500 239197414 407346706 143348970 60722446 664904326 352123022 291011666 594294166 397870656 60694236 376586636 486260888 114933906 493037208 5321608 90019990 601686988 712093982 575851770 411329684 462785470 563110618 232790384 511246848 521904074 550301294 142371172 241067834 14042944 249208926 36834004 69321106 467588012 92173320 360474676 221615472 340320496 62541478 360772498 372355942 445408968 342087972 685617022 307398890 437939090 720057720 718957462 387059594 583359512 589920332 500463226 770726204 434976772 567860154 510626506 614077600 620953322 570332092 623026436 502427638 640333172 370673998'
y = x.split()

result = map(intVal, y) 

#print(sherlockAndMinimax(list(result), 70283784, 302962359))

z = '635179944 592614358 645156538 601132234 72927588 782907998 26680576 571904512 253411364 368495632 668408894 715988190 473032290 221000496 166917988 579752154 157507364 169860230 693307354 154889188 598650762 721921752 691564182 40331570 680814954 699857994 283203518 248907756 42917082 510182506 103334006 659157584 68613710 41025968 514681540 388857390 732578568 312342822 544403214 414550896 401504698 342138612 578598706 455969120 673917170 671475360 622813896 327454610 742037798 192108990 115056746 453856008 67302432 568454084 178080688 624229470 47759236 7828940 554075052 636698586 56519734 254355714 149844386 684772334 714305610 572611200 740611006 350803732 625347950 27623254 429722502 772950450 508854614 18633596 529333176 635794634 102605328 122897004 595455366 105384508 220658676 370461750 782829740 371224392 595323626 302478768 448101966 213876262 477578452 724776600 623913570 456079206 284937928 441662568 21517112 446207966 467159802 620366990 178426646 130044896'
y = z.split()

result = map(intVal, y) 

print(sherlockAndMinimax(list(result), 64214888, 789945206))