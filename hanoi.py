# def moveTower(height,fromPole, toPole, withPole): 
#     if height >= 1: 
#         moveTower(height-1,fromPole,withPole,toPole) 
#         moveDisk(fromPole,toPole) 
#         moveTower(height-1,withPole,toPole,fromPole) 
# def moveDisk(fp,tp): 
#     print("moving disk from",fp,"to",tp) 
# moveTower(3,"A","B","C")

# Recursive Python function to solve Tower of Hanoi

def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)

# Driver code
n = 3
TowerOfHanoi(n, 'A', 'B', 'C')  # A, B, C are the names of the rods
