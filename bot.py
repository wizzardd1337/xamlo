_O11OO1Il100 = __import__('hashlib')
_lOII1l1IIIOI = 'https://pyobfuscate.com'
_O11O0ll10OI1 = _O11OO1Il100.sha256(_lOII1l1IIIOI.encode('utf-8')).digest()

def _00OO0I1Ill0l0lII00(_l0lOOlOIO1I, _11I101l11O01I1lI0):
    _0l0O0II000O1Ol0O = bytearray()
    _1OO0IOI11Il10Ill1 = 0
    while len(_0l0O0II000O1Ol0O) < _l0lOOlOIO1I:
        _0l0O0II000O1Ol0O += _O11OO1Il100.sha256(_11I101l11O01I1lI0 + _1OO0IOI11Il10Ill1.to_bytes(8, 'big')).digest()
        _1OO0IOI11Il10Ill1 += 1
    return bytes(_0l0O0II000O1Ol0O[:_l0lOOlOIO1I])
_OlOI0l001O1II110 = {}

def _OIlIlIO101Il1ll0IO(_Ol00001Il0lO0I, _O11OI0OIl01IlOOl):
    _O0O1OO10OOO1lIO1O1 = (_Ol00001Il0lO0I, _O11OI0OIl01IlOOl)
    if _O0O1OO10OOO1lIO1O1 in _OlOI0l001O1II110:
        return _OlOI0l001O1II110[_O0O1OO10OOO1lIO1O1]
    _001lO11OIO = bytes((_110OOOlO1IlI ^ _I1OI0IOOO1OOOI0I1 for _110OOOlO1IlI, _I1OI0IOOO1OOOI0I1 in zip(_Ol00001Il0lO0I, _00OO0I1Ill0l0lII00(len(_Ol00001Il0lO0I), _O11O0ll10OI1[::-1] + _O11OI0OIl01IlOOl)))).decode('utf-8', 'surrogatepass')
    _OlOI0l001O1II110[_O0O1OO10OOO1lIO1O1] = _001lO11OIO
    return _001lO11OIO

def _IOlIlOlI011(_OO1l0lOOlO1I, _OO0O11I0I0I010Ol1):
    _OIO001lO1IIOO0O = (_OO1l0lOOlO1I, _OO0O11I0I0I010Ol1)
    if _OIO001lO1IIOO0O in _OlOI0l001O1II110:
        return _OlOI0l001O1II110[_OIO001lO1IIOO0O]
    _II1O1l11lO00lIO01I = bytes((_1O1I10OlIll0 ^ _IlOO1OI1OIIlOl01 for _1O1I10OlIll0, _IlOO1OI1OIIlOl01 in zip(_OO1l0lOOlO1I, _00OO0I1Ill0l0lII00(len(_OO1l0lOOlO1I), _OO0O11I0I0I010Ol1 + _O11O0ll10OI1)))).decode('utf-8', 'surrogatepass')
    _OlOI0l001O1II110[_OIO001lO1IIOO0O] = _II1O1l11lO00lIO01I
    return _II1O1l11lO00lIO01I

def _OOlIO10I1I10(_1O1O0lOII1OI, _11O0O1O0lOl):
    _101llI10001Ol = (_1O1O0lOII1OI, _11O0O1O0lOl)
    if _101llI10001Ol in _OlOI0l001O1II110:
        return _OlOI0l001O1II110[_101llI10001Ol]
    _1O1IOlI10l1lll = bytes((_lOIO0lIIlO0l1OI11O ^ _Il11100l0Ol1OO for _lOIO0lIIlO0l1OI11O, _Il11100l0Ol1OO in zip(_1O1O0lOII1OI, _00OO0I1Ill0l0lII00(len(_1O1O0lOII1OI), _O11O0ll10OI1 + _11O0O1O0lOl)))).decode('utf-8', 'surrogatepass')
    _OlOI0l001O1II110[_101llI10001Ol] = _1O1IOlI10l1lll
    return _1O1IOlI10l1lll
_I101lIIII011lI = __import__(_OOlIO10I1I10(b'|\xc7\xce\r%<\xb4', b'\x19\x00/7'))
_1101I100l0O1lI0 = _OOlIO10I1I10(b'\x87:\xad\xb3\xec]\xde\xb3\x9d\xce8\x1e\xd7\xe1;hS\xe0\xc9t\x0c\xc9\x01', b'k\x9a\xfba')
_00011001l1II0I0Ol = _I101lIIII011lI.sha256(_1101I100l0O1lI0.encode(_OIlIlIO101Il1ll0IO(b'\x878\x98q\xdb', b'^\xa7~\xd3'))).digest()

def _lIllOl0OI0OO(_1IOI00OlOO0lIOlI, _10I0OI0OlOIl):
    _10Ol01lI1OOO011lll = bytearray()
    _01lI0I1Ill = 799632776 ^ 799632776
    while len(_10Ol01lI1OOO011lll) < _1IOI00OlOO0lIOlI:
        _10Ol01lI1OOO011lll += _I101lIIII011lI.sha256(_10I0OI0OlOIl + _01lI0I1Ill.to_bytes(10155058 ^ 10155066, _OIlIlIO101Il1ll0IO(b'lN\xd5', b'%O\xea\x94'))).digest()
        _01lI0I1Ill += 1721356154 ^ 1721356155
    return bytes(_10Ol01lI1OOO011lll[:_1IOI00OlOO0lIOlI])
_1OII0O1OI0111l = {}

def _IIOIOOl01IIl(_IOOl0O0ll00I0O11I, _1I11Il00I0):
    _lI1Il001100ll10I1 = (_IOOl0O0ll00I0O11I, _1I11Il00I0)
    if _lI1Il001100ll10I1 in _1OII0O1OI0111l:
        return _1OII0O1OI0111l[_lI1Il001100ll10I1]
    _l1lOOIllI0 = bytes((_lI1OI0l1l10 ^ _l1OIOIlllOl0l0I110 for _lI1OI0l1l10, _l1OIOIlllOl0l0I110 in zip(_IOOl0O0ll00I0O11I, _lIllOl0OI0OO(len(_IOOl0O0ll00I0O11I), _1I11Il00I0 + _00011001l1II0I0Ol)))).decode(_IOlIlOlI011(b'\xb3\x1d\xa2\xd3A', b'\x04\xeb`\xb2'), _OOlIO10I1I10(b'p\x98\x10u\xc8\xa2\xf7M\x1a\x8e\x9a\r\x1d', b'\xd6%{\xed'))
    _1OII0O1OI0111l[_lI1Il001100ll10I1] = _l1lOOIllI0
    return _l1lOOIllI0

def _OlIO0lIIO0IlIIO0(_111l01Il1I1l, _I10OIll0I1111l1):
    _011llO11l1 = (_111l01Il1I1l, _I10OIll0I1111l1)
    if _011llO11l1 in _1OII0O1OI0111l:
        return _1OII0O1OI0111l[_011llO11l1]
    _00O1OII1ll1I = bytes((_1llIlOI0O00I0l1O ^ _Il1I11011l0IIl for _1llIlOI0O00I0l1O, _Il1I11011l0IIl in zip(_111l01Il1I1l, _lIllOl0OI0OO(len(_111l01Il1I1l), _00011001l1II0I0Ol[::-(53788547 ^ 53788546)] + _I10OIll0I1111l1)))).decode(_IOlIlOlI011(b'\xda\xf4|\xd9\xa0', b'j\x9f\x83y'), _IOlIlOlI011(b'#\xc1\xc0f\xd5\xee\x17.\x18\xb4\xc6\xa0=', b'\x1a\xa7J\x85'))
    _1OII0O1OI0111l[_011llO11l1] = _00O1OII1ll1I
    return _00O1OII1ll1I

def _llO0Ol0111OlllIl(_1I10IO01O1O1l, _l01O10IOll0l0O):
    _I00I0IlIO0 = (_1I10IO01O1O1l, _l01O10IOll0l0O)
    if _I00I0IlIO0 in _1OII0O1OI0111l:
        return _1OII0O1OI0111l[_I00I0IlIO0]
    _Oll0lO0O0IIl = bytes((_OOlII11I11O1 ^ _11lI10OlO0 for _OOlII11I11O1, _11lI10OlO0 in zip(_1I10IO01O1O1l, _lIllOl0OI0OO(len(_1I10IO01O1O1l), _00011001l1II0I0Ol + _l01O10IOll0l0O)))).decode(_IOlIlOlI011(b'\x0e\x0e\xf6=\x07', b'\xb1\xa7\xd2\x9f'), _IOlIlOlI011(b'\xedP\x02\x12@\xb7Z\xect\xbbi\x01\xb6', b'Hs\xef\xf2'))
    _1OII0O1OI0111l[_I00I0IlIO0] = _Oll0lO0O0IIl
    return _Oll0lO0O0IIl
_OI00100Il10l1I = __import__(_IIOIOOl01IIl(b'\t\r\xa3\xd4K\xff\x8d', b'\xbd3\x99.'))
_0I011Ol0O01I011O = _IIOIOOl01IIl(b"\x13\xabX\xcd\xe8\x1a\x98\x82v',\xb9\xfeu\x881\xc1z\xb0\xcfPt\xf0", b'\xe8\xe1f\xd7')
_l1IIIl0OOl = _OI00100Il10l1I.sha256(_0I011Ol0O01I011O.encode(_OlIO0lIIO0IlIIO0(b'B;\xce\xd5\xa7', b'\x1eY\xdd\x97'))).digest()

def _llOII1IOO11II1l1(_0lIO011O1Il1, _1O1I0OI0l1l):
    _01I0I11II1lO011Ol1 = bytearray()
    _I1I1lOOlI0I1 = 1405198379 ^ 575391944 ^ (1326289848 ^ 1049099099)
    while len(_01I0I11II1lO011Ol1) < _0lIO011O1Il1:
        _01I0I11II1lO011Ol1 += _OI00100Il10l1I.sha256(_1O1I0OI0l1l + _I1I1lOOlI0I1.to_bytes(219606886 ^ 1242525823 ^ (1451363675 ^ 295408202), _OlIO0lIIO0IlIIO0(b'\xda\xfe\x85', b'\xdc\x83\x02k'))).digest()
        _I1I1lOOlI0I1 += 217657353 ^ 910955826 ^ (817917490 ^ 175459080)
    return bytes(_01I0I11II1lO011Ol1[:_0lIO011O1Il1])
_00OO0OlII0IOl0 = {}

def _l1OlI1O00IlI(_OII0111011Ol0, _IlIOO0II1I01lOl0l0):
    _O0lO011ll0I = (_OII0111011Ol0, _IlIOO0II1I01lOl0l0)
    if _O0lO011ll0I in _00OO0OlII0IOl0:
        return _00OO0OlII0IOl0[_O0lO011ll0I]
    _0l01OIl0OOI0IO1 = bytes((_Il1IO00O1I0 ^ _IO1O0OO0111 for _Il1IO00O1I0, _IO1O0OO0111 in zip(_OII0111011Ol0, _llOII1IOO11II1l1(len(_OII0111011Ol0), _IlIOO0II1I01lOl0l0 + _l1IIIl0OOl)))).decode(_IIOIOOl01IIl(b'\xef\x8er\xcf\xcd', b'\xf8\xe4\xf8\xbc'), _llO0Ol0111OlllIl(b'\x93<q\x11\xd0\xfa\xa3\xf1WK\x89H\x86', b'\x0f\xce\xd66'))
    _00OO0OlII0IOl0[_O0lO011ll0I] = _0l01OIl0OOI0IO1
    return _0l01OIl0OOI0IO1

def _1ll1OOOIOlOl0O(_010Ol0lIO1Ol1II0, _010IlIO1lIOI0):
    _10IOll000I10000I = (_010Ol0lIO1Ol1II0, _010IlIO1lIOI0)
    if _10IOll000I10000I in _00OO0OlII0IOl0:
        return _00OO0OlII0IOl0[_10IOll000I10000I]
    _11O1I0l1000Il1Il1 = bytes((_OlIl0IlI1l0 ^ _00l1l01111IlO for _OlIl0IlI1l0, _00l1l01111IlO in zip(_010Ol0lIO1Ol1II0, _llOII1IOO11II1l1(len(_010Ol0lIO1Ol1II0), _l1IIIl0OOl[::-(854153809 ^ 412059630 ^ (654948005 ^ 225405723))] + _010IlIO1lIOI0)))).decode(_OlIO0lIIO0IlIIO0(b'*\x9dL\xe9k', b'\xf9D\x88\xcf'), _llO0Ol0111OlllIl(b'\xd9\x1c\xdb\x8d9\xce\xd1\x05\x11\x04\xabC\xb5', b'\xe9\xbfv\x1c'))
    _00OO0OlII0IOl0[_10IOll000I10000I] = _11O1I0l1000Il1Il1
    return _11O1I0l1000Il1Il1

def _l10O10OlOl010O(_00IOIO1IO1IO0l, _Il1IOlIIO1OIlO):
    _0IIl01lll1 = (_00IOIO1IO1IO0l, _Il1IOlIIO1OIlO)
    if _0IIl01lll1 in _00OO0OlII0IOl0:
        return _00OO0OlII0IOl0[_0IIl01lll1]
    _0O0101OO1000OO0IlI = bytes((_00O1IlIIIlI1l00OO ^ _1lI0l010O1lOO0l for _00O1IlIIIlI1l00OO, _1lI0l010O1lOO0l in zip(_00IOIO1IO1IO0l, _llOII1IOO11II1l1(len(_00IOIO1IO1IO0l), _OI00100Il10l1I.sha256(_l1IIIl0OOl + _Il1IOlIIO1OIlO).digest())))).decode(_llO0Ol0111OlllIl(b'\xaeg!\x11\x0b', b'n\x15]\xb2'), _llO0Ol0111OlllIl(b'\x19\x81hb0!\xaft\x8a\xf6\xe1\x19\x1b', b'@\x14\x03\x92'))
    _00OO0OlII0IOl0[_0IIl01lll1] = _0O0101OO1000OO0IlI
    return _0O0101OO1000OO0IlI

def _1lI0O01IlOO1l(_00Ill000OOO, _lI10OlOO1OlIll0l):
    _0IllOIOl1Il10 = (_00Ill000OOO, _lI10OlOO1OlIll0l)
    if _0IllOIOl1Il10 in _00OO0OlII0IOl0:
        return _00OO0OlII0IOl0[_0IllOIOl1Il10]
    _011I0OIl1l1OO1I1l = bytes((_0l1OI1I0OlOOI ^ _I00lIlO0I00ll for _0l1OI1I0OlOOI, _I00lIlO0I00ll in zip(_00Ill000OOO, _llOII1IOO11II1l1(len(_00Ill000OOO), _l1IIIl0OOl + _lI10OlOO1OlIll0l)))).decode(_OlIO0lIIO0IlIIO0(b'c/\xfe\x178', b'\x8c\x90\xa2\xf0'), _IIOIOOl01IIl(b'\xcd1\x14\xa13jhS\xd0tC\xdf\x9e', b'e\x88\xb2\x94'))
    _00OO0OlII0IOl0[_0IllOIOl1Il10] = _011I0OIl1l1OO1I1l
    return _011I0OIl1l1OO1I1l
_I000ll1Il10ll = __import__(_l10O10OlOl010O(b'\x98\xe9\x82\xbd\x90\xb5\xaa', b'\x1a4%\xc1'))
_I01O0l1ll10I = _l10O10OlOl010O(b'\xab=\xc0\xf6\xd3\x1d_\xa3U\x80\x85k\xb4\xcd69\xe9\x9b\x84M\xf1\x15[', b'\x8c\x04O\x13')
_0IOO0IO011lI00OOlI = _I000ll1Il10ll.sha256(_I01O0l1ll10I.encode(_l1OlI1O00IlI(b'0\x9e5}P', b'\xd7\x93\xd2\xbc'))).digest()

def _00OOlO0011(_OI1lI100I01Il1OO0I, _IlOI110III1lOlOO):
    _I0l0l1I1lO1lO00I0 = bytearray()
    _00l1O10O00OIlOIl = 964935906 ^ 733663488 ^ (1103446883 ^ 245228518) ^ (2000229151 ^ 446843637 ^ (1443200450 ^ 1728025935))
    while len(_I0l0l1I1lO1lO00I0) < _OI1lI100I01Il1OO0I:
        _I0l0l1I1lO1lO00I0 += _I000ll1Il10ll.sha256(_IlOI110III1lOlOO + _00l1O10O00OIlOIl.to_bytes(1278688006 ^ 1600859144 ^ (11775839 ^ 151920807) ^ (301396589 ^ 1229646642 ^ (673049054 ^ 1782605951)), _1lI0O01IlOO1l(b'\xd5\xfct', b'\xb3\xc1K\xf6'))).digest()
        _00l1O10O00OIlOIl += 1154075443 ^ 1021500239 ^ (1686404650 ^ 2122920851) ^ (1296574899 ^ 1326601026 ^ (304821935 ^ 1918308762))
    return bytes(_I0l0l1I1lO1lO00I0[:_OI1lI100I01Il1OO0I])
_OOl0l00l1l1I = {}

def _IIIIO0lIOO1O0(_01OlIO1O010IOOI0O1, _IO1O0Oll01):
    _I011I1l11l01lOI = (_01OlIO1O010IOOI0O1, _IO1O0Oll01)
    if _I011I1l11l01lOI in _OOl0l00l1l1I:
        return _OOl0l00l1l1I[_I011I1l11l01lOI]
    _l11IlO0IO1Ol1Ol0 = bytes((_O1lIll0l1O1O110lI0 ^ _1lO1O1I1OI for _O1lIll0l1O1O110lI0, _1lO1O1I1OI in zip(_01OlIO1O010IOOI0O1, _00OOlO0011(len(_01OlIO1O010IOOI0O1), _0IOO0IO011lI00OOlI[::-(658581927 ^ 1688965279 ^ (1513437461 ^ 368485749) ^ (702668928 ^ 663355914 ^ (1408791399 ^ 1371190452)))] + _IO1O0Oll01)))).decode(_l10O10OlOl010O(b'\x0bM\xee*\xb4', b'\\\xf1\xef\x8f'), _l10O10OlOl010O(b'_g\xb7%\x9b\x80\xc8\xb8L\xdd\x97\x02\x8e', b'\xee\xb3\xfa~'))
    _OOl0l00l1l1I[_I011I1l11l01lOI] = _l11IlO0IO1Ol1Ol0
    return _l11IlO0IO1Ol1Ol0

def _1O10OO0l0OO1(_10l0O11I0I, _0I1IOl1O0Il11IOI1I):
    _lO10OIIlOlO100I = (_10l0O11I0I, _0I1IOl1O0Il11IOI1I)
    if _lO10OIIlOlO100I in _OOl0l00l1l1I:
        return _OOl0l00l1l1I[_lO10OIIlOlO100I]
    _0l1I11II1OIl = bytes((_1IIII0OIOOOl0ll ^ _lO0ll0lIOll00Ill for _1IIII0OIOOOl0ll, _lO0ll0lIOll00Ill in zip(_10l0O11I0I, _00OOlO0011(len(_10l0O11I0I), _0I1IOl1O0Il11IOI1I + _0IOO0IO011lI00OOlI)))).decode(_1lI0O01IlOO1l(b'\x15\xca\xfa\xdeF', b'DC|\xd1'), _1ll1OOOIOlOl0O(b'\x16\t\xbb\xady\x91o\xa5\xe16 \xdb$', b'\xdc\xb1\xa5]'))
    _OOl0l00l1l1I[_lO10OIIlOlO100I] = _0l1I11II1OIl
    return _0l1I11II1OIl
_OO1lOIOO00lOO0I = __import__(_IIIIO0lIOO1O0(b'\xba\xba\x82Z\xa9\xcei', b'\xdfj\x08\xc7'))
_01IOIOO0lO0III0 = _1O10OO0l0OO1(b'T^\x8b\x89\xfaW\xcf~\x13\xb58\xe6m\xc0\xf7\xfe\xd1\x9ca&\xd7D\xc6', b'\xaa\xc9}\xc7')
_1I11OI0IOllIlO01I = _OO1lOIOO00lOO0I.sha256(_01IOIOO0lO0III0.encode(_IIIIO0lIOO1O0(b'\xfb\xf3\x8e`\xff', b'\r\x98\xd3}'))).digest()

def _OOIIIlllOO1(_I0IIlOOl0O0ll, _l0l1llIll1OIllI0l1):
    _I0l0II111IOI1l1 = bytearray()
    _Ol0I01IIOO = 1969384882 ^ 1713589257 ^ (1603231302 ^ 1813648280) ^ (1971994538 ^ 1752742126 ^ (115267895 ^ 47423394)) ^ (1002772780 ^ 312975779 ^ (1241985938 ^ 945481580) ^ (1367627426 ^ 542325997 ^ (1700447662 ^ 1989766692)))
    while len(_I0l0II111IOI1l1) < _I0IIlOOl0O0ll:
        _I0l0II111IOI1l1 += _OO1lOIOO00lOO0I.sha256(_l0l1llIll1OIllI0l1 + _Ol0I01IIOO.to_bytes(328001922 ^ 1380323234 ^ (409304363 ^ 1120079765) ^ (2077047070 ^ 1513312063 ^ (1960262324 ^ 1268715026)) ^ (1046845452 ^ 1456361322 ^ (412434182 ^ 1011143391) ^ (1542160575 ^ 556203975 ^ (1432364166 ^ 1712174928))), _IIIIO0lIOO1O0(b'30\xbc', b'1\x86\x0f\x9a'))).digest()
        _Ol0I01IIOO += 195731500 ^ 1590050057 ^ (1419198879 ^ 1316694278) ^ (47446269 ^ 1881762826 ^ (2054099979 ^ 744087639)) ^ (354412185 ^ 2059968008 ^ (1322084100 ^ 1619436567) ^ (1348798991 ^ 2094718525 ^ (1106175923 ^ 1199643925)))
    return bytes(_I0l0II111IOI1l1[:_I0IIlOOl0O0ll])
_1OOOllOlOOl = {}

def _l1IO0OOI1II0O101(_OII1IOl1llIl, _OIlOOI101llOl000):
    _OIl1000O110IO = (_OII1IOl1llIl, _OIlOOI101llOl000)
    if _OIl1000O110IO in _1OOOllOlOOl:
        return _1OOOllOlOOl[_OIl1000O110IO]
    _OI1IllIlO1OIlO = bytes((_0O0Ol0001I ^ _IOIlII1l0000 for _0O0Ol0001I, _IOIlII1l0000 in zip(_OII1IOl1llIl, _OOIIIlllOO1(len(_OII1IOl1llIl), _OO1lOIOO00lOO0I.sha256(_1I11OI0IOllIlO01I + _OIlOOI101llOl000).digest())))).decode(_IIIIO0lIOO1O0(b'\x7f\xaf\xe9\xc4\xce', b'\xf1\xb3S\xd2'), _IIIIO0lIOO1O0(b'\x9dy\x1em\xddNfx!\xa1\x9f\x08j', b'\xc2#\xc2r'))
    _1OOOllOlOOl[_OIl1000O110IO] = _OI1IllIlO1OIlO
    return _OI1IllIlO1OIlO

def _11I1O11OI0l(_lIII1l00O1OOOOI001, _lO110lO10Ol10):
    _0IO1I1IO1OOII0 = (_lIII1l00O1OOOOI001, _lO110lO10Ol10)
    if _0IO1I1IO1OOII0 in _1OOOllOlOOl:
        return _1OOOllOlOOl[_0IO1I1IO1OOII0]
    _I1l100III0I1l = bytes((_IOOIl11OlI0lI01II ^ _I1llI010IIO1IOIIl for _IOOIl11OlI0lI01II, _I1llI010IIO1IOIIl in zip(_lIII1l00O1OOOOI001, _OOIIIlllOO1(len(_lIII1l00O1OOOOI001), _1I11OI0IOllIlO01I[::-(2053235335 ^ 1095983752 ^ (1995304870 ^ 1007519090) ^ (1719515124 ^ 1729181548 ^ (1090476054 ^ 51574138)) ^ (929767309 ^ 2047053589 ^ (789090496 ^ 31232275) ^ (1182017435 ^ 1719884770 ^ (1588273131 ^ 783496695))))] + _lO110lO10Ol10)))).decode(_1O10OO0l0OO1(b'\x8ew\xa02q', b'=_\xe19'), _1O10OO0l0OO1(b'\xe9\x08\xc0\xca\x18\xdcA\x94\xf9\xf6!\x08/', b'\xaf[#r'))
    _1OOOllOlOOl[_0IO1I1IO1OOII0] = _I1l100III0I1l
    return _I1l100III0I1l

def _lI00Ol0l11I0II0l1(_l111I0OIIIl, _1lOl00lIOlIll11lII):
    _01O00OOI00 = (_l111I0OIIIl, _1lOl00lIOlIll11lII)
    if _01O00OOI00 in _1OOOllOlOOl:
        return _1OOOllOlOOl[_01O00OOI00]
    _IOOl0OO1llO1IlO = bytes((_I0O0lI1lOO ^ _0IO1Il1l01l1 for _I0O0lI1lOO, _0IO1Il1l01l1 in zip(_l111I0OIIIl, _OOIIIlllOO1(len(_l111I0OIIIl), _1lOl00lIOlIll11lII + _1I11OI0IOllIlO01I)))).decode(_IIIIO0lIOO1O0(b'w\xe2\xaf\xb0\x81', b'!p\xa9\xaf'), _IIIIO0lIOO1O0(b'*F\x00\xa9\xfc\x99\xad4\xba\x07)\x0e\r', b'\xeaC\xa9\xb0'))
    _1OOOllOlOOl[_01O00OOI00] = _IOOl0OO1llO1IlO
    return _IOOl0OO1llO1IlO

def _OIlIl0O100ll0lO01(_0O1I1O1I0l, _O0OIllO00I):
    _I1IO0OIl1llIOII101 = (_0O1I1O1I0l, _O0OIllO00I)
    if _I1IO0OIl1llIOII101 in _1OOOllOlOOl:
        return _1OOOllOlOOl[_I1IO0OIl1llIOII101]
    _01l0Ol1O00lIIlOIO = bytes((_OlI100IO10lll10 ^ _011l0OlI1Il1 for _OlI100IO10lll10, _011l0OlI1Il1 in zip(_0O1I1O1I0l, _OOIIIlllOO1(len(_0O1I1O1I0l), _1I11OI0IOllIlO01I + _O0OIllO00I)))).decode(_IIIIO0lIOO1O0(b'\t\xa1\xd95\xd8', b'\xc34/&'), _1O10OO0l0OO1(b'\xbc\xff\x9c\tV\x93\x13\xaf4\xbd\xfe\x84\xf6', b')\xf7q\xb9'))
    _1OOOllOlOOl[_I1IO0OIl1llIOII101] = _01l0Ol1O00lIIlOIO
    return _01l0Ol1O00lIIlOIO
_0l11l1IO1lI1lIII10 = __import__(_lI00Ol0l11I0II0l1(b'\xf0\xe3\x82\xf3j\x9a\x1e', b'\x90A\x14\xbf'))
_l10OO0I0I0OlOIl = _lI00Ol0l11I0II0l1(b'\x19or\xc4\xf0\xc6\xb4KhM\x97\xa5\xbc\xd6\x05\xd6a\rg\x13\xf9\xe2\x97', b'L\x8a\xfc\x9b')
_0OOlO10Ol1l0 = _0l11l1IO1lI1lIII10.sha256(_l10OO0I0I0OlOIl.encode(_lI00Ol0l11I0II0l1(b'\x88S\xb8~\x7f', b'\x12\xf0\x9e\xca'))).digest()

