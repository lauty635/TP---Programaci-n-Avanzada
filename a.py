from graphviz import Digraph

# Create a UML-like class diagram using graphviz
dot = Digraph(comment='Diagrama de Clases To-Do API', format='png')
dot.attr(rankdir='LR')

# Define classes with record shape, escaping angle brackets for abstract
dot.node('TodoDB', label='{TodoDB|+ id: int\l+ title: str\l+ description: str\l+ completed: bool\l}', shape='record')
dot.node('TodoCreate', label='{TodoCreate|+ title: str\l+ description: str?\l+ completed: bool\l}', shape='record')
dot.node('TodoResponse', label='{TodoResponse|+ id: int\l+ title: str\l+ description: str?\l+ completed: bool\l}', shape='record')
dot.node('TaskBase', label='{TaskBase\\<\\<abstract\\>\\>|- _title: str\l- _description: str\l- _completed: bool\l+ title\l+ description\l+ completed\l+ toggle_completed()\l+ __str__()\l}', shape='record')
dot.node('Todo', label='{Todo|+ toggle_completed()\l+ to_dict()\l}', shape='record')

# Inheritance edges (arrowhead onormal indicates generalization)
dot.edge('TodoResponse', 'TodoCreate', arrowhead='onormal')
dot.edge('Todo', 'TaskBase', arrowhead='onormal')

# Dependency/use edges (dashed)
dot.edge('TodoCreate', 'TodoDB', style='dashed', label='datos para create/update')
dot.edge('TodoDB', 'TodoResponse', style='dashed', label='atributos al serializar')

# Render and display
file_path = dot.render(filename='/home/ivan/Desktop/TP---Programaci-n-Avanzada/todo_api_uml', cleanup=True)
file_path
