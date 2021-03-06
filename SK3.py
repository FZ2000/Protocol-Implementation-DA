# -*- generated by 1.0.12 -*-
import da
PatternExpr_209 = da.pat.TuplePattern([da.pat.ConstantPattern('m1'), da.pat.FreePattern('A'), da.pat.FreePattern('B')])
PatternExpr_218 = da.pat.FreePattern('A')
PatternExpr_311 = da.pat.TuplePattern([da.pat.ConstantPattern('m2'), da.pat.FreePattern('Pab'), da.pat.FreePattern('enc_SA')])
PatternExpr_320 = da.pat.FreePattern('S')
PatternExpr_354 = da.pat.TuplePattern([da.pat.ConstantPattern('m4'), da.pat.FreePattern('Na'), da.pat.FreePattern('enc_CA')])
PatternExpr_363 = da.pat.FreePattern('Ca')
PatternExpr_406 = da.pat.TuplePattern([da.pat.ConstantPattern('m8'), da.pat.FreePattern('Nb'), da.pat.FreePattern('enc_AV')])
PatternExpr_415 = da.pat.FreePattern('B')
PatternExpr_455 = da.pat.TuplePattern([da.pat.ConstantPattern('m10'), da.pat.FreePattern('enc_SK'), da.pat.FreePattern('enc_BVA')])
PatternExpr_464 = da.pat.FreePattern('Ca')
PatternExpr_519 = da.pat.TuplePattern([da.pat.ConstantPattern('m5'), da.pat.FreePattern('A'), da.pat.FreePattern('Na')])
PatternExpr_528 = da.pat.FreePattern('A')
PatternExpr_548 = da.pat.TuplePattern([da.pat.ConstantPattern('m7'), da.pat.FreePattern('Nb'), da.pat.FreePattern('enc_SK'), da.pat.FreePattern('enc_AV'), da.pat.FreePattern('enc_BV')])
PatternExpr_561 = da.pat.FreePattern('Cb')
PatternExpr_598 = da.pat.TuplePattern([da.pat.ConstantPattern('m11'), da.pat.FreePattern('enc_BVA')])
PatternExpr_605 = da.pat.FreePattern('Cb')
PatternExpr_651 = da.pat.TuplePattern([da.pat.ConstantPattern('m3'), da.pat.FreePattern('A')])
PatternExpr_658 = da.pat.FreePattern('A')
PatternExpr_695 = da.pat.TuplePattern([da.pat.ConstantPattern('m9'), da.pat.FreePattern('B'), da.pat.FreePattern('Na'), da.pat.FreePattern('Nb'), da.pat.FreePattern('Pab'), da.pat.FreePattern('enc_SA'), da.pat.FreePattern('enc_AV'), da.pat.BoundPattern('_BoundPattern709_')])
PatternExpr_712 = da.pat.FreePattern('A')
PatternExpr_840 = da.pat.TuplePattern([da.pat.ConstantPattern('m6'), da.pat.FreePattern('A'), da.pat.FreePattern('Na')])
PatternExpr_849 = da.pat.FreePattern('B')
_config_object = {}
from sa.secalgo import *
configure(sym_cipher='DES')

def bxor(b1, b2):
    result = b''
    for (b1, b2) in zip(b1, b2):
        result += bytes([(b1 ^ b2)])
    return result

