def b8zs(bits: str) -> list[int]:
    result = []
    last_polarity = 1
    
    i = 0
    while i < len(bits):
        if i <= len(bits) - 8 and bits[i:i+8] == "00000000":
            if last_polarity == 1:
                result.extend([0, 0, 0, -1, 1, 0, 1, -1])
                last_polarity = -1
            else:
                result.extend([0, 0, 0, 1, -1, 0, -1, 1])
                last_polarity = 1
            i += 8
        else:
            # codificação AMI normal para outros bits (se input menor que 0 bits)
            bit = int(bits[i])
            if bit == 0:
                result.append(0)
            else:
                result.append(last_polarity)
                last_polarity = -last_polarity
            i += 1
    
    return result

def nrz_l(bits: str) -> list[int]:
    return [1 if bit == '0' else -1 for bit in bits]

def nrz_i(bits: str) -> list[int]:
    result = []
    level = -1
    for bit in bits:
        if bit == '1':
            level *= -1
        result.append(level)
    return result

def ami(bits: str) -> list[int]:
    result = []
    last_polarity = 1
    for bit in bits:
        if bit == '0':
            result.append(0)
        else:
            result.append(last_polarity)
            last_polarity *= -1
    return result

def pseudoternary(bits: str) -> list[int]:
    result = []
    last_polarity = 1
    for bit in bits:
        if bit == '1':
            result.append(0)
        else:
            result.append(last_polarity)
            last_polarity *= -1
    return result

def manchester(bits: str) -> list[int]:
    result = []
    for bit in bits:
        if bit == '0':
            result.extend([1, -1])  
        else:
            result.extend([-1, 1])  
    return result


def manchester_differential(bits: str) -> list[int]:
    result = []
    level = 1  

    for bit in bits:
        bit = int(bit)
        if bit == 0:
            level = -level
            result.append(level)  
            level = -level
            result.append(level)  
        else:
            result.append(level)  
            level = -level
            result.append(level)  

    return result

def hdb3(bits: str) -> list[int]:
    result = []
    last_polarity = -1 
    pulse_count = 0    

    i = 0
    while i < len(bits):
        if bits[i:i+4] == "0000":
            if pulse_count % 2 == 0:
                last_polarity *= -1
                b = last_polarity
                v = last_polarity
                result.extend([b, 0, 0, v])
            else:
                v = last_polarity
                result.extend([0, 0, 0, v])
            pulse_count = 0
            i += 4
        else:
            if bits[i] == '1':
                last_polarity *= -1
                result.append(last_polarity)
                pulse_count += 1
            else:
                result.append(0)
            i += 1
    return result

def mlt_3(bits: str) -> list[int]:
    result = []
    levels = [0, 1, 0, -1]  
    state_index = 0

    for bit in bits:
        if bit == '1':
            state_index = (state_index + 1) % 4
        result.append(levels[state_index])
    return result

def ternary_nrz(data: str) -> list[int]:
    result = []
    last_level = 0

    for bit in data:
        if bit == '0':
            if last_level >= 0:
                last_level = -1
            else:
                last_level = 0
        else:
            if last_level <= 0:
                last_level = 1
            else:
                last_level = 0
        result.append(last_level)
    return result

def unipolar_rz(data: str) -> list[int]:

    result = []

    for bit in data:
        if bit == '1':
            result.extend([1, 0])
        else: 
            result.extend([0, 0])
    
    return result

""" 
    NRZ-L - bit 0: tensao 1     I    bit 1: tensao 0

    NRZ-I - bit 0: mantem a mesma tensao    I   bit 1: inverte a tensao 

    AMI - bit 0: tensao 0   I   bit 1: inverte tensao (-1, 1) 

    Pseudoternário - bit 0: inverte tensao (-1, 1)      I       bit 1: tensao 0      

    Manchester - bit 0: descida (1, 0)     I       bit 1: subida (0, 1)

    Manchester Diferencial - bit 0: inverte [(1, 0), (0, 1)]    I   bit 1: nao inverte

    b8zs - eh um AMI que quando tem 1 seguido de 00000000 retorna 000+-0-+, se for -1 retorna 000-+0+-

    hdb3 - eh um AMI que (contendo 0000):
            1: {
                par: -00-
                impar: 000+
            }
            -1 {
                par: +00+
                impar: 000-
            }

    unipolar - bit 0: fica um ciclo com tensao 0    I   bit 1: fica meio periodo em 1

    ternary - 
        0: {
            anterior: {
                1: -1
                0: -1
                -1: 0
            }
        }
        1: {
            anterior: {
                1: 0
                0: 1
               -1: 1
            }    
        }

    mlt 3 - bit 0: tensao mantem a mesma        I       bit 1: vai alternando entre 1 -> 0 -> -1 -> 0

"""