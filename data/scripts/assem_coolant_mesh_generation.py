import numpy as np
from assem_constants import *  # noqa

def generate_outer_flibe():
    outer_flibe_points = """// Outer FliBe Points \n"""
    outer_flibe_points += "Point(1) = {0, %f, 0, 1.0}; \n" % (H_half_point)
    outer_flibe_points += "Point(2) = {%f, %f, 0, 1.0}; \n" % (flibe_thickness_hyp, H_half_point)
    H_half_point_opp = pc.H_side_big * np.cos(pi/3)
    Hi_half_point_opp = pc.H_side * np.cos(pi/3)
    outer_flibe_points += "Point(3) = {%f, 0, 0, 1.0}; \n" % (H_half_point_opp)
    outer_flibe_points += "Point(4) = {%f, %f, 0, 1.0}; \n" % (flibe_thickness_hyp+Hi_half_point_opp, flibe_thickness)
    outer_flibe_points += "Point(5) = {%f, 0, 0, 1.0}; \n" % (H_half_point_opp+pc.H_side_big)
    outer_flibe_points += "Point(6) = {%f, %f, 0, 1.0}; \n" % (flibe_thickness_hyp+Hi_half_point_opp+pc.H_side, flibe_thickness)
    
    outer_flibe_lines = """
// Outer FliBe Lines
Line(1) = {1, 2};
Line(2) = {2, 4};
Line(3) = {4, 6};
Line(4) = {6, 5};
Line(5) = {5, 3};
Line(6) = {3, 1};
"""

    outer_flibe_surfaces = """
// Outer FliBe Surfaces 
Curve Loop(1) = {1, 2, 3, 4, 5, 6};
Plane Surface(1) = {1};
Physical Surface("outer_flibe") = {1};

"""
    return outer_flibe_points + outer_flibe_lines + outer_flibe_surfaces

def generate_slot_flibe():
    slot_flibe_points = """// Slot FliBe Points \n"""
    slot_flibe_points += "Point(7) = {%f, %f, 0, 1.0}; \n" % (pc.H_side_big - pc.CS_l, H_half_point)
    slot_flibe_points += "Point(8) = {%f, %f, 0, 1.0}; \n" % (pc.H_side_big - pc.CS_l, H_half_point - pc.CS_w / 2)
    slot_flibe_points += "Point(9) = {%f, %f, 0, 1.0}; \n" % (pc.H_side_big, H_half_point)
    slot_flibe_points += "Point(10) = {%f, %f, 0, 1.0}; \n" % (pc.H_side_big-pc.CS_w / 2 * cos(pi / 3), H_half_point - pc.CS_w / 2)
    slot_flibe_points += "Point(11) = {%f, %f, 0, 1.0}; \n" % (pc.H_side_big+pc.CS_l * cos(pi / 3), H_half_point-pc.CS_l*sin(pi / 3))
    slot_flibe_points += "Point(12) = {%f, %f, 0, 1.0}; \n" % (pc.H_side_big+pc.CS_l * cos(pi / 3)-(pc.CS_w / 2)*sin(pi/3), H_half_point-pc.CS_l*sin(pi / 3)-(pc.CS_w / 2)*cos(pi/3))
    
    slot_flibe_lines = """
// Slot FliBe Lines
Line(7) = {7, 9};
Line(8) = {9, 11};
Line(9) = {11, 12};
Line(10) = {12, 10};
Line(11) = {10, 8};
Line(12) = {8, 7};
"""
    slot_flibe_surfaces = """
// Slot FliBe Surfaces 
Curve Loop(2) = {12, 7, 8, 9, 10, 11};
Plane Surface(2) = {2};
Physical Surface("slot_flibe") = {2};
"""
    return slot_flibe_points + slot_flibe_lines + slot_flibe_surfaces

inner_flibe_223_x = pc.H_side_big - pc.D_to_center_width -  pc.F_len - 2 * pc.F_A1_D_gap
inner_flibe_223_y = H_half_point - pc.D_to_center
inner_flibe_224_x = inner_flibe_223_x + pc.P_small_gap / tan(pi/3)
inner_flibe_224_y = inner_flibe_223_y - pc.P_small_gap
inner_flibe_237_x = pc.H_side_big - pc.D_to_center_width
inner_flibe_237_y = H_half_point - pc.D_to_center
inner_flibe_238_x = inner_flibe_237_x + pc.P_small_gap / tan(pi/3)
inner_flibe_238_y = inner_flibe_237_y - pc.P_small_gap

