import ctypes,os,time

os.environ['path'] += ';C:\Program Files\Thorlabs\Kinesis'
lib = ctypes.cdll.LoadLibrary('D:\Masterarbeit\Thorlabs.MotionControl.KCube.StepperMotor.dll')


SN_Y = ctypes.c_char_p(bytes('26000306', 'utf-8'))

# a = lib.TLI_BuildDeviceList()
# b = lib.TLI_GetDeviceListSize()

c = lib.SCC_Open(SN_Y)
time.sleep(0.5)
# lib.SCC_SetVelParams(SN_Y,10000,1000000)
s = lib.SCC_StartPolling(SN_Y,200)
# d = lib.SCC_Home(SN_Y)
# time.sleep(2)
# s = lib.SCC_MoveToPosition(SN_Y,37546)
# time.sleep(0.5)
# f = lib.SCC_RequestStatusBits(SN_Y)
# while 1:
#     g11 = ctypes.wintypes.DWORD(lib.SCC_GetStatusBits(SN_Y))
#     g12 = hex(g11.value)
#     print(g12)
#     time.sleep(0.2)

# s = lib.SCC_StopPolling(SN_Y)
time.sleep(0.5)

Acce = ctypes.c_short()
MaxV = ctypes.c_short()

k = lib.SCC_GetMotorTravelLimits(SN_Y,ctypes.byref(Acce),ctypes.byref(MaxV))

# g = ctypes.c_long(lib.SCC_GetJogStepSize(SN_Y))

# while 1:
#     p = lib.SCC_GetPosition(SN_Y)
#     time.sleep(0.2)
#     print(p)


h = ctypes.c_short(lib.SCC_GetStageAxisMaxPos(SN_Y))
i = ctypes.c_short(lib.SCC_GetStageAxisMinPos(SN_Y))
a=1


