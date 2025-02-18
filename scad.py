import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    oomp_mode = "project"
    #oomp_mode = "oobb"

    if typ == "all":
        filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr", "laser", "true"]
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]

        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = ""
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        names = []
        
        names.append("precision_screwdriver_bit_lock_piece")
        
        #tests
        names.append("precision_screwdriver_test_fluting")
        names.append("precision_screwdriver_test_knurl")
        names.append("precision_screwdriver_test_nut_drop")

        #main
        names.append("precision_screwdriver")


        for name in names:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3["width"] = 1
            p3["height"] = 1
            #p3["thickness"] = 6
            p3["extra"] = "hex_head_2_5_mm"
            part["kwargs"] = p3
            nam = name
            part["name"] = nam
            if oomp_mode == "oobb":
                p3["oomp_size"] = nam
            parts.append(part)


    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        
        sort.append("name")
        sort.append("extra")
        #sort.append("width")
        #sort.append("height")
        #sort.append("thickness")
        
        scad_help.generate_navigation(sort = sort)


width_bit_locker = 7    
height_bit_locker = 3
depth_bit_locker = 14

def get_precision_screwdriver_bit_lock_piece(thing, **kwargs):
    #return get_precision_screwdriver_bit_lock_piece_keyed_screw(thing, **kwargs)
    return get_precision_screwdriver_bit_lock_piece_old_1_twist_lock(thing, **kwargs)



