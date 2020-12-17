from compas_ags.diagrams import FormDiagram
from compas_ags.diagrams import ForceDiagram
from compas_ags.diagrams import FormGraph
from compas_ags.ags.graphstatics import form_update_q_from_qind
from compas_ags.ags.graphstatics import force_update_from_form
from compas_plotters import MeshPlotter
import compas_ags

from compas_ags.viewers import Viewer

# FILE = compas_ags.get('examples/truss2.obj')
FILE = compas_ags.get('debugging/truss.obj')

graph = FormGraph.from_obj(FILE)

form = FormDiagram.from_graph(graph)
force = ForceDiagram.from_formdiagram(form)

uv_i = form.edge_index()

for u, v in form.leaf_edges():
    index = uv_i[(u, v)]
    pt1, pt2 = form.edge_coordinates(u, v)
    if pt1[0] == pt2[0]:
        form.edge_force((u, v), 10.0)

# plotter = MeshPlotter(form)
# plotter.draw_edges(text={key: str(uv_i[key]) for key in form.edges()})
# plotter.show()

form_update_q_from_qind(form)
force_update_from_form(force, form)

viewer = Viewer(form, force, delay_setup=False, figsize=(12, 7.5))
viewer.draw_form()
viewer.draw_force()
viewer.show()