def generate_fuel_cells():
    fuel_cell_points = """
// Fuel Cell Points \n"""
    graphite_plank_65_x = F_starting_point
    graphite_plank_65_y = inner_flibe_224_y - 0.35
    graphite_plank_y = graphite_plank_65_y
    graphite_plank_x = graphite_plank_65_x
    point = 13
    for j in range(12):
        for i in range(11):
            fuel_cell_points += "Point(%d) = {%f, %f, 0, 1.0}; \n" % (point, graphite_plank_x + i * F_cell_width, graphite_plank_y)
            point += 1 
        if (j % 2) == 0:
            graphite_plank_y -= F_cell_height
        else:
            graphite_plank_y -= 2 * graphite_thickness + pc.P_big_gap
            graphite_plank_x += xgap_btwn_fuel_cells

    fuel_cell_lines = """
// Fuel Cell Lines \n"""
    # horizontal lines
    line, left, right = 13, 13, 14
    for j in range(12):
        for i in range(10):
            fuel_cell_lines += "Line(%d) = {%d, %d}; \n" % (line, left, right)
            line += 1
            left += 1
            right += 1
        left += 1
        right += 1
    # vertical lines
    top, bot = 13, 24
    for j in range(6):
        for i in range(11):
            fuel_cell_lines += "Line(%d) = {%d, %d}; \n" % (line, top, bot)
            line += 1
            top += 1
            bot += 1
        top += 11
        bot += 11

    fuel_cell_surfaces = """
// Fuel Cell Surfaces \n"""
    surface, loop, top, right, bot, left = 3, 3, 13, 134, 23, 133
    for j in range(6):
        for i in range(10):
            fuel_cell_surfaces += "Curve Loop(%d) = {%d, %d, -%d, -%d}; \n" % (loop, top, right, bot, left)
            fuel_cell_surfaces += "Plane Surface(%d) = {%d}; \n" % (surface, loop)
            fuel_cell_surfaces += "Physical Surface('%s') = {%d}; \n" % ("fuel_cell_"+str(j*10+i), surface)
            surface += 1
            loop += 1
            top += 1
            right += 1 
            bot += 1 
            left += 1
        top += 10
        right += 1
        bot += 10
        left += 1
    return fuel_cell_points + fuel_cell_lines + fuel_cell_surfaces

def generate_plank_points():
    graphite_plank_points = """
// Graphite Plank Points \n"""
    # left side
    graphite_plank_199_x = inner_flibe_224_x - pc.P_D_jut_hyp
    graphite_plank_199_y = inner_flibe_223_y - pc.P_small_gap
    graphite_plank_points += "Point(199) = {%f, %f, 0, 1.0}; \n" % (graphite_plank_199_x, graphite_plank_199_y)
    point = 200 
    graphite_plank_x, graphite_plank_y = graphite_plank_199_x, graphite_plank_199_y
    for i in range(200, 211):
        if (i %2) == 0:
            graphite_plank_x += pc.P_A1_adj
            graphite_plank_y -= pc.P_A1_height
        else:        
            graphite_plank_x += pc.P_big_gap / tan(pi/3)
            graphite_plank_y -= pc.P_big_gap
        graphite_plank_points += "Point(%d) = {%f, %f, 0, 1.0}; \n" % (point, graphite_plank_x, graphite_plank_y)
        point += 1
    # right side 
    graphite_plank_211_x = inner_flibe_238_x + pc.P_D_jut_hyp
    graphite_plank_211_y = inner_flibe_237_y - pc.P_small_gap
    graphite_plank_points += "Point(211) = {%f, %f, 0, 1.0}; \n" % (graphite_plank_211_x, graphite_plank_211_y)
    point = 212
    graphite_plank_x, graphite_plank_y = graphite_plank_211_x, graphite_plank_211_y
    for i in range(212, 223):
        if (i %2) == 0:
            graphite_plank_x += pc.P_A1_adj
            graphite_plank_y -= pc.P_A1_height
        else:        
            graphite_plank_x += pc.P_big_gap / tan(pi/3)
            graphite_plank_y -= pc.P_big_gap
        graphite_plank_points += "Point(%d) = {%f, %f, 0, 1.0}; \n" % (point, graphite_plank_x, graphite_plank_y)
        point += 1
        
    return graphite_plank_points 