def get_precision_screwdriver_bit_lock_piece_keyed_screw(thing, **kwargs):

    width_bit_locker = 7    
    height_bit_locker = 3
    depth_bit_locker = 14

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    dep = depth_bit_locker

    #add cube
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_cube"    
    wid = width_bit_locker
    hei = height_bit_locker
    dep = dep
    size = [wid, hei, dep]
    p3["size"] = size
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add slot
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_slot"
    p3["radius_name"] = "m3"
    p3["m"] = "#"
    wid = 5
    p3["width"] = wid
    p3["depth"] = height_bit_locker
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth_bit_locker - wid + 1.5
    pos1[1] += -height_bit_locker/2
    p3["pos"] = pos1
    rot1 = copy.deepcopy(rot)
    rot1[1] = 90
    rot1[2] = 90
    p3["rot"] = rot1
    oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_precision_screwdriver_bit_lock_piece_old_1_twist_lock(thing, **kwargs):

    global width_bit_locker, height_bit_locker, depth_bit_locker
    width_bit_locker = 8   
    height_bit_locker = 6
    depth_bit_locker = 7

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    dep = depth_bit_locker

    #add cube
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_cube"    
    wid = width_bit_locker
    hei = height_bit_locker
    dep = dep
    size = [wid, hei, dep]
    p3["size"] = size
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add nut
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_nut"
    p3["radius_name"] = "m3"
    #p3["overhang"] = True
    p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add screw_socket_cap
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_screw_socket_cap"
    p3["radius_name"] = "m3"
    p3["m"] = "#"
    p3["clearance"] = "top"
    p3["depth"] = 25
    p3["overhang"]  = False
    pos1 = copy.deepcopy(pos)
    pos1[2] += dep
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_precision_screwdriver_test(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    radius_big = 10
    radius_little = 4
    height_driver = 30
    depth_taper = 12
    #hex holder bottom
    
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"    
    p3["depth"] = depth_taper
    p3["shape"] = f"oobb_cylinder"  
    p3["r2"] = radius_big
    p3["r1"] = radius_little
    p3["zz"] = "bottom"
    p3["rot"] = [0,0,0]
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add cylinder top
    hex_offset = 10
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    dep = height_driver - hex_offset
    p3["depth"] = dep
    p3["radius"] = radius_big
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth_taper
    p3["pos"] = pos1
    p3["rot"] = [0,0,0]
    p3["zz"] = "bottom"
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)



    

    
    #get holder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    #p3["type"] = "p"
    pos1 = copy.deepcopy(pos)
    p3["pos"] = pos1

    p3["rot"] = [0,0,0]
    p3["m"] = "#"    
    p3["clearance"] = 0.2
    p3["clearance_top"] = True
    return_value_2 = get_holder_blank(thing, **p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [0,0,180]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # left
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -250
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_precision_screwdriver_test_nut_drop(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #main
    radius_big = 10/2
    
    #height_driver = 95
    
    diameter_top_taper = 18
    height_top = 5
    height_top_taper = 35  - height_top
    diameter_top = 18
    #taper
    depth_taper = 3    
    #hex
    hex_side_ratio = 1.1547
    radius_bottom_hex_small = 10/2 * hex_side_ratio
    radius_bottom_hex_big = 13/2 * hex_side_ratio
    depth_bottom_hex_small = 6
    depth_bottom_hex_big = 9

    fudge_factor_bit_lift_extra = 27 
    fudge_fudge_factor_bit_lift_extra = fudge_factor_bit_lift_extra - 25


    lift_bottom_hex_big = 14 + fudge_factor_bit_lift_extra #18
    
    #technical
    bottom_of_shaft = depth_taper + depth_bottom_hex_big + depth_bottom_hex_small + lift_bottom_hex_big + 3
    #lift_bit = bottom_of_shaft - 5 + fudge_fudge_factor_bit_lift_extra
    radius_little = 4.25/2
    #radius_bit_main = 4/2#4.25/2

    

    #donut cutouts
    orings = []
    length_of_gap = lift_bottom_hex_big /2
    middle_of_hex = depth_taper + depth_bottom_hex_small + length_of_gap
    top_of_hex = middle_of_hex + length_of_gap + depth_bottom_hex_big
    donut_shift = 1.8
    #second_donut_level = top_of_hex + length_of_gap + donut_shift

    inside_only = False
    #inside_only = True

    #optional
    include_knurl = True


    ##### new
    
    #constants
    hex_side_ratio = 1.1547

    #handle variables
    height_driver = 95
    radius_main = 10/2

    

    #hex_top_piece
    depth_top_hex = 9
    radius_top_hex = 13/2 * hex_side_ratio
    lift_top_hex = 45

    #hex_bottom_piece
    depth_bottom_hex = 6
    radius_bottom_hex = 10/2 * hex_side_ratio

    #taper bottom
    depth_taper_bottom = 3
    radius_taper_bottom_hex = radius_bottom_hex / hex_side_ratio

    #top taper
    depth_top_taper = height_driver - lift_top_hex - depth_top_hex
    radius_top_taper_little = radius_top_hex / hex_side_ratio
    radius_top_taper_big = 18/2

    #bit variables
    lift_bit = 14
    radius_bit_main = 4/2
    radius_bit_main_clearance = radius_bit_main + 0.25




    
    #main_cylinder
    if True:                
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = height_driver        
        p3["depth"] = dep - depth_taper_bottom
        p3["radius"] = radius_main
        pos1 = copy.deepcopy(pos)
        p3["pos"] = pos1
        pos1[2] += depth_taper_bottom
        p3["zz"] = "bottom"
        #p3["m"] = "#"
        if not inside_only:    
            pass        
            oobb_base.append_full(thing,**p3)
        
    #hex_top_piece
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["height"] = depth_top_hex
        p3["radius"] = radius_top_hex
        pos1 = copy.deepcopy(pos)
        pos1[2] += lift_top_hex
        p3["pos"] = pos1
        rot1 = [0,0,360/12]
        p3["rot"] = rot1
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3) 

    #top_taper
    if False:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = depth_top_taper
        p3["depth"] = dep
        p3["r2"] = radius_top_taper_big
        p3["r1"] = radius_top_taper_little
        pos1 = copy.deepcopy(pos)
        pos1[2] += height_driver
        p3["pos"] = pos1               
        #p3["m"] = "#"
        p3["zz"] = "top"
        if not inside_only:
            pass
            oobb_base.append_full(thing,**p3)
        
    
    #add lock piece
    if True:
        shift_x = 0

        #lock piece drop
        clear = 0.25
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        wid = height_bit_locker + clear
        hei = width_bit_locker + clear
        dep = height_driver - lift_top_hex - depth_top_hex/2 + depth_bit_locker/2
        height_locker = dep
        size = [wid, hei, dep]
        p3["size"] = size
        pos1 = copy.deepcopy(pos)
        pos1[0] += shift_x
        pos1[1] += 0
        pos1[2] += height_driver
        p3["pos"] = pos1
        p3["m"] = "#"
        p3["zz"] = "top"
        oobb_base.append_full(thing,**p3)

        #bottom lock piece
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube_new"
        wid = height_bit_locker + clear
        hei = width_bit_locker + clear
        dep = depth_bit_locker + clear
        size = [wid, hei, dep]
        p3["size"] = size
        pos1 = copy.deepcopy(pos)
        pos1[0] += shift_x #* 2
        pos1[1] += 0
        pos1[2] += height_driver - height_locker
        p3["pos"] = pos1
        p3["m"] = "#"
        repeats = 100
        angle = -45 / repeats
        for i in range(repeats):
            p4 = copy.deepcopy(p3)
            rot2 = [0,0,angle * i]
            p4["rot"] = rot2
            oobb_base.append_full(thing,**p4)

        #poke hole
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_hole"
        p3["radius_name"] = "m3"    
        p3["m"] = "#"
        #p3["zz"] = "middle"
        de = 100
        p3["depth"] = de
        pos1 = copy.deepcopy(pos)
        pos1[0] += shift_x - de/2
        pos1[1] += 0
        pos1[2] += height_driver - height_locker + depth_bit_locker/2
        p3["pos"] = pos1
        rot1 = [0,0,0]
        rot1[1] = 90
        p3["rot"] = rot1
        oobb_base.append_full(thing,**p3)

        


    

        

    #get holder
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"        
        pos1 = copy.deepcopy(pos)
        #pos1[0] += 20
        pos1[2] += lift_bit
        p3["pos"] = pos1        
        #p3["m"] = "#"    
        p3["clearance"] = 0.2
        p3["clearance_top"] = True
        p3["length"] = 100
        p3["radius_bit_main"] = radius_bit_main
        pos1 = copy.deepcopy(pos)
        
        
        return_value_2 = get_holder_blank(thing, **p3)

    

            

    

def get_precision_screwdriver_test_knurl(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    

    #main
    radius_big = 10/2
    
    height_driver = 95
    
    diameter_top_taper = 18
    height_top = 5
    height_top_taper = 35 + 5 - height_top
    diameter_top = 18
    #taper
    depth_taper = 3    
    #hex
    hex_side_ratio = 1.1547
    radius_bottom_hex_small = 10/2 * hex_side_ratio
    radius_bottom_hex_big = 13/2 * hex_side_ratio
    depth_bottom_hex_small = 6
    depth_bottom_hex_big = 9

    fudge_factor_bit_lift_extra = 27

    lift_bottom_hex_big = 14 + fudge_factor_bit_lift_extra #18
    
    #technical
    bottom_of_shaft = depth_taper + depth_bottom_hex_big + depth_bottom_hex_small + lift_bottom_hex_big + 3
    lift_bit = bottom_of_shaft - 5 + fudge_factor_bit_lift_extra
    radius_little = 4.25/2
    radius_bit_main = 3.25/2#4.25/2

    

    #donut cutouts
    orings = []
    length_of_gap = lift_bottom_hex_big /2
    middle_of_hex = depth_taper + depth_bottom_hex_small + length_of_gap
    top_of_hex = middle_of_hex + length_of_gap + depth_bottom_hex_big
    donut_shift = 1.8
    #second_donut_level = top_of_hex + length_of_gap + donut_shift

    inside_only = False
    #inside_only = True


    
    #top piece
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = height_top
        p3["depth"] = dep
        rad = diameter_top / 2
        p3["radius"] = rad
        pos1 = copy.deepcopy(pos)
        current_z = height_driver - dep/2
        current_z = 0
        pos1[2] += current_z
        p3["pos"] = pos1
        p3["rot"] = [0,0,0]
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3)
      
    #knurl
    if True:
        repeats = 36
        angle = 360 / repeats
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        wid = 1
        hei = 1
        dep = 5
        size = [wid, hei, dep]
        p3["size"] = size
        p3["m"] = "#"   
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0#wid/2
        pos1[1] += 0#hei/2
        pos1[2] += current_z
        p3["pos"] = pos1
        p3["zz"] = "middle" 
        p3["rot"] = [0,0,45]     
        for i in range(repeats):
            rot = [0,0,angle * i]
            shift_x = rad + wid/2
            shift = [shift_x,0,0]
            rot_shift = [shift,rot]
            
            p3["rot_shift"] = [rot_shift]
            #p3["rot"] = rot
            oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [0,0,180]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # left
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -250
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

    

def get_precision_screwdriver_test_fluting(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    

    #main
    radius_big = 10/2
    
    height_driver = 95
    
    diameter_top_taper = 18
    height_top = 5
    height_top_taper = 35 + 5 - height_top
    diameter_top = 18
    #taper
    depth_taper = 3    
    #hex
    hex_side_ratio = 1.1547
    radius_bottom_hex_small = 10/2 * hex_side_ratio
    radius_bottom_hex_big = 13/2 * hex_side_ratio
    depth_bottom_hex_small = 6
    depth_bottom_hex_big = 9

    fudge_factor_bit_lift_extra = 27

    lift_bottom_hex_big = 14 + fudge_factor_bit_lift_extra #18
    
    #technical
    bottom_of_shaft = depth_taper + depth_bottom_hex_big + depth_bottom_hex_small + lift_bottom_hex_big + 3
    lift_bit = bottom_of_shaft - 5 + fudge_factor_bit_lift_extra
    radius_little = 4.25/2
    radius_bit_main = 3.25/2#4.25/2

    

    #donut cutouts
    orings = []
    length_of_gap = lift_bottom_hex_big /2
    middle_of_hex = depth_taper + depth_bottom_hex_small + length_of_gap
    top_of_hex = middle_of_hex + length_of_gap + depth_bottom_hex_big
    donut_shift = 1.8
    #second_donut_level = top_of_hex + length_of_gap + donut_shift

    inside_only = False
    #inside_only = True


    if True:
        oring = {}
        
        #lower oring
        oring["id"] = 8/2
        dep = 150
        oring["depth"] = dep    
        pos1 = copy.deepcopy(pos)
        pos1[2] += middle_of_hex
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[2] += donut_shift * 2
        pos12 = copy.deepcopy(pos1)
        pos12[2] += donut_shift
        pos13 = copy.deepcopy(pos1)
        pos13[2] += -donut_shift
        pos14 = copy.deepcopy(pos1)
        pos14[2] += -donut_shift * 2
        poss.append(pos11)
        poss.append(pos12)
        poss.append(pos13)
        poss.append(pos14)        
        oring["pos"] = poss
        orings.append(oring)

        #top oring
        oring = copy.deepcopy(oring)
        oring["id"] = 11/2
        pos1 = copy.deepcopy(pos)
        pos1[2] += top_of_hex + length_of_gap/2 
        oring["pos"] = pos1
        orings.append(oring)

        #top top small diameter
        oring = copy.deepcopy(oring)
        oring["id"] = 14/2
        dep = 16
        oring["depth"] = dep
        pos1 = copy.deepcopy(pos)
        pos1[2] += height_driver - 15.5
        oring["pos"] = pos1
        orings.append(oring)



    #bottom taper piece
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"    
        p3["depth"] = depth_taper
        p3["shape"] = f"oobb_cylinder"  
        #p3["r2"] = radius_big
        p3["r2"] = radius_bottom_hex_small - 1
        p3["r1"] = radius_little
        p3["zz"] = "bottom"
        p3["rot"] = [0,0,0]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)  
        #pos1[1] += 10       
        p3["pos"] = pos1
        if not inside_only:
            oobb_base.append_full(thing,**p3)
        
    
    #main_cylinder
    if True:    
    #if False:    
        hex_offset = 0
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = height_driver - hex_offset - height_top_taper
        reduction =  depth_taper + depth_bottom_hex_small 
        p3["depth"] = dep - reduction
        p3["radius"] = radius_big
        pos1 = copy.deepcopy(pos)
        pos1[2] += reduction
        p3["pos"] = pos1
        p3["rot"] = [0,0,0]
        p3["zz"] = "bottom"
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3)
        
    #top_taper
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = height_top_taper
        p3["depth"] = dep
        p3["r2"] = diameter_top_taper / 2
        p3["r1"] = radius_big
        pos1 = copy.deepcopy(pos)
        pos1[2] += height_driver - height_top_taper/2 - height_top
        p3["pos"] = pos1               
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3)
        
    #top piece
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = height_top
        p3["depth"] = dep
        p3["radius"] = diameter_top / 2
        pos1 = copy.deepcopy(pos)
        pos1[2] += height_driver - dep/2
        p3["pos"] = pos1
        p3["rot"] = [0,0,0]
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3)
        
    #hex_bottom
    if True:
        #10mm piece
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["height"] = depth_bottom_hex_small
        p3["radius"] = radius_bottom_hex_small
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth_taper
        p3["pos"] = pos1        
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3)
        
        #13 mm piece
        p3 = copy.deepcopy(p3)
        p3["height"] = depth_bottom_hex_big
        p3["radius"] = radius_bottom_hex_big
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth_taper + depth_bottom_hex_small + lift_bottom_hex_big
        p3["pos"] = pos1
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3)
        

   #fluting
    if True:
        diameter_flute_tube = 5
        diameter_flute_ring = 150
        center_gap = 7
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oring"
        p3["depth"] = diameter_flute_tube/2
        p3["id"] = diameter_flute_ring/2
        pos1 = copy.deepcopy(pos)
        pos1[0] += diameter_flute_ring/2 + diameter_flute_tube/2 + center_gap/2
        pos1[1] += 0
        pos1[2] += middle_of_hex
        p3["pos"] = pos1
        p3["m"] = "#"
        rot = [90,0,0]
        p3["rot"] = rot
        #rot_shift
        repeats = 6
        angle = 360 / repeats
        for i in range(repeats):
            rot = [0,0,angle * i]
            shift = [0,0,0]
            rot_shift = [shift,rot]
            p3["rot_shift"] = [rot_shift]
            oobb_base.append_full(thing,**p3)
        


    #add orings
    if True:
    #if False:
        for oring in orings:
            oring_poss = oring["pos"]
            #if not an array of arrays make it one
            if not isinstance(oring_poss[0], list):
                oring_poss = [oring_poss]            
            for oring_pos in oring_poss:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oring"
                p3["depth"] = oring["depth"]
                p3["id"] = oring["id"]
                pos1 = copy.deepcopy(pos)
                pos1[0] += oring_pos[0]
                pos1[1] += oring_pos[1]
                pos1[2] += oring_pos[2]
                p3["pos"] = pos1
                
                #p3["m"] = "#"
                if not inside_only:
                    oobb_base.append_full(thing,**p3)
        

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [0,0,180]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # left
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -250
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


