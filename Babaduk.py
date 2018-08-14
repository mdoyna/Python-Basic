import math

points_T = float(input())
points_S = float(input())
points_R = float(input())
points_A = float(input())

waste_T = points_T * 0.10
waste_S = points_S * 0.05

Total_points_F = (points_T - waste_T) + (points_S - waste_S)
Total_point_M = (points_R + points_A) - (points_R + points_A) / 6

Diff = abs(Total_point_M - Total_points_F)

if Diff > 0 and Total_points_F > Total_point_M:
    print("GIRLS WIN")
    print(f"Difference: {math.floor(Diff)}")
elif Diff > 0 and Total_point_M > Total_points_F:
    print("BOYS WIN")
    print(f"Difference: {math.floor(Diff)}")
else:
    print(f"EQUAL: {math.floor(Total_points_F)}")
