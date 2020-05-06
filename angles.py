import math

## Measurements given by the user (H = Home / O = Outgoing)
HLeverLength = float(input("Give the length of the HomeLever: "))
OLeverLength = float(input("Give the length of the OutgoingLever: "))
HFingerThickness = float(input("Give the thickness of the HomeFinger: "))
OFingerThickness = float(input("Give the thickness of the OutgoingFinger: "))
HFingerLength = float(input("Give the length of the HomeFinger: "))
OFingerLength = float(input("Give the length of the OutgoingFinger: "))
## Angle given by the potentiometer (would need calibration to fit the actual angle)
PotentiometerAngle = float(input("Give the angle of the Potentiometer (for testing purposes): "))



## Calculated Variables

## Origin of the First Circle (The second Circle has 0,0 as an origin)
OriginC1X = - HFingerLength + math.cos(PotentiometerAngle)*HLeverLength
OriginC1Y = HFingerThickness + math.sin(PotentiometerAngle)*HLeverLength
## Radius of the second Circle
RCircle2 = math.sqrt(OFingerLength**2 + OFingerThickness**2)
## Angle between the second circle's radius and the Outgoing Finger
AngleRCOF = math.atan(OFingerThickness/OFingerLength)



## Intersection Point

## Distance between Circles
DCircles = math.sqrt(OriginC1X**2+OriginC1Y**2)
## Normalized Vector of the distance
NormalizedVectorDX = OriginC1X / DCircles
NormalizedVectorDY = OriginC1Y / DCircles
## Distance from the origin of the first circle along the vector connecting the two origins 
a = (OLeverLength**2-RCircle2**2+DCircles**2)/(2*DCircles)
## Distance from that vector and perpendicular to it
h = math.sqrt(OLeverLength**2-a**2)
## Intersection Point / only the point to the right of the vector is chosen since the other is not possible
IntersectionPointX = OriginC1X + a * NormalizedVectorDX + h * NormalizedVectorDY
IntersectionPointY = OriginC1Y + a * NormalizedVectorDY + h * ( - NormalizedVectorDX)
## Calculating the angle of the actual finger joint (can be written in radians or degrees)
IntersectionPointAngle = math.atan(IntersectionPointY/IntersectionPointX)
JointAngle = math.degrees(math.pi - (IntersectionPointAngle - AngleRCOF))

print(JointAngle)