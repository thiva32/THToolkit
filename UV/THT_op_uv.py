import bpy 
from bpy.types import Operator


class THT_OP_UVStart:
    bl_label = "Start UV"
    bl_label = "uv.start"


    def execute():
        

        return{'FINISHED'}
    



uvoperators = [THT_OP_UVStart]

def register():
    for uvop in uvoperators:
        bpy.utils.register_class(uvop)

def unregister():
    for uvop in uvoperators:
        bpy.utils.unregister_class(uvop)