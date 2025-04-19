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

""" 
    NRZ-L

    NRZ-I

    AMI

    Pseudoternário

    Manchester

    Manchester Diferencial

"""