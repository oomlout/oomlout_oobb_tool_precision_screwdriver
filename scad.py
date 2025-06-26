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
        

        #screwdriver
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 1
        p3["height"] = 1
        #p3["thickness"] = 6
        #p3["extra"] = ""
        part["kwargs"] = p3
        nam = "precision_screwdriver"
        part["name"] = nam
        if oomp_mode == "oobb":
            p3["oomp_size"] = nam
        parts.append(part)

        #bit lock
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 1
        p3["height"] = 1
        #p3["thickness"] = 6
        #p3["extra"] = ""
        part["kwargs"] = p3
        nam = "bit_lock"
        part["name"] = nam
        if oomp_mode == "oobb":
            p3["oomp_size"] = nam
        parts.append(part)



        #label top
        if True:
            extras = []
            if True:
                #hex
                sizes = ["5", "4", "3.5", "3", "2.5", "2", "1.5","0.9","0.7","1.3"]
                for siz in sizes:
                    ex = {"shape": "hex", "size": siz}
                #slotted
                sizes = ["0.8", "1", "1.2", "1.5", "1.8", "2", "2.5", "3","4"]
                for siz in sizes:
                    ex = {"shape": "slotted", "size": siz}
                    extras.append(ex)
                #phillips
                sizes = ["0", "00", "000", "1"]
                for siz in sizes:
                    ex = {"shape": "phillips", "size": siz}
                    extras.append(ex)
                
                


            
            for ex in extras:
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                p3["width"] = 1
                p3["height"] = 1
                p3["thickness"] = 1.5
                shape = ex.get("shape", "")
                p3["shape"] = shape
                siz = ex.get("size", "")
                p3["siz"] = siz
                extra = f"{shape}_shape_{siz}_size"
                p3["extra"] = extra
                part["kwargs"] = p3
                nam = "label_top"
                part["name"] = nam
                if oomp_mode == "oobb":
                    p3["oomp_size"] = nam
                parts.append(part)



    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        #sort.append("width")
        #sort.append("height")
        #sort.append("thickness")
        
        scad_help.generate_navigation(sort = sort)


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


