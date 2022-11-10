import math
def intersection(x1,y1,r1,x2,y2,r2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if d <= r1-r2:
        return "C2  is in C1"
    elif d <= r2-r1:
        return "C1  is in C2"
    elif d < r1+r2:
        return "Circumference of C1  and C2  intersect"
    elif d == r1+r2:
        return "Circumference of C1 and C2 will touch"
    else:
        return "C1 and C2  do not overlap"


def test_intersection():
    assert intersection(5, 4, 2, 3, 9, 2) == "C1 and C2  do not overlap"
    assert intersection(5, 4, 3, 5, 10, 3) =="Circumference of C1 and C2 will touch"
    assert intersection(6, 4, 3, 10, 4, 2) == "Circumference of C1  and C2  intersect"
    assert intersection(5, 4, 3, 5, 4, 2) == "C2  is in C1"
    assert intersection(5, 4, 2, 5, 4, 3) == "C1  is in C2"