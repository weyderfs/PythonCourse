import math
#from math import radians, sin, cos, tan

a = float(input("Input the Angle: "))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print("You inputed {:.2f}º the Sine is {:.2f}, the Cosine is {:.2f} and Tangent is {:.2f}".format(a, sen, cos, tan))
