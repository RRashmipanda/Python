import functions

area = functions.calculate_area(5, 10)
tringle_area = functions.calculate_triangle_area(4, 6)

print("area of rectangle is", area)
print("triangle area is", tringle_area)



#if functions is not in same directory, use the full path like import Modules.functions

# you can also use by sys module like this:
import sys
sys.path.append('C:\\Code\\10_Modules')
import functions