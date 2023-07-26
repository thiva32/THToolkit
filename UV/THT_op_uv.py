import bpy 
from bpy.types import Operator




  

class THT_OP_UVRename(Operator):
   
    bl_label = "Rename Selected Mesh UV"
    bl_idname = "uv.rename"
    bl_description = "Rename UV"
    bl_options = {'REGISTER'}

#define input parameter
    uvindex : bpy.props.IntProperty(name= "UV index",soft_min = 0,soft_max=10)
    uvname : bpy.props.StringProperty(name = "UV Name",default="")

#check if selected items are mesh objects
    @classmethod
    def poll(cls,context):
        return context.selected_objects and all(obj.type =='MESH' for obj in context.selected_objects)

    
    def execute(self,context):

#loop through each selected objects
        for obj in bpy.context.selectable_objects:
            if obj.type == 'MESH':
                uv_maps = obj.data.uv_layers
                if self.uvindex < 0 or self.uvindex >= len(uv_maps):
                    self.report({'ERROR'},"Invalid uv map index !!!")
                    
                    continue
                
                uv_maps[self.uvindex].name = self.uvname
                self.report({'INFO'},f"UV map {self.uvindex} renamed to {self.uvname}")

        return {'FINISHED'}

           
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


uvoperators = [THT_OP_UVRename]


def register():
    for uvop in uvoperators:
        bpy.utils.register_class(uvop)

        

def unregister():
    for uvop in uvoperators:
        bpy.utils.unregister_class(uvop)

        