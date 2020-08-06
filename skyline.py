
# First version of merging two outlines
# Logic: Sorting based on x-coordinate values
def merge1_outlines(u, v):

    skyline = []
    i, j, m, n = 0, 0, len(u), len(v)

    while i < m and j < n:
        if u[i][0] < v[j][0]:
            skyline.append(u[i])
            i += 1
        else:
            skyline.append(v[j])
            j += 1

    while i < m:
        skyline.append(u[i])
        i += 1

    while j < n:
        skyline.append(v[j])
        j += 1

    return skyline

# Second version of merging two outlines
# Logic: Sorting based on x-coordinate values and changing the height based on the max of y coords
# There will be a jump in skyline only when y increases
# Otherwise, we check if it should drop to a previous height or to the ground
def merge2_outlines(u, v):

    skyline = []
    i, j, m, n = 0, 0, len(u), len(v)

    while i < m and j < n:
        if u[i][0] < v[j][0]:
            uy = u[i][1]
            vy = v[j][1]
            x = u[i][0]
            y = max(uy, vy)
            skyline.append((x, y))
            i += 1
        else:
            vy = v[j][1]
            uy = u[i][1]
            x = v[j][0]
            y = max(uy, vy)
            skyline.append((x, y))
            j += 1

    while i < m:
        skyline.append(u[i])
        i += 1

    while j < n:
        skyline.append(v[j])
        j += 1

    return skyline

# Third and final version of merging two outlines
# Logic: preventing redundant heights by checking y coords and popping off the last element
def merge3_outlines(u, v):
    skyline = []
    i, j, m, n = 0, 0, len(u), len(v)

    while i < m and j < n:
        if u[i][0] < v[j][0]:
            uy = u[i][1]
            vy = v[j][1]
            x = u[i][0]
            y = max(uy, vy)
            if len(skyline) != 0 and skyline[-1][1] == y:
                temp = skyline.pop()

            skyline.append((x, y))
            i += 1
        else:
            vy = v[j][1]
            uy = u[i][1]
            x = v[j][0]
            y = max(uy, vy)
            if len(skyline) != 0 and skyline[-1][1] == y:
                temp = skyline.pop()

            skyline.append((x, y))
            j += 1

    while i < m:
        if len(skyline) != 0 and skyline[-1][1] == u[i][1]:
            temp = skyline.pop()
        skyline.append(u[i])

        i += 1

    while j < n:
        if len(skyline) != 0 and skyline[-1][1] == v[j][1]:
            temp = skyline.pop()
        skyline.append(v[j])

        j += 1

    return skyline

def merge3_outlines(u, v):
    skyline = []
    i, j, m, n = 0, 0, len(u), len(v)

    while i < m and j < n:
        if u[i][0] < v[j][0]:
            uy = u[i][1]
            vy = v[j][1]
            x = u[i][0]
            y = max(uy, vy)
            if len(skyline) != 0 and skyline[-1][1] == y:
                temp = skyline.pop()

            skyline.append((x, y))
            i += 1
        else:
            vy = v[j][1]
            uy = u[i][1]
            x = v[j][0]
            y = max(uy, vy)
            if len(skyline) != 0 and skyline[-1][1] == y:
                temp = skyline.pop()

            skyline.append((x, y))
            j += 1

    while i < m:
        if len(skyline) != 0 and skyline[-1][1] == u[i][1]:
            temp = skyline.pop()
        skyline.append(u[i])

        i += 1

    while j < n:
        if len(skyline) != 0 and skyline[-1][1] == v[j][1]:
            temp = skyline.pop()
        skyline.append(v[j])

        j += 1

    return skyline

def construct_outline(rs):

    if len(rs) == 0:
        return []

    if len(rs) == 1:
        return rs[0]

    mid = len(rs) // 2
    u = construct_outline(rs[:mid])
    v = construct_outline(rs[mid:])

    return merge3_outlines(u, v)

# Here is the "main" function to construct an outline of given rectangles

# A sample set of rectangles could be
rs = [ [(1,0),(5,11)], [(2,0),(7,6)], [(3,0),(9,13)], [(12,0),(16,7)], [(14,0),(25,3)], [(19,0),(22,18)], [(23,0),(29,13)], [(24,0),(28,4)] ]

# To test the merge1_outlines(u, v) from the question
# To test the merge2_outlines(u, v) from the question
# To test the merge3_outlines(u, v) from the question

u = [(1, 0), (3, 11), (9, 13), (12, 0), (16, 7)]
v = [(14, 0), (19, 3), (22, 18), (23, 3), (29, 13)]

print(merge1_outlines(u, v))
print(merge2_outlines(u, v))
print(merge3_outlines(u, v))

print(construct_outline(rs))

# Submitted by Nivedhitha D