def generate_inner_flibe_points():
    inner_flibe_points = """
// Inner FliBe Points \n"""
    # left side
    inner_flibe_points += "Point(223) = {%f, %f, 0, 1.0}; \n" % (inner_flibe_223_x, inner_flibe_223_y)
    inner_flibe_points += "Point(224) = {%f, %f, 0, 1.0}; \n" % (inner_flibe_224_x, inner_flibe_224_y)
    point = 225
    inner_flibe_x, inner_flibe_y = inner_flibe_224_x, inner_flibe_224_y
    for i in range(11):
        if (i %2) == 0:
            inner_flibe_x += pc.P_A1_adj
            inner_flibe_y -= pc.P_A1_height
        else:
            inner_flibe_x += pc.P_big_gap / tan(pi/3)
            inner_flibe_y -= pc.P_big_gap
        inner_flibe_points += "Point(%d) = {%f, %f, 0, 1.0}; \n" % (point, inner_flibe_x, inner_flibe_y)
        point += 1
    inner_flibe_points += "Point(236) = {%f, %f, 0, 1.0}; \n" % (inner_flibe_x + pc.P_small_gap / tan(pi/3), inner_flibe_y - pc.P_small_gap)
    # right side
    inner_flibe_points += "Point(237) = {%f, %f, 0, 1.0}; \n" % (inner_flibe_237_x, inner_flibe_237_y)
    inner_flibe_points += "Point(238) = {%f, %f, 0, 1.0}; \n" % (inner_flibe_238_x, inner_flibe_238_y)
    inner_flibe_x, inner_flibe_y = inner_flibe_238_x, inner_flibe_238_y
    point = 239
    for i in range(11):
        if (i %2) == 0:
            inner_flibe_x += pc.P_A1_adj
            inner_flibe_y -= pc.P_A1_height
        else:
            inner_flibe_x += pc.P_big_gap / tan(pi/3)
            inner_flibe_y -= pc.P_big_gap
        inner_flibe_points += "Point(%d) = {%f, %f, 0, 1.0}; \n" % (point, inner_flibe_x, inner_flibe_y)
        point += 1
    inner_flibe_points += "Point(250) = {%f, %f, 0, 1.0}; \n" % (inner_flibe_x + pc.P_small_gap / tan(pi/3), inner_flibe_y - pc.P_small_gap)
    return inner_flibe_points

def coolant_variation_points_curves(radius_vals):
    channel_variation_points = """
// Channel Variation Points \n"""
    channel_variation_curves ="""
// Channel Variation Curves \n"""
    inner_flibe_x, inner_flibe_y = inner_flibe_224_x, inner_flibe_224_y
    pt = 251
    circ = 199
    right_point, left_point = 239, 225
    up, down = {}, {}
    extra_line = {}
    for j in range(10):
        radius = radius_vals[int(j/2)]
        up[j] = []
        down[j] = []
        extra_line[j] = []
        if (j %2) == 0:
            channel_variation_points += "// Inner FliBe %d Top\n" % (int(j/2))
            channel_variation_curves += "// Inner FliBe %d Top\n" % (int(j/2))
            inner_flibe_x += pc.P_A1_adj
            inner_flibe_y -= pc.P_A1_height
            direction = 0
        else:
            channel_variation_points += "// Inner FliBe %d Bot\n" % (int(j/2))
            channel_variation_curves += "// Inner FliBe %d Bot\n" % (int(j/2))
            inner_flibe_x += pc.P_big_gap / tan(pi/3)
            inner_flibe_y -= pc.P_big_gap
            direction = 1
        center_point = inner_flibe_x + pc.D_A1_width / 2
        after_points = np.arange(center_point, inner_flibe_x + pc.D_A1_width, radius)
        start_pt = pt
        center_pt = pt
        for i, point in enumerate(after_points):  
            channel_variation_points += "Point(%d) = {%f, %f, 0, 1.0}; \n" % (pt, point, inner_flibe_y)
            pt += 1
        curve_after_pts = np.arange(start_pt+1, pt-1, 2)
        for i, pt_i in enumerate(curve_after_pts):
            if (i % 2) == direction:
                up[j].append(circ)
                channel_variation_curves += "Circle(%d) = {%d, %d, %d}; \n" % (circ, pt_i+1, pt_i, pt_i-1)
            else:
                down[j].append(circ)
                channel_variation_curves += "Circle(%d) = {%d, %d, %d}; \n" % (circ, pt_i-1, pt_i, pt_i+1)
            circ += 1
        channel_variation_curves += "Line(%d) = {%d, %d}; \n" % (circ, pt_i+1, right_point)
        extra_line[j].append(circ)
        circ += 1
        right_point += 1
        
        before_points = np.arange(center_point, inner_flibe_x, -radius)
        start_pt = pt
        for i, point in enumerate(before_points):
            channel_variation_points += "Point(%d) = {%f, %f, 0, 1.0}; \n" % (pt, point, inner_flibe_y)
            pt += 1 
        curve_before_pts = np.arange(start_pt+1, pt-1, 2)
        for i, pt_i in enumerate(curve_before_pts):
            if i == 0:
                before_point = center_pt
            else:
                before_point = pt_i-1
            if (i % 2) == direction:
                down[j].append(circ)
                channel_variation_curves += "Circle(%d) = {%d, %d, %d}; \n" % (circ, pt_i+1, pt_i, before_point)
            else:
                up[j].append(circ)
                channel_variation_curves += "Circle(%d) = {%d, %d, %d}; \n" % (circ, before_point, pt_i, pt_i+1)
            circ += 1
        channel_variation_curves += "Line(%d) = {%d, %d}; \n" % (circ, pt_i+1, left_point)
        extra_line[j].append(circ)
        circ += 1
        left_point += 1
    return channel_variation_points + channel_variation_curves, circ, up, down, extra_line

