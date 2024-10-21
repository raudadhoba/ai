print("Associative LAW") 
print("AND: A.(BC) = (AB).C = A.B.C")
A = int(input("Enter value of A")) 
B=int(input("Enter value of B"))
C=int(input("Enter value of C")) 
LHS = A * (B * C) 
RHS1  = (A * B) * C 
RHS2 = A  * B * C 
if LHS==RHS1 & LHS==RHS2:
    print("LHS = A.(B.C): ", LHS) 
    print("RHS = (A.B).C: ", RHS1) 
    print("RHS = A.B.C: ", RHS2) 
    print("Associative Law is proved for AND")