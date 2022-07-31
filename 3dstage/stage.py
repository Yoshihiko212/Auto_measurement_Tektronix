import pyvisa

#　　　　　　　　　　　　↓↓↓↓　三軸コマンドのurl　↓↓↓↓
#https://jp.optosigma.com/html/jp/software/motorize/manual_jp/SHOT-302GS_304GS.pdf


class Autostage:
    rm_ = pyvisa.ResourceManager()
    def __init__(self,interface):#接続先を指定
        self._stage = self.rm_.open_resource(interface)
    
        
    #移動量指定(正方向移動)　パルス数で指定(三軸ごとに1パルスの移動量が違うので)
    def move_plus(self,axis,pulsecount):

        self._stage.write(f"M:{axis}+P{pulsecount}")
        self._stage.write("G:")

    #移動量指定(負方向移動)　パルス数で指定(三軸ごとに1パルスの移動量が違うので)
    def move_minus(self,axis,pulsecount):
        self._stage.write(f"M:{axis}-P{pulsecount}")
        self._stage.write("G:")
        
    #原点復帰
    def to_zero(self):
        self._stage.write("A:W+P0+P0+P0+P0")
        self._stage.write("G:")
    
    #原点指定 
    def set_zero(self):
        self._stage.write("R:W")

    #移動場所指定
    def move_to(self,x,y,z,theta):
        self._stage.write(f"A:W+P{x}+P{y}+P{z}+P{theta}")
        self._stage.write("G:")

