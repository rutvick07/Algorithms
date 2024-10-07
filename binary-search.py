import time, random
numList = [num for num in range(0,9999999)]
searchNum = int(input('Enter the number to search: '))
#print(numList)
def normalSearch():
    steps = 0
    startTime = time.process_time()
    for i,num in enumerate(numList):
        steps += 1
        if num == searchNum:
            print(f'{numList[i]} number found at index {i}')
            break
        else:
            continue
    endTime = time.process_time()
    evalTime = endTime - startTime
    print(f'It took {evalTime}s and {steps} steps to perform the search.')        

def binarySearch():
    steps = 0
    sortedNumList = sorted(numList)
    high = len(sortedNumList) - 1
    low = 0
    startTime = time.process_time()
    while low <= high:
        steps += 1 
        mid = (low + high)//2
        if searchNum < sortedNumList[mid]:
            high = mid - 1
        elif searchNum > sortedNumList[mid]:
            low = mid + 1
        elif searchNum == sortedNumList[mid]:
            print(f'{sortedNumList[mid]} found at index {mid}')
            break
        else:
            print(f'{searchNum} not found in the given list.')
            break
    endTime = time.process_time()
    evalTime = endTime - startTime
    print(f'It took {evalTime}s and {steps} steps to perform the search.')        

print('=================== Normal Search ==========================')
normalSearch()
print('\n')
print('=================== Binary Search ==========================')
binarySearch()
