class Processor:
    def __init__(self):
        self.registers = [0] * 32
        self.pc = 0  # Program Counter
        self.memory = [0] * 16777216  # Inicializar la memoria con ceros (16 MiB)

    def execute_instruction(self, instruction):
        opcode = instruction.opcode
        operands = [int(operand) for operand in instruction.operands]

        if opcode == 0:  # NOP
            pass  # No operation

        elif opcode == 1:  # LDA
            register_index = operands[0]
            address = operands[1]
            self.registers[register_index] = self.read_memory(address)

        elif opcode == 2:  # ADD
            register_index1 = operands[0]
            register_index2 = operands[1]
            destination_index = operands[2]

            value1 = self.registers[register_index1]
            value2 = self.registers[register_index2]

            result = value1 + value2
            self.registers[destination_index] = result

        elif opcode == 3:  # SUB
            register_index1 = operands[0]
            register_index2 = operands[1]
            destination_index = operands[2]

            value1 = self.registers[register_index1]
            value2 = self.registers[register_index2]

            result = value1 - value2
            self.registers[destination_index] = result

        elif opcode == 4:  # STA
            register_index = operands[0]
            address = operands[1]
            value = self.registers[register_index]
            self.write_memory(address, value)

        elif opcode == 5:  # LDI
            register_index = operands[0]
            immediate_value = operands[1]
            self.registers[register_index] = immediate_value

        elif opcode == 6:  # AND
            register_index1 = operands[0]
            register_index2 = operands[1]
            destination_index = operands[2]

            value1 = self.registers[register_index1]
            value2 = self.registers[register_index2]

            result = value1 & value2
            self.registers[destination_index] = result

        elif opcode == 7:  # OR
            register_index1 = operands[0]
            register_index2 = operands[1]
            destination_index = operands[2]

            value1 = self.registers[register_index1]
            value2 = self.registers[register_index2]

            result = value1 | value2
            self.registers[destination_index] = result

        elif opcode == 8:  # NOT
            register_index = operands[0]
            destination_index = operands[1]

            value = self.registers[register_index]
            result = ~value
            self.registers[destination_index] = result

        elif opcode == 9:  # XOR
            register_index1 = operands[0]
            register_index2 = operands[1]
            destination_index = operands[2]

            value1 = self.registers[register_index1]
            value2 = self.registers[register_index2]

            result = value1 ^ value2
            self.registers[destination_index] = result

        elif opcode == 10:  # ROL
            register_index = operands[0]
            destination_index = operands[1]

            value = self.registers[register_index]
            result = (value << 1) | (value >> 31)  # Left rotation by 1 bit
            self.registers[destination_index] = result

        elif opcode == 11:  # JMP
            address = operands[0]
            self.pc = address

        elif opcode == 12:  # JC
            address = operands[0]
            if self.get_carry_flag():
                self.pc = address

        elif opcode == 13:  # JZ
            address = operands[0]
            if self.get_zero_flag():
                self.pc = address

        elif opcode == 14:  # OUT
            register_index = operands[0]
            value = self.registers[register_index]
            self.output(value)

        elif opcode == 15:  # HLT
            self.halt()

        # Implementar más operaciones según tus necesidades

    def read_memory(self, address):
        return self.memory[address]

    def write_memory(self, address, value):
        self.memory[address] = value

    def set_carry_flag(self, value):
        self.carry_flag = value

    def set_zero_flag(self, value):
        self.zero_flag = value

    def get_carry_flag(self):
        return self.carry_flag

    def get_zero_flag(self):
        return self.zero_flag

    def output(self, value):
        print(f"Output: {value}")

    def halt(self):
        print("Halting the processor")
        exit()

class Instruction:
    """
    Constructor de la clase Instruction.

    Args:
        opcode (int): Opcode de la instrucción.
        operands (list): Lista de operandos de la instrucción.
    """
    def __init__(self, opcode, operands):
        self.opcode = opcode
        self.operands = operands
    """
    Obtiene el opcode de la instrucción.

    Returns:
        int: Opcode de la instrucción.
    """
    def get_opcode(self):
        return self.opcode
    """
    Obtiene la lista de operandos de la instrucción.

    Returns:
        list: Lista de operandos de la instrucción.
    """
    def get_operands(self):
        return self.operands
    """
    Establece el opcode de la instrucción.

    Args:
        opcode (int): Opcode de la instrucción.
    """
    def set_opcode(self, opcode):
        self.opcode = opcode

    """
    Establece la lista de operandos de la instrucción.

    Args:
        operands (list): Lista de operandos de la instrucción.
    """
    def set_operands(self, operands):
        self.operands = operands

    """
    Convierte la instrucción a su representación binaria.

    Returns:
        str: Representación binaria de la instrucción.
    """
    def to_binary(self):
        opcode_binary = bin(self.opcode)[2:].zfill(7)
        operands_binary = [bin(operand)[2:].zfill(25) for operand in self.operands]
        return opcode_binary + ''.join(operands_binary)

