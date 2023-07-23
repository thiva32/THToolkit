# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "THToolkit",
    "author" : "Thiva",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}



from . import THT_ui_panel
from .modelling import THT_op_modelling
from .cleanup import THT_op_cleanup

def register():
    THT_ui_panel.register()
    THT_op_modelling.register()
    THT_op_cleanup.register()

def unregister():
    THT_ui_panel.unregister()
    THT_op_modelling.unregister()
    THT_op_cleanup.unregister()

if __name__=='__main__':
    register()
    