import bpy
from bpy_types import Panel





class THT_PT_clnMain(Panel):

    bl_label = "Cleanup"
    bl_idname = "THT_PT_clnMain"
    bl_category = 'THToolkit'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    
    

    def draw(self,context):

        layout = self.layout

    
#MESH CLEANUP RELATED SCRIPTS

class THT_PT_clnLooseAttributes(Panel):

    bl_label = "Loose Attributes"
    bl_idname = "THT_PT_clnLooseAttributes"
    bl_category = 'THToolkit'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'THT_PT_clnMain'
    
    
    

    def draw(self,context):

        layout = self.layout
        box = layout.box()
        row = box.row(align=True)
        
        
        row.operator('object.loosevert',text="Vertices",icon='SNAP_VERTEX')
        row = box.row(align=True)
        row.operator('object.looseedge',text="Edge",icon='EDGESEL')
        row = box.row(align=True)
        row.operator('object.looseface',text="Face",icon='FACESEL')

class THT_PT_clnMesh(Panel):

    bl_label = "Mesh Cleanup"
    bl_idname = "THT_PT_clnMesh"
    bl_category = 'THToolkit'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'THT_PT_clnMain'
    
    
    

    def draw(self,context):

        layout = self.layout
        box = layout.box()
        row = box.row(align=True)
        
        
        row.operator('object.ngon',text="N-Gon",icon='UV_FACESEL')
        row = box.row(align=True)
        row.operator('object.nmanifold',text="Non-Manifold",icon='OBJECT_DATAMODE')
        row = box.row(align=True)
        row.operator('object.removeunusedmat',text="Remove Unused Mat",icon='MATERIAL_DATA')

        
        
        
      



clnpanels=[THT_PT_clnMain,
          THT_PT_clnLooseAttributes,
          THT_PT_clnMesh]

def register():
    for cp in clnpanels:
        bpy.utils.register_class(cp)

def unregister():
    
     for cp in clnpanels:
        bpy.utils.unregister_class(cp)