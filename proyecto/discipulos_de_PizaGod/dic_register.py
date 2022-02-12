#diccionario para los registros

registers = {"x0" : 0, "x1" : 1, "x2" : 2, "x3" : 3, "x4" : 4, "x5" : 5, "x6" : 6, "x7" : 7}
labels = { "MAIN" : 1, "INC" : 4, "DEC" : 9, "FUNC" : 8, "EXIT" : 15,}

def reg_decode(func_type, instr, regs):
	if func_type == "r": 
	        #special case "sll" | "srl"
	        if (instr == "sll") or (instr == "srl"):
	        	try:
	        		if (regs[0] < regs[1]):
	        			return [registers[regs[1]], registers[regs[1]], registers[regs[1]], 0] 
	                else:
	                	return [registers[regs[0]], registers[regs[1]], registers[regs[0]], 0] 
	            except:
	                return 0 #incompleto
			if (instr == "jr"):
				try:
					return [registers[regs[0]], 0, 0, 0]
	            except:
	            	return None   
	                       
	        try:
	        	return[registers[regs[1]], registers[regs[2]], registers[regs[0]], 0]
	        except:
	            return None
	            
	    elif func_type == "b":
	        try:
	            return [registers[regs[0]], registers[regs[1]], labels[regs[2]]]    
	        except:
	            return None