def get_precision_screwdriver(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #main
    radius_big = 10/2
    
    #height_driver = 95
    
    diameter_top_taper = 18
    height_top = 5
    height_top_taper = 35  - height_top
    diameter_top = 18
    #taper
    depth_taper = 3    
    #hex
    hex_side_ratio = 1.1547
    radius_bottom_hex_small = 10/2 * hex_side_ratio
    radius_bottom_hex_big = 13/2 * hex_side_ratio
    depth_bottom_hex_small = 6
    depth_bottom_hex_big = 9

    fudge_factor_bit_lift_extra = 27 
    fudge_fudge_factor_bit_lift_extra = fudge_factor_bit_lift_extra - 25


    lift_bottom_hex_big = 14 + fudge_factor_bit_lift_extra #18
    
    #technical
    bottom_of_shaft = depth_taper + depth_bottom_hex_big + depth_bottom_hex_small + lift_bottom_hex_big + 3
    #lift_bit = bottom_of_shaft - 5 + fudge_fudge_factor_bit_lift_extra
    radius_little = 4.25/2
    #radius_bit_main = 4/2#4.25/2

    

    #donut cutouts
    orings = []
    length_of_gap = lift_bottom_hex_big /2
    middle_of_hex = depth_taper + depth_bottom_hex_small + length_of_gap
    top_of_hex = middle_of_hex + length_of_gap + depth_bottom_hex_big
    donut_shift = 1.8
    #second_donut_level = top_of_hex + length_of_gap + donut_shift

    inside_only = False
    #inside_only = True

    #optional
    include_knurl = True


    ##### new
    
    #constants
    hex_side_ratio = 1.1547

    #handle variables
    height_driver = 95
    radius_main = 10/2

    

    #hex_top_piece
    depth_top_hex = 9
    radius_top_hex = 13/2 * hex_side_ratio
    lift_top_hex = 45

    #hex_bottom_piece
    depth_bottom_hex = 6
    radius_bottom_hex = 10/2 * hex_side_ratio

    #taper bottom
    depth_taper_bottom = 3
    radius_taper_bottom_hex = radius_bottom_hex / hex_side_ratio

    #top taper
    depth_top_taper = height_driver - lift_top_hex - depth_top_hex
    radius_top_taper_little = radius_top_hex / hex_side_ratio
    radius_top_taper_big = 18/2

    #bit variables
    lift_bit = 14
    radius_bit_main = 4/2
    radius_bit_main_clearance = radius_bit_main + 0.25




    if False:
        oring = {}
        
        #lower oring
        oring["id"] = 8/2
        dep = 150
        oring["depth"] = dep    
        pos1 = copy.deepcopy(pos)
        pos1[2] += middle_of_hex
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[2] += donut_shift * 2
        pos12 = copy.deepcopy(pos1)
        pos12[2] += donut_shift
        pos13 = copy.deepcopy(pos1)
        pos13[2] += -donut_shift
        pos14 = copy.deepcopy(pos1)
        pos14[2] += -donut_shift * 2
        poss.append(pos11)
        poss.append(pos12)
        poss.append(pos13)
        poss.append(pos14)        
        oring["pos"] = poss
        orings.append(oring)

        #top oring
        oring = copy.deepcopy(oring)
        oring["id"] = 11/2
        pos1 = copy.deepcopy(pos)
        pos1[2] += top_of_hex + length_of_gap/2 
        oring["pos"] = pos1
        orings.append(oring)

        #top top small diameter
        oring = copy.deepcopy(oring)
        oring["id"] = 14/2
        dep = 16
        oring["depth"] = dep
        pos1 = copy.deepcopy(pos)
        pos1[2] += height_driver - 15.5
        oring["pos"] = pos1
        orings.append(oring)



        



    #bottom taper piece
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"    
        p3["depth"] = depth_taper_bottom
        p3["shape"] = f"oobb_cylinder"  
        #p3["r2"] = radius_big
        p3["r2"] = radius_taper_bottom_hex
        p3["r1"] = radius_bit_main_clearance
        p3["zz"] = "bottom"
        p3["rot"] = [0,0,0]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)  
        #pos1[1] += 10       
        p3["pos"] = pos1
        if not inside_only:
            oobb_base.append_full(thing,**p3)

    #hex_bottom_piece
    if True:
        #10mm piece
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["height"] = depth_bottom_hex
        p3["radius"] = radius_bottom_hex_small
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth_taper
        p3["pos"] = pos1        
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3)
    
    #main_cylinder
    if True:                
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = height_driver        
        p3["depth"] = dep - depth_taper_bottom
        p3["radius"] = radius_main
        pos1 = copy.deepcopy(pos)
        p3["pos"] = pos1
        pos1[2] += depth_taper_bottom
        p3["zz"] = "bottom"
        #p3["m"] = "#"
        if not inside_only:            
            oobb_base.append_full(thing,**p3)
        
    #hex_top_piece
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["height"] = depth_top_hex
        p3["radius"] = radius_top_hex
        pos1 = copy.deepcopy(pos)
        pos1[2] += lift_top_hex
        p3["pos"] = pos1
        rot1 = [0,0,360/12]
        p3["rot"] = rot1
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3) 

    #top_taper
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = depth_top_taper
        p3["depth"] = dep
        p3["r2"] = radius_top_taper_big
        p3["r1"] = radius_top_taper_little
        pos1 = copy.deepcopy(pos)
        pos1[2] += height_driver
        p3["pos"] = pos1               
        #p3["m"] = "#"
        p3["zz"] = "top"
        if not inside_only:
            pass
            oobb_base.append_full(thing,**p3)
        
    
    
    
    #top piece
    if False:
        old_version = False
        if not old_version:
            #bottom cylinder piece
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"oobb_cylinder"
                dep = height_top/2
                p3["depth"] = dep
                rad = diameter_top / 2
                p3["radius"] = rad
                pos1 = copy.deepcopy(pos)
                current_z = height_driver - height_top
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["rot"] = [0,0,0]
                #p3["m"] = "#"
                if not inside_only:
                    pass
                    oobb_base.append_full(thing,**p3)
            
            #top oring
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "positive"
                p3["shape"] = f"oring"
                oring_diameter = 5
                id = diameter_top - 2*oring_diameter
                p3["id"] = id / 2
                dep = 5
                p3["depth"] = dep    
                pos1 = copy.deepcopy(pos)
                pos1[2] += height_driver - oring_diameter
                p3["pos"] = pos1
                #p3["m"] = "#"
                if not inside_only:
                    pass
                    oobb_base.append_full(thing,**p3)
                
            
            #filler piece
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "positive"
                p3["shape"] = f"oobb_cylinder"
                dep = height_top
                p3["depth"] = dep
                rad = (diameter_top - oring_diameter) / 2
                p3["radius"] = rad
                pos1 = copy.deepcopy(pos)                
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["rot"] = [0,0,0]
                #p3["m"] = "#"
                if not inside_only:
                    pass
                    oobb_base.append_full(thing,**p3)
            
            #knurl
            if include_knurl:
                repeats = 36
                angle = 360 / repeats
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oobb_cube"
                wid = 1.5
                hei = 1.5
                dep = 5
                size = [wid, hei, dep]
                p3["size"] = size
                #p3["m"] = "#"   
                pos1 = copy.deepcopy(pos)
                pos1[0] += 0#wid/2
                pos1[1] += 0#hei/2
                pos1[2] += current_z + dep/2
                p3["pos"] = pos1
                p3["zz"] = "middle" 
                p3["rot"] = [0,0,45]     
                for i in range(repeats):
                    rot = [0,0,angle * i]
                    shift_x = diameter_top/2 + wid/2 #- 0.25
                    shift = [shift_x,0,0]
                    rot_shift = [shift,rot]
                    
                    p3["rot_shift"] = [rot_shift]
                    #p3["rot"] = rot
                    oobb_base.append_full(thing,**p3)
        if old_version:
            #cylinder
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"oobb_cylinder"
                dep = height_top
                p3["depth"] = dep
                rad = diameter_top / 2
                p3["radius"] = rad
                pos1 = copy.deepcopy(pos)
                current_z = height_driver - dep/2
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["rot"] = [0,0,0]
                #p3["m"] = "#"
                if not inside_only:
                    oobb_base.append_full(thing,**p3)
            
            #knurl
            if include_knurl:
                repeats = 36
                angle = 360 / repeats
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oobb_cube"
                wid = 1.5
                hei = 1.5
                dep = 5
                size = [wid, hei, dep]
                p3["size"] = size
                #p3["m"] = "#"   
                pos1 = copy.deepcopy(pos)
                pos1[0] += 0#wid/2
                pos1[1] += 0#hei/2
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["zz"] = "middle" 
                p3["rot"] = [0,0,45]     
                for i in range(repeats):
                    rot = [0,0,angle * i]
                    shift_x = rad + wid/2 #- 0.25
                    shift = [shift_x,0,0]
                    rot_shift = [shift,rot]
                    
                    p3["rot_shift"] = [rot_shift]
                    #p3["rot"] = rot
                    oobb_base.append_full(thing,**p3)

    #add screw locker
    if False:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"        
        p3["shape"] = f"oobb_screw_countersunk"
        dep = 13
        p3["depth"] = dep
        p3["radius_name"] = "m3"
        p3["nut"] = True
        p3["clearance"] = ["top", "bottom"]
        p3["overhang"] = False
        pos1 = copy.deepcopy(pos)
        
        pos1[0] += dep/2
        pos1[1] += 0
        pos1[2] += lift_bottom_hex_big + depth_top_hex - 0.5
        p3["pos"] = pos1
        rot1 = [0,90,0]        
        p3["rot"] = rot1
        #p3["m"] = "#"        
        oobb_base.append_full(thing,**p3)

    #add screw locker clearance
    if False:
        shift_y = 0
        #shift_y = 30      
        extra = 10  
        bot = lift_top_hex - extra
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"        
        p3["shape"] = f"oobb_cube"
        clear = 0.5
        hei = width_bit_locker + clear
        wid = height_bit_locker + clear
        dep = height_driver - bot
        size = [wid, hei, dep]
        p3["size"] = size
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0
        pos1[1] += shift_y
        pos1[2] += bot
        p3["pos"] = pos1
        p3["m"] = "#"
        #p3["zz"] = "mi"
        oobb_base.append_full(thing,**p3)
        
            
    #add lock piece
    if True:
        shift_x = 0

        #lock piece drop
        clear = 0.25
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        wid = height_bit_locker + clear
        hei = width_bit_locker + clear
        dep = height_driver - lift_top_hex - depth_top_hex/2 + depth_bit_locker/2
        height_locker = dep
        size = [wid, hei, dep]
        p3["size"] = size
        pos1 = copy.deepcopy(pos)
        pos1[0] += shift_x
        pos1[1] += 0
        pos1[2] += height_driver
        p3["pos"] = pos1
        p3["m"] = "#"
        p3["zz"] = "top"
        oobb_base.append_full(thing,**p3)

        #bottom lock piece
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube_new"
        wid = height_bit_locker + clear
        hei = width_bit_locker + clear
        dep = depth_bit_locker + clear
        size = [wid, hei, dep]
        p3["size"] = size
        pos1 = copy.deepcopy(pos)
        pos1[0] += shift_x #* 2
        pos1[1] += 0
        pos1[2] += height_driver - height_locker
        p3["pos"] = pos1
        p3["m"] = "#"
        repeats = 100
        angle = -45 / repeats
        for i in range(repeats):
            p4 = copy.deepcopy(p3)
            rot2 = [0,0,angle * i]
            p4["rot"] = rot2
            oobb_base.append_full(thing,**p4)

        #poke hole
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_hole"
        p3["radius_name"] = "m3"    
        #p3["m"] = "#"
        #p3["zz"] = "middle"
        de = 100
        p3["depth"] = de
        pos1 = copy.deepcopy(pos)
        pos1[0] += shift_x - de/2
        pos1[1] += 0
        pos1[2] += height_driver - height_locker + depth_bit_locker/2
        p3["pos"] = pos1
        rot1 = [0,0,0]
        rot1[1] = 90
        p3["rot"] = rot1
        oobb_base.append_full(thing,**p3)

        

    #get holder
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"        
        pos1 = copy.deepcopy(pos)
        #pos1[0] += 20
        pos1[2] += lift_bit
        p3["pos"] = pos1        
        #p3["m"] = "#"    
        p3["clearance"] = 0.2
        p3["clearance_top"] = True
        p3["length"] = 100
        p3["radius_bit_main"] = radius_bit_main
        pos1 = copy.deepcopy(pos)
        
        
        return_value_2 = get_holder_blank(thing, **p3)

    #add lock nut
    if False:

        #add nut cutout
        nut_wall_thickness = 1.75
        fudge_nut_wall_spacing = 0.75
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_nut"
        p3["depth"] = radius_big - nut_wall_thickness
        p3["radius_name"] = "m3"
        #p3["hole"] = True    
        pos1 = copy.deepcopy(pos)        
        pos1[0] += 0
        pos1[1] += 0
        pos1[2] += depth_taper + depth_bottom_hex_small + depth_bottom_hex_big / 2 + lift_bottom_hex_big
        poss = []
        repeats = 5        
        shift_down = 0
        p3["pos"] = poss
        rot = [90,360/12,0]
        p3["rot"] = rot
        p3["m"] = "#"        
        for i in range(repeats):            
            p4 = copy.deepcopy(p3)
            pos11 = copy.deepcopy(pos1)
            shift_down = i * 2.75
            pos11[2] += shift_down
            p4["pos"] = pos11
            oobb_base.append_full(thing,**p4)
        
        #pocket for nut
        p4 = copy.deepcopy(p3)
        pos11 = copy.deepcopy(pos1)
        p4["pos"] = pos11
        p4["depth"] = radius_bottom_hex_big - nut_wall_thickness - fudge_nut_wall_spacing
        oobb_base.append_full(thing,**p4)

        



        #add hole for grub screw
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_hole"
        dep = 12
        p3["depth"] = dep
        #p3["radius_name"] = "m3"
        p3["radius"] = 1.6/2
        p3["include_nut"] = True
        p3["clearance"] = ["top", "bottom"]
        pos12 = copy.deepcopy(pos1)
        pos12[2] += 0
        p3["pos"] = pos12
        rot = [90,0,0]
        p3["rot"] = rot
        p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        #add nut chute
        if False:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_nut"
            p3["radius_name"] = "m3"
            #p3["depth"] = 10
            pos1 = copy.deepcopy(pos)
            pos1[0] += 0
            pos1[1] += 0
            pos1[2] += depth_taper + depth_bottom_hex_small + depth_bottom_hex_big / 2 + lift_bottom_hex_big
            poss = []
            repeats = 30
            shift_down = 3
            for i in range(repeats):
                pos11 = copy.deepcopy(pos1)            
                pos11[2] += shift_down * i
                poss.append(pos11)
            p3["pos"] = poss
            rot = [90,0,0]
            p3["rot"] = rot
            p3["m"] = "#"
            p3["zz"] = "middle"
            oobb_base.append_full(thing,**p3)

            

    #add orings
    if False:
    #if False:
        for oring in orings:
            oring_poss = oring["pos"]
            #if not an array of arrays make it one
            if not isinstance(oring_poss[0], list):
                oring_poss = [oring_poss]            
            for oring_pos in oring_poss:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oring"
                p3["depth"] = oring["depth"]
                p3["id"] = oring["id"]
                pos1 = copy.deepcopy(pos)
                pos1[0] += oring_pos[0]
                pos1[1] += oring_pos[1]
                pos1[2] += oring_pos[2]
                p3["pos"] = pos1

                #p3["m"] = "#"
                if not inside_only:
                    oobb_base.append_full(thing,**p3)

    #fluting
    if False:
        diameter_flute_tube = 5
        diameter_flute_ring = 150
        center_gap = 7
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oring"
        p3["depth"] = diameter_flute_tube/2
        p3["id"] = diameter_flute_ring/2
        pos1 = copy.deepcopy(pos)
        pos1[0] += diameter_flute_ring/2 + diameter_flute_tube/2 + center_gap/2
        pos1[1] += 0
        pos1[2] += middle_of_hex
        p3["pos"] = pos1
        #p3["m"] = "#"
        rot = [90,0,0]
        p3["rot"] = rot
        #rot_shift
        repeats = 6
        angle = 360 / repeats
        for i in range(repeats):
            rot = [0,0,angle * i]
            shift = [0,0,0]
            rot_shift = [shift,rot]
            p3["rot_shift"] = [rot_shift]
            oobb_base.append_full(thing,**p3)    


