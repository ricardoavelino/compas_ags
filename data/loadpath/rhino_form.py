from compas_ags.diagrams import FormDiagram
from compas_rhino.helpers import NetworkArtist
from compas.utilities import geometric_key
from compas.utilities import XFunc

import rhinoscriptsyntax as rs
import json


# Plot Thrust Network

fnm = 'H:/data/loadpath/fan.json'
form = FormDiagram.from_json(fnm)

print(form.attributes['loadpath'])

artist = NetworkArtist(form, layer='Thrust')
artist.clear_layer()
artist.draw_edges(color='ee0000')

rs.LayerVisible('Dots', False)
rs.LayerVisible('Thrust', False)

#form.set_vertices_attributes(form.vertices(), {'z': 0})

# Copy Form

#rs.EnableRedraw(False)
#rs.CurrentLayer('Copy')
#rs.DeleteObjects(rs.ObjectsByLayer('Copy'))
#
#for uv in form.edges():
#    u, v = uv
#    q = form.get_edge_attribute(uv, 'q')
#    sp = form.vertex_coordinates(u)
#    ep = form.vertex_coordinates(v)
#    id = rs.AddLine(sp, ep)
#    rs.ObjectName(id, str(q))
#    
#rs.EnableRedraw(True)

# Analyse

#gkey_key = form.gkey_key()
#for guid in rs.ObjectsByLayer('Copy'):
#    q = float(rs.ObjectName(guid))
#    u = gkey_key[geometric_key(rs.CurveStartPoint(guid))]
#    v = gkey_key[geometric_key(rs.CurveEndPoint(guid))]
#    try:
#        form.edge[u][v]['q'] = q
#    except:
#        form.edge[v][u]['q'] = q
#
#form = XFunc('compas_ags.ags.loadpath3.z_from_form')(form)

#artist = NetworkArtist(form, layer='Analysis')
#artist.clear_layer()
#artist.draw_vertices()
#artist.draw_edges()

#form.to_json(fnm)