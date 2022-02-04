addi $s0,$s0,1
addi $s2,$s0,0x02
addi $s3,$s0,0xA0
addi $s4,$s0,-1
add $s6,$s2,$s1
and $s7,$s4,$s3
or $s5,$s3,$s4
sllv $s3,$s3,$s1 #para usar registros esvalue en el mnmonico
srlv $s3,$s3,$s1