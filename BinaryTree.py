


class BinaryNode():
    def __init__(self, pData, pSmall, pBig):
        self.data = pData
        self.bigger = pBig
        self.smaller = pSmall
        self.searched = False


class BinaryTree():
    def __init__(self):
        self.root = None
        self.counter = 0
        self.arr = []
        self.arrSRB = []
        self.arrSBR = []

    def insertValue(self, pValue):
        if (self.root == None):
            self.root = BinaryNode(pValue, None, None)
            self.counter += 1
            return


        aux = self.root
        while True:
            if(pValue > aux.data):
                if(aux.bigger == None):
                    aux.bigger = BinaryNode(pValue,None,None)
                    self.counter += 1
                    return
                aux = aux.bigger

            else:
                if(aux.smaller == None):
                    aux.smaller = BinaryNode(pValue, None, None)

                    self.counter += 1
                    return
                aux = aux.smaller



    def showTreeRSB(self):
        aux = self.root

        if (self.root == None):
            return "Empty tree"

        self.searchRootRSB(root = aux)

        return self.arr



    def searchRootRSB(self, root):
        self.arr.append(root.data)

        if(root.smaller != None):
            self.searchRootRSB(root.smaller)

        if(root.bigger != None):
            self.searchRootRSB(root.bigger)

        return

    def showTreeSRB(self):
        aux = self.root

        if (self.root == None):
            return "Empty tree"

        self.searchRootSRB(root=aux)

        return self.arrSRB

    def searchRootSRB(self, root):

        if (root.smaller != None):
            self.searchRootSRB(root.smaller)

        self.arrSRB.append(root.data)

        if (root.bigger != None):
            self.searchRootSRB(root.bigger)

        return

    def showTreeSBR(self):
        aux = self.root

        if (self.root == None):
            return "Empty tree"

        self.searchRootSBR(aux)

        return self.arrSBR


    def searchRootSBR(self, root):

        if (root.smaller != None):
            self.searchRootSBR(root.smaller)

        if (root.bigger != None):
            self.searchRootSBR(root.bigger)

        self.arrSBR.append(root.data)

        return

    def formatTree(self):
        string = ""

        for i in range(9):
            matrix = [["[]"] * 9]
            string += str(matrix)
            string += "\n"




        print(string)





tree = BinaryTree()
tree.insertValue(13)
tree.insertValue(11)
tree.insertValue(22)
tree.insertValue(10)
tree.insertValue(12)
tree.insertValue(15)
tree.insertValue(23)
tree.insertValue(99)
print(tree.counter)
print(tree.showTreeRSB())
#tree.formatTree()
print(tree.showTreeSRB())
print(tree.showTreeSBR())