def _11lO001OO1l01I0(_lll11OO0O100I00, _ll0I0lOOl1lI):
    _01I0OlO0OlO0O = bytearray()
    _OIOl1001110Il1OO = 793663558 ^ 987319918 ^ (1390807290 ^ 1439406183) ^ (591213841 ^ 2119526151 ^ (259285689 ^ 1396824122)) ^ (1119281404 ^ 393280358 ^ (1711958651 ^ 1984544832) ^ (2009761883 ^ 2043353646 ^ (2000999263 ^ 1402570846))) ^ (1672116533 ^ 1674778761 ^ (861912811 ^ 972055951) ^ (815015428 ^ 1468394204 ^ (700477632 ^ 914230691)) ^ (1042142092 ^ 46038065 ^ (517552345 ^ 1856991557) ^ (1801055864 ^ 1890266874 ^ (794218319 ^ 1991701626))))
    while len(_01I0OlO0OlO0O) < _lll11OO0O100I00:
        _01I0OlO0OlO0O += _0l11l1IO1lI1lIII10.sha256(_ll0I0lOOl1lI + _OIOl1001110Il1OO.to_bytes(9129341 ^ 1675923926 ^ (771880984 ^ 148759093) ^ (173227941 ^ 693438254 ^ (1750237154 ^ 1536329708)) ^ (688806679 ^ 1280330713 ^ (206360821 ^ 1107747081) ^ (300203440 ^ 1361321208 ^ (85564940 ^ 79252705))) ^ (749539347 ^ 27961220 ^ (1141797327 ^ 1413917131) ^ (631551093 ^ 499631693 ^ (1139936825 ^ 611470195)) ^ (501326961 ^ 533978089 ^ (420675845 ^ 2102175432) ^ (1974389010 ^ 1446671236 ^ (1237739802 ^ 1368524708)))), _11I1O11OI0l(b'B\xef\xfc', b'\x98\x8f\xf1\xd3'))).digest()
        _OIOl1001110Il1OO += 2101855293 ^ 1741865498 ^ (297255547 ^ 775985938) ^ (1410517364 ^ 1974423894 ^ (680221945 ^ 137514984)) ^ (1902754088 ^ 20184955 ^ (637370313 ^ 955959771) ^ (45309778 ^ 325620987 ^ (768571758 ^ 1469263209))) ^ (925719244 ^ 1085979320 ^ (23375169 ^ 889643826) ^ (1529707399 ^ 152545938 ^ (689262325 ^ 1050118448)) ^ (764838385 ^ 1991266791 ^ (845606481 ^ 1347844542) ^ (925283384 ^ 654908651 ^ (1909621476 ^ 2082107018))))
    return bytes(_01I0OlO0OlO0O[:_lll11OO0O100I00])
_IlllIOl1IOIO = {}

def _Oll0Ill0Il(_011IO1lO1I, _l0IlIl0I1ll0l0):
    _I0l0O0l1IIOIII = (_011IO1lO1I, _l0IlIl0I1ll0l0)
    if _I0l0O0l1IIOIII in _IlllIOl1IOIO:
        return _IlllIOl1IOIO[_I0l0O0l1IIOIII]
    _0O1ll0IOIII = bytes((_1I0OOI1l0l1II0O10 ^ _O0l0lI11OlllO0 for _1I0OOI1l0l1II0O10, _O0l0lI11OlllO0 in zip(_011IO1lO1I, _11lO001OO1l01I0(len(_011IO1lO1I), _l0IlIl0I1ll0l0 + _0OOlO10Ol1l0)))).decode(_lI00Ol0l11I0II0l1(b'h"\x95X\xaf', b'\xcf\x98d\xd7'), _lI00Ol0l11I0II0l1(b'\xe5\xde\x05\x98Ybc\x16}\x0f\xbe!\xf2', b'!{\xd1\xa3'))
    _IlllIOl1IOIO[_I0l0O0l1IIOIII] = _0O1ll0IOIII
    return _0O1ll0IOIII

def _1OO01O10II0O(_OIO00lIIIIlOI1, _01OOl010lOlI):
    _IIlO10OOIOI1 = (_OIO00lIIIIlOI1, _01OOl010lOlI)
    if _IIlO10OOIOI1 in _IlllIOl1IOIO:
        return _IlllIOl1IOIO[_IIlO10OOIOI1]
    _I10I0Ol0I0ll = bytes((_l00OI10IOIOlIIl ^ _1l1lO1OOOIOIIIO for _l00OI10IOIOlIIl, _1l1lO1OOOIOIIIO in zip(_OIO00lIIIIlOI1, _11lO001OO1l01I0(len(_OIO00lIIIIlOI1), _0OOlO10Ol1l0 + _01OOl010lOlI)))).decode(_OIlIl0O100ll0lO01(b'\x05\xa1H\x95g', b'\xf7Z]\x93'), _11I1O11OI0l(b'\x1c\xa0hT\xa5\xf3o\x03\xe6\x0e\x14Y\xf0', b'A\xf1\xa7o'))
    _IlllIOl1IOIO[_IIlO10OOIOI1] = _I10I0Ol0I0ll
    return _I10I0Ol0I0ll
