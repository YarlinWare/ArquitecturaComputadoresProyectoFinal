from gui.gui import GUI
from processor.processor import Processor

# Crear una instancia del procesador y la GUI
processor = Processor()
gui = GUI(processor)
processor.gui = gui  # Agregar una referencia de la GUI al procesador
gui.window.mainloop()