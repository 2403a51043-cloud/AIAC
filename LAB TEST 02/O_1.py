def is_point_on_edge(px, py, poly):
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        # Check if point is on the line segment
        if (min(x1, x2) <= px <= max(x1, x2)) and (min(y1, y2) <= py <= max(y1, y2)):
            # Compute cross product to check colinearity
            dx1, dy1 = x2 - x1, y2 - y1
            dx2, dy2 = px - x1, py - y1
            if dx1 * dy2 == dy1 * dx2:
                return True
    return False

def point_in_polygon(poly, pts):
    result = []
    n = len(poly)
    for px, py in pts:
        if is_point_on_edge(px, py, poly):
            result.append(True)
            continue
        cnt = 0
        for i in range(n):
            x1, y1 = poly[i]
            x2, y2 = poly[(i + 1) % n]
            # Check if the ray crosses the edge
            if ((y1 > py) != (y2 > py)):
                x_cross = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
                if px < x_cross:
                    cnt += 1
        result.append(cnt % 2 == 1)
    return result

def parse_tuple_list(s):
    s = s.strip()
    if s.startswith('[') and s.endswith(']'):
        s = s[1:-1]
    tuples = []
    for part in s.split('),'):
        part = part.strip().lstrip('[').lstrip('(').rstrip(']').rstrip(')')
        if part:
            x, y = map(float, part.split(','))
            tuples.append((x, y))
    return tuples

if __name__ == "__main__":
    print("Enter polygon vertices as (x1,y1),(x2,y2),... :")
    poly_input = input()
    poly = parse_tuple_list(poly_input)
    print("Enter query points as (x1,y1),(x2,y2),... :")
    pts_input = input()
    pts = parse_tuple_list(pts_input)
    res = point_in_polygon(poly, pts)
    print("Result of point-in-polygon queries (True means inside or on edge, False means outside):")
    print(res)
    print("Acceptance Criteria: Edges counted as inside")

