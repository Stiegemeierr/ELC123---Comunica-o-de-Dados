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
    level = 1
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
            result.extend([-1, -1])  
    return result

def manchester_differential(bits: str) -> list[int]:
    result = []
    current_level = 1
    for bit in bits:
        if bit == '0':
            current_level *= -1
        result.extend([current_level, -current_level])
    return result

def hdb3(bits: str) -> list[int]:
    result = []
    last_polarity = -1
    pulse_count = 0
    i = 0

    while i < len(bits):
        if i <= len(bits) - 4 and bits[i:i+4] == "0000":
            if pulse_count % 2 == 0:
                result.extend([0, 0, 0, last_polarity])
                pulse_count = 1
            else:
                last_polarity *= -1
                result.extend([last_polarity, 0, 0, last_polarity])
                pulse_count = 0
            i += 4
        else:
            bit = bits[i]
            if bit == '0':
                result.append(0)
            else:
                last_polarity *= -1
                result.append(last_polarity)
                pulse_count += 1
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


""" 
    NRZ-L - WORKING

    NRZ-I - WORKING

    AMI - WORKING 

    Pseudoternário - WORKING

    Manchester - FIX 

    Manchester Diferencial - WORKING ? 

    b8zs - WORKING ?

    hdb3 - FIX

"""