import bpy
from bpy_types import Panel



class THT_PT_Main(Panel):

    bl_label = "THToolkit"
    bl_idname = "THT_PT_Main"
    bl_category = 'THToolkit'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

   
    
    def draw(self,context):
        layout = self.layout
        box = layout.box()
        row = box.row(align=True)

        
        row.label(text=" Version 0.1 ")
        
        

       

from .modelling import THT_ui_modelling
from .UV import THT_ui_uv
from .cleanup import THT_ui_cleanup
        
      
        
      
        


panels = [THT_PT_Main]

def register():
    
    for pnl in panels:
        bpy.utils.register_class(pnl)
        THT_ui_modelling.register()
        THT_ui_uv.register()
        THT_ui_cleanup.register()
        
        

    

def unregister():
    
    for pnl in panels:
        bpy.utils.unregister_class(pnl)
        THT_ui_modelling.unregister()
        THT_ui_uv.unregister()
        THT_ui_cleanup.unregister()
        





        