def generate_inner_flibe_lines_surfaces(new_line, up, down, extra_line):
    surface = 63
    inner_flibe_lines = """
// Inner FliBe Lines \n"""
    inner_flibe_surfaces = """
// Inner FliBe Surfaces \n"""
    line = new_line
    lt, lb, rt, rb = 223, 224, 237, 238
    index = 0
    for i in range(7):
        inner_flibe_lines += "// Inner FliBe %d \n" % (i)
        inner_flibe_surfaces += "// Inner FliBe %d \n" % (i)
        inner_flibe_lines += "Line(%d) = {%d, %d}; \n" % (line, rt, rb)
        line += 1 
        inner_flibe_lines += "Line(%d) = {%d, %d}; \n" % (line, lb, lt)
        line += 1
        if i in [0, 6]:
            inner_flibe_lines += "Line(%d) = {%d, %d}; \n" % (line, lt, rt)
            line += 1 
            inner_flibe_lines += "Line(%d) = {%d, %d}; \n" % (line, rb, lb)
            line += 1 
            inner_flibe_surfaces += "Curve Loop(%d) = {%d, %d, %d, %d}; \n" % (surface, line-4, line-3, line-2, line-1)
        else:
            inner_flibe_surfaces += "Curve Loop(%d) = {" % (surface)
            for pt_up in up[index]:
                #print(1, pt_up)
                inner_flibe_surfaces += str(-pt_up) + ", "
            for pt_down in down[index]:
                #print(2, pt_down)
                inner_flibe_surfaces += str(pt_down) + ", "
            for pt_up in up[index+1]:
                #print(3, pt_up)
                inner_flibe_surfaces += str(pt_up) + ", "
            for pt_down in down[index+1]:
                #print(4, pt_down)
                inner_flibe_surfaces += str(-pt_down) + ", "
            inner_flibe_surfaces += str(extra_line[index][0]) + ", "
            inner_flibe_surfaces += str(-extra_line[index][1]) + ", "
            inner_flibe_surfaces += str(-extra_line[index+1][0]) + ", "
            inner_flibe_surfaces += str(extra_line[index+1][1]) + ", "
            inner_flibe_surfaces += str(line-2) + ", " + str(line-1) + "}; \n"
            index += 2
        inner_flibe_surfaces += "Plane Surface(%d) = {%d}; \n" % (surface, surface)
        surface += 1
        lt, lb, rt, rb = lt+2, lb+2, rt+2, rb+2
    inner_flibe_surfaces += "Physical Surface('inner_flibe') = {63, 64, 65, 66, 67, 68, 69}; \n"
    return inner_flibe_lines + inner_flibe_surfaces, line

