#diccionario para los registros
#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# registros rs, rt, rd
# return[rs, rt, rd, filler]
# return[rs, rt, rd, filler]
# return[rs, rt, immediate]  

registers = {"x0" : 0, "x1" : 1, "x2" : 2, "x3" : 3, "x4" : 4, "x5" : 5, "x6" : 6, "x7" : 7 }
labels = { "MAIN" : 1, "INC" : 4, "DEC" : 9, "FUNC" : 8, "EXIT" : 15 }

def reg_decode(func_type, instr, regs):
    
    #instrucciones tipo "r"
    if func_type == "r":   
        if (instr == "sll") or (instr == "srl"): #excepeciones de "r", no tienen rs, tienen un corrimiento
            try:
                if (regs[0] < regs[1]):
                    return [registers[regs[1]], registers[regs[1]], registers[regs[1]], 0] 
                else:
                    return [registers[regs[0]], registers[regs[1]], registers[regs[0]], 0] 
            except:
                return None                

        if (instr == "jr"): # excepcion ---> rs, rt y el corrimiento
            try:
                return [registers[regs[0]], 0, 0, 0]
            except:
                return None   
            
        #las demas tipo "r"           
        try:      
            return[registers[regs[1]], registers[regs[2]], registers[regs[0]], 0]
        except:
            return None
            
    #para las tipo b        
    elif func_type == "b":
        try:
            return [registers[regs[0]], registers[regs[1]], labels[regs[2]]]    
        except:
            return None

    #para las tipo "i"
    elif func_type == "i":
        if (instr == "sb") or (instr == "lb"): # excepciones de las tipo i
            try:
                if len(regs[1]) > 1 and regs[1][1] == "x":
                    imm = int(regs[1], base=16)
                else:
                    imm = int(regs[1])
               
                return[registers[regs[2]], registers[regs[0]], imm]
            except:
                return None
        
        #las demas tipo i
        try:
            if len(regs[2]) > 1 and regs[2][1] == "x":
                imm = int(regs[2], base=16)
            else:
                imm = int(regs[2])
        
            return [registers[regs[1]], registers[regs[0]], imm]
        except:
            return None       
    
    elif func_type == "j": #tipo jump
        return [labels[regs[0]]]
      
    else:
        return None