def get_precision_screwdriver_old_3_twist_lock_maybe_wrong_handed(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #main
    radius_big = 10/2
    
    #height_driver = 95
    
    diameter_top_taper = 18
    height_top = 5
    height_top_taper = 35  - height_top
    diameter_top = 18
    #taper
    depth_taper = 3    
    #hex
    hex_side_ratio = 1.1547
    radius_bottom_hex_small = 10/2 * hex_side_ratio
    radius_bottom_hex_big = 13/2 * hex_side_ratio
    depth_bottom_hex_small = 6
    depth_bottom_hex_big = 9

    fudge_factor_bit_lift_extra = 27 
    fudge_fudge_factor_bit_lift_extra = fudge_factor_bit_lift_extra - 25


    lift_bottom_hex_big = 14 + fudge_factor_bit_lift_extra #18
    
    #technical
    bottom_of_shaft = depth_taper + depth_bottom_hex_big + depth_bottom_hex_small + lift_bottom_hex_big + 3
    #lift_bit = bottom_of_shaft - 5 + fudge_fudge_factor_bit_lift_extra
    radius_little = 4.25/2
    #radius_bit_main = 4/2#4.25/2

    

    #donut cutouts
    orings = []
    length_of_gap = lift_bottom_hex_big /2
    middle_of_hex = depth_taper + depth_bottom_hex_small + length_of_gap
    top_of_hex = middle_of_hex + length_of_gap + depth_bottom_hex_big
    donut_shift = 1.8
    #second_donut_level = top_of_hex + length_of_gap + donut_shift

    inside_only = False
    #inside_only = True

    #optional
    include_knurl = True


    ##### new
    
    #constants
    hex_side_ratio = 1.1547

    #handle variables
    height_driver = 95
    radius_main = 10/2

    

    #hex_top_piece
    depth_top_hex = 9
    radius_top_hex = 13/2 * hex_side_ratio
    lift_top_hex = 45

    #hex_bottom_piece
    depth_bottom_hex = 6
    radius_bottom_hex = 10/2 * hex_side_ratio

    #taper bottom
    depth_taper_bottom = 3
    radius_taper_bottom_hex = radius_bottom_hex / hex_side_ratio

    #top taper
    depth_top_taper = height_driver - lift_top_hex - depth_top_hex
    radius_top_taper_little = radius_top_hex / hex_side_ratio
    radius_top_taper_big = 18/2

    #bit variables
    lift_bit = 14
    radius_bit_main = 4/2
    radius_bit_main_clearance = radius_bit_main + 0.25




    if False:
        oring = {}
        
        #lower oring
        oring["id"] = 8/2
        dep = 150
        oring["depth"] = dep    
        pos1 = copy.deepcopy(pos)
        pos1[2] += middle_of_hex
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[2] += donut_shift * 2
        pos12 = copy.deepcopy(pos1)
        pos12[2] += donut_shift
        pos13 = copy.deepcopy(pos1)
        pos13[2] += -donut_shift
        pos14 = copy.deepcopy(pos1)
        pos14[2] += -donut_shift * 2
        poss.append(pos11)
        poss.append(pos12)
        poss.append(pos13)
        poss.append(pos14)        
        oring["pos"] = poss
        orings.append(oring)

        #top oring
        oring = copy.deepcopy(oring)
        oring["id"] = 11/2
        pos1 = copy.deepcopy(pos)
        pos1[2] += top_of_hex + length_of_gap/2 
        oring["pos"] = pos1
        orings.append(oring)

        #top top small diameter
        oring = copy.deepcopy(oring)
        oring["id"] = 14/2
        dep = 16
        oring["depth"] = dep
        pos1 = copy.deepcopy(pos)
        pos1[2] += height_driver - 15.5
        oring["pos"] = pos1
        orings.append(oring)



        



    #bottom taper piece
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"    
        p3["depth"] = depth_taper_bottom
        p3["shape"] = f"oobb_cylinder"  
        #p3["r2"] = radius_big
        p3["r2"] = radius_taper_bottom_hex
        p3["r1"] = radius_bit_main_clearance
        p3["zz"] = "bottom"
        p3["rot"] = [0,0,0]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)  
        #pos1[1] += 10       
        p3["pos"] = pos1
        if not inside_only:
            oobb_base.append_full(thing,**p3)

    #hex_bottom_piece
    if True:
        #10mm piece
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["height"] = depth_bottom_hex
        p3["radius"] = radius_bottom_hex_small
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth_taper
        p3["pos"] = pos1        
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3)
    
    #main_cylinder
    if True:                
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = height_driver        
        p3["depth"] = dep - depth_taper_bottom
        p3["radius"] = radius_main
        pos1 = copy.deepcopy(pos)
        p3["pos"] = pos1
        pos1[2] += depth_taper_bottom
        p3["zz"] = "bottom"
        #p3["m"] = "#"
        if not inside_only:            
            oobb_base.append_full(thing,**p3)
        
    #hex_top_piece
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["height"] = depth_top_hex
        p3["radius"] = radius_top_hex
        pos1 = copy.deepcopy(pos)
        pos1[2] += lift_top_hex
        p3["pos"] = pos1
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3) 

    #top_taper
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = depth_top_taper
        p3["depth"] = dep
        p3["r2"] = radius_top_taper_big
        p3["r1"] = radius_top_taper_little
        pos1 = copy.deepcopy(pos)
        pos1[2] += height_driver
        p3["pos"] = pos1               
        #p3["m"] = "#"
        p3["zz"] = "top"
        if not inside_only:
            pass
            oobb_base.append_full(thing,**p3)
        
    
    
    
    #top piece
    if False:
        old_version = False
        if not old_version:
            #bottom cylinder piece
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"oobb_cylinder"
                dep = height_top/2
                p3["depth"] = dep
                rad = diameter_top / 2
                p3["radius"] = rad
                pos1 = copy.deepcopy(pos)
                current_z = height_driver - height_top
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["rot"] = [0,0,0]
                #p3["m"] = "#"
                if not inside_only:
                    pass
                    oobb_base.append_full(thing,**p3)
            
            #top oring
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "positive"
                p3["shape"] = f"oring"
                oring_diameter = 5
                id = diameter_top - 2*oring_diameter
                p3["id"] = id / 2
                dep = 5
                p3["depth"] = dep    
                pos1 = copy.deepcopy(pos)
                pos1[2] += height_driver - oring_diameter
                p3["pos"] = pos1
                #p3["m"] = "#"
                if not inside_only:
                    pass
                    oobb_base.append_full(thing,**p3)
                
            
            #filler piece
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "positive"
                p3["shape"] = f"oobb_cylinder"
                dep = height_top
                p3["depth"] = dep
                rad = (diameter_top - oring_diameter) / 2
                p3["radius"] = rad
                pos1 = copy.deepcopy(pos)                
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["rot"] = [0,0,0]
                #p3["m"] = "#"
                if not inside_only:
                    pass
                    oobb_base.append_full(thing,**p3)
            
            #knurl
            if include_knurl:
                repeats = 36
                angle = 360 / repeats
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oobb_cube"
                wid = 1.5
                hei = 1.5
                dep = 5
                size = [wid, hei, dep]
                p3["size"] = size
                #p3["m"] = "#"   
                pos1 = copy.deepcopy(pos)
                pos1[0] += 0#wid/2
                pos1[1] += 0#hei/2
                pos1[2] += current_z + dep/2
                p3["pos"] = pos1
                p3["zz"] = "middle" 
                p3["rot"] = [0,0,45]     
                for i in range(repeats):
                    rot = [0,0,angle * i]
                    shift_x = diameter_top/2 + wid/2 #- 0.25
                    shift = [shift_x,0,0]
                    rot_shift = [shift,rot]
                    
                    p3["rot_shift"] = [rot_shift]
                    #p3["rot"] = rot
                    oobb_base.append_full(thing,**p3)
        if old_version:
            #cylinder
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"oobb_cylinder"
                dep = height_top
                p3["depth"] = dep
                rad = diameter_top / 2
                p3["radius"] = rad
                pos1 = copy.deepcopy(pos)
                current_z = height_driver - dep/2
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["rot"] = [0,0,0]
                #p3["m"] = "#"
                if not inside_only:
                    oobb_base.append_full(thing,**p3)
            
            #knurl
            if include_knurl:
                repeats = 36
                angle = 360 / repeats
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oobb_cube"
                wid = 1.5
                hei = 1.5
                dep = 5
                size = [wid, hei, dep]
                p3["size"] = size
                #p3["m"] = "#"   
                pos1 = copy.deepcopy(pos)
                pos1[0] += 0#wid/2
                pos1[1] += 0#hei/2
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["zz"] = "middle" 
                p3["rot"] = [0,0,45]     
                for i in range(repeats):
                    rot = [0,0,angle * i]
                    shift_x = rad + wid/2 #- 0.25
                    shift = [shift_x,0,0]
                    rot_shift = [shift,rot]
                    
                    p3["rot_shift"] = [rot_shift]
                    #p3["rot"] = rot
                    oobb_base.append_full(thing,**p3)


    #add bit locker clearance
    if True:
        shift_y = 0
        #shift_y = 30
        lif = 3
        bot = lift_top_hex + lif
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"        
        p3["shape"] = f"oobb_cube"
        clear = 0.5
        hei = width_bit_locker + clear
        wid = height_bit_locker + clear
        dep = height_driver - bot
        size = [wid, hei, dep]
        p3["size"] = size
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0
        pos1[1] += shift_y
        pos1[2] += bot
        p3["pos"] = pos1
        p3["m"] = "#"
        #p3["zz"] = "mi"
        oobb_base.append_full(thing,**p3)
        
        #add twist_clearance
        if True:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"        
            p3["shape"] = f"oobb_cube_new"
            wid = wid
            hei = hei
            dep = depth_bit_locker + clear
            size = [wid, hei, dep]
            p3["size"] = size            
            pos1 = copy.deepcopy(pos)
            pos1[0] += 0
            pos1[1] += shift_y
            pos1[2] += bot
            p3["pos"] = pos1
            p3["m"] = "#"
            p3["zz"] = "bottom"
            repeats = 100
            angle = 45 / repeats
            for i in range(repeats):
                rot = [0,0,angle * i]
                p3["rot"] = rot
                oobb_base.append_full(thing,**p3)
            


        

    #get holder
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"        
        pos1 = copy.deepcopy(pos)
        #pos1[0] += 20
        pos1[2] += lift_bit
        p3["pos"] = pos1        
        #p3["m"] = "#"    
        p3["clearance"] = 0.2
        p3["clearance_top"] = True
        p3["length"] = 100
        p3["radius_bit_main"] = radius_bit_main
        pos1 = copy.deepcopy(pos)
        
        
        return_value_2 = get_holder_blank(thing, **p3)

    #add lock nut
    if False:

        #add nut cutout
        nut_wall_thickness = 1.75
        fudge_nut_wall_spacing = 0.75
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_nut"
        p3["depth"] = radius_big - nut_wall_thickness
        p3["radius_name"] = "m3"
        #p3["hole"] = True    
        pos1 = copy.deepcopy(pos)        
        pos1[0] += 0
        pos1[1] += 0
        pos1[2] += depth_taper + depth_bottom_hex_small + depth_bottom_hex_big / 2 + lift_bottom_hex_big
        poss = []
        repeats = 5        
        shift_down = 0
        p3["pos"] = poss
        rot = [90,360/12,0]
        p3["rot"] = rot
        p3["m"] = "#"        
        for i in range(repeats):            
            p4 = copy.deepcopy(p3)
            pos11 = copy.deepcopy(pos1)
            shift_down = i * 2.75
            pos11[2] += shift_down
            p4["pos"] = pos11
            oobb_base.append_full(thing,**p4)
        
        #pocket for nut
        p4 = copy.deepcopy(p3)
        pos11 = copy.deepcopy(pos1)
        p4["pos"] = pos11
        p4["depth"] = radius_bottom_hex_big - nut_wall_thickness - fudge_nut_wall_spacing
        oobb_base.append_full(thing,**p4)

        



        #add hole for grub screw
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_hole"
        dep = 12
        p3["depth"] = dep
        #p3["radius_name"] = "m3"
        p3["radius"] = 1.6/2
        p3["include_nut"] = True
        p3["clearance"] = ["top", "bottom"]
        pos12 = copy.deepcopy(pos1)
        pos12[2] += 0
        p3["pos"] = pos12
        rot = [90,0,0]
        p3["rot"] = rot
        p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        #add nut chute
        if False:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_nut"
            p3["radius_name"] = "m3"
            #p3["depth"] = 10
            pos1 = copy.deepcopy(pos)
            pos1[0] += 0
            pos1[1] += 0
            pos1[2] += depth_taper + depth_bottom_hex_small + depth_bottom_hex_big / 2 + lift_bottom_hex_big
            poss = []
            repeats = 30
            shift_down = 3
            for i in range(repeats):
                pos11 = copy.deepcopy(pos1)            
                pos11[2] += shift_down * i
                poss.append(pos11)
            p3["pos"] = poss
            rot = [90,0,0]
            p3["rot"] = rot
            p3["m"] = "#"
            p3["zz"] = "middle"
            oobb_base.append_full(thing,**p3)

            

    #add orings
    if False:
    #if False:
        for oring in orings:
            oring_poss = oring["pos"]
            #if not an array of arrays make it one
            if not isinstance(oring_poss[0], list):
                oring_poss = [oring_poss]            
            for oring_pos in oring_poss:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oring"
                p3["depth"] = oring["depth"]
                p3["id"] = oring["id"]
                pos1 = copy.deepcopy(pos)
                pos1[0] += oring_pos[0]
                pos1[1] += oring_pos[1]
                pos1[2] += oring_pos[2]
                p3["pos"] = pos1

                #p3["m"] = "#"
                if not inside_only:
                    oobb_base.append_full(thing,**p3)

    #fluting
    if False:
        diameter_flute_tube = 5
        diameter_flute_ring = 150
        center_gap = 7
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oring"
        p3["depth"] = diameter_flute_tube/2
        p3["id"] = diameter_flute_ring/2
        pos1 = copy.deepcopy(pos)
        pos1[0] += diameter_flute_ring/2 + diameter_flute_tube/2 + center_gap/2
        pos1[1] += 0
        pos1[2] += middle_of_hex
        p3["pos"] = pos1
        #p3["m"] = "#"
        rot = [90,0,0]
        p3["rot"] = rot
        #rot_shift
        repeats = 6
        angle = 360 / repeats
        for i in range(repeats):
            rot = [0,0,angle * i]
            shift = [0,0,0]
            rot_shift = [shift,rot]
            p3["rot_shift"] = [rot_shift]
            oobb_base.append_full(thing,**p3)    

    
