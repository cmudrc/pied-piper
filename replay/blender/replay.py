import bpy
from bpy.types import Operator, Panel
from bpy_extras.io_utils import ImportHelper


#my_module = bpy.data.texts["load_file"].as_module()
class Data():
    def __init___(self, data):
        self.data = data
    
    def number_of_steps(self):
        ######
        return 5


class LoadFile(Operator, ImportHelper):
    bl_label = "Load File"
    bl_idname = "object.load_file"
    
    # ImportHelper mixin class uses this
    filename_ext = "txt"
    filename_ext = "." + filename_ext
    
    filter_glob: bpy.props.StringProperty(
        default="*"+filename_ext,
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    def execute(self, context):
        return self.read_data(context, self.filepath)
    
    def read_data(self, context, filepath):
        print("reading data...")
        f = open(filepath, 'r', encoding='utf-8')
        data = f.read()
        f.close()

        # would normally load the data here
        print(data)
        #d = Data(data)

        return {'FINISHED'}


class PiedPiperPanel(Panel):
    bl_label = "Data"
    bl_idname = "PT_PiedPiperPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pied Piper"
    
    def draw(self, context):
        layout = self.layout
        
        #row = layout.row()
        #row.label(text="Load the simulation file", icon="FILEBROWSER")
        row = layout.row()
        row.operator(LoadFile.bl_idname, text="Load Simulation Result", icon="FILEBROWSER")
        row = layout.row()
        
                

def register():
    bpy.utils.register_class(PiedPiperPanel)
    bpy.utils.register_class(LoadFile)
    
    
def unregister():
    bpy.utils.unregister_class(PiedPiperPanel)
    bpy.utils.unregister_class(LoadFile)
    
    
if __name__ == "__main__":
    register()