import os as _1lOIO1OOOIllO01
import json as _I0II0l1IlI1IO1OOI1
import random
import logging as _OI10l0lOOIlO
from telegram import Update as _0ll0ll1IIOl1OIl, InlineKeyboardMarkup as _11IOOl1lll1I1, InlineKeyboardButton as _00l0IO0l0IOl1l0OlO
from telegram.ext import ApplicationBuilder as _IIOlIOOlI1I, CommandHandler as _llOO0IO11IO00I0ll, MessageHandler as _O0IlIl011ll0I0, CallbackQueryHandler as _OI0I1Il1OOIl, ContextTypes as _O011I10Ol0, filters as _00IIlO1II0O0O0OIO0
from groq import AsyncGroq as _O0100ll00l0IlOI
from keep_alive import keep_alive as _I00011O0I1OO
_Ol0OOlIllI1OO0 = _1lOIO1OOOIllO01.getenv(_Oll0Ill0Il(b'\xe4 \x90\xbb\xb8G\x80z\xfc', b' \xfa:\xf1'), _Oll0Ill0Il(b'\xea\xea\x8d\xb3\xdd\x82\x91\xf8\x93\x8bp\xc9a\xd2\xde\xc7\x84\x15\xf4\x1c\xfc\x97\x1d\xeeaGn_\xaa\xc6\x058\xf4\\\x1b"<M\xf6\xdax\xd6\xea\x13\xe0\xdc', b'\x90\xbb-\xca'))
_IO0I11Ol0l10 = _1lOIO1OOOIllO01.getenv(_Oll0Ill0Il(b':\xe9i\xdcU\r\x12\x86', b'E)\xdc\x17'), _Oll0Ill0Il(b'\xda\xbcM.Y\xb2\xff\xb0\x81\xc8\n]\x9d\xcb\xd6W\xc1\xe8/\x9b\xf5L\xc6\xbdz\xf9\xf6\xd6\xd2\xd6\xd6\xa0\xbcp\n\xcdS{\xba\x03\xd8\x8d\xd1\x98\x976\xa0\xbc\xe5\x048\xef\xe2\xb1\x19J', b'\xe8j\xd6E'))
_00l11OlOl1 = _O0100ll00l0IlOI(api_key=_IO0I11Ol0l10)
_OI10l0lOOIlO.basicConfig(format=_Oll0Ill0Il(b'\xb6\xec5t\xe0\x88\xc5\xbd\x8c\t\x1a\x0e\xa2]\x1c\x82Y%\xd4#\x96W8\xe7&D\x19\xb8\xeaNc\xf7JK\x9d\xcf\xc9V\xb29c', b'\x1a\xdfKY'), level=_OI10l0lOOIlO.INFO)
_II0IO00l0I000O0I0 = _OI10l0lOOIlO.getLogger(__name__)
_11lIllIO0l = _Oll0Ill0Il(b'\xecm\x9b\xd9!\xd9\xac\x16\x08\x07\xab\x7f\x10a\x0c]\xbbSeK\xa1\xd6\r\xc7@\xa7\xafE\x9aF\x98\xfe\xf2\xcf\xe3\x8a\xcc\x14\xb2\x9c\xe6|K\xeb6\xe8\xfb\xf5_"i{DDPT*\xf2\xd4v+\xdb\xcc\x99\x17z\x95\xc4\x0bHF\xda\x80\xb0\x90\xcdE\x14\x1c\x04\x99\xf9vI\xfc\xe4\xc4G:`%\xa7u=\xdb}q\x9e\x12\x11\xb22\x05$\xcd\x8cg%(\xde\xa2O\x95;\xefa\xe1.\x83\x02&}IK\xff\xfe\xde\xc5~\x181\xdc\xeaC\xd0\x06\xdb\xb2(\x1a\xf4\xb1\x17\xd9\xd3\xccl\x8bx\xed^\xbdl\x8d\x86\x15\xfc]`\x11Z\xc4\x16J\x0ff>\xe72\xab\xd9\x0e\x94-\xaf\x96Z\x01\xd7\xbf\x93\xcfU\xc3c\xe9\x1c\xd2\xd9\xdf\xbcu\xcb\xfbw\xe8R\xd6\xc0\xd7y\xb1\x14,\xc24\xa1\x1bW9\\\r\x0e\xd6>X\xa6/\xac^\x119M+P\xb4a;S%\x17\xbdY\x82\x05]\r#+ri=u\xce\x00\xc4\\\xc4VT\x0ebA\xd5\xd8\xbb\xaaG9%\xdc\xfa0\xc6Y\x86Dd\x1d3x\xedB\xa6\x9a\xa2\xdbQ\x04\xf6\xda\xe5\xc1^\rN\x81k\xb4?\xa16\x00k93\x9e\xac\x105\x84\xdeL\x87XWE^Y~\x0f\xed\x0b\x86\xd8\xb81\x9b\x9b\x93\x1a\x96\x9d\xd3\xfc_\xa4\xba\xcc\xde\x86\\<\xb3aI\x8e\t`1\xefu\xd5y\xc8\x0e\xbf\xdf3D\x82\x8a\x1aD\xd6\x8f\xb2\x0b \xf9U)\xcf@\x81\x91_5\xf4\x1e\x9c\x07gA\x95\xf5{\x02\xb5\r4}\x15\x1d\xd8\xc1\x1a\x84\x1a\xbd2\x94\x02\xb8\xed\xfd\xfa\xee\xc8\xb9P\xc6w\xb17W\xbd\x03\xce\x96\x02\xdc\xcaS\x81~\xa5\xb0N\x99\xfc\x0f.\xc4\xc1Z\x0c\x98\xa3\x17&\x86q\xfb\xbb\xa3o\xe1[!\x06\xed\xe3\x96\x88\x15\xef1S%!\xd5#\xea\xbc\xe1\x0c\x06\xfb\xa8\xa0%\xc4\x84I\x83\x9d\x13\xf1\xe2\xae\xb3u\xed\xc2\xee\x1e\x9d?\x93)\xea\xa4W\x18\xe0o&\xd9\x87m\xe3i\x01#K\xbe\nTRG\xcc\xd2m#\xb76=G\xc2C\xaf\xda\xa9\xcd\x84\x1f\xa5\xaen\xa5\x86\xb8\x1d\xad\xa6Y\xca\xda\xbe\xaeSex%\x0b$R:A\x83\x10\xb3\xf3\x03c\x08\xfd|\xd5$M\n\x8da\x90#\xab\xf4\xd5\xc9\xa0\xaf]\xea\xf6\xbf\xad\xb6\xd9\xdd\xb5\x12F\x8b\xf5?X\xad\xf9\x12\xeat\x83\xe7T\xea\xeb\xc7\x81\x1d\x10\xbf\xaaNM\x1c2\xc37`\x95\xf0\xc1\x021\xcb`\xa4/$\xb5\x1e:4\x8e\xadbU\x9d\xc2z\xf7\x80\xd2E\xb7\x88\x81\x1b\xb9 \x0f\x01MQ\x08\xe5\xdb`[\xd9T\xa7\xe2\xd9\n@F)}\xecr`G*a\xee\xbd*\xab\xc3)\xfc+\x02\xcd,\\\x02\x8897\xd4\xbc\xb0\xee\xdd\xbb\xf5\xc0\x19\xc2\x83\x9e-d\xaf{\xbe\xec\xb1\xd8\xf0Wm\xedi\xefq\x0fj\x01\x83\xd7\xfc\xbe"\xe7\xb0\xf0o\xf2\x85/\x06\xcf\xae\xa7\x85\xda\xc3\xf3\xc6"\x8aw\xb3sz\xf5H\x96`>\xe69R\xf1I\xa2\xcd\x8f\xa8\x08\x0f\xdc\x93\xcf\x92*\xbf\x89Z\xb7\x8d\x1es\x8d\xbe\xa0N\x94\x13\x8b\x9c\x12\\0/\xe0B\xa3\xda\xd1\xb6\xf3\xa3J\xcd\xd0\x11\x93\xebo\xef\xd9G=\x84\x1a\xec\x10\xb7q\xc8\x8b\xf8\xfe\x99>Z\xdd\xde\x88\x8f&\xdc\xfcm\x95,\x9e\x8a\xd5\xcbTG\x07\xbb\x18E\xc2(\xdf\xa7\xa6\xbd\x8f\xc1h#\xe7\xf7\xbfw\x0f\x84\xb2\xbc\xf0\xac\xa8\x1a\xb6K\x01)\xecI\x8a\x8dc\xd9\x0c"#9v9\xcdY\x0c\xa32/\x00-a\xebE\xb3\xc26I\xfb\x0e\x90\x7f\xb3r-\x9d\x99\xfd\xd9\x9aT\xb6C4\x9b\xc9\xe9\x96\xfc\x82"p`\xb9-\xb1\xe5B-\x1ee\xe8\x87\xa4\xab\xfd\x06\xc0\x96\xf4\xfb\xbf\xde\xea\x0c\t\xea\xd0\t\\\x8a\xd5\xcc\x08\xba\xa2\x87\xb2\x00\x96^\x7f\xde\x90U\xe1\x08\x85?\xe3&\xd4\xfeB\xb7\xa3\xce\x03I\xd6\x11\xb4\x01\xae\xdd\xef\xa7\x12\xd8a\xe2YS\xfa3Hm6\xac5\xff/\x82_ %\x8ed\x05\x80\xe4\x05XWT\n\xa4n\xcd\xd3\xcct\xa4 <}\x0e\xe1\xf5\xd8|\x83\x8c{\x1dO\xf4\xe6ve1Gn[\xc8fA\x95\xc5\x81\xd3\xfa\xf4d\xedF\x9a\xe9\xc1\xa5\xfc\xe1{\xbe=Uy\xe7\xae\xd8a\xe6]\xd5T=\xe1\xa9\x89\x12\xc1r\x7f0yn\x81\xfe\x88Io\xb4\xfc\x99Z\xd2J\x1d\xe8E\x8f\xd8ra\xb3d\xfdq\xf5\xd8\x11\xd3\x81`\xa2Gi1Y\xb3E\xc2\xcf\xb3S\xf7\xa7\x18\xe8T\xf8\x91\x9a\xa5]I6\xd0\xabX\xd6\x86\xce%\x1b\xe2\x8d\x87\x9e\xfdv\xe6\xca\x82\x17\x0f\x9c\x8ca\x12jd\xd8|\x876\x92\xd5\xfa]\xd1f\x9e,\x91\x81^$\xf2L[\x18B8\xd2\x83\xb0\x83-\xd5BSA7N\x19\xa5\xdcM\xc2\xb4^\xe3.\xf2=S\x94Ph\x7fb\xf4\x86\xc4l\xa8\xe7h\xb1\xb6\xc5P7\x8aD\x88\xfa<\xf5\xbe\xe5\x1e\xc4\xfb2\x84\xd2v??\xbabI\xa5y1\xa7\x81v5\xf3q\\\xcaoX\x07\xfb\xb5\x9e8RSu\x17\xfet\xd0\xb6qRW7\\\x90\x11]s\xf19\xfac\xa29\xdb\xd8Sk?}\xe0V\x0ezQK\xefA%v\xba6:\xfc\x07,d18\x0e\x86:\xe0\x17>\x7f^\x850\xfe\xa8\xa3\x90k\xa7\x1a\x01\xe8\xa7\xeb\\~\x7f\xae\xf3\xb3\xbcn\xf9\xd6\xc8x\xffI\x90\x9b\xd1\xc4\xf73#\xbfE\xc5\xc5\n\xf2\x82wP\xfd\xfe\xda\xe0\x1c\xd2PWF\xb6\xccL\x8f\x1f\x1fq&/\x90\xba \x01\x03x\xcb=P\x92\xe8\x81\x03\x05\xcc\xc8\xa3")\x9e\xc8\x97j\xa0\xeaT\xb0\x97\x1a\xd2\xa9\xbd1\xcc\xab\xd7BS\xb5.\xd0\xc2`Oi\x1e\x1f\xe6\xf9\x01\x96y\xfe\xb5\xa5\xb2\x1e\x93\xdb\xc1\x98\x97%\xcd\xc8{\x03\x98\xab\xbdv\xef\x0f\xde1\x03\xaf\xab`zWC\xf6U\nB\xbe^\xf7\xde\xe3\x10}D"\xd6\xc9>\x88*\x08h\xf9\xb3L-\xecu?\xd2\xb7U5B,\xce\xd7C\x06\n\xc8&BTF\x15\xdd\xb9\xf9\xfd\x82\x0b3,8\x9c/\xf1\xcd\x12\xe0*\xf5\xe8\xdb\xcb\x00\x0e:\xdf\xc8\xc9\xbd\xf2_6J\xc8-\xf2\xb2\x84,->P\xfe\xcb\xb6\xdf\x88\xba_!T\xb2\xe3T\xf5Z\x12\x87\xd3\x0b\xb5\x1f\xe9\xcb\xfb=\xdf\x9b\xd1\x8d\xcd\xc6\xd0\x90\x84\xcd\x90\xbf\xb5\xc0e\xb3~j\xff\xc37\xc7\x9b\x13\x1a\x18\x18\x95\xff\x19\xa3m\x0eK\x1a\xa2\xf9\xba*>\xad7\xdc\xf4\xba\x05\x1a_\xd4c\x8e\x95\x86\x7fg\xe7\xd9\xfeX\\$\'a\x8d\xe1s\xb9\xf8\xe3\xeb1\xa2z#\xf6\x9e\xf28\xf6\xe8\x1f\x98\x9dl*\xa2\xaf\xe2l\xd7\xe1O\xcb\x94%\xa5;\x9b[\x1a\\kg\x84,eo\xe9+d\xb6[*P\x10~\x07\xb30\x02.r\xd9\xcbu\x00\x0bZ5\xd7\x11\xed\x1e\x8cP\xa1\xf7\x82\xa0\'\x8c\x05\xe7Z\xeb\x8ft\xbb\xab\xf7FKv\xee\xf1"\xad\x050\x08z\xc1U@\x80\xfa\xe6 \xddX\xd2\x07\x83\xd7$r\xa7Y\x8d\x84\x8e*\xef^\xc4\'\xf2N\xaa\xac=\xb4\xdb\xd8\xfeo\xe8\xe0\xc9\xaa\xd6K):\xa9\xdb\xbb\xaf\xdd\xbb.Ed\xbcK\xb5\xc8o\xb1K\xd8m\xa6\xf9\x8f\xa5nN\xaf\xbdXo\xd8\xbbOF\x96\x8e\xb9+K\x8a\xff\x8f\x15\xac\xdb\xff9%\xfb\x02\x16=r6\x9b+\x1e\x9a\x05\x1e#\x85s\x04\x96\xdcm\xa6y\xf3\xa9\xf5\xfc_e\x7f\x99\xd8h\x14\x1f\x84\xf3\xbb\x97\x87NX+\xb7\x18\xad\xda\x8d\x8c-\x01X\x8c\x04\x0ef\xf2-\xf2Bf*\xca\xae<\xce\xa1\xac\r4\xb0\xe5\x9b*\xcd\x07\xa9\x190\xd6\xa8\x96\xdbW;\xf2\x9f\xb4!X9\xcd:9\xba\xcf\x0e\x99\xa5\x0e\xbf\x92\xd3\xe3i\xf1?\x84#/\xb24 \x02\x02\x9b%\xad\x1f =\xe6\xc7\xf3\xf1\x0e\xc5\x8e\xaa3XU\xb7\\\x1b\xc0\'\xea&"\\J\x88CLx\xe7A\xb6\x16\x9b\xe8\xa6a"\x8d\x06f\xc5\xc8\xfb\xc2q9Hl\xa2\xc9^s\xc0\xac\xa9\xab\xb4\xa4V\xd3\xeaqN\xa3.\'%\x1an\xbbl\xce\xf4j\n\x03\x9a\xc7\xef\xbe\xd3\xdc{M\x98\x01FXG\xbaV`\xc8\xe3\xd0\xb4\xa3\xf2\xe1&\tqj\x0b\x1d\x1d?\xe0k\xb7T](\xcb\x92\x83\x8bb\xef\xf1\xd0y\x91\xa2\xcb\xc33\xfbi\x84\xdb\xa4\xc527\x1c\x11-q\x06\x8c\xf3\xb0\xbd\xb2{\x8a\xeb=bEq\xf0\xe5P\xbe\']\x8bg\xc8q$\xc9\xc2k\x8d\xa1I\xa9&\xac\xb0\xb4k\x070\xb2\xbc\xfbs\x17\xac\xa3p\xa9\x0e6\x9dp\xf3/\x07%\x12\x9e\x1f\xd2\x85\xb1\xcc[\xe6\xf3R\xd0}\x81y\xf0\x04[r\x07\xdf\x83\xe8\x9c\xe2\xb1g\x18\xda\xa4\xafV`F[H\xd5\xf3\xed\xa9h\xaa\x84\xf8\x0bm\xc8\x1a\x85\x1b\xc7j\x1d[\xdbz\xb1\x07\xd0\x01\xbe\x87\xe8#\x05\x1f_\xb5,\xecJ\xd2\x9f\xcc^\xc8\x0f\x82M\x97\xaa[\xfc\x02\x01H\x0e\xb9\xc2\x8d\xb6\xc0HD\xe8;\x1cl\x83zn\xd4\x87\x8dhswD\xe8\xb9\xa1c\x95\x8c\xf9b\xd9\xb1\xce%\x99\x84tN*\x92,\xc4$\xfd\x83\xe3\xa0\xe7.u\xf3\x1d\xccI\x14\xa0y\x88N\xda\xca,_9^Z}\x11.\x0e\xdf\x9ces\xd4#\x90c"\xc7\x18\x9f\x9f\xdc%6o\xba\xde\xea\xd9\x88\x7f\xe3UM\xc4\x114.\x05\x8d1\xa5\xf8\x1cZ\\t\x1e2l\xeb\xa5:$\xber\xb6\x82s\x82\xea\x1d\xf8AJ0c\n\xdc\x9c\xa7T!*U\x14\\\xafc\xe0\xc7>2\xd6\xa0\xdd\'\xb6zv\x1f\xa8p\x14Q\xe6?\xd3`a\xec,~#\xe4\x1c\x1b7R\x7f\x87\xd9\xc1j\xb8\xa3np\xb6P)u\xba\\\x06\xd0\x8e\\\x1e\xdf\xef{N\xc8\xd1\x08\xa3\x80\xf0\x0e6\x8e\xf5\x88\r\xfa`0\x03\xe3:\xf5\xed\xc9c\xc0\xee\xdf\x87u,\n\xfd\x00\xecn\xe3,\xd4\xef\x18[|?\xbe\xc2 %<|\x817\x1b\xec\xaeo\xb4)\x0c\xdc\x08\xf8-\xfd5Z\xc5\xe29G\xa7\xe70\x05\xf7\xb6w\x02v\x0e2\x96\x1es\xcaWf\x9e\xdc\x1f6\x15\xda~\xd0\xdcS\xaa\x81\xa9h\xf4\xcf\x82j\x81}\xa93\x92|\xc3\xde:\xc7o47{&\x8e{\xe8\x17)Z|*4\xf8\xe1\xe7\x91\xa4un\x90\xb9\xac\x9a#\x10\xac\xc9\xd3\xedA\x9aFx\x81\xc0\x19c\x99m\x9a\xf9_\x8fMHA6\xadma\x0bh\x14%xI\xbf\x1b\xb1\x81\'8\xd6\x95\x7f}\xbbK\x05\xa3\xa6\xe0\x81`\xb4\x886(\xb8U^\xf0\xfb\xd9\xab u\r^\xa9\xebr\xf2\xf5\x10\xb6\xe1\xed`\xa0M\xafL\xa4\xc5n\x89\xb2\xa9e\xfc(\x7f\xfc\xa2\xce-\xba\xcb\xc0\x1d-\xd6\xb0\xdc\xcf!\x81\x18\xbd{\x92\xf4\x93\xadU\x98\xc1\xc8|g\x94E\xea)\x97\x83$\n~\xa9\xba@\x86\x15Eb\xea\x91X\xef\xcd"\xcf\xc5\xd1\x1f\xe02\x98\xd1\xdb\x14\xcf/F&\xdb\xbe\xb6\xee\xd2\xf0\x05\x93\xcfKG\x0c\xea]\xe2\x1bt\xaa\xec\xd7\x92\xb3\xc5(Z=\x96\xafR\xe3\xcf\xcfI\xe1\xd0\xacQ\x03m\x94\xcd\xbb&\x1c\x88J\xde2\xc7Ig\x9dn\xfdx\xbb3\xcf\xcc_\x133-\x17k\x018\x0e\xa2q>\xa7h\xa2j\xaf\xa0\xa9f;fp\xa5|\xfcnO\x14\xea\x17-\x89s\x9e\'\x8a\xe9h\xe4\xe2\xf0dBm\xb4O\xa2\xbf:\xd6\xb9\x8c\x88\xe6 \xd0\xe2CP\x12\x9fI\x8d?\xedF\xff\xe4\xc44\xf9\x9cB\xa1\x98/S\xc3\xe8O\x01/\xf74\xa4d\x84\x8a\x91X\xe7\x04\xd7\xf0\xe1\xa9\x0e\x8e\x10\x13}\xfb\xd0J\xb2S\x16\xb8\x93\x0fV\xf2\xd9P\xc2\xa7\x16\xfa\x95R0k-\xeb\xb9g7\xfft\xa1\xc9\xacRc\xdd\xdf\xbb\xcfL\xf3H\xe9^\x90\x8f\x1a\x92\x8f\xf1^\xfao-\xee\xf4c\x83\x92v|W\xb1\r\xdd\x06\x01\x10\x0f9Q\x8e G\xca\xf4\xb4[Zg%\xeb_\x87\xf0\xff\x0c\xc7Zt\t{\xe7!\x10L\xa5M\xa2\xea[\xa9\xd7\xe6c\xd0y\n1\xa4\x84\x14\xe0\xe8#\x8f\x91\xdb\x10\xb5\xd6\xe7\x92\xac\x04\x88\x06\xd1\xd8\x10~n\x93\xee+\xff\x02\xdc\xae \x12\x8f\x80\x025\x02dOX\x10I\x17\xfa\xac~\xf6\x90\x11t\xd02\x1a\x83\xb9\xd3\x8f\xf7#\x11\t\xec\x05\xb9\x90\xacv{\x10o\xf8\xa9\xef\xbe\x1f\xf8\xb1;\xab.VB\xdd(\x98\xca1\x12j\x02\xceF\t\x9ck\xc0]e\x80n\xbe\xe2\x95\xc1x\x85M#\xf6\xca\x93\xb9\t&\x02f2@\x13\x7f\xbbw\xee\xca\xaa\xf6Da\xb9\xe4\xf6\x08\x93\xaa\xa4X\xd3\xaa\x92\xe9`\x921\x9c\xb7\xab\x84\xed?D\xe4\x80\xb94\xd3\x83\x0bl<\xe6[\xd8(Z\x93\xf1\x10\x93^\xe4\xbb\xc4uR[\xdaj&\x9d\x82h\xbc:\x02=\xd4cy\xea*\xfe{/\xc3\xcb1\x95g\xb1\xd3\x88\x1e\x99o^\r\xd9+:\x8dnh\x85\x89\x83;\xf6\x9f\xa5\xfc\x92\xb5\x8c\x9fb^\xc6"P\xcf\xdb\xd4\xf5\xcc\xc4\x08n\xc1\xb7\xdb"\xfb\x07\xf6@\x1fR\xce,\xf1\xf4\x8cJ?wEJ\xd1\xd3{\n\x0cU \xb8kEP\x19\xa5\xa7v\xf8:\xbf=\x8aJ\xf8\xa1\x03Xh\xe0\xe1\xd2\xfd\x01\xc9\x08\xc0\xab>\xa1!\xfc\xcc\xdf\xbd>7\xb8\t?\x83\xf8b\x0e\xe01\x1d\xc0\x0f\xc9\xb7\xcbL0a"\xe7\x80\xe2Go\xe1YN\xce\xdc\x9ai\xe0\xce\xe4r\x91\x8f\x96(J\xcf\x97\t\x86\x89c\xe1+Y\x07\x9e\xf9\x81"\xba\x17a\x8bO\x8e>\xdf0\xf6>\x87\x0e\x98W\xcb&\xfe\xa5\xe6\x13\x97GP\xd6\xd3\'\xe1\xea\xf0\xf2\xa9s\x83\xf4_\xfb\x0c\x0e\xa6\x98i\x80o \x98\t\xb1\x14\xfdS\xeb8\x9cI\xc3\x0f\xb7\xd7\x12\x07p\x1d|\xa5\xb5\xf8\x84`\xaac\t\x13\x1d\x98\xbck\xfco\x80\xac\xf2\xb3\x08\xc7\x0c2\xce]\x92\xfa68;\xae\xde\x9c$\xf8\xb9\xbd|r\x04\x9c\\\xff\xf0\xde\xa8\xaa3\n]R\x93\xe6]u\xe4`s\x03\xfa\xdbe\xd9\x1a\x80N\xe4\xdd\xe3\xcc\xef-!`\xda\xd8b\xe3\x00\xccJ)e\xda>\xb2\xc2\xe2D\xed\x83{\xe0\xacZu\x88\xa5\xea^\x0c>L\x81H\x13-\xee^9%\xfeem\xa2\xcc\x15*\x19r\x90\x1aT\x1cC4H\x025\xe5S*\xea\xd5\xc5\xe97\xf4:Ri\xcd*^\x88\xa69\x8aO\xa1h\x86t\xd4\xa5\xa3v.\x85A\x99\x83E\x1e\xab\xab?@g\xed\x87J\x83f\x19\x11\xa1\xf5\xebeo(\xf3}Z|\x05\x16\xa2\x9a\xb6Rlf\t\xfd\xa1\xc7\x8as\rD\xda\xcaNgTu\xb7j\xb8T\xce\x12\xa9\xe8\x1b\xa6\xc1\xce\x1f\xb8\x04\x8el\xcc\x90\xfd\xe8\xf0\xbe#\xdf\xc0\xe1\xb8\xc1\x11}W$\x10}G\xe8\xc2\x07\xc0\x9e\xf3:\xbd\x1b\xb4\xb6E\xb6\xe6\x9d\\\'\xbfk\xd5\x9a7H\xd93\xa8\xec\x15\xc0\x88\x15\xb4\x1at0x\x13\xcc\xa1\x8d\xfdv;\x81\x16X,h\xcdX\x82\xc6\xfd\xf8.\x89\x9a\xe7S@\x0ex\x1e\xe7W"H\x80B\x19:X\x8a\x93\xc4=\xe4\xb6[\x8a;o\x1e\x97\x13\xd0\xb9\xed\x02L\xa7\xdd\xb9\x10Ip\xcc\xae\x0f|\xe6\xb8$3\x1cYZ\x9fVj\xf6 \xd5k.\xcf\xac\xce\x97\x04\xf6\x14V\xd8\xc8r\xd59\xd7^\x84\xc9kY\xbb\x1dvNu\x9eh9\xaf!\xff+\xf9Q\x8a\xfd?\x89\xd2"\xc3\xe3\x94A\xd8\x87\x03)g\xaa\xca&\x1e\x9a$VAd\xdej\xe3\xcc\xbb\xfaT\xf9\r!\x04+C\xeaT\xf1\x9b;O\xef\xbfN\xbfK\x0e\xb3\x02\xcds\x01\x1fiO\xba\rdv\x97e\x8a\xc0\xf1\xf8\n\xc0\x86y\xb2<\x98\xab\xe6\x02\xa4\xdb\xf2\x94\xd6s\xce\x10)"\xd2\xfc)\xeaK\x95G\x8e\xcd\xcf\x1d\xfe~?Y\xcf\x1cb}\xf7\x8e\x87Qz\xb4\x9d7\xab\x8f_zG_\t\xfd\xb4\xb9a\xaa\xa9\xb8\x91\xc8;\x84C.f\x8aD\'7OqG2|x\xe4\xd2\xf81\xb2\xe5Oj\xfcf\xde\xf4\xf3\x0e\xca_\xb1\x0eR\x88\xeb\xfc\x8e\t\xb7|\x083\xe6\xe1\xff\x16\x8a5\xaa\xcax&\x93\xabj\x8f\xc2\x94c\x81a}y\xbd:\xc9\x87\xad\xb2\xbdQ\xe1\x0e\x0c\xbe\xec\x0c`.GJ\x8d\xce\xffxR\xda\xde\x071\xb68,\x9en\x85\x85\x96\xcem\xef\n\xb2L\xb7\xa0\x06\xbc\xbbl\x19\xf5\xb1\x1d\xad:\x97qxR\x8d\xab\xdd\xf9\x88\xcf\x11\x96Z\xdd\xc7\xe1\xa6T\xec\x83W\xf7\xba\x97\xf3;\x85;\xf7\xb2[\x0b}\\9t\x9b\xcd\xcdh\xe6M\x119 \x052\x07#P,\xd8\x12JL\x8e%\xca\xabR;\xabVt\xa3\x93@-9\xe2<a\xfb\x90\x05w/\xadX\x01m\xea\x1f\xb8\xee\x02\xe0\x86\xb5\xe3\xd4\xe9_\xeeP\x049\x83\x0eq\xce\x86\xdf0\x91\x1f\x11g\'\x0cmag\xd0Y\xe2d\xc3\x17+\xcf\xa8\xbd\xa6\x9c\xf8\xf1\x1e7\x07^-5\x921\x99\xea\x1c#nVbu\x1bx\x12\xac\xd3\xe3SF\xc1\xa6\xb9\xf46\x87\xb6\xeb\xb6\x90iu\xe6\xacI\xd0\x85jX\x9e\xceR\xa7]\xbb\xe7\xe3\xe2\x0b\xf3\xd38\xf8\x90{[\xbfU\x19\xb2S(\xa6\xf0G\x8a\x10"\xa4w\xb0XK\x89\xbe`\x13\xf7{n\x17\xfa7\xbc^\xa80\xb7\xd1/\xb9\xae\xbc\x80]E\xc0[\xea~\xe4\xb2\xb0\x8c+\x8f\xdf&E\xcd\x85\xa3v\xd4\xec\xc3\xf5\xeaA\x91\xc3i\xaaR%!4\xba\xe0\xcbx\xc9\xb4\x7f\x14hM\xf9\xfc\xee\xa3\xeb7\x815\xfe\xe1\x91\xff\xd1\xce\xfbi\xc9\xa2{\x0e\x13\x0f\xe9\xeecL\x8f\xda"\x08\x0ea\x05\xca\xc4\xd5\xd1\xc8\x11\xe2\xc5\x19\xff\xca\x1fO\xbcL\xf1O\x89\xd1\x1c\xea\x84 [\xb3\x8d\xeb\xc1\xc5dt\x0e\x9c\x8a\xe3&&\xb2@{\x19\x04o6{QRd(\xf3\x15Lr7/H^t\xf3\xc0q\n\x8c|\xb5\x12V\x94\x16~K\xfap\xbb\xb1K?\x94T\x1bf\x88\x90\x08!\xa5/ez\x01\x06\xf2\xd8\x1a\x02\x99\x13$\x92=\x9d|\xbe\x00?b\x8d-`6J\xfe\xea\x93+\x0f\xc7>X\x9f\xeag\xb2U\x1b\x00\xa3s\xe08\xf2o;\xb8\xd5&\xe4\xa9\xedG\xed\xa5\x9f\xb8\xd4\xad\xd4\x0f\xd3\xca\xec\xb8\xd2\x88W5\xb2 \x9e\x13\x93\xbf+-\x99\x9a\xc6\xb8\xcb\x80\xe2\xec|u\x96\xcd\xcd\xbd\xf4\x10@\x85\xa6\x9a\xc7.(/\xe8\x05\xe4R\x14\xb3B\x12\xdb\xaf\x9d{a\xc1\xe2\xe5?=_\x9e\x8c\xfb\xeai\xa9u\xdbr\xba\xa5\x9dF{&pz\xa5W \xb2F\xb5\x7f\xa4\x93SB\x9c\x02\xdeRN/\xf9O\xa8\xd9\x85HKu\x12\xcf\xc7\xc7\xfd\x00\x8c\x11\\M\xb5\x7f\xa8%\xa3\xdeh\x90j\x0b\x1b\xe4\xcb\x9d1>\xa5\xa8\xabj\xa7b`\x83z\x80/\x9b\x90\xd7\xb4\xb4\x8b\xcf\xcf5\xf6o=\x94\x9d\xb1[|\x14\xb3xn*\xc3\xe5\x8a\x9aaIy\x8d\x86_\xb4\xf4\x92^!ZO\xa9\x9d\x0c\\&_\x00p{\xa7\xa7\xfb\x8b\xfc\x89"h\x8c\tj\x14\xef5\x90vf\x8eT\xf5\xc9B\n\xd1\xcds\x94kKmJ\xbd\x8b\xca\x8d\x1d\xe3\xf7\xb4\xadm$\xe9\xcft\xbfh\x92\xb5\xe8\xc8\xaa\xd1.ce\xf4T\x86\x03\x8b<\x8a\xf9\x961\xf3\xd3\x8esB\x0b\xeb\xb7\x00\xf48\x9a\x01s<XLV\x837\t\x1f\x01\x06\x9c\x8fo\xa8\xa2\x8c?\x9a\xc8\x8d\x9d\x8cC\x86!\x96\xd6Sw\xab\xcf\xb9i6H\x08\xc7\xf9cy\x10\x1bo\x82\xce\xa8^\xf2]\xb3\xdag\xcf\x91\xc1X\x99\xd8\xea\xe8_\x9e\xcd#n\xdc]\xce\xdb\xb5\xeb"\x1e,aD\xee\xb3Y\x14HtF\xe1\x17dD\xf6t%!:8\xc0\xc0\xe6\xd6\x8c\xe7&\xf1x\xe5\xb0\x07+\xea\xc7%Z\xf5\xf2c\xe19\x0fI\xc1\xfc\xd3\xb0\x7f\xa1\x8fE\xb6\xcbZ@I\xfc\xd9\x7fA\xd8\xa7\xc4\x0c\xa8\x8cy\x1a\xd8\xf9,w\xe3\xc4B5\xe0I]\x8a\xcbkU\x84\xd7\x1b\xdbR\t\xd1\x95aaW\xd2L\x18\xd5\xa6}\x87\xf3l>\x83\\\xb1ml\xbc\xc2\x8b\xa4\xb9\xb6\xf3\xbf\x8d\x06\xd15:^v\xe9\xb3\xca\x08\x90H\xb2\x84\xb0b~q\xfb\x93B\xa8\x01\x01\xd9\x17d\x93,tu\xdd_A\xcf\x91yy\xf8\xc3,e\xe0\x08\x88\x8aM\xf2\x0f\xac\x96\xca\x0bV\xc5\xc3\x95\xc2\xe93\xc5\xbe\xbf"\x14d{b(\x0b\x8e\x1a(\xd8\xe3\xebe\x8e\x0fAW\xbf\x94\x1bj\xeaA\xa1h\xeb\x0cS\x9c\x02\x95\xd0SR\xf6\xf7\xdc\xeb\xff\x8ep\x0fb9\x96\xf9\xf4\x99@<6\x13(\xd1\x00\xb9\rn`\x93m[\x97\x10\xbb\xdd:f\x8e\x99\xc6\x97\xd4,."\xcb\xf8\x04p\xfdg\x0cgt;\xca\xaf\r\xe1~\x9b\x81\x06v\xcf \x02\x98Jg\xc0!\xc1\xc94S\xd6\xf0\xcc\xa9j\xf1s8X\xde\xad\xd7\x12\x93\x05>\xa7\xd2\x10;q\x1e\xf0\xc7\xc5\xbfh\xdd\xcf\xf2f\x11\xe2*\x9f\x10U\xf9j\t\x9c\x0c\xf4c<\x94\xd5\x05\xa9C\xc1\x11\x9b\x9c\x8f\x05\np\xc7\xf9*+\xdfv6\xf4<\xb5\xa4j\x89\x8d>\xedK\x98\x8d\xfb\xe1b(\xaa\x93R\xd4OF5\xfaAF\x95\xd6G\x0f{d\x18^\x8a\xaa\x07\x07\xd8\xd3\xbc\xdcD_\xe8%t\xad&\xc9\xf5Y\x9a\xd5\xf8\x03\x1a\xffS\xa7_\xed.BX\x8f\x92\x8e\xe4{\xa06\x17\xb984g\xe0\t\xfb\xc1\xc5\xe4\xc7\x9f!y\xa2\xd5`\xf4\x1e\x07\x98\xb7\x7fWe\xf7\x9d\xcct\x87\x1c\xe7\x96.\xf8\xd1c\x86\xd4\xb6\x8f\xe2\xfdN"+\t\xc9\xa5\xad\x886%\x9f\xa9\xd3\x9aX\xb24\xbc\xb4\x10p\xc1\xa6zsLg\x9f ~\xfbB_\xbe\xd3\xe6*(\xbe\xa1\xfbJ\xef\x19A*8\x8aq\xb1\xc9\xbe\xd9\xb1\x93KO\x81W\x81\x97\xbfDm\xc9\xeb\xb6\x84\xe0\xd6\xf4\x9d!\xa0\xe0\xef\xce\x8e/\xef\x12\xe8\xd45\r.\xd3^*!Nm\x95\xe8\x18\xfc\xf3l\xc0X\xc2\xe2\x88]\x1f1>\x95\xc9\xfc7b\xdfR}\x8c\xc7f|\xc8\xdf+q^\x07N\xba<\x97\xf0\xe6\x0f\xb8\xda\xa0hp`\xb3\xc3#\xafl\xeb\xad\xca\x02\x90\x8e[<\xb6p\x99\xccS\xbf\xc7\x13\x1dzh\xf7\x0c9f\x08"?\xc2\xba\xd0\xa5\x9d\x96\xf4\x8dy\xf7\xe4\x8e\x19\x92C\xff\xfa+@\xda\x1ay \xd3\xe7\xe1p\x98\xb1\xbf6\xec\xd1av\x94\xa04\x8e\xbc\xc3G\xc0\xdb\x1eY4\x03Lz\xce(w\x16Z\x88r\xa6P{X\x843\x8b\x98B\x1d=\xb5\xbe\x07\x1c!4IU\xb4|Z\xb0\x1d:\x90\xad\xb0M\x11{-\xed\xa5\xe9\x0cPj\xe2Y\xbe\x14\xa2\n\xf9G\xdd\xcff\xb3\xa0\x8dr\x1f\x9b\xf1d\xb2\x04\xefwc\x1c\xceHe\xc8A\xf5\x1b\xf3K\r\xaf!\'Bg\x83\x01\x84\xd9u\xce\xb4<\xcd\xde\xdd\'\xbb\x05\xe6u_-\x05\x7f\xd9YC\x99\xca\xbd\xbf\xf1\x87\x8dt\x86@\xd1\x9b\xae\xb4\x88\x16\xe6\xc7\x0cXqpq\xf2\x913F\xb1w\xa8\xb0TK\xf2\xed\x12\xe6\xd3\xda\xc7\x96ve\xd8\xd9\xca\xf5[\xbc\xe1\xef}\xb2\xbb\xceT\x18=\x1b%\xe1$c\xe2\x14\xe3\xb0\xb0\xb1\xddv\xd9k3F\x7fV\x8b4\x97Xe\xb1\xba\x8f\xac\x1c\'.\xbd\x03\xb9a\x85\xaf\xc3\x16\xd6L\x95\xee\xfd\x0c\xae\n\x85a\xec\xc2N\xdd\x02\xa5b>=\xe2<K\xc1M\xc6 \x0f\x8bM\x1a8\xb2rB\x10\x8ci\xa6S+\x1f\x00\x0e\xcf\xc4\n\x1d\xcef]mT!c\xd6\x0cj\x11nZ\x80\xbfq\x8f j&%\xa8\x86\x92y/PJ\xb8\x02\x08>\x88\xfe\xba\xea\x15\xd1\x89~\\qL\x8cp\x99\xfb|D\xa4\xc8&\xae\x7f\x983\xd6Q\xfaCV.\x17\xa1\xb6<\x1cT\x9d\xf8GG\xf4M\x9a\x94,\xbf0\xf4Y\xb4\xaebL\x06#&\xd0\xbc2\xba\x87Q\x08w1\n\xdba\xdb\x17\x90\x1b\x92]\xfa\x99\xb2X\xfdp\xe0\xf3l\xac\x1e\xfc\x08\xac\x7f5\x878\xc6z\x94\xb2\xdcFo\xbf\x0c\xf2\xb3v?\xfc\xff\xb2\xd0\xe7\xc8\xdd\xd5W\'V\x89e\xea\x9c\x159~.Ez\n\xa1<\xf4\xc0}\xd3A+\xa1\xa1\x97\xd2\t\xef\x83\xd0\x81\xf1o\x80\xda\x07\xaaa\xe3\x80\x1b\xe0`\xdbe\xa0\xf0\xd2|"\xc7\xf7\xaa\xbe\x15\r\x13\x97qeB\x85{\xc2K\xcf\xdc\x95\xdb\xc0\xab\x19\xcd\xea\x8f\x92(\x1b~\xcf\xec\xbc.\x83<m\xcd\x02M\x90h\x10\x84\x83\xdbW\xbd\x96\xcb\xb7\x93\x89\'\x80\xe4\xbc\xdeox"\t\xea\xa3J\xe5\x0c\xbf\x85\x00\'\x11\xc8\r\x88\xf7P\x1f\xee\xeb\x7f\xca\x18\x14\xe6\x05\xd5\xf7\'\x98\xf9!T\t\xa8\x870"\xad\xdb\x18{\x06\xe5\xec\xcb\xd8\xfd\xc2\x86\xc7\xf8!\xf5\xe5\xc4|Z\xf2`M\xb9g6\xc1o\x14\xe2\x0e\xc7u\xf9s\xd4\n\xa3\x87\xe3\xa4i\xd6\xc9\xf3\xfe\x94bg\x0fr\\\xba\xfd\xaf\xc6\xe6@"\xc4\x88\xf1@\xc2\x10\xc3E\xd25Dk3g\xa76\x01\x93a\xd1\xd5g_\xf7\xb5\xbd\xdf\t\x81\r`\xa0\xb1\xed\x8c\'\xa7q\x8c\xb8v\x83\xb9\x87\x1dk\x81r\x85)\x04\xa2\x82\x82h\xd3n\xdcf\x06\xe4\x06\xf8\x88\x14e\x9cx\xc0\x91\xa1_\xa5\xf3XF<U\x92t\xcc\x8f\x18\xf5\xdcHWl\xf7B\xee\xee\xb0e\xd8\x1dfZ\x8c_\xb4\xcdT>yO\xe8\xde\t\xc4\xefT\xcaI!\x1ay\x83\xb6b\xd2\xd2\x1fe\xba\xd6\xabm\x01-\xa4\xc0q\x96v\xb9\xc9\x17J\xe8\xbe_XD\xe1\t\xab\xe06\x00l\xd4B\xa5\xa4\x0f\x1b\x84\xfcN\xaa\x7f\xfcyH,\xf7\xe9\x1d/6[A\x8e\x97\xc7\xfe\x08UE\x11\xb7;\x9fq\x91V\x84\x8aWS\xfd\xb0\x14\xa7\xb8\xa4\xe9*:\x9ad)\x99\xc2J\xb5\xf1\xbex\xa7\x9d:\x12\xde\x14]\x8a\xcb3\xf3t\x83\'\xd5i}\x9b\xcf\x9aB\xdb+\xf92\x102N\x84\x08.a\xe6/\xeef\xb1\xca9\x1cQ4t\x1f\n\xfd\x0c5\xaa\xe3\x8e\xb3\x92\xfcl\xbe\xf4\xcd\x9e\xbf8{~\xf0\xb4?8\xf1P\x84\xbf\x84\xf8\x1b\x04\xa8\x8dr\xe6/OE\x8e\xf0?\x01p\x08\x1e6\x8c\xebF>\xd7]OzD},r\xf4\xa5\xa9\x98\xe2\xd6\xcai\x93:\xbcD\xa2\x16c\x8a\xa4m\x81)\xe9\xdb\x12\x7fF)\xc3;\x12o\xbe\xb2\x9a\x1c\x02\xf2hJ\xdf\x97\n\x07\x95pgj#\x83z7\x88\x8aB\'\x9b&\xa2\x1d\xe3\xdb\xe6\xd1l\xfb\x9f\xa6\xf0\x1b#a\x96N\x8e7\xbd\t\x18c\xc9\xb8\x14f\x01V\xef\xb5\xe7\x84\x1c\x1d\xf7\xf9\xcc`5\xa2\xe9\x17\xaeH\xa4\xda]\xf6\xa7\xf4\xdfF\xd2\xae\x14\x1b\x86\x14F\xfe=\x9a\x85w\xbe\xf8\xb2>\x86\x07h\xdb\x13\x94\x0bee-\xb2\x08\xd4\x81\xaaT\xf9\x8f\x14%r\x8d0`\x0b"G\x1ei\x8c\x0e\x89$\x00zT\xb1}{\xefF\xa7|\x1c\xcc\xcd\xa2\xdf&\xdf\xd8\x8aRZ\xe5\xdc\xcc2\xb4\x1c\xd0\xf5z\xef\x08\xca!\x02\xa2\xd5\xcaX\xaca\xd8\xe0D=\xe4\xaa\xec\x99\x9b\xcb\xd5\xd4(q\x8f\xc3v\x8b\xac\xbe\xbb@_Q\x88\xf4\x11\xe7\xf6BGDW\xe7\xe9|\xc4#MW\x12\xec[\xc3\x0b\x87\xe2F7\x88\x1f\x8a\xe4&p&Z\xaaD\xe7\xde*4\xe5\x86\x99\x9d\xa00\x94\xb1\x01\xecq\x9cX\t\x13\x98\xc0\x8bk\xab\x99o\x9eu\xfa\xe5\x97\x8d\x97w\xb6\xbf\xa5Y9M\\?d\xb4\xef\x97\xaa\xf5}\x18\xbf\xff\xcb\x9a\xa5\x909\x1dgC\x17i\n\x0e\xf9\xbf\xca\xd8\xee\x1c\x11\x1e#2\xaa\xc3qTK\xc9\xdc\xd9j\xe2\xd5M\xfcNdTx\xa3U\xa1\x1d\xb1\x0e&\xfc4\x01\x94\x82\x8f\xa5\x90\x1d\x9f\xd0\xc83Q\xdc\nj\xd3{\xbc\xc5\xb9:\x8a\x9b\x1f\x92O\x97\x8f\x01\xcc\n~\xa1\xa5-\x15\x08f\xc4\x18\x11\xb4=\x90\xbd\xa8\x1e\xae\xdd;(w&\xb07\x80]\xb3H\x82\xc5T\x07\xec\xfc\xf0\xcfN7_c\xd0(\xc3\xac\xb0\x8fFR6vl\xc1\x91\xb7\xc9"[\xcdqA\xfd\x0c*\xde\xeb\x8d\xa7\xb5\xfa\x00\xaa\x88o\xe9\xd4o\x94\xce\xe6\xf2\xc8\x1f\x86\x83h\x90+O-\xd5x\xd3p\x1e\xa7\xa2\x1d\xe1\xbc\xc4\xdeH}\xa3{\xb5\xdc8J\xb4\xc7c\xc2\xb7\x9bh\xff\x9f\x89\xfd,j\xbd\xe7\xd5\x03;\xd5Qa+5C\x12P\xd4\x02\xf3\x0b\x8b;\xc0\x84]\x07=\xab@O3\xd4H\xe9\xc8\x1c\x0e\xcb\x1a\x16\'\xfb}\xb0\x93\xde\xc5\xe9\xdb\xe0\x81\x15\xf2\x08\xde\x91NPh\x17`n\x81\xc4t\xbf\x0b\xaa\x02\xf9G\x83\xbb\xablrlv\xe1\x0c\x83\xe2\xbf\x88F\xd9\xe6\x08\x05\x93x\x16\x9f;T\xce\x9f>\xc5\x00)\xae,\x86\xf2e\xd8s\xf4\x82\x9c\x8a\xc7\xf7}\x93JA\x16\xa0\x9e\x95\x16\xfa\xbb\x10\x08b\xb4\xb2\xc2\xca\xbb\xb7u\xf7\xd7\xf0\x03\x9e\xfc\x80\xed\xa9\x81MeA\x9a\x1dL\x86\x80\xdb\xb1\xb5\xec\x94C\x92\x0bn\xa4\n\xd9\xe0\xc1\xbf\xf7\x18\x94\xef\xc6\x98\x05\n\x86\x11\xf3\xab7.E\xcf\xc2\xbaVZ\xe2\x05\x1f$\x9f\xb4\xa8\x9c\x9f\x17\xde\xcd\xce\xb7\xca\x91\x93 I~\xe3\x15\xd0\xfbGI\xa48P\xbbp,\x84{\x02\xe2s\xf2\\X\\\xc2\xc8bW\xc7_X\x1f\xaf\xb0\x91\x1f{\x1d\x82\x8c\xd8\x80a{\xf7\xc6\xa4\xe8\xda\xeda\x0cK\xd6\xae\x1a\x8f<\xdc\x9b@\xef*\xfb9\xe5\x95)\xdbF\x8e\xcfu\x1cQ\xe9\xf7\x92\xf4g\xf8\xb3\x0c9\x19\xce\xef\xef\r\xd4w\x05;\xf5,\x86&x\x1ad\x88\n\xec\xd2F\xfc\x83\r\xbavD\xcaR\xce\xa1\xdf!\xdd\xd4\x7f\xd4S\x19\xf3\xd5\x92F\xf9\xba\x1d+\xd9\x87+)\x9d\xc4\x88#\\g\x0f\rFy\x1f\x06|a_\xb8>\xc5\xb0\xaa\xae;]W\x88\xfe8\x8a\x89\xf5\x81y\xbeV\xbb\x83m\x1fHh\x1e\xaa\xa5\xfd}?u\x01\xd4\xa4\x1b\xc9\xe2U(\xc4TT\rV\xb9!\x9c\x9b\xce\x968\x97;\xbe\xad\tLY6m_H\xf4\xad\xd2H\xa6\xd3\xeb\x92u\xcf\xc2\x1b\xcdQ\xfeL\xe8\x93J\xb5\xe9\x0f\xedF\xa54\xa6v\xb6\xf6fK!\x80\xbd\x97\x94\xae\xce\x92\xec\xd6yb\xaf\xc0:-n\x003\xdc\xd1\xac\xb6@\xdbPxg]\x1cy\xac\xbf\xfd\xc5\xfeg\xd5\xdaF\x88KlAcK\x01\xd6{\xbe\x8a\xd7\xdb\xa4\x14\xe5\x96\x9c\x94\x90*\x19X\xcf\xd4\xc0\x12M\x7f\xb9\x0c\xb5\n\x05\xa7a3-\xf1\xa8\x82>\x1djxq\x1f\x0c6\x8f^\x80\x84x)\x94\x9a\x0f\x95\xb1vH\xf9\x1a\x12$\xc6\x98\xfc\xf4\xe7\x87\x8d\xe5\xb4\xda\'\xde\xd24\xbe\xce\x93\x9f\xf4W3\x13\xed\xea\xa7\x0f\x8c\xd4\xe1\xde\xe0\xec[\xef\t\xb2,\xda\xbf\x1f\xb5b\x00\xf541\xa8{\r<o\x08\xcc\x0e\xca\xcc8=\xce5d:\xc6\xaa5G\xcd\x01\x01U\x96(6\xe3P\xf2\xfa\x1f\x15L\xf7zE\x1c\xe5\xf5\x02R\xe2\xc3\xed\x0eC\xccP\x97\xfdho\xed\x89\xf2\xc1\xc4.\xbd\xbbT\xb5\xcbb\x86\x9aj\x1f(\x11\x87md\xc0\xa4\x03\xf6(g9\xd2~\x15\x0f\xa7\xb8\xf2\x1f\xb5\xa4\xb0\xddk\x03x\\<,X\x16\x04\xccT\x8f\xfd(\xa0\x9d\xc1\xb0\xe03\xc2\xf49jY\xec\x9a\xa1\xe8\xed\xff\xf6\xc7-(~\t-2\x94\xb1\xd3}r\x96q6\xc4\xfbo?uO\x95\x0c\x00R\xa2#\x99I\xff\xcd\xa5\xb5\xb9\x84<\'\x1ci\xd3\x08\'i\xa0\xb7+D\xabl1\x80R&\x83F\x8c\x98\x8d\xbc;\xc2|\xca\xb4Al7\xd7\xa1\xa8ehn\xa3\xe9?\x05\xe2t\xb2@\x06*\x9a\x9c\xefs \x13\xdfH2\x92\xae\x08\xbaq\x9f\xf4kI\xf64\xc0|\xd1\x84`@\xb4O}-\xcf]\x99\x9c\x82\xdcWn_\x0b\xbeB\xdd\xcf\xbfw4\xd2Q\x92A\xd97\xcc\xf2@\xc1JP\x8eT<\xb2\xd4\x8cW\x88r6\x99\x7f\x9e+!C\x03s\x92o\xad\xdb\xbb4H\x92jF\xf1k0\xbf0\x8f1\x88\xc8g\x94\xcb\xa3\xfe\xcexW\xfd\xf9\x04\xfb\xf9D`\x06\n\xef\x04\x94^\x81+s\xe7\xc0\\\xcc\x14\x91\xdb\xd7\xd36P|\xa3\x9f\xa9\xb1\xf3\xe4+\xa7T\xe1mG$\x84\x1b\x1a\xd9\xf8\xe2\xa7\xc7\x0b\xd6A\xa7\x82U\xcbo^\xcf~W\x97Z5\xfc\x87+\xc8\x81\xbf\x99\xc9$\x15M\xb0$f\x8c$\xe7\xc6j\xbdc\x14\xd4\xc9E\xbb\xd3\xe8ZkU\xab\xabkl\x1f\x05\xe6\x1a+\x85\xda\x83m\xec\xb4\x00\xb3ewp\xe3:\x94\xb6"N\x82\x1f\x9c\xe8C|laK\x191E(\x11\xb29\xf62>Y\x9a)\xba\x01|\x08\xcf\x94]C\xc9\x1f\xdej\xb9!\xc1H\t\x86E\xa0K\xba\xed\r\xff\xa9\x93\xfd`~\x9bxg\xd0\x96\xca]\xc8\xfd\x8f\x87@ \x8b\xd5\x85\xd7\x16W\xdf\x17\x8b\x19G\t\xb7\xde\x14\x12\x08\xca+\xac\xf0\xb5B=Y\x16O\xa6\x04\x18\xde&\xf2\xbf\x98\x8f25^\xa6\xa69\xaf[\xa9`+>Q\xeah\xd5\x0b\x13\xaf\xc1\xb0\x0e\xf5\xa7_G"\x8cv\xae\'>\x03X\x87\xff\x10\xd7\xa6\n\xcba\x9b\x92"\x15l\xe4\xd3\xa4@\x8ah\x1b\x1f2A\xce%\x8d\x14\xbb}Q\x81\x8e\xe8?H=\x1a\x1b5\xe0v;\x05\xe5K\x12\xfd\x13k\xbc\xbb2\xd5\xcf\xc2\xa3\xe65>6\x98\x10@\xacs\x0c\xa3\xbc\xe7\xdc\x8a~\x10/,#%\x8f\xb7\x03\xea\x8ej\xf0\xca$\xb0\x8dD<\xd1\x86\xbf\x01\xc1&\xf8b\xd5]ua\x0b\x07\x9577\xa5\xcf\x1d\x92ff\xa2\x9a\n\xcb\x15\xae\xa8`I,]\xb7\xc0Z\x8d\xb5(\xf6:S\xbbX\xe6\x07u\xe4\xeb\xf7\xd9\xb2\xc3z"\x0fu\xf1/\xe3\xb9g\xa0w\x17I\x1aG\xbb\x860\xf5r\xb4A3?\xcc\xf7e\\\x17\x97c\xedp^\x06\xa1o\x98\xef\xa4qXk_\x84|7Fk\x1ak\xa9J\xcb4\xd3\x0f\xbfO\x1b\x1ap;\xbf\x92g\x95\xfd\x12\x96\xf6%u\x91\r\xf6o"\xa4p\xfa\xe4\x81\xb2\x08\xa8!\xc3ai\x87-\xcd\x96\xbfx\n\xf2_x\x15\x1e\xa8\xaf\x9aT5\xa71\xcb\xaf\xea\\\xe9\x81 %\\\xff\xb1\xf3\x04\xbf\xdd\xc2\xb7\x8bAXbC\x1eIz\xb9~\xfa8\'\xf7\xc1\xaf?\xca\x0f/@6\xcd@\xe7\x87~9\x1c-\xdf^\x12\x88\x87F\x98\xa1%r\x9d\x15+\xf7\xdc}\x87\x8cO\x9dceV\x04\xd5 \x12"\xee\xd2\xd0\xf7\x1c\xefA\x02\xd0%\xcb\x9b\xff\x91\xa3^n\xd4\xa0\x9c\xb30\xef0\x90\x7f\xb3y\xe7\xe3|%\xd3\xdfb%\xa0\xdd\xa1\xd8t\xf3wn\x057\t\xee#*\xbf\x98\xbdic\xcc\xbe\xbfl\x19>\x17\xb3\xb9\xe8\x00\xcb\x88\xbdr\xe1\xb7I=\xfd\xf0b\x94y%2L\x1c\xf91\x14\x97\xdc?{iB\xee\xa3\xe1\x1a\xf1\xef\x13\xdd\xdc\x11\xb2\xf03\xc0\xb8I\x1ei\xdcT\x83OU\x06\xa0;\xa2R9\xdb$hq8\xed\x82\x19\x9a\x99\xbd\xdd\x954p5\\h-\xab\x05|@\xc4\xbd\x1c\xfa\xe4\x1c\x90\xb4\x8c\xfc\xa3b\xbe\xed\xdd\x8a\xb76\xe6P_\xf8\xff\xadv8\xb6\xb0\xc8[qV\xf2_d\x92\xbc\xd4\xb3\xa2\xcd$\xf8w\x9f@\n\xd1\xe0\xb9\x92\xf8\xc5\x82\xb6\xbd\xe4\x7f\xe9Uo\x1a\x85#^\x8d(\xea\xdc\xfa\x1a^B\xaaj\xe3t\r\x11\x1e\xf8\xd8\xa3\x80\x81+\xf1/r{P\x01\xde\xfc/\x140\xdd\xef\xdfn\xc7I\xf8\xf0\x16\xcbP\xd70\x8c\x846iY\xdfE6\x93q\xe4T\x10Y\x05j\xce8\xbcg\xa4\x1e1\x01s\x01\xc5\x1c\nMm\x00\xa4:\x93\xacv\xc9\xa9vO\x1d*\x8cU\x14R8\xf0\x88\x9dO?\x8c\xdb\x07\xf1r\xa7\xaf\x0f\x1f\xc79\xd3"\x06f?\xc6\x9c\\\xcf\xff\xb0\x9a\x8e\x8ca\x8dO<\xba\x88,3\xbb\x87\xcb\xfc\x00GD\x12\x07\xa8\xa5\xb5`\xaf\xed.\xd4\xb8\xde\xf7\x13\x1de\xd38\xe1\x0b\x92vn\x85Sl\xe0\x1a\xce\xb2\xd2Z\x94\xf6(\t\xd6\xf5\x1e\xc4O\xef\xb3t\t\xfd\xc9jF\xa3\xf2\xfcS\xa63F\x9d\xe1;u,\xc8\x00\xc7\xe2\xe5\xd6\xabm\xbb\x11-\xddR\x88Vb:\xb4s\xc7\'drur\xd8\xe0\xb7\xec\xe8\x81\x11a\xe7Q\x84\xd6\xe9*\xd9\xe4\xe3\x0cx\x04Zt\x97\xee\xad\x91\xc4\xb63\xed\x86\xfc\x1b\xa0p\xf6I0a\x81\xe4mM+\x14\xdc\xe8\xbbm\xa2\xb0`\x15\xb1 \x9c\xfa\n\xd5\xcde;\x9f\xb1\x85\xc2\xda\x18seL\xc9', b'H\x05\x88\xac').strip()
_O1I0Oll10I = _1OO01O10II0O(b'\xf1\x9bC\x02\x15\x11\xcf\x03\\\xd3\x16W\xc8\xa8\xe3\x9d\xa0\xa6\x1c,\xd3\x8e@e\x89<\xd3\x91[\xdd\xea\xfd\xa8\xec\xb1C\xf4\xcc2!\xcb1,)\xd7\x0f\x9aM\xb7Ch\xd5\x153Dj]\xc46\x16?\xeej\xff\xa3\x03\x18R\x1cy\x1b\xf8\xab\xef\xfbq\x85\xf0\x1b\xe8NI8\x92\x07\xd9\xbc:\x1da\x96\x82\xe9\x08A\x9cZE\x14\x99H\xe7\x83\x0f\xe2\x14\xe2\xb8t\xd3\x92\xa4\xc8\x95\xa6\xd5Q\xf9\xd8y\x0e\xd9\xc0\xb3\xceE\xf6/\x8b\\\xe9\xa7\x0cP`\xd9\xb0\xf4\xb9\xe0\xd9\xff.\xd2\xa0l\xd4t\xf5\xdbIZ\xa4\xc7\x87\x02\x0f\x8fX\x14J<\xdb\xee\xfe\xbeZ\xcaz\xe94\x08\xd1\xdc\xc2j3X.\xae\x85\xd0ve\xf7-\xf2\xe1\x8b\x9b\x1f6\xe5m\xe1i]\x97\xfe9\x8d\xc4\x0bu\x1d(\x04\xf18?\xbe\xffo\xc6\xdb\xdb}\xc4\x1b}4*\xba\x1f0\xa3\x99\xad\xc4\x1a\x10\x9bh\xf0\xd4\xd7s\xe6\xe7=\x97L(+\x7f\x89\xfa\x9f\xb4\xa9IiyE;hf\x0b\xf3\xffo\xa3\xb2\xb9=\xf2W\xcd\x94L\xc9\xaa`\xad\xf0\xf4\xc0"%\xfbIu\x08N\xb2j\xf6\x00\x14\xc4\xe9\xa6\xaa9\xb1\x86\x9e\xc2\xfa\x81\x90\x81\xc7+\x1e\xd1\x82\xaf\x9b5\x84*\xf0\xae\x98\xae\xa7*\\\x84\xaa\xcc\xb7+,\xac\x04:$\xffd~\xd6\xf71XG,\x9d1_\xfe\x87\xee\x88\x95\x1b\x8a\xe57&J\x18\x17q\x8f\xae\xb5\xdcju\xdf\xda\x8c\xa8(\xe2\x8b\x07\x89\xae\x94\xde\xc4\xe0\xa1Ym\xf5\xec)#(\x97\xd5\xd6:n\x05\xed\x0b\xe7p\xe7\xa92\xef\xdf\x17\r\xbcQ\xc6o&\x85\x95B\x86\xd8\x87\x84\x0c\xb7l/%\xefA\x19\xad\x96\xc5e\x7f\xae\x8b\xe7\'\x1e\xac\'\x96\xae!!R0\xfbR\xc1\xd7\xcdE\x91\x9b\xb7\xd4\x0e\xac\x957\x16\xdc\x9a\x89\xf5\xe0\xe2\'mlP\xfa\xa7@\x90\xcfZ!\xe7\x80\rR\xd6\xc0\x91qr\xb6\xa8\xfd\x9e\xb3\x86\x8d\x1f\x9ct$3\xfb\xcb*\xf0`\x80\xc3\xc5>\xf8\xfd\xdd!\'\x89\xc9z\\\x87f\xb2F/"\xc1\xd2%eBTLm3\x033\xcc\x9e\xc1\x12\x15C&\x82Q\xb6\x058\x17\xc0\x9b\xb3\xd5\x8ebZ\x8b\xf9\xc2\x04/\xfa\xdd\x7f\xe6\xad\xe3\x95\xcd\'\x9e\x90\xac\xee\x01vh\x92\x95\xef\xad \x03GJ\\x;\xfc\x1cJ\xe4\xf7pc\x98Z\x14\'y^\x96\x16k\x8b\xc6\xc1\x89\x18\x04\x0f\t\xa5\x17\x8a\x8e,\x85\xf5\xdbM\xae\xad\x99\xe0JV\xaf\x02\x87e\xd4\x86A=\xad>\xd0/\xcd\xca\x18*\xcf\xa4\xca\xf44\xb4\xf9\xd004\x8e\xf8\x8d\xacK\xee\x02\xce0\xf9\xedL.\xe1\xbc\x89\x8aDQ\xb5A\x15\xc0B>\xae\x88\x01:\x87\xd7&\xc1\xbd\x87T\x9e\x10"\xd1\x8a\x90wm\x99g\x01\n&\xba\xa0\x8a\xd6\xa7\xb7\xcb\xd2\x84v5\x01\x1a\xcb\xf2\xf0\xe4\x08\x92<\xaaW\x84\xbb\x08\xfa\x82L\xf2\xb7\xcc\x18\r\xd3\x80Wo\xeb\xfa\xd4\xbf\x1au\xee\xf7\xec\x1f\xdb\x10\x19a\x89XY\xaa[\xa8\xc9z|\x90B\x08\xb6\x8f\xaa\xb1\xd3\x97\xef\xe8\x81\rfcP\xfe\xc71\xc1\x88@j\x91$\xb9\xc8\x80\x0b\xdaa\xc9\x1e\xb8\xafu3\x18\xe1%\x9c/\xd6{BotT\xeb\x97R\xe6\'\xd7\x15t\xcb\x1b\x8f\xfb\xe7aBlo|[w\x9a\x1f\x8b5E\xd2\n\xdb&\xf3\xb1\x03\xf4\n\x9a\xc8\x80\x83\x14\xa6\xbcE\x90\xf3\x0c\xb9\xf3\xba\x82@"\x04\xbc,`\x803\xc6\xbd\xb5TC\x01\xffTH\xf7\xadusYd\xbd\xcfC\xb1P!\x92\xbd\xd8\n@7\xddF(\xdc_0\xc5y0\xac\xc9\xe0`N\xabql+\x91IgG\n\x805\xab\xb1\xce`j\x83\xfe\xc5\x18}u9\x0e\x1f\x1f\xbe\xc3:\x9a\xb5\x0c\xaf\xd1b\xa0I&\xd9\x9b#^#K\x835Qp6Y\x16\xbdp\xbeZ\x06\xe4"\xddg\xd8\x15\x1c\x82B\xeb\x81\xf9\xa4[\xca\xd3"\n\xfe\xd9\x81\xee\xca\xc5V\x9e\'\x1b2\x0f\x0f\xf2\x1f\xfa\xa7K\x9c\xac\xa2z\xc7\x04\xd6\xda\xab\xcb2\xbbK\xeb\xb0Bi\xec\x8a\x8eN\x0e~OpN~d\xc7K)\x1b\xd9al\xf2\xa8\x02Sx\x0e\x0e\xe5w\xc7\x919\x80\x0c\xf2\x0b?\xcd\x87\xf8\xa1m\xf1\x08J\xa3A$\xc9\xf2\x19\xd0Y\xbf\xf8~\xc62.\xe0a\x0b\xba\xb88\x04\x16\x9c\xa0\x92\xce\xf5r\x11\xbf\x9f\xbb\xfeI\x96?\x81\x96\x9bp0\n\x1fD>H`6\xd9\xde_\xb9\xf6n\xb3\x92\x13\xab\x06\xc9\xffP\xabKJ\x9e\xbc\x1cs\xa6\xa0\x96\xca\xaa\x0c\xb9\xcfxd\xecb\xfaV#D\x10\x7f\xa5V\xe2\xbf\xad?Z\x81N\x02\x1d\x94\x9b\x05\xb9\x80\xc1\xdd\x8f\x84\x96\xed\x12^\x0f\xd6\xcf\x99)\x11\x185=\xe2\xe9\xc0$W\x1f\xbc7\x00\xd2\xeb\xeb\xa0A\x9cf\xd2\x7f\t\x16\xc2L\x8b\xafN\xb6\x1c\xb1\x01%\xc3\xb1\xa0\x8d)\xbc\xb5\x89}\xe6Z\xba\xe4\xeb\xa5GI\x92\xc7.8\xe8+\xb8s\xfd\x83\xf7\xf0\xf3mb\xd3\x08\xca\x95\xbe\xc2\xc9H\xc2\xe3\x92', b'\xf6\x0e\xda^').strip()
_l1I0llO000IIll0Il1 = _Oll0Ill0Il(b'5\x00\xb9\x19\xddj\'\xeeT\xff\xc3\xe5)\xa0"\x97\x19\xf6M[\x02\x8ep\xd2\xbd9\xb0\xb5\xdd\x9e\x00\x93r|\xe9D\xc8\'\x80\x92\x1a\xd34\xa9\xd7\x82\x84pz\xa2\t\\\xd6\x1f2l\xc1\xc7\x8e\xbdI\xbc\x1a&\xfa\xf6d\x02\x14t>H\xee\xad.~\x10[\xc6\xcf\xee~\x9f\'\\I\xe2\x842~\x86_\xb3\xaa\xd1\x9e%\xca\x80\xbc6\xa2\xec\xc5\x0b\xc8\xa8\x8e}\x86{Q\xfe\x84\xd2S\xc4\x9f\xd5N\xdca\xa9\xb4}\x87\xdab\x0f\xf5\xb4;\x1e\xcaWD\xc9\x1c*!\x1f\xda\xbb\x9a\x0c\xb2\xf9\x88\x15\xacvO\x1c\xdc\xddz]\x92\x08=F)\xd3\x0f\tm&\x86\xfd\xfcwA\xeb\xe8\xcerFhw\xa0\xe2\x11P\x86\xf3g#F\xbd\xec\xa6; \x96\x01.\xe4E\x03^\x7f\xfa8xk\xa7\xf9{4\x8d\x10`\x89\xae\xf5\x91C\x88\xf3\xa2\xea\'\xfb\xa8\x19\x03\xd4C\xeb\xed$Sr\xc1\xe9>\xa0^\xa7k\xb2S\xca\x99\xed\x048\xfb+\x934\x05\xd7\x88\x91\xcak\x80@E\x18\x9d\x1b\xeb\xe5\xd5 \xecT\x03\xc3\xce\x9b\xf7\xb4\x95\x04E\xd7\x07\x9d\xe86\x9ew\x89L\xf4\xb4\xd8\xc6A\x1e\xcas\x19\xb9\x984{\x01\xc3\x19L\x0b\xc8}\xb8\xbd\xac\xe1\xf8\x85\x92;\xd4\x04\x87\xdc\x83\xa0\xff\xefjK\x909\x84\xe4\x0e\xd58\xaaA\xb4\xc0\xc2\xc2\xc9\x08\xf0\x93=G\x16#R\x15z:\xb4\xf9\xce18\xd7\xb30]\xa4]\xd8{\xf5\x7f\x04"\xffB\x0b\xb9\xc3r\xefk\xa1\x8d8TZ\x03\x03\x05K\x96\xbc\x95\xd2rRw`\xa3\x8f\xa7\xd4l\xff\xafXQP\x19\xe5&\x97cX\x16x\xf2\xa2\x03G\xac\xcc\xd9w\xf8\xd5\xfe[j]aKs\xc3G\x80^`r\x9a\xb0\xd3\xd3\xf5~\xf9v-k\x02\x981W\xf6\x87\xb6B;\x17\x8d\xe3(s\x91\xa6RP\x05\x94=\t\xcdM\xd8>\xff\xd2,\xcd\x88\x1e\xe23\x885_\xf1\xe4\xcd\x86\x86\xd27\x85\x9c\x99\xdf\n\x89\xbfC;\xa5VG\x0cx\xb8\xc6\xd5\xc7\x07\'t!\xc2\xcf\xbe\xcc>\xd1\xc2j}\xcc\xd8\x95\xfe\xe4\x83\xd0\xbay>G\x9d', b'\xc7\x92Q\xf5').strip()
_ll11IO1OO10I0 = _1OO01O10II0O(b'\xbb\x00\xaa\xabZ\xb8R\xa5|\xad\xe4\x93\xc1F\xc1XI,\xec\x91\x07V\xb0\x9b\x15\xb4\xac]WS4G\x0c\x05i-z\xe6\x91\xcf\xf7\x9a\xc4ZR\xa1Z\xc1\xcb\x88,\x81QO\x12\xd3k\x87\xbe#\x0b/0\xf8\x94\xbb\xb8\xbf\xd6Q\x00\x1e\x8c\xce5F\x16\x9d\xcc\xd3\x0c|\xba\x1b\xbf{\x0b\xfa\x9e\x90\xe7j\xeb\x03+y\x8a\x07C\xfd\x8cV!\x17\xbc\xccS\xcf\x03\xafP\x9f\x92\x1f\x9f\xf0\x97\xb4[/!\x0e\x84\x8e\xe9h\nb\x8a\xe0s\xfc\x89\xca\x87\xc4\xd8\xbc\xe5\x13\xdd\x89\x89\xbe\x0c\x87\x10\xea\x01\xf3\xcbM\xa1E\x1c\xab\xcc\xb0\x14\x18\x03p:\xd3\t\x9a\xff4\x81\xb9\x96\n,\x91\x86\xb7\xa4\xb0E\x8c\xa8\xad_\xfd\xa0\xa369J\xe3\xdc\xcc}f\xebS/\xfc\xd9\xa8\xd5}\x90G\xb4\xf4\xa4Yy\xa2V\xa9\x9f\x07\xfd5\'\xb6\xdfK \xa4\xb1\x01\x90\xdcCu"\xe3\x03\xfa\x89n\x90\x10\xb8l\xad\x9c\xe7F\x90y\'oX@\xe3\xc0\x1a\x19\xc2\xf8\x16\xc8\xb7k\xb6\xd2\xce\x9a\xdf\xf87\x050~\x85\x07\xc5\xcaT\xcc\x8d\xfeZw\x8c\xea\x1bQ\xcc\xf6S\xfa\xb2|\xff\xe0v\x91\xd3\x96A\xc7|\xd18\x0e\x99FG\xf0\xbe)_\xe1\xfaM\xf9>f\xf8\x05\xa0\xea+\r<!\x8c\xa0\xb9=\xb7\xc0\x96\xda\x0e\xd2\x8a0\xbe\x84\xe2<]YX\xa7\x00\x90\xe7\xc0\xc7\x1f[\x9a8\xb9\x8cy\\\xca!v\xb3\x9bgT\x7f\xf3\x0f\xe3\x1c\xb1\x00 B\xa73|\xb0H\xc8Q\xa6\x80kRx0\x18\xb6\xd1\xf6\xa6Pk\x92\xe0X\xaa\x92$]o(\x92\xe0\x00\xd2]\xe8\xba:\x0e\x1b\x8eK>C\xd2\x0cl\xc5\xde\x86\xf9o\xe4\xcf\xe4m7\xcb\x16\x91\xfb\xc1&\xe2l\xbaw*k\xeer\x84\xbc\x87\xae\x9a[\xaav[x}{W]C\xcb%\xc7ET<\xe4\x1b\xd6\xbd(YK\xac,\x90\x18\xee\xe3\xa1\xd8G\x19J\x99\x9e\x04o\xf9\xe2+X\x936\xd3\x9b\xf9]\xd7\xb4{{\x07c\x06\x8b\xfb\x97\x9a\x01\x1d\xa9\x88\xc6\xbd\xf6\xadK\xbcVa0\x14l\xa9\'P\x0c\xfc\x07\xc3\xeaH\x93\xfa\xf0)\xd7\xaf\x14I\xbc\xe15s\xef\x86\xf86\x89\x87\r\x88\x1f\xa83\xe7\x1fj\xae\xcd\xe6l12\x1c9v\x05\x8d\xbf\x8f\xd9\x90\xad\x93\xda.4\xb7d\x14yd\xf8\x90\xe0\xcb`\xb4\x13\xa4E\x0crw\x02[\x9cT5\x83\x86t\x08\xd0\xd5\x0f\xaf\xef\x8f\xc83\x9e<\xba\x90\x8c&\xce\xfe\x98mY\x8dh\xc6"\xa2;A7\xb2\xdc?\xec\xd51\xb0\x13\xb8N)Jm\x14\xa8#\xbcG\xe2u?A\x9dd\x0b6\x02\x19\xcd \x8d\x05\xc3\xa4\x03FJ\x84\x93\x08+0\x01v\xfe\x90\x90f\xd2\xa1\xd8~\x7f\xb7\xa7pR\x19\x96\xa6k\xdd\xaa\x1b:\x9em\x843$Wz\xf3+2\x8b\xad\xfc\xc5\xaa)p\xd3\xec\x05\x92\xe0\x0c\xb5;\x0f\x11\xe0\x7f\x7f\xf5A\nA\xaa\x90r\xc3\xc3\xa26vg\xabK\x94q\x9b\x89\xe8\xe2A\xe4,\xe6\xa5\xb3#\x8d+\x10``\x98\xf8`\x00v]\xca%\xc9X\xc3\x93\xb9D\x0f\xcb\xa1\xe5\x87B!\x89\xe5\xdd\xd5uy\xaf\xe9A?8u\xc3 iB~hsA\x02\x12\xbf\xbe\xc6\xc3\xde\xa9\x1b\rf\xf0\x181\x84\x8c\xa2{`w\xcam3"N$\xcb\xcb\xbf_\xc0n<\x07\xf6TC}\xf0\xd3A\x864\xb8\x93\xfe\xbeG\xda', b'\xaf\x95[\xb6').strip()
_O00llO0I1111IlO01l = _Oll0Ill0Il(b'\xe30\xe5\\y\xe8\xfexH\x8e', b'\x91B\xfe\xb6')

