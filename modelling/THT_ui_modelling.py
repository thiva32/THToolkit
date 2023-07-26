import bpy
from bpy_types import Panel





class THT_PT_mdlMain(Panel):

    bl_label = "Modelling"
    bl_idname = "THT_PT_MdlMain"
    bl_category = 'THToolkit'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    
    

    def draw(self,context):
        layout = self.layout

    
#ADD MESH RELATED SCRIPTS

class THT_PT_mdlMyCube(Panel):

    bl_label = "Mesh"
    bl_idname = "THT_PT_MdlMyCube"
    bl_category = 'THToolkit'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'THT_PT_MdlMain'
    
    
    

    def draw(self,context):

        layout = self.layout
        td = context.scene
        box = layout.box()
        row = box.row(align=True)
        
        
        row.operator('object.mycube',text="My Cube",icon='CUBE')
       
#TRANSFROM RELATED SCRIPTS

class THT_PT_mdlPivotToSelected(Panel):

    bl_label = "Transform"
    bl_idname = "THT_PT_PivotToSelected"
    bl_category = 'THToolkit'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'THT_PT_MdlMain'
    
    

    def draw(self,context):

        layout = self.layout
        box = layout.box()
        row = box.row(align=True)
        row.scale_y = 1.5
        
        
        row.operator('object.pivottoselected',text="Pivot To Selected",icon='CUBE')
        
        row.operator('object.temppivot',text="Temp Pivot",icon='CUBE')




class THT_PT_mdlEdgeTools(Panel):

    bl_label = "Edge Tools"
    bl_idname = "THT_PT_EdgeTools"
    bl_category = 'THToolkit'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'THT_PT_MdlMain'
    
    

    def draw(self,context):

        layout = self.layout
        box = layout.box()
        row = box.row(align=True)
       
        row.label(text = "Edge")
        row = box.row()
        row.operator('object.alternatedgering',text="Select Alternate Edges",icon='SNAP_EDGE')

        
        
        


        

#EDIT MESH RELATED SCRIPTS

class THT_PT_mdlEditMesh(Panel):

    bl_label = "Edit Mesh"
    bl_idname = "THT_PT_mdlEditMesh"
    bl_category = 'THToolkit'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'THT_PT_MdlMain'
    
    

    def draw(self,context):

        layout = self.layout
        td = context.scene
        box = layout.box()
        row = box.row(align=True)

        
        row.operator('object.converttoinstance',text="Convert To Instance",icon='CUBE')
        
        
        


        
        

        
        



mdlpanels = [THT_PT_mdlMain,THT_PT_mdlMyCube,
             THT_PT_mdlPivotToSelected,THT_PT_mdlEditMesh,
             THT_PT_mdlEdgeTools,]

def register():
    for mp in mdlpanels:
        bpy.utils.register_class(mp)

def unregister():
    
     for mp in mdlpanels:
        bpy.utils.unregister_class(mp)



