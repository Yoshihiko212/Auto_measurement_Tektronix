import numpy as np

class Element:
    #接点の数
    NumberOfNodeInElement = 2

    def __init__(self):
        #要素の長さ
        self.length = 0
        #要素の断面積
        self.area = 0
        #ヤング率
        self.young = 0
        #要素を構成する接点番号
        self.ix = np.zeros(self.NumberOfNodeInElement)
        #要素を構成する接点の座標値
        self.xe = np.zeros(self.NumberOfNodeInElement)
        #要素の接点変位
        self.ue = np.zeros(self.NumberOfNodeInElement)
        #Bmatrix
        self.Bmatrix = np.zeros(self.NumberOfNodeInElement)
        #要素剛性行列
        self.Kmatrix = np.zeros((self.NumberOfNodeInElement,self.NumberOfNodeInElement))

    #Bmatrixの計算
    def makeBmatrix(self):
        self.length = self.xe[1]-self.xe[0]
        self.Bmatrix = np.array([[-1/self.length, 1/self.length]])

    #要素剛性行列の計算
    def makeElementStiffness(self):
        self.volume = self.area*self.length
        self.Kmatrix = self.young*self.volume*np.dot(self.Bmatrix.T,self.Bmatrix)

    #応力の計算
    def stressCalculation(self):
        return self.young*np.vdot(self.Bmatrix,self.ue)

        
Ele = Element()
Ele.xe = np.array([50,150])
Ele.area = 100
Ele.young = 200000
Ele.ue = np.array([0.01,0.025])

Ele.makeBmatrix()
Ele.makeElementStiffness()
scal = Ele.stressCalculation()