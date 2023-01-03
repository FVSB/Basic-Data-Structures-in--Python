
class BST:

    def __init__(self, key, parent=None, left=None, right=None, size=1, high=0):
        self.key = key
        self.root = parent
        self.left = left
        self.right = right
        self.Size = size
        self.High = high
        self.Max = self.key
        self.Max_Node = self
        self.Min = self.key
        self.Min_Node = self

    def __str__(self):
        return str(self.key)
    # Comparador de igualdad

    def __eq__(self, __o: object) -> bool:
        return self.key == __o.key
    # Comparador de desigualdad

    def __ne__(self, __o: object) -> bool:
        return self.key != __o.key
    # Comparador de mayor estricto

    def __gt__(self, __o: object) -> bool:
        return self.key > __o.key

    # Comparador de menor estricto
    def __lt__(self, __o: object) -> bool:
        return self.key < __o.key

    # Comparador de mayot o igual
    def __ge__(self, __o: object) -> bool:
        return self.key >= __o.key

    # Comparador de menor o igual
    def __le__(self, __o: object) -> bool:
        return self.key <= __o.key

    def Re_Calculate(self):
        left_High: int = -1
        right_High: int = -1
        left_Size: int = 0
        right_Size: int = 0
        left_Min = self.Min
        Left_Min_Node = self.Min_Node
        right_Max = self.Max
        right_Max_Node = self.Max_Node

        if (self.left is not None):
            left_High = self.left.High
            left_Size = self.left.Size
            left_Min = self.left.Min
            Left_Min_Node = self.left.Min_Node

        if (self.right is not None):
            right_High = self.right.High
            right_Size = self.right.Size
            right_Max_Node = self.right.Max_Node
            right_Max = self.right.Max

        self.High = 1+(max(left_High, right_High))
        self.Size = 1+(left_Size+right_Size)

        if left_Min < self.Min:
            self.Min = left_Min
            self.Min_Node = Left_Min_Node

        if self.Max > right_Max:
            self.Max = right_Max
            self.Max_Node = right_Max_Node

    # Observar el balance de un nodo
    def Balance(self) -> int:
        left_High: int = -1
        right_High: int = -1
        if (self.left is not None):
            left_High = self.left.High
        if (self.right is not None):
            right_High = self.right.High
        return left_High-right_High

    def Balancerar(self):
        val = self.Balance()
        if (val > -1 and val < 2):
            return
        if (val > 1):
            if (self.left.Balance() < 0):
                self.left.RotateLeft()
            self.RotateRight()

    def Rotate_Left(self):
        # Mi hijo derecho
        My_Right_Child = self.right
        # El menor de los mayores
        Min_Of_Max = My_Right_Child.Min_Node
        # Al padre del Min_Of_Max se le asigna el hijo derecho de Min_Of_Max
        Min_Of_Max_Right_Child = Min_Of_Max.right
        Min_Of_Max_Right_Child.root = Min_Of_Max.root
        Min_Of_Max.root.left = Min_Of_Max_Right_Child
        # Asignar al padre el Min_of_Max como hijo derecho
        Min_Of_Max.right = Min_Of_Max.root
        # Asignarme como hijo izquierdo del Min_of_Max
        Min_Of_Max.left = self
        # Asignar a mi padre como padre del Min_of_Max
        Min_Of_Max.root = self.root
        # Asignar a mi padre como el Min_of_Max
        self.root = Min_Of_Max

    # Insertar un nodo

    def Insert(self, key):
        if (self.key > key):
            if (self.left is None):
                self.left = BST(key, self)

            else:
                self.left.Insert(key)
        else:
            if (self.right is None):
                self.right = BST(key, self)
            else:
                self.right.Insert(key)
        self.Re_Calculate()

    def Search(self, key) -> bool:
        if (self.key == key):
            return True
        elif (self.key < key):
            if (self.left is None):
                return False
            else:
                return self.left.Search(key)
        else:
            if (self.right is None):
                return False
            else:
                return self.right.Search(key)
