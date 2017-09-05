import numpy as np

class Spectrometer(object):
    """Class to represent an imaging spectrometer"""
    def __init__(self, fov, ifov, px,frame_pd=.002):
        self._fov = fov
        self._ifov = ifov
        self._px = px
        self._frame_pd = frame_pd
    

    def setFramePeriod(self,pd):
        self._frame_pd = pd

    @property
    def fieldOfView(self):
        return self._fov

    @property
    def crossFieldOfView(self):
        return self._ifov

    @property
    def scanLinePixels(self):
        return self._px

    def swathWidthAt(self,alt):
        return 2*alt*np.tan(np.radians(self.fieldOfView/2))
    
    def crossSwathWidthAt(self,alt):
        return 2*alt*np.tan(np.radians(self.crossFieldOfView/2))
    
    def pixelSizeAt(self,alt):
        return self.swathWidthAt(alt)/self.scanLinePixels

    def squareScanSpeedAt(self,alt):
        """the speed the spectrometer must move at to record square pixels"""
        return self.crossSwathWidthAt(alt)/self._frame_pd
        

#Predefined Spectrometers
class AVIRISClassic(Spectrometer):
    def __init__(self):
        Spectrometer.__init__(self,34,0.027,677)

class AVIRISNextGen(Spectrometer):
    def __init__(self):
        Spectrometer.__init__(self,36,0.023,640)

class HeadwallNanoHyperspec(Spectrometer):
    def __init__(self):
        Spectrometer.__init__(self,15.9,0.0249,640)

class HeadwallVNIR_SWIR_co_boresi(Spectrometer):
    def __init__(self):
        Spectrometer.__init__(self,20.887,0.030,380)

class SpecimFENIX(Spectrometer):
    def __init__(self):
        Spectrometer.__init__(self,32.3,0.028,384)

class NorskElektroOp(Spectrometer):
    def __init__(self):
        Spectrometer.__init__(self,34,0.02,384)

def spectrometerByName(name):
    return {
        "AVIRIS Classic":AVIRISClassic,
        "AVIRIS Next Gen":AVIRISNextGen,
        "Headwall Nano Hyperspec":HeadwallNanoHyperspec,
        "Headwall VNIR-SWIR co-boresi":HeadwallVNIR_SWIR_co_boresi,
        "Specim FENIX":SpecimFENIX,
        "Norsk Elektro Optikk HySpex":NorskElektroOp
    }[name]


if __name__ == '__main__':
    spec = HeadwallNanoHyperspec()
    spec.setFramePeriod(0.005)
    print(spec.swathWidthAt(20.12))
    print(spec.crossSwathWidthAt(20.12))
    print(spec.squareScanSpeedAt(20.12))