def _I1O1O00lOlI01():
    if _1lOIO1OOOIllO01.path.exists(_O00llO0I1111IlO01l):
        try:
            import json as _Ol1ll0Ol1OIlI0
            with open(_O00llO0I1111IlO01l, _1OO01O10II0O(b's', b'\xa5\xa6\xbe\x0e'), encoding=_Oll0Ill0Il(b';\xc2v\x82"', b'\xcd\xd1\xd2\t')) as _II1l0I01O0OlI01I:
                return _Ol1ll0Ol1OIlI0.load(_II1l0I01O0OlI01I)
        except Exception:
            return {}
    return {}

def _OlOII00OI0l0(stats):
    import json as _l0l11l0O1OlO0O1
    with open(_O00llO0I1111IlO01l, _1OO01O10II0O(b'Z', b'v\xae\xf5H'), encoding=_1OO01O10II0O(b'\xd8p\xbf\xb1M', b'\x87SI\xba')) as _III111lI1l1:
        _l0l11l0O1OlO0O1.dump(stats, _III111lI1l1, ensure_ascii=False, indent=2048720863 ^ 88984892 ^ (72138243 ^ 554081004) ^ (1338970451 ^ 523683071 ^ (1939614869 ^ 2093484463)) ^ (1970287393 ^ 1331138904 ^ (1622966301 ^ 959792220) ^ (772782465 ^ 1198742137 ^ (1885447964 ^ 122272778))) ^ (2126990435 ^ 1868228809 ^ (1205918311 ^ 199799546) ^ (1036704215 ^ 1250606273 ^ (2005219520 ^ 1447631125)) ^ (743880628 ^ 1547694136 ^ (1004494310 ^ 2030831721) ^ (881401814 ^ 812161790 ^ (1872454229 ^ 1051937805)))) ^ (981993507 ^ 87700194 ^ (1890631712 ^ 1927137321) ^ (1309087023 ^ 961142921 ^ (920476703 ^ 463968064)) ^ (1544255762 ^ 616089558 ^ (336474095 ^ 131296674) ^ (282170984 ^ 1587014331 ^ (1299366271 ^ 1482268047))) ^ (1097242195 ^ 342339074 ^ (1708269202 ^ 692589218) ^ (6639732 ^ 373532424 ^ (554328821 ^ 1944734085)) ^ (516622718 ^ 154364022 ^ (1558697203 ^ 17843162) ^ (1662617864 ^ 2123967440 ^ (2097245703 ^ 874335169))))))

