import bpy
from bpy_types import Panel





class THT_PT_uvMain(Panel):

    bl_label = "UV-Unwrap"
    bl_idname = "THT_PT_UVMain"
    bl_category = 'THToolkit'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    
    

    def draw(self,context):
        layout = self.layout

    

class THT_PT_Rename_UV(Panel):

    bl_label = "Rename-UV"
    bl_idname = "THT_PT_Rename-UV"
    bl_category = 'THToolkit'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'THT_PT_UVMain'
    
    
    

    def draw(self,context):

        layout = self.layout
        row = layout.row(align=True)
        
        
        row.operator('uv.start',text="Unwrap",icon='UV')
       


        


        

        
        



uvpanels = [THT_PT_uvMain,THT_PT_Rename_UV]

def register():
    for pnl in uvpanels:
        bpy.utils.register_class(pnl)

def unregister():
    
     for pnl in uvpanels:
        bpy.utils.unregister_class(pnl)



