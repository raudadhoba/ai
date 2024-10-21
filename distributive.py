print("Distributive LAW")

A = int(input("Enter value of A"))

B=int(input("Enter value of B"))

C=int(input("Enter value of C"))

LHS=A*(B+C)

RHS=(A*B)+(A*C)

if LHS==RHS:

    print("LHS =A^ * (B + C) : ", LHS)

    print("RHS =( A ^ * B)+(A^ * C) : ", RHS)

    print("Distributive Law is proved")