def get_label_top(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    shape = kwargs.get("shape", "")
    siz = kwargs.get("siz", "")
    
    #add cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_cylinder"    
    p3["radius"] = 16/2
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add hex piece
    if True:
        clearance = 0.2 - 0.025
    #hex bit is 0.25 inch6.35 mm
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        rad =  (0.25 * 25.4) / 2  * 1.1546 + clearance# 7.32 hopefully 
        p3["radius"] = rad
        dep = 6
        p3["height"] = dep
        #p3["depth"] = 4
        pos1 = copy.deepcopy(pos)        
        pos1[2] += -dep
        p3["pos"] = pos1
        #p3["m"] = "#"    
        oobb_base.append_full(thing,**p3)


    #add shape
    depth_indent = 0.5
    if True:
        
        if shape == "hex":
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"polyg"
            p3["sides"] = 6
            p3["radius"] = 4.5
            p3["height"] = depth_indent
            pos1 = copy.deepcopy(pos)       
            pos1[1] += -3 #+ 45
            pos1[2] += depth/2 - depth_indent
            p3["pos"] = pos1
            p3["m"] = "#"    
            oobb_base.append_full(thing,**p3)
        elif shape == "slotted":
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_cube"
            wid = 8
            hei = 2
            dep = depth_indent
            size = [wid, hei, dep]
            p3["size"] = size
            p3["depth"] = depth_indent
            pos1 = copy.deepcopy(pos)       
            pos1[1] += -2
            pos1[2] += depth/2 - depth_indent
            p3["pos"] = pos1
            p3["m"] = "#"
            oobb_base.append_full(thing,**p3)
        elif shape == "phillips":
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_cube"
            wid = 8
            hei = 2
            dep = depth_indent
            size = [wid, hei, dep]
            p3["size"] = size
            p3["depth"] = depth_indent
            pos1 = copy.deepcopy(pos)       
            pos1[1] += -3
            pos1[2] += depth/2 - depth_indent
            p3["pos"] = pos1
            p3["m"] = "#"
            oobb_base.append_full(thing,**p3)
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_cube"
            wid = 2
            hei = 8
            dep = depth_indent
            size = [wid, hei, dep]
            p3["size"] = size
            p3["depth"] = depth_indent
            pos1 = copy.deepcopy(pos)       
            pos1[1] += -3
            pos1[2] += depth/2 - depth_indent
            p3["pos"] = pos1
            p3["m"] = "#"
            oobb_base.append_full(thing,**p3)

    #add size
    if True:        
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_text"
        p3["depth"] = depth_indent
        pos1 = copy.deepcopy(pos)       
        if len(siz) == 1:   
            pos1[1] += 4
        else:
            pos1[1] += 3.5
        pos1[2] += depth/2 - depth_indent
        p3["pos"] = pos1
        p3["text"] = siz
        p3["font"] = "SegoiUI:Bold"
        if len(siz) == 1:
            p3["size"] = 4.5
        else:
            p3["size"] = 4
        p3["m"] = "#"
        
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

def get_precision_screwdriver(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #variables
    hex_side_ratio = 1.1547
    radius_main = 11 / 2

    #1_driver_bit
    driver_bit_lift = 25
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        #p3["m"] = "#"
        p3["clearance"] = 0.2
        p3["clearance_top"] = True
        p3["length"] = 100
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0 #+ 45
        pos1[2] += driver_bit_lift
        p3["pos"] = pos1
        get_tool_screwdriver_bit_quarter_inch_drive_100_mm_depth(thing, **p3)

    current_z = 0
    #2_indent_bottom
    indent_bottom_depth = 6
    current_depth = indent_bottom_depth
    indent_bottom_radius_bottom = 2.5/2
    indent_bottom_radius_top = radius_main
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_cylinder"
        p3["depth"] = indent_bottom_depth
        p3["r1"] = indent_bottom_radius_bottom
        p3["r2"] = indent_bottom_radius_top
        pos1 = copy.deepcopy(pos)
        pos1[2] += indent_bottom_depth/2
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)
    current_z += current_depth

    #3_hex_bottom
    hex_bottom_depth = 6
    current_depth = hex_bottom_depth
    hex_bottom_radius = 10/2 * hex_side_ratio
    hex_bottom_joiner_donut_bottom_radius = 25/2
    hex_bottom_joiner_donut_top_radius = 25/2
    hex_bottom_joiner_donut_id = hex_bottom_radius / hex_side_ratio
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["height"] = hex_bottom_depth
        p3["radius"] = hex_bottom_radius
        pos1 = copy.deepcopy(pos)
        pos1[2] += current_z
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        #joiners
        #shaft top joiner
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oring"
        dep = hex_bottom_joiner_donut_bottom_radius
        p3["depth"] = dep
        p3["id"] = hex_bottom_joiner_donut_id
        pos1 = copy.deepcopy(pos)
        pos1[2] += current_z #+ dep/2
        
        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        p4 = copy.deepcopy(p3)
        dep = hex_bottom_joiner_donut_top_radius
        p4["depth"] = dep
        pos1 = copy.deepcopy(p4["pos"])
        pos1[2] += hex_bottom_depth
        p4["pos"] = pos1
        #p4["m"] = "#"
        oobb_base.append_full(thing,**p4)


    current_z += current_depth

    #4_shaft_bottom
    shaft_length_total = 75
    shaft_bottom_depth = 40
    shaft_bottom_radius = radius_main
    current_depth = shaft_bottom_depth
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_cylinder"
        dep = shaft_bottom_depth
        p3["depth"] = dep
        p3["radius"] = shaft_bottom_radius
        pos1 = copy.deepcopy(pos)
        pos1[2] += current_z + dep/2
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)
    current_z += current_depth

    #5 hex_top
    hex_top_depth = 12
    current_depth = hex_top_depth
    hex_top_radius = 13/2 * hex_side_ratio
    hex_top_joiner_donut_radius = 10/2
    hex_top_joiner_donut_id = radius_main
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"polyg"
        p3["sides"] = 6
        p3["height"] = hex_top_depth
        p3["radius"] = hex_top_radius
        pos1 = copy.deepcopy(pos)
        pos1[2] += current_z
        p3["pos"] = pos1
        rot1 = copy.deepcopy(rot)
        rot1[2] = 360/12
        p3["rot"] = rot1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        #joiners
        #shaft top joiner
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oring"
        dep = hex_top_joiner_donut_radius
        p3["depth"] = dep
        p3["id"] = hex_top_joiner_donut_id
        pos1 = copy.deepcopy(pos)
        pos1[2] += current_z #+ dep/2
        pos2 = copy.deepcopy(pos)
        pos2[2] += current_z + hex_top_depth
        p3["pos"] = pos2

        poss = []
        poss.append(copy.deepcopy(pos1))
        poss.append(copy.deepcopy(pos2))
        p3["pos"] = poss
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

    current_z += current_depth

    #6_shaft_top
    shaft_top_depth = shaft_length_total - shaft_bottom_depth
    shaft_top_flair = 1
    shaft_top_radius_bottom = radius_main
    shaft_top_radius_top = shaft_top_radius_bottom + shaft_top_flair
    
    

    current_depth = shaft_top_depth

    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_cylinder"
        dep = shaft_top_depth
        p3["depth"] = dep
        p3["r1"] = shaft_top_radius_bottom
        p3["r2"] = shaft_top_radius_top
        pos1 = copy.deepcopy(pos)
        pos1[2] += current_z + dep/2
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        


    current_z += current_depth

    #7_top_cylinder
    top_cylinder_depth = 9
    top_cylinder_radius = 18/2
    top_cylinder_top_donut_radius = 10/2
    top_cylinder_bottom_donut_radius = (top_cylinder_radius-shaft_top_radius_top)#/2
    top_cylinder_bottom_top_donut_id = top_cylinder_radius - top_cylinder_bottom_donut_radius


    current_depth = top_cylinder_depth
    if True:
        #middle cylinder
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_cylinder"
        ex = top_cylinder_bottom_donut_radius
        dep = top_cylinder_depth - ex
        p3["depth"] = dep
        p3["radius"] = top_cylinder_radius - (top_cylinder_top_donut_radius/2)
        pos1 = copy.deepcopy(pos)
        pos1[1] += 0 #+ 30
        pos1[2] += current_z + dep/2 + ex
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        #bottom cylinder
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_cylinder"
        dep = top_cylinder_depth - top_cylinder_top_donut_radius/2 -  top_cylinder_bottom_donut_radius/2 * 2
        p3["depth"] = dep
        p3["radius"] = top_cylinder_radius
        pos1 = copy.deepcopy(pos)
        pos1[2] += current_z + dep/2 + top_cylinder_bottom_donut_radius
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        #top oring
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oring"
        p3["depth"] = top_cylinder_top_donut_radius
        p3["id"] = top_cylinder_radius - top_cylinder_top_donut_radius
        pos1 = copy.deepcopy(pos)
        pos1[2] += current_z + top_cylinder_depth - top_cylinder_top_donut_radius/2
        p3["pos"] = pos1
        p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        #bottom transition
        if True:
            #bottom oring top
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "positive"
            p3["shape"] = f"oring"
            p3["depth"] = top_cylinder_bottom_donut_radius
            p3["id"] = top_cylinder_bottom_top_donut_id
            pos1 = copy.deepcopy(pos)
            pos1[2] += current_z + top_cylinder_bottom_donut_radius
            pos1[1] += 0 #+30
            p3["pos"] = pos1
            p3["m"] = "#"
            oobb_base.append_full(thing,**p3)

            #bottom oring bottom
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "negative"
            p3["shape"] = f"oring"
            p3["depth"] = top_cylinder_bottom_donut_radius  
            p3["id"] = top_cylinder_bottom_top_donut_id
            pos1 = copy.deepcopy(pos)
            pos1[2] += current_z
            pos1[1] += 0 #+30
            p3["pos"] = pos1
            #p3["m"] = "#"
            oobb_base.append_full(thing,**p3)

            #center fill cylinder
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "positive"
            p3["shape"] = f"oobb_cylinder"
            dep = top_cylinder_bottom_donut_radius * 1.5
            p3["depth"] = dep
            p3["radius"] = top_cylinder_bottom_top_donut_id + top_cylinder_bottom_donut_radius/2
            pos1 = copy.deepcopy(pos)
            pos1[2] += current_z + dep/2
            pos1[1] += 0 #+30
            p3["pos"] = pos1
            #p3["m"] = "#"
            oobb_base.append_full(thing,**p3)

        #knurl
    if True:
        rad = top_cylinder_radius + .2
        repeats = 36
        angle = 360 / repeats
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        wid = 1
        hei = 1
        dep = top_cylinder_depth
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
            shift_x = rad + wid/2
            shift = [shift_x,0,0]
            rot_shift = [shift,rot]
            
            p3["rot_shift"] = [rot_shift]
            #p3["rot"] = rot
            oobb_base.append_full(thing,**p3)

    #8_screw_lock            
    screw_lock_depth = 8
    screw_lock_lift =  indent_bottom_depth + hex_bottom_depth + shaft_bottom_depth + hex_top_depth/2#driver_bit_lift + 30 + 5
    width_bit_locker = 7    
    height_bit_locker = 3
    depth_bit_locker = 14
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
        p3["shape"] = f"oobb_screw_countersunk"
        dep = screw_lock_depth
        p3["depth"] = dep
        p3["nut"] = True
        p3["clearance"] = ["top","bottom"]
        p3["radius_name"] = "m3"
        pos1 = copy.deepcopy(pos)
        y_shift = (shaft_top_radius_bottom - screw_lock_depth)
        pos1[0] += 0 + dep/2 - y_shift#+ 45 
        
        pos1[2] += screw_lock_lift
        p3["pos"] = pos1
        rot1 = copy.deepcopy(rot)
        rot1[1] += 90
        rot1[2] += 10
        p3["rot"] = rot1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        #add screw locker clearance
    
        shift_y = 0
        #shift_y = 30      
        extra = 10  
        bot = screw_lock_lift - extra
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"        
        p3["shape"] = f"oobb_cube"
        clear = 0.5
        hei = width_bit_locker + clear
        wid = height_bit_locker + clear
        dep = 120 - bot
        size = [wid, hei, dep]
        p3["size"] = size
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0 #+ 45
        pos1[1] += shift_y
        pos1[2] += bot
        p3["pos"] = pos1
        #p3["m"] = "#"
        #p3["zz"] = "mi"
        oobb_base.append_full(thing,**p3)

    pass
    
def get_bit_lock(thing, **kwargs):

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

def get_tool_screwdriver_bit_quarter_inch_drive_100_mm_depth(thing, **kwargs):
    clearance = kwargs.get("clearance", 0)
    include_bit = kwargs.get("include_bit", True)
    clearance_top = kwargs.get("clearance_top", False)
    radius_bit_main = kwargs.get("radius_bit_main", 3.5/2)
    pos = kwargs.get("pos", [0, 0, 0])
    rot = kwargs.get("rot", [0, 0, 0])
    
    length = kwargs.get("length", 150)

    # setting up for rotation object
    typ = kwargs.get("type", "p")
    kwargs["type"] = "positive" #needs to be positive for the difference to work
    rot_original = rot   
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
        rad = (0.25 * 25.4) / 2  * 1.1546 + clearance# 7.32 hopefully 
        p3["radius"] = rad
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

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)