# Define array photoNames[]
# Every 0.25 seconds:
#     Take a photo
#     Add it to photoNames[]
#     Find diff between now photo and the one before
#     Calculate the speed using that
#     Add that entry to the dict array
#     Have 600*4 iterations happened (600 being 10 minutes in seconds and 4 being the number of iterations per secons) yet?
#         If so, break the loop
#         Else, find the current time and then wait until the next quarter-second before going back to the top
# Find the average of the data
# Output it as per guidelines

import photoManager
import physicsCalculator
import diffChecker
import finals
import time

photoNames = []

for i in range(600*4):
    photoNames.append(takePhoto())
    if photoNames.length > 2:
        distance = findDiff(photoNames[0:], photoNames[1:])
    
    time.sleep(0.25)