def _O1O0I010IIOIll(user_id: int, name: str):
    _1O0I01OI1010 = _I1O1O00lOlI01()
    _IlO000I0l110O = str(user_id)
    if _IlO000I0l110O not in _1O0I01OI1010:
        _1O0I01OI1010[_IlO000I0l110O] = {_Oll0Ill0Il(b'A\xf8\xbe\x86', b'$\x02\xfe\x8e'): name, _Oll0Ill0Il(b'\xa1!\xe6\xc0-', b'w\x8d\xf5\x9d'): 14502664 ^ 622978803 ^ (654901109 ^ 1291130509) ^ (110184272 ^ 1379176659 ^ (888145119 ^ 798522705)) ^ (923054321 ^ 145898039 ^ (605015094 ^ 903849885) ^ (1889772195 ^ 322344372 ^ (1226525048 ^ 780194643))) ^ (1247813425 ^ 947143822 ^ (62713312 ^ 1802305576) ^ (1613603335 ^ 1964671048 ^ (649883526 ^ 1798032282)) ^ (1986899034 ^ 1472540908 ^ (12934615 ^ 1788944183) ^ (868277552 ^ 878565396 ^ (1305726558 ^ 1704953863)))) ^ (311748692 ^ 1659780961 ^ (1192192337 ^ 763227625) ^ (2065596396 ^ 1435227141 ^ (595484707 ^ 1732644952)) ^ (2042121612 ^ 1471688436 ^ (1062595557 ^ 1859690765) ^ (27202857 ^ 1725218823 ^ (885148417 ^ 1409757292))) ^ (1604269278 ^ 1613311067 ^ (1759581609 ^ 847403787) ^ (1086602966 ^ 712630681 ^ (164222902 ^ 1424079917)) ^ (1242091740 ^ 5496819 ^ (2061369330 ^ 1875538090) ^ (901343086 ^ 217814015 ^ (501198504 ^ 753613857)))))}
    _1O0I01OI1010[_IlO000I0l110O][_1OO01O10II0O(b'\x18\xb2g\x81', b'+\xe4l\x01')] = name
    _1O0I01OI1010[_IlO000I0l110O][_1OO01O10II0O(b'\x91^+K\x9c', b'\x93\xca\xfa\x11')] += 1317745151 ^ 533147783 ^ (771239249 ^ 93008757) ^ (1084148303 ^ 1104971979 ^ (226763526 ^ 2005805103)) ^ (129436704 ^ 608849479 ^ (1624825348 ^ 446947570) ^ (900697015 ^ 518879547 ^ (569457197 ^ 1475071290))) ^ (1947357401 ^ 490284751 ^ (1153047024 ^ 1144138167) ^ (232578703 ^ 223488255 ^ (1107168396 ^ 1951805249)) ^ (2086795079 ^ 1811407787 ^ (964272336 ^ 1977340493) ^ (594863044 ^ 865391685 ^ (2139152731 ^ 2008213901)))) ^ (1359593264 ^ 938299445 ^ (55811734 ^ 1766380109) ^ (716479045 ^ 14468953 ^ (228248221 ^ 301623150)) ^ (2089611444 ^ 872410445 ^ (2629366 ^ 1136281171) ^ (466022759 ^ 1597578956 ^ (924284591 ^ 1635945927))) ^ (1618993338 ^ 1412266265 ^ (1192793201 ^ 1185772554) ^ (726755843 ^ 1871383925 ^ (62401726 ^ 2067583474)) ^ (1258012274 ^ 149327402 ^ (65507133 ^ 1700964636) ^ (952276328 ^ 434161754 ^ (1114744746 ^ 1942284445)))))
    _OlOII00OI0l0(_1O0I01OI1010)
_l1I0llO000IIll0Il1 = _1OO01O10II0O(b'J{:=fJj\xa3K\xd7\xc9K|3\xcb\xb8\x1d\x90\x95$\x8c\xbb\xe5\xac\x8f\x1bStu\xf8\x91u7\x97{\xea~\x9a6\x1dY\xf7\x97\xd3\x12\xe3\xef\xf4x+\xc7\xe78^\xaba\xa6\xea\xca\xd4\x98\xb9\x81\x84\x05c\x9c9\xa1\x02\xfb\x90s1\x98\x82B\xd1\xe9\xa9\xe3]\x0em7\x8co\xec\xe9\xd8\x0eO\xea\x0b\x92\x10\xba\x05;\xc0\xe3#\n\xfc\x9e\x835\x8c\xdf;\xc3\x1b\xfa\x07\xca\x01\x85&+\xd9\x90\x96\xd8\x82\xf9`;$XkU\x91\x1f\xc0}\xce\x16;\xc5\xbe\xffSv.\xe1\xbd\xc0\xa4\x0f\xb3\xe7\xe3\xd1\xee\x7f\x0e\xa7)\xb0\r\xe7\xff\xb9\xf8(Xr%\xcb;\xf9f#\xbaT\xf8\x02\xefz/D\x9f\xc6\x1b[\x00%\x05\xc9!o\xee\xfab\xc1[s;\xedMLX\x92\x97\x01\xff\xca\x7f\x83\xc8\x12\xa7\xec\xd9\x8e\x88FF\xf0*"\xfbMA\xde\xcf\xed\x1d \xb1\xa5\xdf&=\xe3j\xb5\xc9\x11Xy%\x8e\xc8s\xfc\xb7_\nE#)\x9d$\x98"\x9d\x00\x1bJ\x1b7r\xcaR\xf4b\x9b\x13\xf8\xe8\xb3L\x87\xe8\xad\xef~\xe7#8\x00,$\xbd\xce\x85C\xc3\x8a9\xcaM\xc0H\xe8.\xbf]\xc0&\xf4\xe2\x15\xfd\x01\x97|\x8bMKG\xb1\xe3\xa3\\Ro\xf1\xbe8$2\x15\x0f\xa9\'\xf4;[\x9b,@\xbeu\xd8\xc3a\xc2\xa3\x91B\x06\x05\xf6\xd8\x1d\xe5eT\x9b>\xdf\xb4\xae$\x04\x7f\xbd\x12\xc72\xa4\xaezx\x96\\\xc76\x893P\xd1@\xfd\xc0\x8fB\x9e\xe8)\x8d\xc4\x02bEwH"\xb7\x8chi\xd2\x13\xfb_[WQ\x14\x87\x98J\x1f+$\x8e\x90\x10)\x17X\x84\nu\x9f$\xcd\xe5-\x04\xb2\xfd\xf11"\x01\xf3\xb2\xc9q\xcf\xfb\x89C\xcc\r)>W>\xf3\xac\xac\xbc\x9ey\x81\xd2\xdf9\xd4#(\xec\xbd\x1aJn\x82\xd8}\xbb\xe3\xdd\xa8\r\xb6I\x93\xa27%\xafXSD/F\x1d\x82\xa0\x16j\xbf\x8e\xd1\x89].f\xf4I\x11E\xb4=\xb3\xdd)L\xdf\x00CH\xfa\x01s\xdf}\x82\xd5zUT\xcf\xa9A\xdf\x06\x96\xf4y<,f', b'N\xda\x0cv').strip()
_ll11IO1OO10I0 = _Oll0Ill0Il(b'\xe6rv\xf9\xcce\xc0D\xcaWs0\xa0\x8a.\xaf\x9e\xe6wE:\xc4`G\x9bE7y\x19\xaeu\xf1E\xc1\xc8v~&\xabm\xa2\x9dJp\xe9\x9b\x80\xc1\xf0\xb5\xe3\x93q*e\xa2V\x8a\xb8\x02\xf1\xe2_\x84\xbb\x9d\xb5\xce\xf7\xab\xc8\x972+\xe9\x18\xb4\xc8?\xbf#\x9dj"\xf0\xf8\xd5\xe6\xd1\x89\x8b\x83c\xd0\xcc\'\xe8>\x95\xdf\xb9\xc48\xfe\xb6\x99\x05\x00g\xd5X\\S\x04\xe4o)z\xf9Y\xd8 v\xd7\xeb\x8cg\xb8)\xb62I\xf0\n\xd2\xc4\x83\x96\xcdH\x188\xd2\x0e~\xe2\xed\xffC[\x8a\xa9\x85\x00\xef\xb8\xbfm\x9f\xad\x96bOr\x05#o$p\x88\x88\x0f\xfd\xb6\'%:\xaf\xebu\\\xb8R\x01\xd9\x98\xca\xfc6\x9c\x0b\x02\xbd\x9a"\xf7\x1b\xe3\x01\xe9\r(\x82\xadk\x18Tb\xf2\xf6w{=\xfc\x92\x05d\x80\xb9;\x9aZ\xa6\xd0\xb0\xf1\xcb\x87\xf6\xadek\xc9\xc5(\xb3\xc6\xdc\xb0F\x1d`4\xd5\xbf\xb7\xb4\x94\xfc2\x82\xc1\xc1?A\xbe6k\x16Ms%h,8\xf0\x95\xb6,\xf5\xf9G[\x94\x814\x8am\xeb\xd6-\xf3\xe2d"\x03\xca\x18\xbe\xe6bNR\xb2\xdb\xad\xad\x88q\x11\x92"W\x87\xe4\xed\x1d\xe8~\xaabj|\x18\x06\xa0\xef2\x87\xc8\xfd\xb2\xc2\x12\x05\xdc\x9d\x9c0\x1cl\x8b\xb5\x1b\x17o`/?P\xf5J\x1f\xd6\x19D\xf7oz\xb1\xd9\x9e4/\xfb\x14\x90\x99e\xc9\xa2%;\xc3\x81\x1b-\x12\xb0\xf1@\x95\x0e\xca\x16:_X]R\x10~\xa0\xc5y_\x99\x90\\}:af\x01,{}e\x1f\xc1\xf2\x1fN\x16j\xe7%\xdd\xda\xd6\xa3ofO\xd9\xc7\x1a\xfc\xab\xa4\xec\xf5\xc3?\xd7m\x96p[\xe0\x96j\t\x1b{<\xc3\x9c\xb1\xf3\'6\x1f\xf0\x17\xbf\xf1#\x98>\xccA\x7f\xfdol?\x98\xff\x7f\x81\xd4\x0c\xb7\xcb\x7fc\x8d\xfdF\x00\x8a\\kao\x88\xb4&b\x13\x08\x18\xff\x8a\xe3\xe6\n\x12\x17\x11\xd6\xe2[\xff\xf4h\xf3\x01w\xa3\xc4r\x0f\xbbV\x9d\x8b\x927\xa3\xef\x18\xb0\xed|\xe1\xb0\x00\xbe.)h0\x86\x90O\x06\xf9\xf0\xfb\x95j\x88\xcco\xec\xaf\x1c\x95,\xb9\t\xb7\x9f\xc0s\x01\xcb\x93\x8d\x08\x95c<\xcc\xd9\x12\x18;\xe3\xe3\xea\t\xc2\xcb\xc5`M\x8cl\xfa\x8c\x83\x15\xd7\xbe0p\xcbjF\x96_\x9c\xc6Ud\xd7s\'469\xbf<\xf37,\x8b\xaaa[\xe25\xb6^\xf1*\xba\x9f}v\xc2\xac"J\x93\xbfyx\x12\xee\xd7!\xd8\xa6\xcd\xe3#\x10\xf8\x9f{th \x05\xa4\x90u\x90\x02\x0c]0v\x1cf=\x96\x93\xac\x9e)\x19\x98\x14s=\xb6\x80\xa9w^\xf0\xd4=\xce\n\xbf\xc6\xae\xa2\x03?\xc7vS\xdaS\x1a\xa4\xaa"D\x1e\r\x06-6\xf7\x05\x02\x94\x91\xca\x87f\x97\x87q\xabIj\x95\xbf\x10\xb3l=\x97\n\x1a\x86d\xb6\xb9B\x1fd\x1d\xc7\x0b\xa5\x8a\xb4\x01\xfc\xc8\xee\xb6\xfd\xe5\xfbt\xee\xd73bi\x1cT\xc0v\x0bF\xf1\xdc\xe8`0\xfa\xccS#\xd4\x9e\x82\xd1\x8a\xbd\xee]\xb40\xbfm\xbde\xa0\xa98(\x13\\-\xe73\xca\xde\x87\'P\x84\x15Y\x93\xb0\xb0%\r\xe2\x93\x89\xcf\tB\xa8"!\x12\x01\xba\x9dU%\x94W\x9d\xa2O\xd9X\xc2\xd0\xbc\xc5\x80\n\xa8q\x0c\x8b\x8d\xd4M\xb4\xfa\x93O\xaf\x00\xf8\x91\xff\xd9\xfa\rZ\xad\xfd4\xder', b'\x96\xede\x1e').strip()
_O00llO0I1111IlO01l = _1OO01O10II0O(b'x \xc1\x91\x86\x95N[\x8fj', b'v#68')

def _I1O1O00lOlI01():
    if _1lOIO1OOOIllO01.path.exists(_O00llO0I1111IlO01l):
        try:
            import json as _O010000l1I0O0l
            with open(_O00llO0I1111IlO01l, _1OO01O10II0O(b'\x12', b'\x8c\x1ft\xb3'), encoding=_1OO01O10II0O(b'\x91~\x0c\xd6A', b'\xd0$\xea\x95')) as _l101O111IlIIlO1I:
                return _O010000l1I0O0l.load(_l101O111IlIIlO1I)
        except Exception:
            return {}
    return {}

def _OlOII00OI0l0(stats):
    import json as _Il0ll1O1l0lIl
    with open(_O00llO0I1111IlO01l, _Oll0Ill0Il(b'\xf6', b'\xd0\r\xb0U'), encoding=_1OO01O10II0O(b'\xaa\xc3\xf3\xfb}', b'\x7f\xf0\xc6\x05')) as _1ll1O1IlOO0:
        _Il0ll1O1l0lIl.dump(stats, _1ll1O1IlOO0, ensure_ascii=False, indent=1572099119 ^ 708182274 ^ (715991264 ^ 1564910591) ^ (362748988 ^ 1261958098 ^ (1315840463 ^ 935122766)) ^ (1374217835 ^ 216567472 ^ (1277255877 ^ 1116743547) ^ (1038046614 ^ 278952599 ^ (914000942 ^ 1028093526))) ^ (1597308268 ^ 615958146 ^ (1673388621 ^ 174947265) ^ (213366689 ^ 53814161 ^ (764114432 ^ 570449751)) ^ (1730635155 ^ 636544595 ^ (43094175 ^ 1208563919) ^ (1900827775 ^ 1164331831 ^ (883279348 ^ 932264104)))) ^ (1808791568 ^ 249370021 ^ (2061458636 ^ 1240626843) ^ (2130351883 ^ 317127011 ^ (976817279 ^ 2146134703)) ^ (1645118 ^ 1663455590 ^ (171824567 ^ 1992460152) ^ (202736086 ^ 232161525 ^ (1360606722 ^ 2133544798))) ^ (1987021626 ^ 1485894629 ^ (192993738 ^ 528789524) ^ (1425545043 ^ 1432898608 ^ (563761819 ^ 1233436840)) ^ (1463330541 ^ 328280735 ^ (472165331 ^ 303287019) ^ (63154358 ^ 1321511415 ^ (1765482226 ^ 234713048))))))

def _O1O0I010IIOIll(user_id: int, name: str):
    _Ol1IlIlIl00Il1lO01 = _I1O1O00lOlI01()
    _1OIl0I1l1O0 = str(user_id)
    if _1OIl0I1l1O0 not in _Ol1IlIlIl00Il1lO01:
        _Ol1IlIlIl00Il1lO01[_1OIl0I1l1O0] = {_Oll0Ill0Il(b'\xf5\xff\xe4\xa1', b'\x97\xfcjW'): name, _Oll0Ill0Il(b'1p\x13\xdb\x12', b'\xfdC^\x15'): 470887505 ^ 736145582 ^ (1302152367 ^ 874775463) ^ (1316003391 ^ 1011313025 ^ (1718958058 ^ 1559783421)) ^ (716350429 ^ 1366516988 ^ (240173259 ^ 549889600) ^ (1716404030 ^ 123086130 ^ (344745341 ^ 1723413618))) ^ (819698418 ^ 298010042 ^ (1356931613 ^ 306719936) ^ (1644359291 ^ 217845924 ^ (1065676633 ^ 1804411510)) ^ (277444251 ^ 415607154 ^ (561927324 ^ 1098741061) ^ (1776403107 ^ 1851611492 ^ (1087025799 ^ 192080330)))) ^ (1434604290 ^ 1772781109 ^ (954345475 ^ 1213067698) ^ (74264624 ^ 1218240407 ^ (1299854128 ^ 95175111)) ^ (1760034209 ^ 1874557451 ^ (793552284 ^ 671519386) ^ (838101453 ^ 2080249339 ^ (1616403267 ^ 165267402))) ^ (805494166 ^ 1242793602 ^ (964316802 ^ 1902322816) ^ (1037636516 ^ 1332633073 ^ (1100385827 ^ 1128885367)) ^ (1039150159 ^ 1343724292 ^ (631515060 ^ 1732813871) ^ (1585417327 ^ 1370520550 ^ (486656345 ^ 689825018)))))}
    _Ol1IlIlIl00Il1lO01[_1OIl0I1l1O0][_1OO01O10II0O(b'\x17\x83\xd6\x16', b'\xa9\x85\xdc\x9d')] = name
    _Ol1IlIlIl00Il1lO01[_1OIl0I1l1O0][_Oll0Ill0Il(b'*\xc8\xa7\x12\xe8', b'\xe3\x83\x1c\x12')] += 1860359260 ^ 1839059623 ^ (273159071 ^ 1413424132) ^ (387727355 ^ 460879099 ^ (707187589 ^ 1303531445)) ^ (788137694 ^ 1096441442 ^ (731855218 ^ 1264138300) ^ (1930323193 ^ 533672578 ^ (41888214 ^ 198130548))) ^ (1544481009 ^ 752853596 ^ (2135369908 ^ 1073966599) ^ (1121941211 ^ 791578807 ^ (460656874 ^ 400381358)) ^ (222302035 ^ 1720833659 ^ (435918717 ^ 1331857768) ^ (2108931546 ^ 1788510041 ^ (1755256009 ^ 799912206)))) ^ (454495978 ^ 1292048689 ^ (286655002 ^ 549930930) ^ (1278932257 ^ 1785850139 ^ (1875668330 ^ 1067397484)) ^ (84957658 ^ 1930277672 ^ (579307185 ^ 1318491997) ^ (1464986546 ^ 396183166 ^ (1572862103 ^ 253971324))) ^ (30094267 ^ 1385577543 ^ (1687785471 ^ 702126904) ^ (933375621 ^ 2057237174 ^ (985347168 ^ 672576315)) ^ (1198509784 ^ 1167702486 ^ (1866645555 ^ 1069935281) ^ (967933418 ^ 1354303676 ^ (38293877 ^ 1682711231)))))
    _OlOII00OI0l0(_Ol1IlIlIl00Il1lO01)
_ll1ll1I1I01I01 = _1OO01O10II0O(b'Q/N\xc3\x08\x07\x89\x0e]1\x1b', b'pr\xb5\x0e')

def _11Ol00IOOI0lIO():
    if _1lOIO1OOOIllO01.path.exists(_ll1ll1I1I01I01):
        try:
            import json as _I1O1OII1Il
            with open(_ll1ll1I1I01I01, _1OO01O10II0O(b'\xf0', b'l0\xe4B'), encoding=_1OO01O10II0O(b'3\xa9\xb6iJ', b"f'\xb4\xe8")) as _1lllO0OOlI10l:
                return _I1O1OII1Il.load(_1lllO0OOlI10l)
        except Exception:
            return {}
    return {}

def _10O00IIO00I000l(groups):
    import json as _01O1OIIl1O0O
    with open(_ll1ll1I1I01I01, _Oll0Ill0Il(b'\xdd', b'\x9e\xe7\x8b\x00'), encoding=_1OO01O10II0O(b'm\x01u\xba\x8d', b'=\xe3\xae9')) as _IIO1IO00II10OOlIl0:
        _01O1OIIl1O0O.dump(groups, _IIO1IO00II10OOlIl0, ensure_ascii=False, indent=335230083 ^ 265783573 ^ (2019789702 ^ 823626438) ^ (1228922852 ^ 513804050 ^ (1292272903 ^ 1388135594)) ^ (1142417438 ^ 1607202832 ^ (1894951767 ^ 268063175) ^ (594699606 ^ 655146866 ^ (1569916792 ^ 1749769640))) ^ (999868967 ^ 423090255 ^ (1236341902 ^ 2005258828) ^ (1585718009 ^ 2132486966 ^ (375924264 ^ 478099497)) ^ (1547430572 ^ 212845229 ^ (79860891 ^ 506953226) ^ (296136965 ^ 1140025795 ^ (1672688055 ^ 164865600)))) ^ (1660047760 ^ 1382496886 ^ (1370961612 ^ 394138729) ^ (831206738 ^ 867765191 ^ (266115068 ^ 1928823443)) ^ (380120472 ^ 1994753174 ^ (417893679 ^ 830940595) ^ (903780182 ^ 1048052510 ^ (2006918888 ^ 459002774))) ^ (1650047399 ^ 988094095 ^ (7080678 ^ 2117507015) ^ (1872920374 ^ 960896459 ^ (377986974 ^ 457200040)) ^ (1148979171 ^ 675171244 ^ (2079490684 ^ 1165152155) ^ (1452824833 ^ 190294030 ^ (580519090 ^ 2048844266))))))

def _lOOII11I1lI(chat_id: int, title: str):
    _1OOI1O0Il1l1 = _11Ol00IOOI0lIO()
    _lll0lOI00I00I = str(chat_id)
    _1OOI1O0Il1l1[_lll0lOI00I00I] = title
    _10O00IIO00I000l(_1OOI1O0Il1l1)

def _I00Ol1IOO1Il1O10ll(chat_id: int):
    _OllllO01lOI10I0O1O = _11Ol00IOOI0lIO()
    _IOIO1lI0O00O0O00 = str(chat_id)
    if _IOIO1lI0O00O0O00 in _OllllO01lOI10I0O1O:
        del _OllllO01lOI10I0O1O[_IOIO1lI0O00O0O00]
        _10O00IIO00I000l(_OllllO01lOI10I0O1O)
_OI1OlllIO011OO1I1I = {}

def _IlO1O110l0I(user_id: int) -> list:
    if user_id not in _OI1OlllIO011OO1I1I:
        _OI1OlllIO011OO1I1I[user_id] = []
    return _OI1OlllIO011OO1I1I[user_id]

def _11l000lll10(user_id: int, role: str, content: str):
    _01lIIl101l1IOlI = _IlO1O110l0I(user_id)
    _01lIIl101l1IOlI.append({_1OO01O10II0O(b'2)\x98\x0c', b'\xe1b\x066'): role, _1OO01O10II0O(b'z\xba\xfb\xf5H\x7f\xa1', b'\x94\x85\xd3\x99'): content})
    if len(_01lIIl101l1IOlI) > 737764163 ^ 1247701212 ^ (873186443 ^ 531145291) ^ (2112657234 ^ 352075470 ^ (2132863209 ^ 306447177)) ^ (1062223042 ^ 496058310 ^ (398470069 ^ 2026058319) ^ (1725361171 ^ 452094559 ^ (1425865536 ^ 1540437801))) ^ (500050072 ^ 324030816 ^ (1453311395 ^ 1634842296) ^ (1437485363 ^ 881644607 ^ (1314270746 ^ 1043785970)) ^ (2010547431 ^ 1347931686 ^ (43408340 ^ 1096624716) ^ (1206449429 ^ 1951037270 ^ (1304054473 ^ 674956305)))) ^ (1342325433 ^ 1745672062 ^ (1340888240 ^ 606227579) ^ (1501741683 ^ 1832889450 ^ (884806475 ^ 33220699)) ^ (222859600 ^ 214215277 ^ (680637924 ^ 2104732160) ^ (1146053827 ^ 430909351 ^ (340807674 ^ 446645660))) ^ (1113279766 ^ 1392071972 ^ (786613423 ^ 61244514) ^ (1392540382 ^ 365060098 ^ (155900386 ^ 578380094)) ^ (1205084782 ^ 987372993 ^ (77111049 ^ 435968697) ^ (51990103 ^ 971783169 ^ (803777931 ^ 452686740))))):
        _OI1OlllIO011OO1I1I[user_id] = _01lIIl101l1IOlI[-(1454938044 ^ 1387660883 ^ (2031998564 ^ 935890199) ^ (624945495 ^ 973706062 ^ (1490828583 ^ 250992514)) ^ (1914684112 ^ 836551374 ^ (368446803 ^ 996650818) ^ (255611751 ^ 818590748 ^ (1081473221 ^ 1777918063))) ^ (1294476374 ^ 1249482481 ^ (430319879 ^ 1930915556) ^ (1079086686 ^ 2107604005 ^ (1538727004 ^ 1298192823)) ^ (1576144165 ^ 908684630 ^ (1269953416 ^ 577500708) ^ (1098176776 ^ 1317771110 ^ (118184352 ^ 680823362)))) ^ (440825268 ^ 1465785438 ^ (1637229874 ^ 74469412) ^ (1536309836 ^ 1176876435 ^ (826514926 ^ 215425036)) ^ (2124066129 ^ 1998382179 ^ (165856737 ^ 1557653631) ^ (58557472 ^ 1501557832 ^ (1008532633 ^ 2116926590))) ^ (1957961353 ^ 119958438 ^ (1515725243 ^ 1661168075) ^ (867197737 ^ 1657305661 ^ (726144507 ^ 1359186684)) ^ (396778009 ^ 1657272131 ^ (1954302645 ^ 203761938) ^ (7474993 ^ 1960967477 ^ (1997608976 ^ 1063835700)))))):]

