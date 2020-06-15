from compas_rhino import unload_modules
unload_modules("compas")

import os
import rhinoscriptsyntax as rs

from compas_ags.diagrams import FormDiagram
from compas_ags.diagrams import ForceDiagram

from compas_ags.rhino import FormArtist
from compas_ags.rhino import ForceArtist

from compas_ags.constraints import ConstraintsCollection
from compas_ags.rhino import rhino_vertex_constraints


# ==============================================================================
# Load Diagrams
# ==============================================================================

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
form_file = os.path.join(DATA, 'form.json')
force_file = os.path.join(DATA, 'force.json')

form = FormDiagram.from_json(form_file)
force = ForceDiagram.from_json(force_file)

formartist = FormArtist(form, layer='FormDiagram')
forceartist = ForceArtist(force, layer='ForceDiagram')

formartist.draw_diagram()
forceartist.draw_diagram(form=form)


# ==============================================================================
# Constraints
# ==============================================================================
# set constraints
C = ConstraintsCollection(form)

# set vertex constraints
C.constrain_dependent_leaf_edges_lengths()
#constraint_dict = rhino_vertex_constraints(form)
from compas_ags.rhino import rhino_constraint_visualization
constraint_dict = rhino_constraint_visualization(form, scale=0.5)
print(constraint_dict)
C.update_rhino_vertex_constraints(constraint_dict)

cj, cr = C.compute_constraints()
print(cj, cr)


#TODO: show constraints 