def get_precision_screwdriver_old_2(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    

    #main
    radius_big = 10/2
    
    height_driver = 95
    
    diameter_top_taper = 18
    height_top = 5
    height_top_taper = 35  - height_top
    diameter_top = 18
    #taper
    depth_taper = 3    
    #hex
    hex_side_ratio = 1.1547
    radius_bottom_hex_small = 10/2 * hex_side_ratio
    radius_bottom_hex_big = 13/2 * hex_side_ratio
    depth_bottom_hex_small = 6
    depth_bottom_hex_big = 9

    fudge_factor_bit_lift_extra = 27 
    fudge_fudge_factor_bit_lift_extra = fudge_factor_bit_lift_extra - 25


    lift_bottom_hex_big = 14 + fudge_factor_bit_lift_extra #18
    
    #technical
    bottom_of_shaft = depth_taper + depth_bottom_hex_big + depth_bottom_hex_small + lift_bottom_hex_big + 3
    lift_bit = bottom_of_shaft - 5 + fudge_fudge_factor_bit_lift_extra
    radius_little = 4.25/2
    radius_bit_main = 4/2#4.25/2

    

    #donut cutouts
    orings = []
    length_of_gap = lift_bottom_hex_big /2
    middle_of_hex = depth_taper + depth_bottom_hex_small + length_of_gap
    top_of_hex = middle_of_hex + length_of_gap + depth_bottom_hex_big
    donut_shift = 1.8
    #second_donut_level = top_of_hex + length_of_gap + donut_shift

    inside_only = False
    #inside_only = True

    #optional
    include_knurl = True

    if True:
        oring = {}
        
        #lower oring
        oring["id"] = 8/2
        dep = 150
        oring["depth"] = dep    
        pos1 = copy.deepcopy(pos)
        pos1[2] += middle_of_hex
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[2] += donut_shift * 2
        pos12 = copy.deepcopy(pos1)
        pos12[2] += donut_shift
        pos13 = copy.deepcopy(pos1)
        pos13[2] += -donut_shift
        pos14 = copy.deepcopy(pos1)
        pos14[2] += -donut_shift * 2
        poss.append(pos11)
        poss.append(pos12)
        poss.append(pos13)
        poss.append(pos14)        
        oring["pos"] = poss
        orings.append(oring)

        #top oring
        oring = copy.deepcopy(oring)
        oring["id"] = 11/2
        pos1 = copy.deepcopy(pos)
        pos1[2] += top_of_hex + length_of_gap/2 
        oring["pos"] = pos1
        orings.append(oring)

        #top top small diameter
        oring = copy.deepcopy(oring)
        oring["id"] = 14/2
        dep = 16
        oring["depth"] = dep
        pos1 = copy.deepcopy(pos)
        pos1[2] += height_driver - 15.5
        oring["pos"] = pos1
        orings.append(oring)



    #second try
    if False:
        oring = {}
        oring["id"] = 8/2
        dep = 45
        oring["depth"] = dep    
        pos1 = copy.deepcopy(pos)
        pos1[2] += middle_of_hex - donut_shift
        oring["pos"] = pos1
        orings.append(oring)

        oring = copy.deepcopy(oring)
        pos1 = copy.deepcopy(pos)
        pos1[2] += second_donut_level
        oring["pos"] = pos1
        orings.append(oring)

        oring = {}
        oring["id"] = 9/2
        dep = 300
        oring["depth"] = dep
        pos1 = copy.deepcopy(pos)
        pos1[2] += 60
        oring["pos"] = pos1
        orings.append(oring)


    #old donuts
    if False:

        oring = {}
        oring["id"] = 11/2
        dep = 100
        oring["depth"] = dep    
        pos1 = copy.deepcopy(pos)
        pos1[2] += bottom_of_shaft + 6
        oring["pos"] = pos1
        #orings.append(oring)

        default_oring = copy.deepcopy(oring)

        oring = copy.deepcopy(default_oring)
        oring["id"] = 8/2
        dep = 70
        oring["depth"] = dep 
        pos1 = copy.deepcopy(pos)
        pos1[2] += bottom_of_shaft - 24
        oring["pos"] = pos1
        #orings.append(oring)


        oring = copy.deepcopy(default_oring)
        oring["id"] = 11.5/2
        dep = 120
        oring["depth"] = dep 
        pos1 = copy.deepcopy(pos)
        pos1[2] += height_driver - 32.5
        oring["pos"] = pos1    
        #orings.append(oring)

        



    #bottom taper piece
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"    
        p3["depth"] = depth_taper
        p3["shape"] = f"oobb_cylinder"  
        #p3["r2"] = radius_big
        p3["r2"] = radius_bottom_hex_small - 1
        p3["r1"] = radius_little
        p3["zz"] = "bottom"
        p3["rot"] = [0,0,0]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)  
        #pos1[1] += 10       
        p3["pos"] = pos1
        if not inside_only:
            oobb_base.append_full(thing,**p3)
        
    
    #main_cylinder
    if True:    
    #if False:    
        hex_offset = 0
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = height_driver - hex_offset - height_top_taper
        reduction =  depth_taper + depth_bottom_hex_small 
        p3["depth"] = dep - reduction
        p3["radius"] = radius_big
        pos1 = copy.deepcopy(pos)
        pos1[2] += reduction
        p3["pos"] = pos1
        p3["rot"] = [0,0,0]
        p3["zz"] = "bottom"
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3)
        
    #top_taper
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        dep = height_top_taper
        p3["depth"] = dep
        p3["r2"] = diameter_top_taper / 2
        p3["r1"] = radius_big
        pos1 = copy.deepcopy(pos)
        pos1[2] += height_driver - height_top_taper/2 - height_top
        p3["pos"] = pos1               
        #p3["m"] = "#"
        if not inside_only:
            pass
            oobb_base.append_full(thing,**p3)
        
    #top piece
    if True:
        old_version = False
        if not old_version:
            #bottom cylinder piece
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"oobb_cylinder"
                dep = height_top/2
                p3["depth"] = dep
                rad = diameter_top / 2
                p3["radius"] = rad
                pos1 = copy.deepcopy(pos)
                current_z = height_driver - height_top
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["rot"] = [0,0,0]
                #p3["m"] = "#"
                if not inside_only:
                    pass
                    oobb_base.append_full(thing,**p3)
            
            #top oring
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "positive"
                p3["shape"] = f"oring"
                oring_diameter = 5
                id = diameter_top - 2*oring_diameter
                p3["id"] = id / 2
                dep = 5
                p3["depth"] = dep    
                pos1 = copy.deepcopy(pos)
                pos1[2] += height_driver - oring_diameter
                p3["pos"] = pos1
                #p3["m"] = "#"
                if not inside_only:
                    pass
                    oobb_base.append_full(thing,**p3)
                
            
            #filler piece
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "positive"
                p3["shape"] = f"oobb_cylinder"
                dep = height_top
                p3["depth"] = dep
                rad = (diameter_top - oring_diameter) / 2
                p3["radius"] = rad
                pos1 = copy.deepcopy(pos)                
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["rot"] = [0,0,0]
                #p3["m"] = "#"
                if not inside_only:
                    pass
                    oobb_base.append_full(thing,**p3)
            
            #knurl
            if include_knurl:
                repeats = 36
                angle = 360 / repeats
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oobb_cube"
                wid = 1.5
                hei = 1.5
                dep = 5
                size = [wid, hei, dep]
                p3["size"] = size
                #p3["m"] = "#"   
                pos1 = copy.deepcopy(pos)
                pos1[0] += 0#wid/2
                pos1[1] += 0#hei/2
                pos1[2] += current_z + dep/2
                p3["pos"] = pos1
                p3["zz"] = "middle" 
                p3["rot"] = [0,0,45]     
                for i in range(repeats):
                    rot = [0,0,angle * i]
                    shift_x = diameter_top/2 + wid/2 #- 0.25
                    shift = [shift_x,0,0]
                    rot_shift = [shift,rot]
                    
                    p3["rot_shift"] = [rot_shift]
                    #p3["rot"] = rot
                    oobb_base.append_full(thing,**p3)
        if old_version:
            #cylinder
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"oobb_cylinder"
                dep = height_top
                p3["depth"] = dep
                rad = diameter_top / 2
                p3["radius"] = rad
                pos1 = copy.deepcopy(pos)
                current_z = height_driver - dep/2
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["rot"] = [0,0,0]
                #p3["m"] = "#"
                if not inside_only:
                    oobb_base.append_full(thing,**p3)
            
            #knurl
            if include_knurl:
                repeats = 36
                angle = 360 / repeats
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oobb_cube"
                wid = 1.5
                hei = 1.5
                dep = 5
                size = [wid, hei, dep]
                p3["size"] = size
                #p3["m"] = "#"   
                pos1 = copy.deepcopy(pos)
                pos1[0] += 0#wid/2
                pos1[1] += 0#hei/2
                pos1[2] += current_z
                p3["pos"] = pos1
                p3["zz"] = "middle" 
                p3["rot"] = [0,0,45]     
                for i in range(repeats):
                    rot = [0,0,angle * i]
                    shift_x = rad + wid/2 #- 0.25
                    shift = [shift_x,0,0]
                    rot_shift = [shift,rot]
                    
                    p3["rot_shift"] = [rot_shift]
                    #p3["rot"] = rot
                    oobb_base.append_full(thing,**p3)


    #hex_bottom
    if True:
        #10mm piece
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["height"] = depth_bottom_hex_small
        p3["radius"] = radius_bottom_hex_small
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth_taper
        p3["pos"] = pos1        
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3)
        
        #13 mm piece
        p3 = copy.deepcopy(p3)
        p3["height"] = depth_bottom_hex_big
        p3["radius"] = radius_bottom_hex_big
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth_taper + depth_bottom_hex_small + lift_bottom_hex_big
        p3["pos"] = pos1
        #p3["m"] = "#"
        if not inside_only:
            oobb_base.append_full(thing,**p3)
        

    #get holder
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        #p3["type"] = "p"
        pos1 = copy.deepcopy(pos)
        #pos1[0] += 20
        pos1[2] += lift_bit
        p3["pos"] = pos1

        p3["rot"] = [0,0,0]
        p3["m"] = "#"    
        p3["clearance"] = 0.2
        p3["clearance_top"] = True
        p3["radius_bit_main"] = radius_bit_main
        pos1 = copy.deepcopy(pos)
        
        
        return_value_2 = get_holder_blank(thing, **p3)

    #add lock nut
    if True:

        #add nut cutout
        nut_wall_thickness = 1.75
        fudge_nut_wall_spacing = 0.75
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_nut"
        p3["depth"] = radius_big - nut_wall_thickness
        p3["radius_name"] = "m3"
        #p3["hole"] = True    
        pos1 = copy.deepcopy(pos)        
        pos1[0] += 0
        pos1[1] += 0
        pos1[2] += depth_taper + depth_bottom_hex_small + depth_bottom_hex_big / 2 + lift_bottom_hex_big
        poss = []
        repeats = 5        
        shift_down = 0
        p3["pos"] = poss
        rot = [90,360/12,0]
        p3["rot"] = rot
        p3["m"] = "#"        
        for i in range(repeats):            
            p4 = copy.deepcopy(p3)
            pos11 = copy.deepcopy(pos1)
            shift_down = i * 2.75
            pos11[2] += shift_down
            p4["pos"] = pos11
            oobb_base.append_full(thing,**p4)
        
        #pocket for nut
        p4 = copy.deepcopy(p3)
        pos11 = copy.deepcopy(pos1)
        p4["pos"] = pos11
        p4["depth"] = radius_bottom_hex_big - nut_wall_thickness - fudge_nut_wall_spacing
        oobb_base.append_full(thing,**p4)

        



        #add hole for grub screw
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_hole"
        dep = 12
        p3["depth"] = dep
        #p3["radius_name"] = "m3"
        p3["radius"] = 1.6/2
        p3["include_nut"] = True
        p3["clearance"] = ["top", "bottom"]
        pos12 = copy.deepcopy(pos1)
        pos12[2] += 0
        p3["pos"] = pos12
        rot = [90,0,0]
        p3["rot"] = rot
        p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        #add nut chute
        if False:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_nut"
            p3["radius_name"] = "m3"
            #p3["depth"] = 10
            pos1 = copy.deepcopy(pos)
            pos1[0] += 0
            pos1[1] += 0
            pos1[2] += depth_taper + depth_bottom_hex_small + depth_bottom_hex_big / 2 + lift_bottom_hex_big
            poss = []
            repeats = 30
            shift_down = 3
            for i in range(repeats):
                pos11 = copy.deepcopy(pos1)            
                pos11[2] += shift_down * i
                poss.append(pos11)
            p3["pos"] = poss
            rot = [90,0,0]
            p3["rot"] = rot
            p3["m"] = "#"
            p3["zz"] = "middle"
            oobb_base.append_full(thing,**p3)

            

    #add orings
    if True:
    #if False:
        for oring in orings:
            oring_poss = oring["pos"]
            #if not an array of arrays make it one
            if not isinstance(oring_poss[0], list):
                oring_poss = [oring_poss]            
            for oring_pos in oring_poss:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oring"
                p3["depth"] = oring["depth"]
                p3["id"] = oring["id"]
                pos1 = copy.deepcopy(pos)
                pos1[0] += oring_pos[0]
                pos1[1] += oring_pos[1]
                pos1[2] += oring_pos[2]
                p3["pos"] = pos1

                #p3["m"] = "#"
                if not inside_only:
                    oobb_base.append_full(thing,**p3)

    #fluting
    if True:
        diameter_flute_tube = 5
        diameter_flute_ring = 150
        center_gap = 7
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oring"
        p3["depth"] = diameter_flute_tube/2
        p3["id"] = diameter_flute_ring/2
        pos1 = copy.deepcopy(pos)
        pos1[0] += diameter_flute_ring/2 + diameter_flute_tube/2 + center_gap/2
        pos1[1] += 0
        pos1[2] += middle_of_hex
        p3["pos"] = pos1
        #p3["m"] = "#"
        rot = [90,0,0]
        p3["rot"] = rot
        #rot_shift
        repeats = 6
        angle = 360 / repeats
        for i in range(repeats):
            rot = [0,0,angle * i]
            shift = [0,0,0]
            rot_shift = [shift,rot]
            p3["rot_shift"] = [rot_shift]
            oobb_base.append_full(thing,**p3)    

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [0,0,180]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # left
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -250
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_precision_screwdriver_old_1(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    radius_big = 12/2
    radius_little = 4
    height_driver = 50
    depth_taper = 20
    lift_bit = 10
    #hex holder bottom
    
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"    
    p3["depth"] = depth_taper
    p3["shape"] = f"oobb_cylinder"  
    p3["r2"] = radius_big
    p3["r1"] = radius_little
    p3["zz"] = "bottom"
    p3["rot"] = [0,0,0]
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add cylinder top
    hex_offset = 10
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    dep = height_driver - hex_offset
    p3["depth"] = dep
    p3["radius"] = radius_big
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth_taper
    p3["pos"] = pos1
    p3["rot"] = [0,0,0]
    p3["zz"] = "bottom"
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)



    

    
    #get holder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    #p3["type"] = "p"
    pos1 = copy.deepcopy(pos)
    pos1[2] += lift_bit
    p3["pos"] = pos1

    p3["rot"] = [0,0,0]
    p3["m"] = "#"    
    p3["clearance"] = 0.2
    p3["clearance_top"] = True
    return_value_2 = get_holder_blank(thing, **p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [0,0,180]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # left
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -250
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


def get_holder_blank(thing, **kwargs):
    clearance = kwargs.get("clearance", 0)
    include_bit = kwargs.get("include_bit", True)
    clearance_top = kwargs.get("clearance_top", False)
    radius_bit_main = kwargs.get("radius_bit_main", 3.5/2)
    pos = kwargs.get("pos", [0, 0, 0])

    length = kwargs.get("length", 150)

    # setting up for rotation object
    typ = kwargs.get("type", "p")
    kwargs["type"] = "positive" #needs to be positive for the difference to work
    rot_original = get_rot(**kwargs)   
    kwargs.pop("rot", None)
    kwargs.pop("rot_x", None)
    kwargs.pop("rot_y", None)
    kwargs.pop("rot_z", None)

    # storing pos and popping it out to add it in rotation element     
    pos_original = copy.deepcopy(copy.deepcopy(kwargs.get("pos", [0, 0, 0])))
    pos_original_original = copy.deepcopy(pos_original)
    kwargs.pop("pos", None)
    pos = [0,0,0]
    

    
    return_value = []

    #hex shank
    if True:
        #hex bit is 0.25 inch6.35 mm
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["radius"] = (0.25 * 25.4) / 2  * 1.1546 + clearance# 7.32 hopefully 
        height_total = 28 + clearance 
        height_total_local = height_total       
        if clearance_top:
            height_total_local += 200
        else:
            height_total_local = height_total
        p3["height"] = height_total_local
        #p3["depth"] = 4
        pos1 = copy.deepcopy(pos)
        pos1[0] += clearance /2
        p3["pos"] = pos1
        #p3["m"] = "#"    
        return_value.append(oobb_base.oobb_easy(**p3))

    #donut cutouts
    if False:
        #1/16       1/16 inch bit is    1.5875 mm or    0.0625 inch
        #2/16       1/8 inch bit is     3.175 mm or     0.125 inch
        #3/16       3/16 inch bit is    4.7625 mm or    0.1875 inch
        #4/16       1/4 inch bit is     6.35 mm or      0.25 inch
        #5/16       5/16 inch bit is    7.9375 mm or    0.3125 inch
        #6/16       3/8 inch bit is     9.525 mm or     0.375 inch
        #7/16       7/16 inch bit is    11.1125 mm or   0.4375 inch
        #8/16       1/2 inch bit is     12.7 mm or      0.5 inch

        #middle one
        #the donut cutout
        if True:
            #smallest bit is 0.1875 3/16"            
            smallest_bit = 0.1875 * 25.4 - clearance
            # too small     bead_diameter = 0.25 * 25.4
            bead_diameter = (5/16) * 25.4 - clearance
            # too big       bead_diameter = (3/8) * 25.4
            diameter = smallest_bit
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oring"
            p3["depth"] = bead_diameter
            p3["id"] = diameter / 2
            pos1 = copy.deepcopy(pos)
            # top piece too short pos1[2] += height_total - (3/8) * 25.4
            # top piece even shorter pos1[2] += height_total - (5/16) * 25.4
            # top piece too longpos1[2] += height_total - (7/16) * 25.4
            pos1[2] += 17
            #pos1[2] += height_total
            p3["pos"] = pos1
            #p3["m"] = "#"
            return_value.append(oobb_base.oobb_easy(**p3))
    #joining screws
    if False:
        shift_screw = 17
        offset_screw  = 5 
        depth_screw = 12

        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        
        p3["depth"] = depth_screw
        p3["radius_name"] = "m3"
        p3["include_nut"] = True    
        pos1 = copy.deepcopy(pos)        
        pos1[0] += offset_screw
        pos1[1] += -depth_screw/2
        pos1[2] += shift_screw
        p3["pos"] = pos1
        rot = [90,360/12,0]
        p3["rot"] = rot
        p3["m"] = "#"
        p3["clearance"] = ["top", "bottom"]
        oobb_base.append_full(thing,**p3)

        p3 = copy.deepcopy(p3)
        pos1 = copy.deepcopy(p3["pos"])        
        pos1[0] += -offset_screw * 2
        pos1[1] += depth_screw 
        p3["pos"] = pos1
        p3["m"] = "#"
        rot1 = copy.deepcopy(rot)
        rot1[2] += 180 

        p3["rot"] = rot1
        oobb_base.append_full(thing,**p3)
        # bottom one at 0,0,0
        # cone not a donut
        #p3 = copy.deepcopy(p3)
        #pos1 = copy.deepcopy(pos)
        #p3["pos"] = pos1
        #p3["m"] = "#"
        #return_value.append(oobb_base.oobb_easy(**p3))

    #cutout at bottom
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"tube_new"
        p3["height"] = 2
        p3["r2"]= 7.35/2 + clearance/2
        #p3["r1"]= 3.5/2
        p3["r1"]= radius_bit_main + clearance/2
        p3["wall_thickness"] = 8
        pos1 = copy.deepcopy(pos)        
        p3["pos"] = pos1
        #p3["m"] = "#"
        return_value.append(oobb_base.oobb_easy(**p3))

    if include_bit:
        #add bit
        p3 = copy.deepcopy(kwargs)
        #p3["type"] = "n"
        p3["shape"] = f"oobb_cylinder"
        dep = length
        p3["depth"] = dep
        
        p3["radius"] = radius_bit_main + clearance / 2
        pos1 = copy.deepcopy(pos)         
        pos1[2] += -dep/2 + height_total
        p3["pos"] = pos1
        #p3["m"] = "#"
        return_value.append(oobb_base.oobb_easy(**p3))


    # packaging as a rotation object
    return_value_2 = {}
    return_value_2["type"]  = "rotation"
    return_value_2["typetype"]  = typ
    return_value_2["pos"] = pos_original
    return_value_2["rot"] = rot_original
    return_value_2["objects"] = return_value
    return_value_2 = [return_value_2]


    thing["components"].append(return_value_2)

def get_rot(**kwargs):
    rot = kwargs.get("rot", "")
    if rot == "":
        rot_x = kwargs.get('rot_x',0)
        rot_y = kwargs.get('rot_y',0)
        rot_z = kwargs.get('rot_z',0)
        rot = [rot_x, rot_y, rot_z]        
        kwargs["rot"] = rot
        kwargs.pop('rot_x', None)
        kwargs.pop('rot_y', None)
        kwargs.pop('rot_z', None)
        kwargs.pop("rot", None)

    return rot

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)