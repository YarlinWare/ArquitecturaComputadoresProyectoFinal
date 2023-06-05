import tkinter as tk
from processor.processor import Instruction

class GUI:
    def __init__(self, processor):
        self.processor = processor

        # Crear la ventana principal y otros elementos de la GUI
        self.window = tk.Tk()

        # Campo de entrada para el opcode
        self.opcode_label = tk.Label(self.window, text="Opcode:")
        self.opcode_label.pack()
        self.opcode_entry = tk.Entry(self.window)
        self.opcode_entry.pack()

        # Campo de entrada para los operandos
        self.operands_label = tk.Label(self.window, text="Operandos (separados por comas):")
        self.operands_label.pack()
        self.operands_entry = tk.Entry(self.window)
        self.operands_entry.pack()

        self.execute_button = tk.Button(self.window, text="Ejecutar", command=self.execute_instruction)
        self.execute_button.pack()

        self.registers_label = tk.Label(self.window, text="Registros:")
        self.registers_label.pack()

        self.registers_text = tk.Text(self.window, width=40, height=10)
        self.registers_text.pack()

        self.window.mainloop()

    def update_registers_text(self):
        registers_text = ""
        for i, value in enumerate(self.processor.registers):
            registers_text += f"Registro {i}: {value}\n"
        self.registers_text.delete("1.0", tk.END)
        self.registers_text.insert(tk.END, registers_text)

    def execute_instruction(self):
        # Obtener el opcode ingresado por el usuario
        opcode = int(self.opcode_entry.get())

        # Obtener los operandos ingresados por el usuario
        operands_str = self.operands_entry.get()
        operands = [int(operand) for operand in operands_str.split(',')]

        # Crear la instrucción a partir de los datos ingresados
        instruction = Instruction(opcode, operands)

        # Ejecutar la instrucción en el procesador
        self.processor.execute_instruction(instruction)

        # Actualizar la visualización de los registros en la GUI
        self.update_registers_text()