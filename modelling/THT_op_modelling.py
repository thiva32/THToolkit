

import bpy
from bpy.types import Context, Operator





class THT_OP_MDL_mycube(Operator):
    bl_label = "mycube"
    bl_idname = "object.mycube"
    bl_description = "Add My Cube"
    

    def execute(self,context):   


        bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 1), scale=(1, 1, 1))
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)



        return {'FINISHED'}
    
    
class THT_OP_MDL_pivottoselected(Operator):

    bl_label = "pivottoselected"
    bl_idname = "object.pivottoselected"
    bl_description = "Pivot to Selected"
    

    def execute(self,context):   

        
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')    
        


        return {'FINISHED'}
    
class THT_OP_MDL_settemppivot(Operator):

    bl_label = "settemppivot"
    bl_idname = "object.temppivot"
    bl_description = "(WIP) Set Temp Pivot"
    

    def execute(self,context):   
     
     s_obj = bpy.context.selected_objects
     bpy.ops.object.convert(target='MESH', keep_original=True)
     bpy.ops.view3d.snap_cursor_to_active()
     bpy.ops.object.empty_add(type='PLAIN_AXES', radius=5, align='WORLD', location=(0, 0, 0), scale=(5, 5, 5))
     empty_obj = bpy.context.active_object
     bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
     
     

     for obj in s_obj:
         
         obj.parent = empty_obj
         
     
         
        
        
          
          


         
     
     

     return{'FINISHED'}
        
    
    
class THT_OP_MDL_converttoinstance(Operator):

    bl_label = "ConvertToInstance"
    bl_idname = "object.converttoinstance"
    bl_description = "Convert To Instance"
    

    def execute(self,context):   

        bpy.ops.object.make_links_data(type='OBDATA')
    
        return {'FINISHED'}
    
    
class THT_OP_MDL_alternatedgering(Operator):
    
    bl_label = "Alternate Edge Ring"
    bl_idname = "object.alternatedgering"
    bl_description = "Select Alternate Edge Ring"
    bl_options = {'REGISTER','UNDO'}

     
    offset_bool : bpy.props.BoolProperty(name ="Offset",default=False)

    
    
    def execute(self,context):   
        
        o = self.offset_bool
        
        noffset = 0
        if o == True:
            noffset = 1 
        else:
            noffset = 0
        
        message = ("No offset = %i " %noffset)

        self.report({'INFO'},message)

        bpy.ops.mesh.loop_multi_select(ring=True)
        bpy.ops.mesh.select_nth(skip=1, nth=1, offset= noffset)
        bpy.ops.mesh.loop_multi_select(ring=False)
        
           
        return {'FINISHED'}
        


    




mdl_operator = [THT_OP_MDL_mycube,
                THT_OP_MDL_pivottoselected,
                THT_OP_MDL_converttoinstance,
                THT_OP_MDL_alternatedgering,
                THT_OP_MDL_settemppivot,
                ]

def register():
    for mdlop in mdl_operator:
        bpy.utils.register_class(mdlop)

def unregister():
    for mdlop in mdl_operator:
        bpy.utils.unregister_class(mdlop)




