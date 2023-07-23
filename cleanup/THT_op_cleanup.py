import bpy
from bpy.types import Operator

 
       
class THT_OP_Non_Manifold(Operator):
  
    bl_idname ="object.nmanifold"
    bl_label = "Select Non-Manifold"
    bl_description = "Selectc Non-Manifold Geo"

    def execute(self,context):
        
         if bpy.context.active_object.mode == 'EDIT':
             bpy.ops.mesh.select_non_manifold()
         else:
             bpy.ops.object.editmode_toggle()
             bpy.ops.mesh.select_non_manifold()
        
         return {'FINISHED'}	
      
class THT_OP_Ngon(Operator):
  
    bl_idname ="object.ngon"
    bl_label = "Select N-Gon"
    bl_description = "Selects Mesh N-Gon"

    def execute(self,context):
         
         if bpy.context.active_object.mode == 'EDIT':
             bpy.ops.mesh.select_face_by_sides(number=4, type='GREATER')
         else:
             bpy.ops.object.editmode_toggle()
             bpy.ops.mesh.select_face_by_sides(number=4, type='GREATER')
        
         return {'FINISHED'}	
    
class THT_OP_LooseVert(Operator):
  
    bl_idname ="object.loosevert"
    bl_label = "Select Loosevert"
    bl_description = "Selects Loose geo (Vert)"

    def execute(self,context):
        if bpy.context.active_object.mode == 'EDIT':
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            bpy.ops.mesh.select_loose()	
        else:
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            bpy.ops.mesh.select_loose()	

            

        return {'FINISHED'}	
    
class THT_OP_LooseEdge(Operator):
  
    bl_idname ="object.looseedge"
    bl_label = "Select Looseedge"
    bl_description = "Selects Loose geo (EDGE)"

    def execute(self,context):
        if bpy.context.active_object.mode == 'EDIT':
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
            bpy.ops.mesh.select_loose()	
        else:
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
            bpy.ops.mesh.select_loose()	

        

        return {'FINISHED'}	
    
class THT_OP_LooseFace(Operator):
  
    bl_idname ="object.looseface"
    bl_label = "Select Looseface"
    bl_description = "Selects Loose geo (FACE)"

    def execute(self,context):
        if bpy.context.active_object.mode == 'EDIT':
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            bpy.ops.mesh.select_loose()	
        else:
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            bpy.ops.mesh.select_loose()	

            

        return {'FINISHED'}	
    

class THT_OT_RemoveUnusedMat(Operator):
	
	bl_idname ="object.removeunusedmat"
	bl_label = "Remove Unused Materials"
	bl_description = "Remove all materials that are not assigned to anything"
	

	def execute(self,context):
		self.report({'INFO'}, "Unused Material Removed!")
		bpy.ops.object.material_slot_remove_unused()

		return {'FINISHED'}	 





mdl_operator = [THT_OP_Ngon,
                THT_OP_LooseEdge,
                THT_OP_LooseFace,
                THT_OP_LooseVert,
                THT_OP_Non_Manifold,
                THT_OT_RemoveUnusedMat]

def register():
    for mdlop in mdl_operator:
        bpy.utils.register_class(mdlop)

def unregister():
    for mdlop in mdl_operator:
        bpy.utils.unregister_class(mdlop)




