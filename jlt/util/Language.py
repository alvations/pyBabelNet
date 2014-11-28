#!/usr/bin/env python -*- coding: utf-8 -*-

class _Language:
    code = None
    def __init__(self, name, bRightToLeft=False):
        self.name = name
        self.bRightToLeft = bRightToLeft

    def isRightToLeft(self):
        return self.bRightToLeft
    
    def getName(self):
        return self.name
    
    def __str__(self):
        if self.code:
            return self.code
        for k, v in Language.__dict__.iteritems():
            if v is self:
                self.code = k
                return k
    
class Language:
    EN = _Language("English")
    
    AF = _Language("Afrikaans")
    SQ = _Language("Albanian")  
    AR = _Language("Arabic", True)  
    HY = _Language("Armenian")
    AZ = _Language("Azerbaijani")
    
    EU = _Language("Basque")  
    BN = _Language("Bengali") 
    BG = _Language("Bulgarian")
    
    CA = _Language("Catalan")  
    ZH = _Language("Chinese")  
    HR = _Language("Croatian")  
    CS = _Language("Czech")  
    
    DA = _Language("Danish")
    NL = _Language("Dutch")
    
    EO = _Language("Esperanto")
    ET = _Language("Estonian")
    
    FI = _Language("Finnish")
    FR = _Language("French")
    
    GL = _Language("Galician")
    KA = _Language("Georgian")
    DE = _Language("German")
    EL = _Language("Greek")
    
    HE = _Language("Hebrew", True)
    HI = _Language("Hindi")
    HU = _Language("Hungarian")
    
    IS = _Language("Icelandic")
    ID = _Language("Indonesian")
    GA = _Language("Irish")
    IT = _Language("Italian")
    
    JA = _Language("Japanese")
    
    KK = _Language("Kazakh")
    KO = _Language("Korean")
    
    LA = _Language("Latin")
    LV = _Language("Latvian")
    LT = _Language("Lithuanian")
    
    MS = _Language("Malay")
    MT = _Language("Maltese")
    
    NO = _Language("Norwegian")
    
    FA = _Language("Persian", True)
    PL = _Language("Polish")
    PT = _Language("Portuguese")
    
    RO = _Language("Romanian")
    RU = _Language("Russian")
    
    SR = _Language("Serbian")
    SIMPLE = _Language("Simple English")
    SK = _Language("Slovak")
    SL = _Language("Slovenian")
    ES = _Language("Spanish")
    SW = _Language("Swahili")
    SV = _Language("Swedish")
    
    TL = _Language("Tagalog")
    TA = _Language("Tamil")
    TH = _Language("Thai")
    BO = _Language("Tibetan")
    TR = _Language("Turkish")
    
    UK = _Language("Ukranian")
    UR = _Language("Urdu")
    
    VI = _Language("Vietnamese")
    
    CY = _Language("Welsh")