class RoleS(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_RoleSReceivedEvent_0', PatternExpr_209, sources=[PatternExpr_218], destinations=None, timestamps=None, record_history=None, handlers=[self._RoleS_handler_208])])

    def setup(self, Ka, Kb, **rest_1005):
        super().setup(Ka=Ka, Kb=Kb, **rest_1005)
        self._state.Ka = Ka
        self._state.Kb = Kb
        pass

    def run(self):
        super()._label('_st_label_201', block=False)
        _st_label_201 = 0
        self._timer_start()
        while (_st_label_201 == 0):
            _st_label_201 += 1
            if False:
                pass
                _st_label_201 += 1
            elif self._timer_expired:
                pass
                _st_label_201 += 1
            else:
                super()._label('_st_label_201', block=True, timeout=10)
                _st_label_201 -= 1

    def _RoleS_handler_208(self, A, B):
        print('S Receives Message 1(A-->S)')
        enc_Kab = encrypt((A, 0), self._state.Kb)
        Kab = keygen(key_type='DES', block_mode='ECB', key_mat=enc_Kab[:8])
        enc_Pab = encrypt((B, 1), self._state.Ka)
        Pab = bxor(enc_Kab, enc_Pab)
        self.send(('m2', Pab, encrypt((Pab, B, 2), self._state.Ka)), to=A)
        print('S Sends Message 2 (S-->A)')
    _RoleS_handler_208._labels = None
    _RoleS_handler_208._notlabels = None

class RoleA(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._RoleAReceivedEvent_0 = []
        self._RoleAReceivedEvent_1 = []
        self._RoleAReceivedEvent_2 = []
        self._RoleAReceivedEvent_3 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_RoleAReceivedEvent_0', PatternExpr_311, sources=[PatternExpr_320], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_RoleAReceivedEvent_1', PatternExpr_354, sources=[PatternExpr_363], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_RoleAReceivedEvent_2', PatternExpr_406, sources=[PatternExpr_415], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_RoleAReceivedEvent_3', PatternExpr_455, sources=[PatternExpr_464], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, B, S, Ca, Kac, **rest_1005):
        super().setup(B=B, S=S, Ca=Ca, Kac=Kac, **rest_1005)
        self._state.B = B
        self._state.S = S
        self._state.Ca = Ca
        self._state.Kac = Kac
        pass

    def run(self):
        print('Start to run the protocol')
        self.send(('m1', self._id, self._state.B), to=self._state.S)
        print('A Sends Message 1 (A-->S)')
        super()._label('_st_label_308', block=False)
        S = enc_SA = Pab = None

        def ExistentialOpExpr_309():
            nonlocal S, enc_SA, Pab
            for (_, (_, _, self._state.S), (_ConstantPattern330_, Pab, enc_SA)) in self._RoleAReceivedEvent_0:
                if (_ConstantPattern330_ == 'm2'):
                    if True:
                        return True
            return False
        _st_label_308 = 0
        while (_st_label_308 == 0):
            _st_label_308 += 1
            if ExistentialOpExpr_309():
                _st_label_308 += 1
            else:
                super()._label('_st_label_308', block=True)
                _st_label_308 -= 1
        print('A Receives Message 2(S-->A)')
        self.send(('m3', self._id), to=self._state.Ca)
        print('A Sends Message 3 (A-->Ca)')
        super()._label('_st_label_351', block=False)
        enc_CA = Na = Ca = None

        def ExistentialOpExpr_352():
            nonlocal enc_CA, Na, Ca
            for (_, (_, _, self._state.Ca), (_ConstantPattern373_, Na, enc_CA)) in self._RoleAReceivedEvent_1:
                if (_ConstantPattern373_ == 'm4'):
                    if (decrypt(enc_CA, key=self._state.Kac)[0] == Na):
                        return True
            return False
        _st_label_351 = 0
        while (_st_label_351 == 0):
            _st_label_351 += 1
            if ExistentialOpExpr_352():
                _st_label_351 += 1
            else:
                super()._label('_st_label_351', block=True)
                _st_label_351 -= 1
        print('A Receives Message 4(Ca-->A)')
        self.send(('m5', self._id, Na), to=self._state.B)
        print('A Sends Message 5(A-->B)')
        super()._label('_st_label_403', block=False)
        enc_AV = Nb = B = None

        def ExistentialOpExpr_404():
            nonlocal enc_AV, Nb, B
            for (_, (_, _, self._state.B), (_ConstantPattern425_, Nb, enc_AV)) in self._RoleAReceivedEvent_2:
                if (_ConstantPattern425_ == 'm8'):
                    if True:
                        return True
            return False
        _st_label_403 = 0
        while (_st_label_403 == 0):
            _st_label_403 += 1
            if ExistentialOpExpr_404():
                _st_label_403 += 1
            else:
                super()._label('_st_label_403', block=True)
                _st_label_403 -= 1
        print('A Receives Message 8(B-->A)')
        self.send(('m9', self._state.B, Na, Nb, Pab, enc_SA, enc_AV, enc_CA), to=self._state.Ca)
        print('A Sends Message 9(A-->Ca)')
        super()._label('_st_label_452', block=False)
        enc_BVA = enc_SK = Ca = None

        def ExistentialOpExpr_453():
            nonlocal enc_BVA, enc_SK, Ca
            for (_, (_, _, self._state.Ca), (_ConstantPattern474_, enc_SK, enc_BVA)) in self._RoleAReceivedEvent_3:
                if (_ConstantPattern474_ == 'm10'):
                    if True:
                        return True
            return False
        _st_label_452 = 0
        while (_st_label_452 == 0):
            _st_label_452 += 1
            if ExistentialOpExpr_453():
                _st_label_452 += 1
            else:
                super()._label('_st_label_452', block=True)
                _st_label_452 -= 1
        print('A Receives Message 10(Ca-->A)')
        self.send(('m11', enc_BVA), to=self._state.B)
        print('A Sends Message 11(A-->b)')
        print('A - Authorized')

class RoleB(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._RoleBReceivedEvent_1 = []
        self._RoleBReceivedEvent_2 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_RoleBReceivedEvent_0', PatternExpr_519, sources=[PatternExpr_528], destinations=None, timestamps=None, record_history=None, handlers=[self._RoleB_handler_518]), da.pat.EventPattern(da.pat.ReceivedEvent, '_RoleBReceivedEvent_1', PatternExpr_548, sources=[PatternExpr_561], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_RoleBReceivedEvent_2', PatternExpr_598, sources=[PatternExpr_605], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, Cb, Kbc, **rest_1005):
        super().setup(Cb=Cb, Kbc=Kbc, **rest_1005)
        self._state.Cb = Cb
        self._state.Kbc = Kbc
        pass

    def run(self):
        super()._label('_st_label_511', block=False)
        _st_label_511 = 0
        self._timer_start()
        while (_st_label_511 == 0):
            _st_label_511 += 1
            if False:
                pass
                _st_label_511 += 1
            elif self._timer_expired:
                pass
                _st_label_511 += 1
            else:
                super()._label('_st_label_511', block=True, timeout=10)
                _st_label_511 -= 1

    def _RoleB_handler_518(self, A, Na):
        print('B Receives Message 5(A-->B)')
        self.send(('m6', A, Na), to=self._state.Cb)
        print('B Sends Message 5(B-->Cb)')
        super()._label('_st_label_545', block=False)
        enc_BV = Cb = enc_SK = Nb = enc_AV = None

        def ExistentialOpExpr_546():
            nonlocal enc_BV, Cb, enc_SK, Nb, enc_AV
            for (_, (_, _, self._state.Cb), (_ConstantPattern571_, Nb, enc_SK, enc_AV, enc_BV)) in self._RoleBReceivedEvent_1:
                if (_ConstantPattern571_ == 'm7'):
                    if True:
                        return True
            return False
        _st_label_545 = 0
        while (_st_label_545 == 0):
            _st_label_545 += 1
            if ExistentialOpExpr_546():
                _st_label_545 += 1
            else:
                super()._label('_st_label_545', block=True)
                _st_label_545 -= 1
        print('B Receives Message 7(Cb-->B)')
        self.send(('m8', Nb, enc_AV), to=A)
        print('B Sends Message 8(B-->A)')
        super()._label('_st_label_595', block=False)
        Cb = enc_BVA = None

        def ExistentialOpExpr_596():
            nonlocal Cb, enc_BVA
            for (_, (_, _, self._state.Cb), (_ConstantPattern615_, enc_BVA)) in self._RoleBReceivedEvent_2:
                if (_ConstantPattern615_ == 'm11'):
                    if (enc_BVA == enc_BV):
                        return True
            return False
        _st_label_595 = 0
        while (_st_label_595 == 0):
            _st_label_595 += 1
            if ExistentialOpExpr_596():
                _st_label_595 += 1
            else:
                super()._label('_st_label_595', block=True)
                _st_label_595 -= 1
        print('B Receives Message 11(A-->B)')
        print('B - Authorized')
    _RoleB_handler_518._labels = None
    _RoleB_handler_518._notlabels = None

class RoleCa(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._RoleCaReceivedEvent_1 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_RoleCaReceivedEvent_0', PatternExpr_651, sources=[PatternExpr_658], destinations=None, timestamps=None, record_history=None, handlers=[self._RoleCa_handler_650]), da.pat.EventPattern(da.pat.ReceivedEvent, '_RoleCaReceivedEvent_1', PatternExpr_695, sources=[PatternExpr_712], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, Ka, Kac, **rest_1005):
        super().setup(Ka=Ka, Kac=Kac, **rest_1005)
        self._state.Ka = Ka
        self._state.Kac = Kac
        pass

    def run(self):
        super()._label('_st_label_643', block=False)
        _st_label_643 = 0
        self._timer_start()
        while (_st_label_643 == 0):
            _st_label_643 += 1
            if False:
                pass
                _st_label_643 += 1
            elif self._timer_expired:
                pass
                _st_label_643 += 1
            else:
                super()._label('_st_label_643', block=True, timeout=10)
                _st_label_643 -= 1

    def _RoleCa_handler_650(self, A):
        print('Ca Receives Message 3(S-->A)')
        Na = nonce()
        enc_CA = encrypt((Na, 1, 1), self._state.Kac)
        self.send(('m4', Na, enc_CA), to=A)
        print('Ca sends Message 4(Ca-->A)')
        super()._label('_st_label_692', block=False)
        A = enc_SA = enc_AV = Nb = Na = B = Pab = None

        def ExistentialOpExpr_693():
            nonlocal A, enc_SA, enc_AV, Nb, Na, B, Pab
            for (_, (_, _, A), (_ConstantPattern722_, B, Na, Nb, Pab, enc_SA, enc_AV, _BoundPattern730_)) in self._RoleCaReceivedEvent_1:
                if (_ConstantPattern722_ == 'm9'):
                    if (_BoundPattern730_ == enc_CA):
                        if True:
                            return True
            return False
        _st_label_692 = 0
        while (_st_label_692 == 0):
            _st_label_692 += 1
            if ExistentialOpExpr_693():
                _st_label_692 += 1
            else:
                super()._label('_st_label_692', block=True)
                _st_label_692 -= 1
        print('Ca Receives Message 9(A-->Ca)')
        enc_Pab = encrypt((B, 1), self._state.Ka)
        Kab = keygen(key_type='DES', block_mode='ECB', key_mat=bxor(Pab, enc_Pab)[:8])
        if ((decrypt(enc_SA, key=self._state.Ka)[0] == Pab) and (decrypt(enc_SA, key=self._state.Ka)[1] == B) and (decrypt(enc_AV, key=Kab)[0] == Na) and (decrypt(enc_AV, key=Kab)[1] == Nb)):
            self.send(('m10', encrypt((Nb, 0, 0), Kab), encrypt((Nb, 0, 1), Kab)), to=A)
            print('Ca Sends Message 10(Ca-->A)')
    _RoleCa_handler_650._labels = None
    _RoleCa_handler_650._notlabels = None

class RoleCb(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_RoleCbReceivedEvent_0', PatternExpr_840, sources=[PatternExpr_849], destinations=None, timestamps=None, record_history=None, handlers=[self._RoleCb_handler_839])])

    def setup(self, Kb, Kbc, **rest_1005):
        super().setup(Kb=Kb, Kbc=Kbc, **rest_1005)
        self._state.Kb = Kb
        self._state.Kbc = Kbc
        pass

    def run(self):
        super()._label('_st_label_832', block=False)
        _st_label_832 = 0
        self._timer_start()
        while (_st_label_832 == 0):
            _st_label_832 += 1
            if False:
                pass
                _st_label_832 += 1
            elif self._timer_expired:
                pass
                _st_label_832 += 1
            else:
                super()._label('_st_label_832', block=True, timeout=10)
                _st_label_832 -= 1

    def _RoleCb_handler_839(self, A, Na, B):
        print('Cb Receives Message 6(B-->Cb)')
        Nb = nonce()
        enc_Kab = encrypt((A, 0), self._state.Kb)
        Kab = keygen(key_type='DES', block_mode='ECB', key_mat=enc_Kab[:8])
        self.send(('m7', Nb, encrypt((Nb, 0, 0), Kab), encrypt((Na, Nb, 1), Kab), encrypt((Nb, 0, 1), Kab)), to=B)
        print('Cb Sends Message 7(Cb-->B)')
    _RoleCb_handler_839._labels = None
    _RoleCb_handler_839._notlabels = None

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])

    def run(self):
        Ka = keygen('shared', block_mode='ECB')
        Kb = keygen('shared', block_mode='ECB')
        Kac = keygen('shared', block_mode='ECB')
        Kbc = keygen('shared', block_mode='ECB')
        S = self.new(RoleS, (Ka, Kb))
        Ca = self.new(RoleCa, (Ka, Kac))
        Cb = self.new(RoleCb, (Kb, Kbc))
        B = self.new(RoleB, (Cb, Kbc))
        A = self.new(RoleA, (B, S, Ca, Kac))
        self._start(A)
        self._start(B)
        self._start(S)
        self._start(Ca)
        self._start(Cb)