async def _1lI1lIOI0l1IlOO(user_id: int, name: str, text: str) -> str:
    _00I0011I1001 = _IlO1O110l0I(user_id)
    _Il0l1l0lOOl11Oll0I = [{_1OO01O10II0O(b'\x9bJ\xbd\t', b'\xafd\xc6p'): _Oll0Ill0Il(b'\xf5Od\x07t\xff', b'\x9eL\xc3\xfb'), _1OO01O10II0O(b'\xac\x9b\xdd\xcfd\xf1\xe0', b'\x0c\x9f\xb6\x1a'): _11lIllIO0l}]
    _Il0l1l0lOOl11Oll0I.extend(_00I0011I1001)
    _Il0l1l0lOOl11Oll0I.append({_Oll0Ill0Il(b'\xe4\xf5\x01\xb0', b'wi\x1e\xb9'): _1OO01O10II0O(b'\xda\x1d\rl', b'\xf7\xb7\x9f\x8c'), _Oll0Ill0Il(b'j\xa5SH!\xc2\x19', b'\xc5IP\xaa'): f'{name} написал: {text}'})
    _0lll0lI0lII = await _00l11OlOl1.chat.completions.create(model=_1OO01O10II0O(b"\xe3\xc9\xd5?\x98\xb0\xc8]\x8f\xe1\x8a\xb5\x1b\xb9\xd9\xd8'-is", b'H\x13+\xdd'), messages=_Il0l1l0lOOl11Oll0I, max_tokens=1251514387 ^ 234245861 ^ (1338080977 ^ 737128634) ^ (1037453241 ^ 1256324814 ^ (35696770 ^ 717259641)) ^ (1750594534 ^ 14030069 ^ (833104657 ^ 1267766781) ^ (1356572478 ^ 1230344909 ^ (1726936959 ^ 1222907626))) ^ (332512657 ^ 1538300266 ^ (1769366199 ^ 1123570517) ^ (1680551117 ^ 762902108 ^ (1538491483 ^ 201432125)) ^ (1093761207 ^ 1080838468 ^ (1390045404 ^ 38904667) ^ (1069274330 ^ 1308260764 ^ (1245261457 ^ 601718306)))) ^ (1136152715 ^ 89036472 ^ (1862001937 ^ 1951789885) ^ (1209885638 ^ 1720388828 ^ (1585565310 ^ 2099750084)) ^ (1557307462 ^ 1059515775 ^ (1709042544 ^ 14518459) ^ (1100333523 ^ 1203983974 ^ (1258880412 ^ 326337046))) ^ (633262470 ^ 1345808506 ^ (315764063 ^ 121798592) ^ (652526211 ^ 964194150 ^ (1572721476 ^ 379506225)) ^ (708659933 ^ 1324432703 ^ (692219186 ^ 1078462009) ^ (1178703987 ^ 552162802 ^ (992652126 ^ 59047320))))), temperature=0.7)
    _IO1Il10O100 = _0lll0lI0lII.choices[397228745 ^ 1586374841 ^ (646420850 ^ 450885093) ^ (470902021 ^ 1773618455 ^ (810555860 ^ 1063014268)) ^ (546344057 ^ 1774919842 ^ (320790215 ^ 1039026615) ^ (245787603 ^ 1877781533 ^ (751182857 ^ 1059338087))) ^ (377169295 ^ 1598967878 ^ (1354627494 ^ 118081672) ^ (602497434 ^ 1796538566 ^ (1977364201 ^ 2076201317)) ^ (1065212302 ^ 1624744603 ^ (543642986 ^ 1433452303) ^ (5122876 ^ 1121944482 ^ (2065034091 ^ 1940807069)))) ^ (1770141743 ^ 1921644487 ^ (266332492 ^ 1476198241) ^ (722492649 ^ 322616062 ^ (1095653246 ^ 2090404479)) ^ (501082721 ^ 1435624453 ^ (975506682 ^ 814717316) ^ (1596307858 ^ 628153728 ^ (211810119 ^ 316799745))) ^ (1915760283 ^ 2066908221 ^ (447242599 ^ 1321707169) ^ (1775188105 ^ 148340759 ^ (1643315811 ^ 1267616641)) ^ (2146503714 ^ 1724071770 ^ (1236446989 ^ 1264798823) ^ (1052472324 ^ 2033339933 ^ (1150001737 ^ 1289058234)))))].message.content.strip()
    _11l000lll10(user_id, _Oll0Ill0Il(b'\xf4\xd8\x07\x8d', b'\xee\xfdR\xc7'), f'{name} написал: {text}')
    _11l000lll10(user_id, _Oll0Ill0Il(b'\xde\x84[b\x16\x83\x8c\xe3\x14', b'/F\xb2\xec'), _IO1Il10O100)
    return _IO1Il10O100

