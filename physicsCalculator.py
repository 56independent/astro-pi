#findSpeed(distance, time, height=ISS_HEIGHT) -> speed (m/s) - Finds our current speed using data; ISS_HEIGHT is a global variable.

pixelDistance = 100
time = 0.25
height = 408

def findSpeed(pixelDistance, time, height):
  import math

  #Determine the line of sight distance from the observer to the ISS using the Pythagorean theorem
  lineSight = (height**2)+(pixelDistance**2)
  lineSight = math.sqrt(lineSight)

  #Calculate the angle of elevation
  angleElevation = pixelDistance / height

  #Use the tangent to find the real-world corresponding distance
  realDistance = angleElevation * lineSight

  #Calculate the pixel scale factor
  scaleFactor = realDistance / pixelDistance

  #Adjust for the pixel scale factor
  finalDistance = realDistance * scaleFactor
  
  #Calculate the speed of the ISS
  speed = finalDistance / time
  return speed

print(findSpeed(pixelDistance, time, height))