def generate_plank_lines_surfaces(new_line, up, down, extra_line, new_line1):
    surface, loop = 70, 70
    graphite_plank_lines = """
// Graphite Plank Lines \n"""
    graphite_plank_surfaces = """
// Graphite Plank Surfaces \n"""
    left_plank, right_plank, line = 199, 211, new_line
    left_inner_flibe, right_inner_flibe = 224, 238
    fuel_cell_horz, fuel_cell_vert = 13, 133 
    index = -1
    for i in range(6):
        graphite_plank_lines += "Line(%d) = {%d, %d}; \n" % (line, left_inner_flibe, left_plank)
        line += 1
        graphite_plank_lines += "Line(%d) = {%d, %d}; \n" % (line, left_plank, left_plank+1)
        line += 1
        graphite_plank_lines += "Line(%d) = {%d, %d}; \n" % (line, left_plank+1, left_inner_flibe+1)
        line += 1
        graphite_plank_lines += "Line(%d) = {%d, %d}; \n" % (line, right_inner_flibe+1, right_plank+1)
        line += 1
        graphite_plank_lines += "Line(%d) = {%d, %d}; \n" % (line, right_plank+1, right_plank)
        line += 1
        graphite_plank_lines += "Line(%d) = {%d, %d}; \n" % (line, right_plank, right_inner_flibe)
        line += 1
        graphite_plank_surfaces += "Curve Loop(%d) = {" % (loop)
        if i != 0:
            for pt_up in up[index]:
                graphite_plank_surfaces += str(pt_up) + ", "
            for pt_down in down[index]:
                graphite_plank_surfaces += str(-pt_down) + ", "
            graphite_plank_surfaces += str(-extra_line[index][0]) + ", "
            graphite_plank_surfaces += str(extra_line[index][1]) + ", "
        if i != 5:
            for pt_up in up[index+1]:
                graphite_plank_surfaces += str(-pt_up) + ", "
            for pt_down in down[index+1]:
                graphite_plank_surfaces += str(pt_down) + ", "
            graphite_plank_surfaces += str(extra_line[index+1][0]) + ", "
            graphite_plank_surfaces += str(-extra_line[index+1][1]) + ", "
        if i == 0:
            graphite_plank_surfaces += str(new_line1+3) + ", "
        if i == 5:
            graphite_plank_surfaces += str(new_line1 + 16) + ", "
        graphite_plank_surfaces += str(line-6) + ", " +\
                                   str(line-5) + ", " +\
                                   str(line-4) + ", " +\
                                   str(line-3) + ", " +\
                                   str(line-2) + ", " +\
                                   str(line-1) + "}; \n"
        loop += 1
        graphite_plank_surfaces += "Curve Loop(%d) = {" % (loop)
        for j in range(10):
            graphite_plank_surfaces += str(-fuel_cell_horz) + ", "
            fuel_cell_horz += 1
        for j in range(10):
            graphite_plank_surfaces += str(fuel_cell_horz) + ", "
            fuel_cell_horz += 1
        graphite_plank_surfaces += str(fuel_cell_vert) + ", "
        fuel_cell_vert += 10
        graphite_plank_surfaces += str(-fuel_cell_vert) + "}; \n"
        fuel_cell_vert += 1

        graphite_plank_surfaces += "Plane Surface(%d) = {%d, %d}; \n" % (surface, loop-1, loop)
        graphite_plank_surfaces += "Physical Surface('%s') = {%d}; \n" % ("graphite_plank_"+str(i+1), surface)
        loop += 1
        surface += 1
        index += 2
        left_plank, right_plank = left_plank+2, right_plank+2
        left_inner_flibe, right_inner_flibe = left_inner_flibe+2, right_inner_flibe+2
    return graphite_plank_lines + graphite_plank_surfaces, line

def graphite_structure_lines_surfaces(new_line, new_line1, new_line2):
    graphite_structure_lines = """
// Graphite Structure Lines \n"""
    graphite_structure_surfaces = """
// Graphite Stucture Surfaces \n"""
    line = new_line
    loop, surface = 82, 76
    graphite_structure_lines += "Line(%d) = {%d, %d}; \n" % (line, 7, 2)
    line += 1
    graphite_structure_lines += "Line(%d) = {%d, %d}; \n" % (line, 6, 11)
    line += 1
    graphite_structure_lines += "Curve Loop(%d) = {%d, 2, 3, %d, 9, 10, 11, 12}; \n" % (loop, line-1, line-2)
    loop += 1
    graphite_structure_lines += "Curve Loop(%d) = {" % (loop)
    loop += 1
    for i in range(new_line2, new_line2+36):
        graphite_structure_lines += str(-i) + ", "
    num = new_line1
    for i in range(18):
        if i < 17:
            if i not in [3, 16]:
                graphite_structure_lines += str(num) + ", "
        else:
            graphite_structure_lines += str(num)
        num += 1
    graphite_structure_lines += "}; \n"
    graphite_structure_surfaces += "Plane Surface(%d) = {%d, %d}; \n" % (surface, loop-2, loop-1)
    graphite_structure_surfaces += "Physical Surface('graphite_structure') = {%d}; \n" % (surface)
    surface += 1
    return graphite_structure_lines + graphite_structure_surfaces