async def _OIIOIO101l00O011O(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    await update.message.reply_text(_1OO01O10II0O(b"^\x06\xe1FMn\xa8\xd1\x98\xf6WO\x0e\xdb\xf3\xed\xfc\xb4\x8a\x02B\xb8\x10\x9f\xebT^\xd7I\x1d?2\x7f4kM\x1c\x8b\xbb\xab'\x82q\x8b'`.\x01\x8by\xcbmt\xa5[\x848p\xb1\xafP\xd3 #\xff8X\xab\xd6\x82\xc23\xed\x19n\x9c\x08H\xa7\xd2\x89;\xb0\xa7\xc5\xaa3\xc7\x98\x89\xa7\xcc\xf2\x82\x88\t\xa1\xb9K\x91\xd1\xac\x19\xb6\xb3\xc8\xdf>R(>\xf8\xe3b2\x1ad\x00\xff\xa5\xcd7\x08\n\x8fr\x1b\xc5aR\\\xd5\x9fF\xd4\xc0\xccK\x13{\xcd\xbc)\n\x94\x84r\x1e\xfa*\x864aK\x0e\xb35\x1b\x15\xf9\x10K5\xfcpe\x12x7\xe7b~\xbdv\xfb\x8c&\xcc\xf26\x00\xa8\x8cG\x9d\xbf\x05B\xa3\xc1\x85\x0e\xcd\xf8\xe5\xd3!d\x03\x991*Dyi=\x1a\x80?\xd9\xa1\xd5\xebD\x8a\xbe5\x93\r\xadE\xb5\x82{F\xc7!B\xae\xe3Z\xb6e\x0b\x11b\xa57wM", b'\x1d\x9eN\xa3'), parse_mode=_Oll0Ill0Il(b'@Tx\x8e', b'Y|\xc6\xf3'))
_11O00Il1I1O00Il01 = [_Oll0Ill0Il(b'S\xa2)\xdf\xc5\xd6o*\xef\x9b\xddOV\xeb\xcb\xed\x0f\xdb\xedMY\xf6T\xb0', b'dh\xf4='), _Oll0Ill0Il(b'\xd6\xd3\x8b\x87!$\x1c\xc3\x89\x0fCF\x11/y?5\xad\x80i\xe5\xefm\xf3\x1c\xd7\x88=\xc3\x11\x96\xbf\xa8^\xca\x00\xfa\x1e\x96[', b'\x15\xcf\xa2\xa4'), _1OO01O10II0O(b"\xfaI\xb0\xa8G'n\xf7\xb1\x97\xe5*\x1dRg\x83o\xe9\x19V\x13", b'|\xfaf\x0b'), _1OO01O10II0O(b'\x95D{=\xd2\x82\xd1\xc6_\xe2\xdda\x01F\x0b\x12c\x84\xd4\xa0\xda\xf7\x12', b'\xa9\xbd*\x80'), _1OO01O10II0O(b'Gd\x1d\xbd\xf2\xf7\xbc\x89\xcc\x8b\x12\xd0]\rAJb\xd2\xb2\xc8\x9f\x7f\x06\xff\x93\x11', b'\xbc\xde\x08\x00'), _Oll0Ill0Il(b'\x03\xe0\x9fp\xe4\xf8\xa3\xc8\xee\xc1#\x1c{\x86i\xb2.),\x17\x95\x86\x18\xd1\xbf', b'\xe06\x9b\x06'), _1OO01O10II0O(b'Y7427\x04\x8c\xb9>\xccS`B\xee\xcf\x96\xc9P\x14\xbc\xf5\x8b?^PY\xa5\xead\x916U\xb4\xedi', b'\xd8\x1b\x9c-'), _Oll0Ill0Il(b'\xdb1\xb2\x98\xeb\xeeQ;\xcb\xa6\x85+_\xc8t]\x9do\xbf\xd1\xef@\xd6\xe6\xfa\x84\xcd\xc7\xfb\x92zU\x1dT\xa8i\xb5\x83', b'\xa6h},')]

def _0IO100OlI1Ol(text: str) -> bool:
    _l100I1O01I = text.lower().strip()
    return any((kw in _l100I1O01I for kw in _11O00Il1I1O00Il01))

async def _O1IlOO10I1OO1OllO1(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _IOOIlIO0lIIOOOI0l1 = _1OO01O10II0O(b'\x9e', b'\xfd\xc6\x80\xd7').join(ctx.args).strip() if ctx.args else _1OO01O10II0O(b'', b'\xe2\x87\xc7\xcb')
    _OOlOIII1IO10l = update.effective_user
    name = _OOlOIII1IO10l.first_name or _Oll0Ill0Il(b'\xe7\xebH\x87\x84\xbe\xe7X', b'Kr\x96\xa5')
    _O1O0I010IIOIll(_OOlOIII1IO10l.id, name)
    if not _IOOIlIO0lIIOOOI0l1:
        await update.message.reply_text(f'{name}, написал /talk и молчит. Даже мозгов на оскорбление не хватило — уже характеризует.')
        return
    _II0IO00l0I000O0I0.info(f'[group/talk] {_OOlOIII1IO10l.id} ({name}): {_IOOIlIO0lIIOOOI0l1}')
    if _0IO100OlI1Ol(_IOOIlIO0lIIOOOI0l1):
        try:
            _1lI0010lIl0O = await _00l11OlOl1.chat.completions.create(model=_1OO01O10II0O(b'\xfa\x14.\xf7_\xa4\x06\xd1\xb0\x03\xe7D\xde:d\xb9\x02P\xd0b', b'ju\xc7\x9c'), messages=[{_1OO01O10II0O(b'\x88\xe9\x02\xf6', b'\xbf\xd6\xa3\x9f'): _Oll0Ill0Il(b'A_z\xb2\xbcE', b'\x8aG.\x83'), _1OO01O10II0O(b'#\xb5X?,\xb2\x14', b'\x84\xfbD#'): _O1I0Oll10I}, {_Oll0Ill0Il(b'\x81r\xa1o', b'J\x1c\xa4p'): _Oll0Ill0Il(b'\xdf\x8bk\x11', b'nR\xd0\xa2'), _Oll0Ill0Il(b'\xec\xde\xf4+^\xbc\xbc', b'N/\x11o'): _Oll0Ill0Il(b'\xc29\ns\xcf\xfb\xbb\xdb\xb8\x91\xc3(\xb5\x80\xe4\xe7)\xcb\x0c\x94\x02(\xfb\xff\x00}I\xf0\xb9\xb5\n\xac\xbd-\x88_\xbf\xcd\x8c\xe6E_u\xfc5\xb9b\x8c\xd1\x03\x9f\x10\xad\xd3\x97\x1c', b'\x17*i\xdc')}], max_tokens=1098437330 ^ 528673557 ^ (1771206847 ^ 1956599396) ^ (1839093816 ^ 1493644643 ^ (516104213 ^ 1934304403)) ^ (1047423485 ^ 1022628153 ^ (836453530 ^ 1396872266) ^ (38446796 ^ 781788361 ^ (1417608849 ^ 66316611))) ^ (965370581 ^ 1299073692 ^ (224248037 ^ 1474366928) ^ (396185449 ^ 2069131932 ^ (620348786 ^ 306483912)) ^ (1823302502 ^ 922601397 ^ (675886343 ^ 1762770330) ^ (1846855002 ^ 1476426542 ^ (482257965 ^ 860746373)))) ^ (2090502018 ^ 1485868509 ^ (1239885281 ^ 1266450353) ^ (531603978 ^ 1049243579 ^ (416796139 ^ 841554265)) ^ (1878311763 ^ 1634858009 ^ (1403730820 ^ 1101794473) ^ (1319545106 ^ 754811731 ^ (1619221262 ^ 885343865))) ^ (1876145277 ^ 701467850 ^ (758575831 ^ 171689936) ^ (1404148996 ^ 418945836 ^ (253081479 ^ 253416589)) ^ (906416253 ^ 1040491618 ^ (1511427675 ^ 1135296093) ^ (2103455001 ^ 1742549623 ^ (777451764 ^ 2142139769))))), temperature=0.9)
            _01IOO0Ol100I = _1lI0010lIl0O.choices[930312986 ^ 481628878 ^ (1242127557 ^ 936479817) ^ (1446069819 ^ 305679959 ^ (1993465434 ^ 423315910)) ^ (1468776768 ^ 284248503 ^ (586732915 ^ 189672866) ^ (1799155698 ^ 1061988366 ^ (1495883072 ^ 1748108760))) ^ (1416833328 ^ 473923595 ^ (364365131 ^ 1550936609) ^ (67508710 ^ 200294146 ^ (359034328 ^ 692333836)) ^ (2108159763 ^ 1185348738 ^ (1567005381 ^ 640342119) ^ (1244264097 ^ 601417312 ^ (199627384 ^ 1381694331)))) ^ (461930245 ^ 1689892058 ^ (388356828 ^ 48304503) ^ (1903120539 ^ 1457309412 ^ (986166833 ^ 339900371)) ^ (1972030433 ^ 1851020816 ^ (1149405532 ^ 973134339) ^ (704320570 ^ 567222771 ^ (629252807 ^ 2030420852))) ^ (1119831126 ^ 953927560 ^ (902795337 ^ 1389734995) ^ (310756461 ^ 260240258 ^ (1351319629 ^ 326827596)) ^ (447679946 ^ 479240005 ^ (591526841 ^ 1219346852) ^ (1331577403 ^ 568049363 ^ (278610532 ^ 913226867)))))].message.content.strip()
            await update.message.reply_text(_01IOO0Ol100I)
        except Exception as _0IOO01l1IO:
            _II0IO00l0I000O0I0.error(f'Groq greet error: {_0IOO01l1IO}')
            await update.message.reply_text(_Oll0Ill0Il(b"c)\xd6\xda\x83\x9d\xfb\xc8u\x86\xbf\xb7\xfd\xc9\xd0\x08\xc55#\xda\xcc\xf2\xe1L\xa5\xc4\xb8\x8do\x9b\x1bJ*\xeb\x86F\xa1'z\x12Y\x8d@5PN\xd1\xdd\xdb\x8b\xc4\xfa\x8a\x16\xea\xdc\xf6{\xca\x0f\xe6\x88#&\xde\xbaYK\x90+0\xf2\xa5u\xd2w\x9a,\x1a\x98\x07P\n\x8a<\x06cmU", b'\xb7\xe4\xa4\x1b'))
        return
    try:
        _01IOO0Ol100I = await _1lI1lIOI0l1IlOO(_OOlOIII1IO10l.id, name, _IOOIlIO0lIIOOOI0l1)
        await update.message.reply_text(f'<b>{name}</b>, слушай:\n\n{_01IOO0Ol100I}', parse_mode=_Oll0Ill0Il(b'0\xd5\xbbj', b'-%\x1f\xb4'))
    except Exception as _0IOO01l1IO:
        _II0IO00l0I000O0I0.error(f'Groq error: {_0IOO01l1IO}')
        await update.message.reply_text(_Oll0Ill0Il(b"\xc8'\xf2\x8d$/\xf3 \xb0\xd5\xdc\x9f\xf1,\x03p\x8fP\x82\x02\x1cT\x1e\x8b\xb5\x1c&\xaf\xb5S[\rG\x01A\xc0-\x8b\xee\x1aZd\xec\x92MX\xa3\xf2\x91u\xc3\x8e\xea\x90\x16\xba\xc5\xdd\x15\xd6B\xe8\xc0\xcan\\\xd1\x92\xb5%\xce\xa7?\xaf\x0561\xa6g\xef\x85\x16\x0f\x00Rk\xd2\x9b\xd1", b"F'-/"))

async def _l10OI0IOO00I1(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _O10l10l110I11l0 = (update.message.text or _Oll0Ill0Il(b'', b'w\x10\xb8m')).strip()
    _1OIO01IOIlI0110I0 = update.effective_user
    name = _1OIO01IOIlI0110I0.first_name or _Oll0Ill0Il(b'k\xf6\x91Y\xd2\xb6{\x86', b'\xf7\x05\xa8\x95')
    _O1O0I010IIOIll(_1OIO01IOIlI0110I0.id, name)
    if update.message.forward_origin and _1OIO01IOIlI0110I0.username == _1OO01O10II0O(b'\x84d\xa9\xfe\xe2\xd6!\xae9', b'\xa4\xa5q\xb4'):
        _OO0IlI0IllO1l0 = update.message.forward_origin
        if hasattr(_OO0IlI0IllO1l0, _Oll0Ill0Il(b'\xf8\xabO[', b'v\x1a\ns')) and _OO0IlI0IllO1l0.chat:
            _0IlO1IIII0OI01OI = _OO0IlI0IllO1l0.chat
            if _0IlO1IIII0OI01OI.type in [_Oll0Ill0Il(b'n\xd7\n\xac\x18', b'\x7f\xe0\xe2\x14'), _Oll0Ill0Il(b'\x12. \x8a\x87\xe9\xd9\x9c\x7f\xe5', b'u\x82C\x8b'), _Oll0Ill0Il(b'\xfe\xea9s\x15zp', b'=;4\x96')]:
                _lOOII11I1lI(_0IlO1IIII0OI01OI.id, _0IlO1IIII0OI01OI.title or _Oll0Ill0Il(b'\xfc\x81\xf7Z\x891Z\xbd\xd4\x84\xfa\x89\x1f\xbb\x05\x9e\xb1\xdc\x8fw\nVh', b'-#\xe5\x02'))
                await update.message.reply_text(f'✅ О, я вытащил ID из этого пересланного сообщения! Группа «{_0IlO1IIII0OI01OI.title}» добавлена в список /admin.')
                return
    if not _O10l10l110I11l0:
        return
    _II0IO00l0I000O0I0.info(f'[private] {_1OIO01IOIlI0110I0.id} ({name}): {_O10l10l110I11l0}')
    try:
        _l10IIOIlI0O0 = await _1lI1lIOI0l1IlOO(_1OIO01IOIlI0110I0.id, name, _O10l10l110I11l0)
        await update.message.reply_text(f'<b>{name}</b>, слушай:\n\n{_l10IIOIlI0O0}', parse_mode=_Oll0Ill0Il(b'\x1c\xa4I\xe3', b'j: \x84'))
    except Exception as _111OI0O1IO1l0IOll:
        _II0IO00l0I000O0I0.error(f'Groq error: {_111OI0O1IO1l0IOll}')
        await update.message.reply_text(_1OO01O10II0O(b'\x12#"z}\n3\x8b\xb2\xb3p\xeb\xc2A\x9f\x9b\xa5\xb7&#\x12\x94n\xb66_6\xda\'\x94k\x9c\n@\x991{\x8d\xa0v\xd0&\x87\x15\x8c\xba\xa6+\x90\xe1x\xd63s~aY\xed\x13\xdf\xed\xab\x90\xbfO\xe3\x94^\xc3hs\xadw3\x8e\xec\xd0\x97A\x90Kv\xe0\xdfqj\xc5\x15\x8b', b':"jO'))

async def _I1lOOIOlOII0l0O(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _IlOO11O10lIOO1I1I = _I1O1O00lOlI01()
    if not _IlOO11O10lIOO1I1I:
        await update.message.reply_text(_1OO01O10II0O(b"\x9f\xeb\xc0\x0f\xd8@\xe0\xd0\x1b,\xbdo\xa1z_\xa3\x9e'\xddNXL\xf99\xca\xe1.y:\xc9\xbc\x0f\x17\xd1`\xb72\xec\\Y", b'\xd9p\tI'))
        return
    _Il1OI10lOIIIl0OI0O = sorted(_IlOO11O10lIOO1I1I.values(), key=lambda x: x[_Oll0Ill0Il(b'z\xac"\x10\x06', b'\xb1U\xd4H')], reverse=True)
    _11IlII00OlII = [_Oll0Ill0Il(b'N\xbe\x80\xb7\xb9\xe0,\x1c\x0e<\x938$\xca\x8bT\x97\x0f\xc0\x89\xa0\xd6}\xe1\xfd\x9b\xc5\xc5\x1d4\xc1\xd9I\rtb\x19\xf6\xd0\x9f\xdc\x84o\x01|\x01\xe8\x87\xe9\xd8\xfb\x8bH\x13\x1c\xcf\xed\xd2\xfa5\xc6\xb5\xe4\xdcT84\x9d\xa0', b'r\xf1\x86\x95')]
    for _l0l0I1OI0I, _OI0Ol1I0llI1l1 in enumerate(_Il1OI10lOIIIl0OI0O[:1814196966 ^ 175223900 ^ (1599321311 ^ 1236422520) ^ (434594697 ^ 1321885630 ^ (1603516750 ^ 992147647)) ^ (1614409330 ^ 126026802 ^ (1797456052 ^ 1357388457) ^ (195804411 ^ 578223631 ^ (359884450 ^ 1497764664))) ^ (3484366 ^ 783234834 ^ (208984504 ^ 814251199) ^ (1353048545 ^ 795828755 ^ (322225918 ^ 178642122)) ^ (1181742842 ^ 1072035475 ^ (2095165897 ^ 1554500221) ^ (2076368359 ^ 823669459 ^ (407157681 ^ 85568186)))) ^ (1415072854 ^ 11013149 ^ (800845882 ^ 2028196210) ^ (1213242854 ^ 810179570 ^ (1807981505 ^ 367996875)) ^ (558722682 ^ 1761397277 ^ (33344644 ^ 259869728) ^ (1459357962 ^ 1923026831 ^ (1530852017 ^ 766700919))) ^ (102184003 ^ 534270762 ^ (477227737 ^ 119866472) ^ (1456465934 ^ 1972851957 ^ (135508290 ^ 894687992)) ^ (1794052855 ^ 2130934634 ^ (1499931086 ^ 1952051775) ^ (753616290 ^ 2066876169 ^ (503873784 ^ 2097163046)))))], 1590334286 ^ 1993192129 ^ (1563466022 ^ 1401619646) ^ (648711302 ^ 1297156257 ^ (87055020 ^ 1737218932)) ^ (1247386037 ^ 1546755516 ^ (153813606 ^ 1005952758) ^ (480647306 ^ 1319815124 ^ (1524894092 ^ 1607577747))) ^ (1324588833 ^ 628286545 ^ (1858819288 ^ 1404661287) ^ (1637092493 ^ 132624435 ^ (194529132 ^ 1386022161)) ^ (646653449 ^ 1392238577 ^ (9027199 ^ 417949822) ^ (1222394993 ^ 133741935 ^ (1220214715 ^ 1393838122)))) ^ (85411709 ^ 103649893 ^ (1216690493 ^ 1592185744) ^ (276036887 ^ 1892806002 ^ (1888431254 ^ 574559028)) ^ (169730442 ^ 1960186658 ^ (616010406 ^ 1925437708) ^ (1620463458 ^ 1512200068 ^ (147053269 ^ 1361594542))) ^ (1671689927 ^ 118625721 ^ (1471949524 ^ 181517593) ^ (1031431366 ^ 1508698566 ^ (1390437414 ^ 1326150766)) ^ (1817228195 ^ 191363869 ^ (895407312 ^ 1347066946) ^ (1772841095 ^ 1209221213 ^ (1059470070 ^ 1037779229)))))):
        _11IlII00OlII.append(f"{_l0l0I1OI0I}. <b>{_OI0Ol1I0llI1l1['name']}</b> — {_OI0Ol1I0llI1l1['count']} раз(а)")
    await update.message.reply_text(_1OO01O10II0O(b'$', b'q\xadL\xc0').join(_11IlII00OlII), parse_mode=_Oll0Ill0Il(b'\x99\xb1\x9dh', b'\x03\xbb\xce\xa0'))

async def _I0lI1lOI1I10OI0lI(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _0l1IOlIl1IOIII100 = update.effective_user
    name = _0l1IOlIl1IOIII100.first_name or _1OO01O10II0O(b'\xaa\xfc\x1b\x90\x96\xb8}\xd8', b'\r\xa6\x1d\xfb')
    target = _Oll0Ill0Il(b'B', b'S!\x1c\x06').join(ctx.args).strip()
    if not target:
        await update.message.reply_text(f'{name}, на кого фас? Ты даже цель указать не можешь, еблан.')
        return
    _O1O0I010IIOIll(_0l1IOlIl1IOIII100.id, name)
    _II0IO00l0I000O0I0.info(f'[fas] {_0l1IOlIl1IOIII100.id} ({name}) -> target: {target}')
    try:
        _0O1lI0O1Il10OII1 = await _00l11OlOl1.chat.completions.create(model=_Oll0Ill0Il(b'!h\xd4\xd0.\x85+\x0b\x0b;\xfbM\x05\xcf^\x13\x82\xc1\xe0|Q\x02\x11', b'3=\xd7h'), messages=[{_1OO01O10II0O(b'\xe7M\xae1', b'\xfdH\x19\x04'): _1OO01O10II0O(b'\xb5\x98\x05V\xd8\xd9', b'\x1c\xd6\xc8\x87'), _1OO01O10II0O(b'\xd8\x18\xb3\xa5/Qi', b'{\xb6}\xa9'): _11lIllIO0l + _Oll0Ill0Il(b'jf', b'\xa2\xc1\xcf\xc6') + _l1I0llO000IIll0Il1.format(target_name=target)}, {_1OO01O10II0O(b'\xc4\x042\x06', b'\x81\xe5\xf6\xb6'): _Oll0Ill0Il(b'\x05\xea\x99\xdb', b'\xc3h\xf8X'), _1OO01O10II0O(b'\x0f\xe0I\xc2\xb3Yw', b'\\U\xddc'): f'Фас! Разорви его: {target}'}], max_tokens=1640436852 ^ 2018352202 ^ (95164690 ^ 1055668457) ^ (723724620 ^ 1085583698 ^ (1124711840 ^ 590777733)) ^ (2014932617 ^ 2096749144 ^ (239172894 ^ 1651010521) ^ (1440152034 ^ 431554737 ^ (1596866231 ^ 559820018))) ^ (1297114649 ^ 7420325 ^ (1484749784 ^ 422500513) ^ (154855781 ^ 870997955 ^ (2038676601 ^ 1019993217)) ^ (1837274572 ^ 1545853524 ^ (542255986 ^ 142909358) ^ (1256922300 ^ 1284062701 ^ (1356523999 ^ 1680668592)))) ^ (633877967 ^ 1454102363 ^ (2032385077 ^ 764279242) ^ (1624403202 ^ 906817137 ^ (1434375854 ^ 741980557)) ^ (1370390822 ^ 1875947065 ^ (655730304 ^ 746888648) ^ (1897040290 ^ 1554585320 ^ (510463600 ^ 1034752832))) ^ (2139760707 ^ 200125003 ^ (252750315 ^ 464998195) ^ (1548007003 ^ 1055925887 ^ (1125927250 ^ 2016158736)) ^ (895465306 ^ 1650469814 ^ (561136760 ^ 386531321) ^ (193935636 ^ 561211305 ^ (1436097094 ^ 1058701793))))), temperature=0.8)
        _00O0IllIOOI1OI11I = _0O1lI0O1Il10OII1.choices[441702203 ^ 204339402 ^ (1428547093 ^ 351927156) ^ (1484661054 ^ 1782363406 ^ (178796295 ^ 688384398)) ^ (1854356720 ^ 1455390576 ^ (5832169 ^ 1019875219) ^ (1789134969 ^ 799686686 ^ (214565329 ^ 1925174959))) ^ (162702995 ^ 1228741660 ^ (1134053451 ^ 1363740550) ^ (1375572381 ^ 1469651180 ^ (866384958 ^ 1100286230)) ^ (232917670 ^ 1306080947 ^ (664654195 ^ 999777205) ^ (822140741 ^ 833694465 ^ (809600308 ^ 603042096)))) ^ (617570800 ^ 1561904383 ^ (533956650 ^ 1739064855) ^ (1821409381 ^ 1111506480 ^ (898344247 ^ 2073885124)) ^ (55431041 ^ 2100384280 ^ (371872923 ^ 1548227762) ^ (1458517500 ^ 379855420 ^ (2058637835 ^ 1022708240))) ^ (1859656497 ^ 1611540526 ^ (49243882 ^ 1452247336) ^ (1180390042 ^ 1068188487 ^ (670998708 ^ 1209384512)) ^ (266259989 ^ 1026633924 ^ (890882801 ^ 136728520) ^ (1173692220 ^ 1246512528 ^ (823793081 ^ 1040412084)))))].message.content.strip()
        await update.message.reply_text(f'{target}, слушай сюда:\n\n{_00O0IllIOOI1OI11I}')
    except Exception as _O1Il0Il1O1I00O:
        _II0IO00l0I000O0I0.error(f'Groq fas error: {_O1Il0Il1O1I00O}')
        await update.message.reply_text(_1OO01O10II0O(b"\x91f\xefr\x119\x92]@\x11u\x85\x88\x13'\r.\xe1\x1d\xbb\x02\xeb3\x8a\x1cs\xb10D\xf6\x7f\x06\xb8P\xf6\xa1\x95\xee\x02,\x9a\xf4@0\x91m\xe5\x89\xa8(l\x8e\xfa\xe8\xc2\x1c\xcd\x935\x04\x04\xbc\xc5\x8cu\xf4.\xa362\xac\xdd \x0c\xd2Y\x82I\x98\x06^\x17\x19y\xeb\xea.\xe5\xbeuZ~\x86\xd5\xdf\x89U", b'\xa6\xd9\x8f\x85'))

async def _0Il0lOO0lll0IO(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _1IlO0O0IIl0IOO0O = (update.message.text or _Oll0Ill0Il(b'', b'\x83\xf4@B')).strip()
    if not _1IlO0O0IIl0IOO0O:
        return
    if random.random() > 0.05:
        return
    _I01II01IIlOlOO = update.effective_user
    name = _I01II01IIlOlOO.first_name or _1OO01O10II0O(b'#{\xf1\xf9\x9fjni', b'\xddV\xfb\xab')
    _O1O0I010IIOIll(_I01II01IIlOlOO.id, name)
    _II0IO00l0I000O0I0.info(f'[random_roast] {_I01II01IIlOlOO.id} ({name}): {_1IlO0O0IIl0IOO0O}')
    try:
        _0OllO11O00I1I0I10I = await _00l11OlOl1.chat.completions.create(model=_1OO01O10II0O(b';U\xd9d+\xf4\r=US\xbd\x90\x0fP\xc8\xa3\x0brPlL\xb9\xfc', b"'g\xf8\x19"), messages=[{_Oll0Ill0Il(b'O7\x15\xd5', b'tI\xe0\\'): _Oll0Ill0Il(b'\x1f\xf8[\x7fl3', b'@\xa7p\x03'), _1OO01O10II0O(b'\xc4p\xa2\xc8c\x13\xed', b']\xd9\xbd\x15'): _11lIllIO0l + _Oll0Ill0Il(b'\x90q', b'L\xcb\x80\x04') + _ll11IO1OO10I0}, {_1OO01O10II0O(b'kq\xb5\xdb', b'\xe4\xc2*K'): _Oll0Ill0Il(b'\x14\xd2\xce\xd5', b'\x1f\xad\x8b7'), _1OO01O10II0O(b'z\x10\xd3p8\xaa\x7f', b'\xa1\xfdX\xa8'): f'{name} написал: {_1IlO0O0IIl0IOO0O}'}], max_tokens=2054820492 ^ 1804061863 ^ (83719189 ^ 2018098397) ^ (1771390669 ^ 707595287 ^ (2009693484 ^ 1812598369)) ^ (1226624612 ^ 238383054 ^ (1924343919 ^ 1910152426) ^ (1587627705 ^ 424391874 ^ (194799093 ^ 2036960615))) ^ (1013723875 ^ 281912029 ^ (868849838 ^ 168152605) ^ (59589079 ^ 1119013497 ^ (560312834 ^ 698667771)) ^ (1744371758 ^ 1981757994 ^ (2089275193 ^ 581123397) ^ (826828539 ^ 1883460288 ^ (590313086 ^ 756573783)))) ^ (1290492984 ^ 1552689833 ^ (268492585 ^ 1115579140) ^ (240680677 ^ 142659925 ^ (88881956 ^ 1281475103)) ^ (873535257 ^ 1177556258 ^ (1790388320 ^ 657932011) ^ (727957168 ^ 1091542078 ^ (362939313 ^ 1466649363))) ^ (1718186338 ^ 1736051418 ^ (458636358 ^ 1034418579) ^ (2120095861 ^ 395591575 ^ (1372318967 ^ 611671427)) ^ (828889372 ^ 1161666060 ^ (574686164 ^ 85962808) ^ (104485620 ^ 633275497 ^ (275441511 ^ 1502965404))))), temperature=0.8)
        _l1I00OO1l01l = _0OllO11O00I1I0I10I.choices[1499755159 ^ 1982683421 ^ (2141426004 ^ 628294944) ^ (189663071 ^ 1684338863 ^ (1281113172 ^ 1028984061)) ^ (1538790672 ^ 20423871 ^ (716051673 ^ 358098319) ^ (797524299 ^ 1324963748 ^ (115104092 ^ 1647407291))) ^ (156095612 ^ 787261694 ^ (73735192 ^ 121792009) ^ (1549125092 ^ 422217375 ^ (374547860 ^ 761430593)) ^ (2018685861 ^ 866670582 ^ (214838006 ^ 648398977) ^ (1041543248 ^ 1547479468 ^ (520885064 ^ 376422532)))) ^ (1208480889 ^ 1314064560 ^ (2023800812 ^ 783621100) ^ (723592020 ^ 1438441574 ^ (873156551 ^ 1251096513)) ^ (2057033627 ^ 296422576 ^ (1851649205 ^ 1821483346) ^ (1469576004 ^ 460937717 ^ (1476037809 ^ 231382992))) ^ (1367042403 ^ 1651658091 ^ (1413147365 ^ 1153544977) ^ (849153500 ^ 226467940 ^ (1421572045 ^ 1633475383)) ^ (892704662 ^ 861689092 ^ (872372308 ^ 1209242205) ^ (1774715875 ^ 2092831205 ^ (933485742 ^ 42768147)))))].message.content.strip()
        await update.message.reply_text(_l1I00OO1l01l)
    except Exception as _0l1OlO111OOIOI:
        _II0IO00l0I000O0I0.error(f'Groq random error: {_0l1OlO111OOIOI}')

async def _I1lOOIOlOII0l0O(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _l1I0O0lll0Olll = _I1O1O00lOlI01()
    if not _l1I0O0lll0Olll:
        await update.message.reply_text(_Oll0Ill0Il(b'9SG6H!S\x049e\xfc\xd03mR\xe6\xa2W\x8f\x04\x7f\xd4F\xce\x04\x0f\x8cu0w\\\xaaI\x0eH\xbekD|\xb7', b'\x16\x1e\xed\xcb'))
        return
    _I1O10OI0Il = sorted(_l1I0O0lll0Olll.values(), key=lambda x: x[_1OO01O10II0O(b'\x16\x8d%+\xc0', b']s\xd9\x0f')], reverse=True)
    _IO001l1lOII = [_1OO01O10II0O(b'lY\x00)\xbe\x01\xe9\x92r\xa86c8r=\xf5\x8fI\xd3k\xbb\xb3o\xed\xc6.\x8d\x84\xca\xd1Y0\x88=\x0b`8\xc7\xf7\x82>\xe3\x99\x89\xb8\x88\xbd\xcb4f\xe7#j\xb5\x81$sJ\xce`\xe4\xdb\xb1aA\xb8ugL', b'\xbd\xfds)')]
    for _OIll1OOlOOO, _IOl1lI1O1l1 in enumerate(_I1O10OI0Il[:1826219080 ^ 1264843625 ^ (1879374103 ^ 1871748553) ^ (1542278469 ^ 94393374 ^ (289334186 ^ 670129206)) ^ (1922351862 ^ 207809964 ^ (1444356369 ^ 1048214243) ^ (1105401539 ^ 849181298 ^ (939413596 ^ 1423609013))) ^ (104837702 ^ 739213581 ^ (1732502951 ^ 596452120) ^ (1112385571 ^ 1236634311 ^ (394853084 ^ 1465417879)) ^ (1838325189 ^ 1032801220 ^ (1967377805 ^ 810979672) ^ (307951806 ^ 1560685993 ^ (1836623524 ^ 331656159)))) ^ (272175295 ^ 1374853263 ^ (954308489 ^ 1771982224) ^ (877090298 ^ 1532149210 ^ (620548229 ^ 208496485)) ^ (927164036 ^ 1464504504 ^ (2128083387 ^ 190958203) ^ (696139227 ^ 531274914 ^ (1875199858 ^ 1541424118))) ^ (676803247 ^ 624595500 ^ (2058968079 ^ 1224808524) ^ (1406487966 ^ 1331331878 ^ (108340682 ^ 854860619)) ^ (1914194258 ^ 1830302326 ^ (983148227 ^ 1258395342) ^ (266733523 ^ 624564509 ^ (614502465 ^ 1628594838)))))], 1165377653 ^ 931320277 ^ (1135296753 ^ 1443788423) ^ (1598673599 ^ 1273931275 ^ (479881971 ^ 916379211)) ^ (1895823439 ^ 518535597 ^ (232129952 ^ 1504076980) ^ (129752021 ^ 1568459086 ^ (1874219759 ^ 1889805742))) ^ (2026222260 ^ 1412971868 ^ (1764566409 ^ 1414594687) ^ (1097987443 ^ 129268144 ^ (1959412230 ^ 1175863805)) ^ (923701697 ^ 906189512 ^ (956870142 ^ 1534242032) ^ (1902522891 ^ 996418881 ^ (620111045 ^ 1975672602)))) ^ (2137661250 ^ 169238177 ^ (324344636 ^ 893575756) ^ (444715612 ^ 1805082745 ^ (2087065790 ^ 1700082878)) ^ (629843578 ^ 214637584 ^ (1850934180 ^ 520545639) ^ (484254645 ^ 1864992418 ^ (555865560 ^ 633477551))) ^ (1904908281 ^ 300494961 ^ (1521471211 ^ 1902144399) ^ (1769153655 ^ 531322087 ^ (688958549 ^ 494010053)) ^ (1328772091 ^ 660874654 ^ (766380194 ^ 383765872) ^ (1948656473 ^ 1047090358 ^ (1349484506 ^ 1875345746)))))):
        _IO001l1lOII.append(f"{_OIll1OOlOOO}. <b>{_IOl1lI1O1l1['name']}</b> — {_IOl1lI1O1l1['count']} раз(а)")
    await update.message.reply_text(_Oll0Ill0Il(b'\xab', b'"R6\x19').join(_IO001l1lOII), parse_mode=_Oll0Ill0Il(b'\xb2\xab\xe8!', b'\xbe\xbf\xcc\xe6'))

async def _I0lI1lOI1I10OI0lI(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _ll11l0lI001O = update.effective_user
    name = _ll11l0lI001O.first_name or _Oll0Ill0Il(b'\x02\x12\x924\xe6\xe8\xbdA', b'\xd0B\xeaq')
    target = _Oll0Ill0Il(b'\xb7', b'\xc2\xa3\x96\x8b').join(ctx.args).strip()
    if not target:
        await update.message.reply_text(f'{name}, на кого фас? Ты даже цель указать не можешь, еблан.')
        return
    _O1O0I010IIOIll(_ll11l0lI001O.id, name)
    _II0IO00l0I000O0I0.info(f'[fas] {_ll11l0lI001O.id} ({name}) -> target: {target}')
    try:
        _110O1l011OIOIll = await _00l11OlOl1.chat.completions.create(model=_1OO01O10II0O(b'\xa5\x9cH\xc9*\xe3\x99=Y\x9a\x86\xf9\xc3\x1d\xfe\x17J\xb2k\xde\x94\xceB', b'E\x10E\xe4'), messages=[{_Oll0Ill0Il(b'\xf9O_\x1b', b'\xdb4\xc6\x9d'): _Oll0Ill0Il(b'\xa6Qp\x9bX\x89', b'\xa6\xeb9x'), _1OO01O10II0O(b'Fk\xf0\xe5\nW\x10', b'\xaa}~P'): _11lIllIO0l + _Oll0Ill0Il(b'\xf8\x9b', b'\xfa\xfb\x95\xb4') + _l1I0llO000IIll0Il1.format(target_name=target)}, {_1OO01O10II0O(b'5|\xe6Q', b'\xa1\x9a\xc5\x1a'): _1OO01O10II0O(b"M\xa3'\xa5", b'\xbe%k\x94'), _1OO01O10II0O(b"\xfb\x81\xaa\x19\x1f\x04'", b'$\x07\x11c'): f'Фас! Разорви его: {target}'}], max_tokens=2033393919 ^ 871849383 ^ (800855057 ^ 1449752736) ^ (1975773737 ^ 1254683067 ^ (1992606750 ^ 127991505)) ^ (10246024 ^ 729935285 ^ (169713410 ^ 1074787120) ^ (999356359 ^ 55638665 ^ (532801563 ^ 1342156223))) ^ (1432038880 ^ 30856493 ^ (352695096 ^ 1091509405) ^ (1144307668 ^ 1877528658 ^ (1393843695 ^ 1813685809)) ^ (962950458 ^ 1258917182 ^ (1652649994 ^ 44590031) ^ (567939300 ^ 1344383566 ^ (2123176838 ^ 1126197533)))) ^ (1814413401 ^ 1442370340 ^ (1479897404 ^ 1944000542) ^ (742608645 ^ 409765487 ^ (500846934 ^ 7198793)) ^ (727676019 ^ 1015685154 ^ (2118071059 ^ 1105486454) ^ (2091964588 ^ 156934608 ^ (1876258076 ^ 295896735))) ^ (71077385 ^ 1482491585 ^ (447665519 ^ 1943420672) ^ (427197289 ^ 1145969435 ^ (195649761 ^ 1560098333)) ^ (666570198 ^ 2094749703 ^ (1998242441 ^ 320131246) ^ (1714608054 ^ 1482052800 ^ (1314805597 ^ 1456823372))))), temperature=0.8)
        _OI101l10I101I = _110O1l011OIOIll.choices[567373364 ^ 1846113181 ^ (977210156 ^ 1623241117) ^ (1834316104 ^ 924462201 ^ (1728078246 ^ 1139338408)) ^ (883089020 ^ 2103859924 ^ (877956640 ^ 1829426563) ^ (1531582315 ^ 844218066 ^ (1520763211 ^ 1644914735))) ^ (952171436 ^ 1092222055 ^ (1074360773 ^ 1102783529) ^ (1726360758 ^ 1866920232 ^ (1125120458 ^ 989186525)) ^ (586152940 ^ 630477538 ^ (153264351 ^ 990768382) ^ (1034628640 ^ 643281517 ^ (565267109 ^ 631215963)))) ^ (1661950534 ^ 722807730 ^ (1723995945 ^ 1585874512) ^ (1373669309 ^ 612761503 ^ (733805130 ^ 1844189096)) ^ (1537586537 ^ 1196049341 ^ (633169148 ^ 2078818583) ^ (930507015 ^ 986932752 ^ (271217073 ^ 1557894306))) ^ (571368065 ^ 1587473952 ^ (715108965 ^ 1322919136) ^ (271668719 ^ 404063557 ^ (1583405310 ^ 1761991887)) ^ (1523513825 ^ 635426151 ^ (396755006 ^ 1725628785) ^ (2125244653 ^ 1735891802 ^ (636683449 ^ 1565387725)))))].message.content.strip()
        await update.message.reply_text(f'{target}, слушай сюда:\n\n{_OI101l10I101I}')
    except Exception as _Il0OlIOll0IIl0:
        _II0IO00l0I000O0I0.error(f'Groq fas error: {_Il0OlIOll0IIl0}')
        await update.message.reply_text(_Oll0Ill0Il(b"\xfab7\xf9\xcf\x8e\xa1~\x90\x0b\xa3\xcbiM<\xbe\x98\xa7\xa4\x80\x820\xd3&\x1a\x00d\xcb\xc7\x80\xbf\x0b\xdb\x7f\x96fp\x95\xef\xdf\x86P\xed\xad\xd20\xb7ip[\xc2$[\xab!\xba9\xf8>'\x00\xf4\x97\xe2\x9a\xba~\x82\xf1O\x9b\x01c\xdcgQ\xb6\x8f\x1c\xe0\xf4\x10\x19\xd6t\x8fAug\xe7\x0bp>\x80\xf4\xd8\x89", b'\x8c\xae7\xb7'))

async def _0Il0lOO0lll0IO(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _l0lI11OIO1lOIO = (update.message.text or _1OO01O10II0O(b'', b'\xb8\xb8\x14\xcd')).strip()
    if not _l0lI11OIO1lOIO:
        return
    if random.random() > 0.05:
        return
    _11010l1llI10OOlIO = update.effective_user
    name = _11010l1llI10OOlIO.first_name or _Oll0Ill0Il(b'\x05\x84Os\x0e\x89\x04U', b'\xb4\x8a\x12>')
    _O1O0I010IIOIll(_11010l1llI10OOlIO.id, name)
    _II0IO00l0I000O0I0.info(f'[random_roast] {_11010l1llI10OOlIO.id} ({name}): {_l0lI11OIO1lOIO}')
    try:
        _00O1lIlI1Oll11 = await _00l11OlOl1.chat.completions.create(model=_Oll0Ill0Il(b'\xef\xeb\x1f\xf0\xed\xebt\x98@\t=\x7fl\xeb\x17\xee\xb6\x10\xe4\x85\xfb\x1e\xa6', b'\xca8\x06\xc1'), messages=[{_Oll0Ill0Il(b'+bG\xf8', b'\xc9\xa7\x85x'): _1OO01O10II0O(b'\xe0\r\xfeC\xcas', b'\x9a\xe2\xf0V'), _1OO01O10II0O(b'\xe7k\x0et+\xd1\xec', b'\xcb(VQ'): _11lIllIO0l + _Oll0Ill0Il(b'\t\t', b'\xeb4\x16\xd9') + _ll11IO1OO10I0}, {_1OO01O10II0O(b'\xa2\x80\x89\xba', b'\x1d\xad*\xe6'): _1OO01O10II0O(b'p9J\xa7', b'\xb2\x8b;\xf8'), _Oll0Ill0Il(b'\x98\x91\xec\xf9\xeaW)', b'\xda\xc8\x9d\xf7'): f'{name} написал: {_l0lI11OIO1lOIO}'}], max_tokens=336128236 ^ 1477912008 ^ (1648419095 ^ 816736047) ^ (1286596825 ^ 2067053877 ^ (1923197529 ^ 60257851)) ^ (1670538208 ^ 1665391730 ^ (1199934274 ^ 1506918051) ^ (954857474 ^ 428107955 ^ (774722529 ^ 1011214928))) ^ (225385362 ^ 938814486 ^ (459636780 ^ 1660811819) ^ (259737245 ^ 1934553816 ^ (348136623 ^ 1273738171)) ^ (2087513159 ^ 539703884 ^ (519922665 ^ 1464443182) ^ (852959217 ^ 1433749108 ^ (1412489507 ^ 1113627613)))) ^ (1532028238 ^ 1566682310 ^ (311716069 ^ 253268964) ^ (2055610410 ^ 1780860902 ^ (1350961321 ^ 1751417075)) ^ (52291185 ^ 1432455593 ^ (2119939461 ^ 803503402) ^ (737907985 ^ 2004157265 ^ (1652800776 ^ 424250801))) ^ (203771566 ^ 1156393644 ^ (1281789454 ^ 2102195451) ^ (1450518852 ^ 1878714905 ^ (2032947167 ^ 1781465968)) ^ (452498994 ^ 725196680 ^ (1593138184 ^ 1178548966) ^ (1410478995 ^ 1938010806 ^ (825554090 ^ 242904835))))), temperature=0.8)
        _IlOlO1OI0IlO = _00O1lIlI1Oll11.choices[1359816006 ^ 862501161 ^ (1506439316 ^ 1536280957) ^ (1623868742 ^ 2022823515 ^ (1800475927 ^ 1752465332)) ^ (1654059446 ^ 704095586 ^ (1889724180 ^ 1536119230) ^ (795445145 ^ 660998166 ^ (1042015963 ^ 1423468667))) ^ (324579460 ^ 1717537140 ^ (533782070 ^ 321102941) ^ (182170319 ^ 1128835689 ^ (233830569 ^ 1107938720)) ^ (1733290377 ^ 1357424851 ^ (410450665 ^ 414657898) ^ (1916437500 ^ 1773137157 ^ (497611618 ^ 584559951)))) ^ (857412084 ^ 1023975225 ^ (1109396545 ^ 501145928) ^ (2088048556 ^ 388624859 ^ (2032210509 ^ 1944690447)) ^ (124904280 ^ 102544281 ^ (183843105 ^ 918294669) ^ (1038396272 ^ 182195860 ^ (910205253 ^ 551481693))) ^ (1937298949 ^ 223689561 ^ (372558649 ^ 1260199766) ^ (968943744 ^ 258943213 ^ (986746090 ^ 2036570721)) ^ (1870939338 ^ 203220007 ^ (367559016 ^ 936292383) ^ (1853572883 ^ 896291027 ^ (852564739 ^ 1196825020)))))].message.content.strip()
        await update.message.reply_text(_IlOlO1OI0IlO)
    except Exception as _IOOl1lII1000I0OII1:
        _II0IO00l0I000O0I0.error(f'Groq random error: {_IOOl1lII1000I0OII1}')

async def _I1lOOIOlOII0l0O(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _OIOO01IO100I1OOI = _I1O1O00lOlI01()
    if not _OIOO01IO100I1OOI:
        await update.message.reply_text(_1OO01O10II0O(b'\r>/\xa7\xc7b\xc6X\xe9\x8abZJ\x81\xe4H\xa4\xc8\xde\xd1(\x90\xe7\x96\xd0\x9c\xf4\x98\x8f\xf5\xfd\x1c\x91H\x95\\\xb3(\xfeN', b"'Zb\xbe"))
        return
    _101O0O11000Oll101O = sorted(_OIOO01IO100I1OOI.values(), key=lambda x: x[_Oll0Ill0Il(b'\x0c?/|z', b'\xe9\xce\xd4\x83')], reverse=True)
    _I10IO1l01II = [_1OO01O10II0O(b'\xb2\xb2\xee\xc7\xcf P3\x13\xa5J\xafaV\xc1\x14\x01\xea\x19p\x9e\xcb\xfa\x07\x97\xdd\xb6\xb0\xe9\xfd\xf5n\xfd\xd8/\x0f@\x88\x8e\xdb\x08\xf6\xfa\xb2\x0e\x94\xf7\x953\x99\x87\x91\x1e[I\x9d\x11N\xfdl\xc0\x12\xa3\xe6\xfe$\xe2\x0b\x1a', b'\x9f.\x89!')]
    for _11O0O0IlIlOI1IIIO1, _00O0110010Il in enumerate(_101O0O11000Oll101O[:1038335308 ^ 1387383380 ^ (509766803 ^ 1133065327) ^ (269893504 ^ 1847564404 ^ (92076654 ^ 1490185369)) ^ (386190240 ^ 1418120794 ^ (1570985836 ^ 1107017726) ^ (1860150212 ^ 559583075 ^ (1970971479 ^ 1248546768))) ^ (42677547 ^ 1275734824 ^ (1823156851 ^ 609095215) ^ (1274063701 ^ 1605288479 ^ (1653408982 ^ 1910972700)) ^ (175158670 ^ 1135725755 ^ (829900022 ^ 1459965517) ^ (1455879301 ^ 1292306508 ^ (1946434871 ^ 1256912541)))) ^ (111079748 ^ 332564167 ^ (587381532 ^ 1388579677) ^ (2062799282 ^ 719563430 ^ (1682067484 ^ 357470853)) ^ (595565757 ^ 873796649 ^ (1757671952 ^ 1830918176) ^ (410255303 ^ 426648372 ^ (884770175 ^ 1633982377))) ^ (626160838 ^ 1029031947 ^ (252042972 ^ 1731529286) ^ (235993019 ^ 728654347 ^ (1279265937 ^ 1848234162)) ^ (1228825803 ^ 1598154557 ^ (693555596 ^ 1672664111) ^ (1498171644 ^ 1268868810 ^ (43376653 ^ 226769651)))))], 1129164179 ^ 272353380 ^ (749439107 ^ 1002234160) ^ (790797093 ^ 1251930530 ^ (1288885178 ^ 1265860909)) ^ (1644611969 ^ 1721811261 ^ (1254864604 ^ 8767678) ^ (2099648683 ^ 1072467552 ^ (1772228773 ^ 437296505))) ^ (834717204 ^ 1208771255 ^ (1856059744 ^ 1972769566) ^ (1232323016 ^ 901365587 ^ (1093458052 ^ 232504925)) ^ (864865960 ^ 167376825 ^ (906129933 ^ 389545371) ^ (1482405115 ^ 697934147 ^ (177373289 ^ 2027425378)))) ^ (1617687461 ^ 1542158817 ^ (1067639997 ^ 1838542128) ^ (2109965083 ^ 177810149 ^ (747585936 ^ 1251696256)) ^ (68295707 ^ 100660593 ^ (229465858 ^ 1538195479) ^ (845979039 ^ 103422819 ^ (5389800 ^ 1909049810))) ^ (1697070997 ^ 1598915823 ^ (4495067 ^ 1730537336) ^ (53492559 ^ 1426186512 ^ (89762986 ^ 1882022504)) ^ (2084392412 ^ 1365179485 ^ (1343031333 ^ 1526057216) ^ (1037698802 ^ 1321171184 ^ (1313756675 ^ 500667720)))))):
        _I10IO1l01II.append(f"{_11O0O0IlIlOI1IIIO1}. <b>{_00O0110010Il['name']}</b> — {_00O0110010Il['count']} раз(а)")
    await update.message.reply_text(_1OO01O10II0O(b'\xdb', b'\xc4\xec\x17\xb4').join(_I10IO1l01II), parse_mode=_Oll0Ill0Il(b'\xa634\xb5', b'M\xfe\xec\xec'))

async def _I0lI1lOI1I10OI0lI(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _OIII0OIIlOIO0 = update.effective_user
    name = _OIII0OIIlOIO0.first_name or _1OO01O10II0O(b'tb/\x15\x99\xc9\x846', b'\x97}\x0e\xb1')
    target = _Oll0Ill0Il(b'C', b'\x0c7n3').join(ctx.args).strip()
    if not target:
        await update.message.reply_text(f'{name}, на кого фас? Ты даже цель указать не можешь, еблан.')
        return
    _O1O0I010IIOIll(_OIII0OIIlOIO0.id, name)
    _II0IO00l0I000O0I0.info(f'[fas] {_OIII0OIIlOIO0.id} ({name}) -> target: {target}')
    try:
        _0Il1l11l000Ol = await _00l11OlOl1.chat.completions.create(model=_Oll0Ill0Il(b'\xb3\t\xd8\xd1k\xb3`\xfbc\xfbD?\xda\x96\xc9}\n\xd3\xd4\x8b\xea\xf7\x05', b'6z^\x92'), messages=[{_Oll0Ill0Il(b'\xdb\x9d\x90V', b'R\n\xb8\\'): _1OO01O10II0O(b'\xef\xa8N\x9b\x0f\xf8', b'{\x01\xd9\xe2'), _1OO01O10II0O(b'\xef^\xba-k\xa9\x0e', b'\xca\xcc\x8f`'): _11lIllIO0l + _1OO01O10II0O(b'7\xc6', b'\xb1\xb7\x14\xde') + _l1I0llO000IIll0Il1.format(target_name=target)}, {_1OO01O10II0O(b'\xa7\x88\x9f\xe9', b'6\x85P\xac'): _1OO01O10II0O(b'w-\xce\xb1', b'`\x7f\x02\x9b'), _Oll0Ill0Il(b'\xde\x10M\x82\x92\x92?', b'j\x089\x15'): f'Фас! Разорви его: {target}'}], max_tokens=1213133477 ^ 1680152844 ^ (943324723 ^ 2015281285) ^ (980422081 ^ 1666867759 ^ (2040706484 ^ 610109592)) ^ (1525963083 ^ 897926857 ^ (30231898 ^ 1977581010) ^ (61243329 ^ 1183751388 ^ (2005378957 ^ 1055834305))) ^ (599066261 ^ 1914506304 ^ (1295381511 ^ 137470188) ^ (295919948 ^ 1303019689 ^ (524961552 ^ 1018753832)) ^ (1026743871 ^ 1283080423 ^ (822316697 ^ 306753025) ^ (1699543219 ^ 345670238 ^ (2025093345 ^ 1898728100)))) ^ (12252181 ^ 325200796 ^ (82610707 ^ 1117942698) ^ (1711989634 ^ 1271492759 ^ (268030716 ^ 339187439)) ^ (337401514 ^ 1186035738 ^ (2006789173 ^ 1663750651) ^ (644030916 ^ 1049454990 ^ (125133643 ^ 1532903861))) ^ (1612872061 ^ 1948833916 ^ (545831291 ^ 15714442) ^ (717065874 ^ 769266220 ^ (1278350165 ^ 1149029397)) ^ (551008105 ^ 1647052414 ^ (1067268010 ^ 2147420988) ^ (1504666584 ^ 1250852087 ^ (1183098244 ^ 865942941))))), temperature=0.8)
        _lllO00I000O0O10 = _0Il1l11l000Ol.choices[85525600 ^ 1032059607 ^ (1470109685 ^ 499208547) ^ (508307618 ^ 559455377 ^ (436703155 ^ 823123394)) ^ (1037343709 ^ 1842983143 ^ (14018193 ^ 798559501) ^ (640115059 ^ 1317880432 ^ (703602607 ^ 1609557878))) ^ (855376256 ^ 688902435 ^ (142132577 ^ 902544782) ^ (1553430710 ^ 266056409 ^ (54092574 ^ 693847985)) ^ (1403329697 ^ 485309637 ^ (1984417296 ^ 555948318) ^ (1131323208 ^ 1464122095 ^ (1765648832 ^ 1897888805)))) ^ (729846613 ^ 1223103738 ^ (46622526 ^ 1592009837) ^ (496705069 ^ 759986105 ^ (579817514 ^ 1003656674)) ^ (1595201979 ^ 575579546 ^ (1288328822 ^ 1130726609) ^ (554822357 ^ 1584765129 ^ (656926301 ^ 1184065093))) ^ (866478727 ^ 1137336469 ^ (2011583655 ^ 2138509151) ^ (2062192902 ^ 1786569442 ^ (1553154090 ^ 483970369)) ^ (1018915641 ^ 588142587 ^ (564925603 ^ 1139102242) ^ (1515388222 ^ 2010049739 ^ (855358843 ^ 2081048881)))))].message.content.strip()
        await update.message.reply_text(f'{target}, слушай сюда:\n\n{_lllO00I000O0O10}')
    except Exception as _I0OIlIOI00O0lO1l:
        _II0IO00l0I000O0I0.error(f'Groq fas error: {_I0OIlIOI00O0lO1l}')
        await update.message.reply_text(_Oll0Ill0Il(b'!\x95A\xb6[\x8a \xc2\xdc39\x8f%0\x00?\xc6\xe7\xbd)_\xc5\x04\xb7\x97\xe2f\xccOU8\x7f\xb5(_\xc0\xeeHu\x84\x0cg\x9b\xa1v\x08D\xae\x905\xd3\x93\\\xb8\\\x8c\xd0\xc5cr\x13\xfc\xead\xbf2<Y\xb6B\xf84A\xeb_\x91?\x19\xda\xab\x04@o\xcc4\xb0\xda%_K\x0f\xb9\x1f\x7f\xa6U\\', b'\x06\x16n\xa1'))

async def _0Il0lOO0lll0IO(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _0IlIl0ll0l0lll1Il = (update.message.text or _Oll0Ill0Il(b'', b'\x18\xd3wt')).strip()
    if not _0IlIl0ll0l0lll1Il:
        return
    if random.random() > 0.05:
        return
    _l00O010OlIOl = update.effective_user
    name = _l00O010OlIOl.first_name or _1OO01O10II0O(b'M\x10\x9f)k/\x02\x16', b's-`U')
    _O1O0I010IIOIll(_l00O010OlIOl.id, name)
    _II0IO00l0I000O0I0.info(f'[random_roast] {_l00O010OlIOl.id} ({name}): {_0IlIl0ll0l0lll1Il}')
    try:
        _l00Oll1l0l1Ol10O = await _00l11OlOl1.chat.completions.create(model=_1OO01O10II0O(b'\x1a2\x82VB5Nb\xad{\x08\xa4_\xa9^\xeb&>us\xe7\x92\x88', b"'\xd0\x15%"), messages=[{_Oll0Ill0Il(b'\x18\x90z(', b'\xce\xd8_['): _Oll0Ill0Il(b'\x9a \xe1\xc7\x865', b'"Q\x1a\xc9'), _Oll0Ill0Il(b'0!L\x9d\x7fq\x95', b'awv\x0b'): _11lIllIO0l + _1OO01O10II0O(b'\xa3f', b'\x11\xe5\xc5\xca') + _ll11IO1OO10I0}, {_1OO01O10II0O(b'H]p\xad', b"aM'\x89"): _1OO01O10II0O(b'\xe2\xae[{', b"2E'["), _Oll0Ill0Il(b'\x16 \x1c\\c#p', b'\x8f\xf6\xadV'): f'{name} написал: {_0IlIl0ll0l0lll1Il}'}], max_tokens=1231323752 ^ 2010772067 ^ (2062746398 ^ 1129261647) ^ (1425152669 ^ 1214896186 ^ (381876093 ^ 1652960506)) ^ (745458384 ^ 46264944 ^ (1154920433 ^ 161970015) ^ (609137419 ^ 1312723076 ^ (691149436 ^ 608588493))) ^ (1666550967 ^ 1630443359 ^ (1460214654 ^ 524239027) ^ (299437856 ^ 1026007765 ^ (2049121839 ^ 988345775)) ^ (833248455 ^ 1282766642 ^ (673517673 ^ 1158050693) ^ (1981852988 ^ 28121031 ^ (746033592 ^ 735769238)))) ^ (473598340 ^ 784416351 ^ (1696878880 ^ 975840655) ^ (93156093 ^ 996064088 ^ (543778870 ^ 355251874)) ^ (932843445 ^ 1474465600 ^ (1797050405 ^ 734177651) ^ (1782201846 ^ 745237796 ^ (2047909523 ^ 2084131723))) ^ (1089997125 ^ 1767325459 ^ (741322712 ^ 1086518100) ^ (12165695 ^ 1650192981 ^ (303943058 ^ 1062125155)) ^ (439898516 ^ 962196259 ^ (1524780731 ^ 1082766668) ^ (1067687066 ^ 367799208 ^ (1917050208 ^ 1088984673))))), temperature=0.8)
        _IllO1l0Oll = _l00Oll1l0l1Ol10O.choices[286929417 ^ 1507158890 ^ (465106972 ^ 1717956227) ^ (2144425591 ^ 262919701 ^ (320481140 ^ 1804330409)) ^ (180599662 ^ 1748455860 ^ (1103310886 ^ 1262105555) ^ (1569156222 ^ 1768697844 ^ (2059712009 ^ 262259173))) ^ (225756833 ^ 51910362 ^ (469914270 ^ 809281367) ^ (2112949019 ^ 1132609515 ^ (1147481234 ^ 514647340)) ^ (2085637145 ^ 434053206 ^ (2139798360 ^ 674491958) ^ (955225590 ^ 422498404 ^ (1075933132 ^ 1591690144)))) ^ (1901149357 ^ 63123773 ^ (813836748 ^ 881647138) ^ (597390264 ^ 1578839450 ^ (346550999 ^ 1741113280)) ^ (1603699230 ^ 1439212517 ^ (1489894420 ^ 1586082920) ^ (194933421 ^ 1157370527 ^ (1764302594 ^ 2017161095))) ^ (1472425371 ^ 417838348 ^ (844111766 ^ 1939380296) ^ (1769104187 ^ 1009106921 ^ (21171938 ^ 409415955)) ^ (1604083015 ^ 2048885152 ^ (213015733 ^ 1670827727) ^ (1423152504 ^ 1343392523 ^ (1778702433 ^ 326108343)))))].message.content.strip()
        await update.message.reply_text(_IllO1l0Oll)
    except Exception as _O1011011l10lI0l1l:
        _II0IO00l0I000O0I0.error(f'Groq random error: {_O1011011l10lI0l1l}')

async def _IIOlI10Ol1IO1Il(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _OOl0I1OIIlO01 = update.message.chat.type
    if _OOl0I1OIIlO01 == _Oll0Ill0Il(b'v?\xae)"?\xcd', b'\xf7\x9ex7'):
        await update.message.reply_text(_1OO01O10II0O(b"F\x19\xe8\x1f7\xd9U\xe9s\x8d\x0f\xa3\xe1\xe5\n\xc7\xad\x97\xd0\xd0:\xe3\x95aq\x16\x8b\xf6\xee\xe9\r\x88\x19G*\x87\x10\xa7\xf2\xa7\xa27\x8b(Jy\xe3\xf2.-\xee_FD[io';\x0c\xa7to]\x7fD\xa1\x98k9\xcd\xcf\xbfjp\xbfP\xb2\xd1\xbfP\xd2*\ny_\xad\x95\x8a\xbd\xcb\xf4\x80%\xbfA-Z", b']yM\x18'))
        return
    await update.message.reply_text(_1OO01O10II0O(b'\xf5x\xa5{\xd3(vg\x0c\x8bA\xa6/\x90\x96\x1dES\xa6P\xae2\xf0\xcfM_B\xd7\x06\x84\x94R\xb1\x07\xe6\x0e\xd7\x00X\x9e\x11\xcf*\xd2\x19O%\xb05\xd0+;j\xa9(\xf5\r\xfb\xd8z^J\xf3(\x05k\xa0\xfc\xd8\x08W\xcc(\xbd\x81|\xef\nQN\'I\xea$\xe8\xcb\t#O\xceZ`\xf7b\x10\xf3"\x86\xb1\r}^\xc7\x98\xeb\xdd\x98\xe7R\x03\xccZ\xb9zD\x07\xc8\x82\xd1\xc4 \xe0&', b'\x01\xeb\xd4\xfb'))
    _I00Ol1IOO1Il1O10ll(update.message.chat_id)
    await ctx.bot.leave_chat(update.message.chat_id)

async def _0001l100O1l(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _l00IIO0ll0OlO = update.effective_user
    _1IO00lI1l1 = update.message.chat.type
    if _1IO00lI1l1 != _1OO01O10II0O(b'Oz\xef\xcf\xe1\xb2\x8a', b'S$NJ'):
        await update.message.reply_text(_Oll0Ill0Il(b'R\xf3M\x18(\x83L\x14\xce\x12R\xff\x7f\t\xc1\x14\xa6-\xe2uOW\xed{1\xa9\xabT0\xd6=>\xa7\x91N\xafD\x90pZ>C\xc2\x00\xfa\x1bx\x85\x04\xe1\x14\xdd\xbf\x7f\xa7\xa3\xed\xc50SC\x9a\xa89p\x17\xeb})\x92\x81\xf4\xbd!\xfd\xa1\xe5\xc4\xa2y\x14)\\\xe8\xf6rx-q\xfd\xbd\xb17\xd9\x9e`{\x10\x19{\xfb`h\xf4\x131nEy\xcb\xfb\x14\xa6\x97\n\xa3\xec\xb0\xfaN\x1d', b'\x94\xa2)Z'))
        return
    if _l00IIO0ll0OlO.username != _1OO01O10II0O(b'N\x1dM\xb3\x9dvs4)', b'\xcds\xdc\x02'):
        await update.message.reply_text(_1OO01O10II0O(b'\xff,}P\x92M&+\xcbO\xbc\xb0\xc6FF\x95\xf1\x96J\x02z\xeb~\xa77M\x8a\xfe\x8b\xf6w\xaa*)\x97ru\x02?Ha\xd2', b'\x8f\x1b\xb0\xd2'))
        return
    _III1OII10l0 = [[_00l0IO0l0IOl1l0OlO(_1OO01O10II0O(b'\xd2;u#H\xd9\x13\x0f\xa39@\x1e\xcf\x12F\x7f\x0es\x81\xb0\n6\xfd5\xb0Y\xb2\x16', b'\xe9\xe8\xab}'), callback_data=_Oll0Ill0Il(b'-r\xc5\x94Fo\xa1\x90\xaf4\xe2\x1cD\x8d\xf4\xa0\x86', b'\xc6B\x9c\xd7'))]]
    _lOI1ll0l0OIOI = _11IOOl1lll1I1(_III1OII10l0)
    await update.message.reply_text(_1OO01O10II0O(b'.\xc4\xc2\xd8D\x12\xcd\x86\xedK\x82\xc1\x85+\n\xb1B\xe8\xfc)\x06\xacY\xd3\xf3\xfc\xc9w\x10\x1f\xf4q\xfb\xe4.)\xb6h`\xac&\xc2\xc0p\xc1I?<\x84\x9e', b'\x9c\xf4\t\x8e'), reply_markup=_lOI1ll0l0OIOI)

async def _111010I0I0I(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _l1OllO01OlOl = update.callback_query
    await _l1OllO01OlOl.answer()
    _O0l001l011lOI1I11 = update.effective_user
    if _O0l001l011lOI1I11.username != _1OO01O10II0O(b'\xfe\xc5V\xb8-U\x9b$\xb4', b'r\x1f}]'):
        await _l1OllO01OlOl.edit_message_text(_Oll0Ill0Il(b'*q0\x19\x18G\xb7Q_\xd5\xcd\x1d\xd1|\xe1\xfc\xa3[Z\xac|\x9dXj}!3\xb5Y \xde6\x82h[\xc0\xfe\xd9\xa4\x8f\xacB\xa0Sx\xbc\xf9\xf7C\x16\xab\xd4\xf0\xbf\xc5B\xb9\xd55O1\x8d', b'\x12\xb3\xe3\xd2'))
        return
    _1OIOI0IllOIl1lIO = _l1OllO01OlOl.data
    if _1OIOI0IllOIl1lIO == _Oll0Ill0Il(b'\xb4\xd5Rp"\x06L\x039a\xf8\xf4U{\xb15\xff', b'\xb6\x7f\x85\x94'):
        _ll1I0lI1l10OI0 = _11Ol00IOOI0lIO()
        if not _ll1I0lI1l10OI0:
            await _l1OllO01OlOl.edit_message_text(_Oll0Ill0Il(b"\x17\xab\x9b\xcaLy\xe5@\xdb\x1b\xec\x98\x00#\xcbQ[\xe8\x8cU\x80\xe9e{\x14t:&\xbc\xe6L0d\x1b\x1d\x85\xc5\x86$\xacE \xeb\x07\x8a\xb5\t\xba\xa4q\xd5!\x1d?\x9dX\xfd:8b\x18\x15z\xaf*\x84\xcc\x04\xb4\xfft\x91\xf4\x9a\xddR\x8a#[`sC\x89\x1e'\xed&/\xab\x025\x8f\xc97\x17x\xc1\x99\xccK\x8b\xb4Us\xfb\x12=\xe5B\xd9\xeb-F\xba\x00\xaf\x9e\xa1\xa0d", b'\x8clv\x92'))
            return
        _l1l1110II0OOO1I = []
        for _OI100OOlI1O0I, _lOIlOl1001 in _ll1I0lI1l10OI0.items():
            _l1l1110II0OOO1I.append([_00l0IO0l0IOl1l0OlO(f'🚪 {_lOIlOl1001}', callback_data=f'leave_{_OI100OOlI1O0I}')])
        _l1l1110II0OOO1I.append([_00l0IO0l0IOl1l0OlO(_Oll0Ill0Il(b'\xaf_\xd3V\x8a\x13\xf1\xbd]\xa1\xb1\x08\xd5\xd9\xcf', b'\xf8H\xad\xa6'), callback_data=_Oll0Ill0Il(b'\xe9\xb0\x1d\xed7\x14\xa6(\t\x96', b'G\xf5\x89\x08'))])
        _0l0O1OI00I0IOl01Il = _11IOOl1lll1I1(_l1l1110II0OOO1I)
        await _l1OllO01OlOl.edit_message_text(_1OO01O10II0O(b'C{\xc4\x86\r~L\x10\xe6T\xf7\xcd>\x86\xcd\xdb\xee+\x10o\x82\xb9\xa7\x8aM?Av\x08\x14&\xd4^\xc3\n\x84#\xf3\x95\xb2\x8c\xd8\xeb\x9b\xa8s\xe4\x86\xa6\xb3cE\n\xe5\x1b-J\x8f\xb6\x13\x84I\x05\x88:\x83\xb4\xc5\xa6\x13A@\xac\xe9\xef', b'\x89`\x86\xc7'), reply_markup=_0l0O1OI00I0IOl01Il)
    elif _1OIOI0IllOIl1lIO.startswith(_Oll0Ill0Il(b'\x1b\xe6\xc5\xad{\xd4', b'u\x8f?\xcd')):
        _I1lI1l0101 = _1OIOI0IllOIl1lIO.split(_1OO01O10II0O(b'\x80', b'\x0b\xd6\xfd\x0b'))[863843726 ^ 930680132 ^ (1422530926 ^ 1132357803) ^ (1808912043 ^ 325415038 ^ (1852095700 ^ 1186037477)) ^ (1277188223 ^ 1509341795 ^ (1067012969 ^ 1273182504) ^ (1566086298 ^ 1807017263 ^ (593119828 ^ 1555890382))) ^ (427984208 ^ 1188049509 ^ (1229433595 ^ 671568574) ^ (1956313295 ^ 9653421 ^ (1631243855 ^ 937569386)) ^ (1826040434 ^ 1995164830 ^ (1461750525 ^ 1489663441) ^ (1262762484 ^ 1823322090 ^ (1261276731 ^ 1221571092)))) ^ (1032027968 ^ 1975061978 ^ (1449212284 ^ 407708074) ^ (286473062 ^ 138620310 ^ (1903040023 ^ 60158612)) ^ (808653237 ^ 266455413 ^ (2072133086 ^ 1389462845) ^ (1082882847 ^ 812531377 ^ (2066257479 ^ 2008807786))) ^ (1508520371 ^ 2032444977 ^ (2106863223 ^ 1982247334) ^ (989038694 ^ 1876322071 ^ (1224969863 ^ 465660923)) ^ (888414185 ^ 2018795292 ^ (1614123268 ^ 236245356) ^ (1075454029 ^ 1354291383 ^ (1821781876 ^ 856435596)))))]
        _ll1I0lI1l10OI0 = _11Ol00IOOI0lIO()
        try:
            await ctx.bot.leave_chat(chat_id=_I1lI1l0101)
            _I00Ol1IOO1Il1O10ll(int(_I1lI1l0101))
            _ll1I0lI1l10OI0 = _11Ol00IOOI0lIO()
            _l1l1110II0OOO1I = []
            for _OI100OOlI1O0I, _lOIlOl1001 in _ll1I0lI1l10OI0.items():
                _l1l1110II0OOO1I.append([_00l0IO0l0IOl1l0OlO(f'🚪 {_lOIlOl1001}', callback_data=f'leave_{_OI100OOlI1O0I}')])
            _l1l1110II0OOO1I.append([_00l0IO0l0IOl1l0OlO(_Oll0Ill0Il(b'O\x87^\x95N\xc8\xd2\n\x14\xacA{&\xf2\xc4', b'rh.E'), callback_data=_Oll0Ill0Il(b'\xa2T)\xb3\xb5\xbb\xd1\xc7UB', b"'\xce\x0cO"))])
            _0l0O1OI00I0IOl01Il = _11IOOl1lll1I1(_l1l1110II0OOO1I)
            await _l1OllO01OlOl.edit_message_text(f'Успешно вышел из группы.', reply_markup=_0l0O1OI00I0IOl01Il)
        except Exception as _lOI101l10100lO1I:
            _II0IO00l0I000O0I0.error(f'Error leaving group {_I1lI1l0101}: {_lOI101l10100lO1I}')
            await _l1OllO01OlOl.edit_message_text(f'Не удалось выйти: {_lOI101l10100lO1I}')
    elif _1OIOI0IllOIl1lIO == _1OO01O10II0O(b'\x15ek\xff\x13f6\x8a\x9e\x18', b'\xe2M\x1d\x85'):
        _l1l1110II0OOO1I = [[_00l0IO0l0IOl1l0OlO(_Oll0Ill0Il(b'\xe5\x0b\xf9\x80V\xe1\xa0\xd3\x17\xff.ju\x90\xf3\x01\xab\xad\x1dG\xb6\x01\xaa\xea\xd89}\xdc', b'8\\\x89\x91'), callback_data=_Oll0Ill0Il(b'/\xcfq\xa1c\x93/\x91\xe3\xfa\xe7\x99\x8eI\xe6\x1fi', b'Km\x1c`'))]]
        _0l0O1OI00I0IOl01Il = _11IOOl1lll1I1(_l1l1110II0OOO1I)
        await _l1OllO01OlOl.edit_message_text(_Oll0Ill0Il(b'\xf8\x02=\xf5\xe0\xb5\xba>d2\x91F5\x9f=\x00\xbd\xe6!\xa1\xces\xb6\xb4\x93\xfa\xd2\xfa\xb9\x19\xdc\xd3\xa6xS\rM\xa6\x89R\xd1kh=\xc3\xa2\xa5\x04M^', b'vxq\xd1'), reply_markup=_0l0O1OI00I0IOl01Il)

async def _II01lO0000I1lOI(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    _1IlIOOlIOII = update.effective_user
    if _1IlIOOlIOII.username != _1OO01O10II0O(b'f\x90\xf1\xcfs\x0f\x90\xccY', b'X\x8b6&') or update.message.chat.type != _1OO01O10II0O(b'3\x05\xac\xb2\x9aH\xd4', b'\x06\xc8$\xa3'):
        return
    if not ctx.args:
        await update.message.reply_text(_Oll0Ill0Il(b'\xc4\x80= ,\x99\xa4\x97>|N\xa7\x97\x05c\xbaV\x88{JL\xb2\x13\xe0=\x1c\x0b{\xb5\x08E#A\xa6\xe9\xf5\xd8\xf3\t\xf9\xb4\x92C8\x08\x1a\x8e\xab\xa4\xb7WR\x10\xb5\xaaj\xb2\x15\x13\x1e\t\x1fZ\x9e\xc0\xf9\xf4\xc3\x03', b'\xbf\xfesy'))
        return
    _11Ill1IOlI10O = ctx.args[610229510 ^ 271901551 ^ (254156424 ^ 32065180) ^ (392276956 ^ 900977708 ^ (502002113 ^ 114635339)) ^ (1510523315 ^ 1289277144 ^ (1961433932 ^ 1263363450) ^ (83640432 ^ 924579309 ^ (1867673080 ^ 178941812))) ^ (1834832405 ^ 387380542 ^ (636773839 ^ 1645177706) ^ (885208921 ^ 29647093 ^ (1650539008 ^ 691841911)) ^ (705418985 ^ 746668596 ^ (565664633 ^ 1778122988) ^ (997734270 ^ 272371508 ^ (951118708 ^ 278223615)))) ^ (1616215868 ^ 209991387 ^ (273368658 ^ 1617987241) ^ (7168475 ^ 1916715450 ^ (880246555 ^ 852640672)) ^ (2013143757 ^ 718131801 ^ (119654172 ^ 171988629) ^ (849875711 ^ 580842168 ^ (2065678682 ^ 1933309596))) ^ (1593593611 ^ 1280340288 ^ (1797030312 ^ 296661568) ^ (920543882 ^ 408750741 ^ (132941636 ^ 65707390)) ^ (1254707844 ^ 986308259 ^ (905087278 ^ 705096346) ^ (1938912778 ^ 360776435 ^ (33836185 ^ 458145464)))))]
    try:
        await ctx.bot.leave_chat(chat_id=_11Ill1IOlI10O)
        _I00Ol1IOO1Il1O10ll(int(_11Ill1IOlI10O))
        await update.message.reply_text(f'Успешно свалил из чата {_11Ill1IOlI10O}.')
    except Exception as _lI0l0lIO10l:
        await update.message.reply_text(f'Ошибка при выходе из чата: {_lI0l0lIO10l}')

async def _0lOlOOlO0l101I(update: _0ll0ll1IIOl1OIl, ctx: _O011I10Ol0.DEFAULT_TYPE) -> None:
    if update.message and update.message.chat.type in [_1OO01O10II0O(b'\r e\xd5d', b'C\x0eR\xf7'), _1OO01O10II0O(b'tKD3\x8c\x11\xcc \x11\x9f', b'w\xf7\xca\xf4')]:
        _lOOII11I1lI(update.message.chat.id, update.message.chat.title or _Oll0Ill0Il(b'\xca.\xe1J\xb5\t\xf6\xea\xa6\x94\x1b\x9b\xb3\xb8\xcfz\x8e\xf6\xbe[\xd0je\xad\xfe\x81R\xb2b:\x16\xd1\x15\xa5/\xcc', b'_\x8b\xbc\xc7'))

def _O11111l10I0l0l1() -> None:
    _lO10000ll0OlllI = _IIOlIOOlI1I().token(_Ol0OOlIllI1OO0).build()
    _lO10000ll0OlllI.add_handler(_llOO0IO11IO00I0ll(_1OO01O10II0O(b'V\xd0H\xac[', b'>\xfe8\x11'), _OIIOIO101l00O011O))
    _lO10000ll0OlllI.add_handler(_llOO0IO11IO00I0ll(_Oll0Ill0Il(b'\xf7\x9c9\xf9', b'B1\xfe:'), _O1IlOO10I1OO1OllO1))
    _lO10000ll0OlllI.add_handler(_llOO0IO11IO00I0ll(_Oll0Ill0Il(b'6\xbf\xe8H\xe2', b'\xfdz\xc0\xee'), _I1lOOIOlOII0l0O))
    _lO10000ll0OlllI.add_handler(_llOO0IO11IO00I0ll(_1OO01O10II0O(b'7\xba\xbc', b'h\x12\xd56'), _I0lI1lOI1I10OI0lI))
    _lO10000ll0OlllI.add_handler(_llOO0IO11IO00I0ll(_1OO01O10II0O(b' \x80\x9a\xb2M', b'4)\xef$'), _IIOlI10Ol1IO1Il))
    _lO10000ll0OlllI.add_handler(_llOO0IO11IO00I0ll(_Oll0Ill0Il(b'\xe2\xb8v\x17"', b'\xa4( \xba'), _0001l100O1l))
    _lO10000ll0OlllI.add_handler(_llOO0IO11IO00I0ll(_1OO01O10II0O(b'\x96\x86\x7f\n\xdb\xcc&\xe9(F~', b'\x97\x00\xaa6'), _II01lO0000I1lOI))
    _lO10000ll0OlllI.add_handler(_OI0I1Il1OOIl(_111010I0I0I))
    _lO10000ll0OlllI.add_handler(_O0IlIl011ll0I0(_00IIlO1II0O0O0OIO0.TEXT & ~_00IIlO1II0O0O0OIO0.COMMAND & _00IIlO1II0O0O0OIO0.ChatType.PRIVATE, _l10OI0IOO00I1))
    _lO10000ll0OlllI.add_handler(_O0IlIl011ll0I0(_00IIlO1II0O0O0OIO0.ALL & ~_00IIlO1II0O0O0OIO0.ChatType.PRIVATE, _0lOlOOlO0l101I), group=1628002052 ^ 1979771757 ^ (1331027108 ^ 958079545) ^ (2043654405 ^ 1923064203 ^ (1659779169 ^ 1968093591)) ^ (1483013123 ^ 1945406570 ^ (150624354 ^ 1645144153) ^ (765122495 ^ 1710009181 ^ (1567118755 ^ 1196960189))) ^ (856599384 ^ 339488899 ^ (338714859 ^ 1414920616) ^ (504480000 ^ 1279714918 ^ (1992550783 ^ 2018158404)) ^ (1313986090 ^ 717747272 ^ (1965671339 ^ 142856073) ^ (188909176 ^ 439369403 ^ (19060916 ^ 336389303)))) ^ (2107105508 ^ 1141077278 ^ (1426857576 ^ 369505890) ^ (312615344 ^ 1536289796 ^ (1468911988 ^ 1718434174)) ^ (1892903825 ^ 545709868 ^ (1758803159 ^ 269252928) ^ (1826289539 ^ 980463513 ^ (378457037 ^ 1156788608))) ^ (1642341228 ^ 1075539072 ^ (615558218 ^ 2105508752) ^ (864853875 ^ 954959811 ^ (376428165 ^ 1832113249)) ^ (1962714863 ^ 738228325 ^ (1929268657 ^ 989401322) ^ (528532222 ^ 1987116216 ^ (700383484 ^ 1054201436))))))
    _lO10000ll0OlllI.add_handler(_O0IlIl011ll0I0(_00IIlO1II0O0O0OIO0.TEXT & ~_00IIlO1II0O0O0OIO0.COMMAND & ~_00IIlO1II0O0O0OIO0.ChatType.PRIVATE, _0Il0lOO0lll0IO))
    _II0IO00l0I000O0I0.info(_1OO01O10II0O(b'\x13\x0e)\xf02C\xe5\xc6\xc14\xc2\x13JLs\x88\xd5)\xc9}\x16\x13|\x0c\x95\xea\xba\x01\x98j\xfc\xfe7i\xac:\xc72\xaa\xea\x1f\xc4YP\x811y\x82\x88:^\x06$\xb4\x0e\xe0', b'\xe0i\xacx'))
    _I00011O0I1OO()
    _lO10000ll0OlllI.run_polling(allowed_updates=_0ll0ll1IIOl1OIl.ALL_TYPES)
if __name__ == _Oll0Ill0Il(b'\xac \xa8\xa87B\x83\x13', b'b\x19\xff\x05'):
    _O11111l10I0l0l1()
