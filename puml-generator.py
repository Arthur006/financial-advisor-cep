from plantuml import PlantUML

# URL of your running PlantUML server
plantuml_server = PlantUML(url='http://plantuml:8080/plantuml/img/')

# Or for SVG output (recommended for web use)
plantuml_server_svg = PlantUML(url='http://plantuml:8080/plantuml/svg/')

# Render a file to SVG
plantuml_server_svg.processes_file('puml/context.puml')

