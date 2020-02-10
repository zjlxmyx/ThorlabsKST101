import ctypes
import os
from ctypes import wintypes

os.environ['path'] += ';C:\Program Files\Thorlabs\Kinesis'
lib = ctypes.cdll.LoadLibrary(r'C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.KCube.StepperMotor.dll')



class Motor:

    # SN is a string
    def __init__(self, SN):
        self.SN = ctypes.c_char_p(bytes(SN, 'utf-8'))
        self.Acce_c = ctypes.c_int(0)
        self.MaxV_c = ctypes.c_int(0)
        self.Acce = 0
        self.MaxV = 0
        self.JogAcce_c = ctypes.c_int(0)
        self.JogMaxV_c = ctypes.c_int(0)
        self.JogAcce = 0
        self.JogMaxV = 0
        self.JogMode_c = ctypes.c_int(0)
        self.StopMode_c = ctypes.c_int(0)
        self.JogMode = 0
        self.StopMode = 0

    # Connect to motor.
    # Returns the error code (see Error Codes) or zero if successful.
    def connect(self):
        lib.TLI_BuildDeviceList()
        err = lib.SCC_Open(self.SN)
        if err:
            print("open device failed with error code ", err)
            return

    # Starts the internal polling loop which continuously requests position and status.
    # Returns true if successful, false if not.
    def start_polling(self, ms):
        err = lib.SCC_StartPolling(self.SN, ms)
        if not err:
            print("start polling failed with error code ", err)

    # Stop the internal polling loop.
    # Returns true if successful, false if not.
    def stop_polling(self):
        err = lib.SCC_StopPolling(self.SN)
        if not err:
            print("stop polling failed with error code ", err)

    # Home the device.
    # Returns the error code (see Error Codes) or zero if move successfully started.
    def home(self):
        err = lib.SCC_Home(self.SN)
        if err:
            print("Home failed with error code ", err)
            return

    # Sets the move velocity parameters.
    # Returns the error code (see Error Codes) or zero if successful.
    def set_vel_params(self, Acce, MaxV):
        err = lib.SCC_SetVelParams(self.SN, Acce, MaxV)
        if err:
            print("set velocity failed with error code ", err)
            return

    # Gets the move velocity parameters.
    # Returns the Acceleration and MaxVelocity
    def get_vel_params(self):
        err = lib.SCC_GetVelParams(self.SN, ctypes.byref(self.Acce_c), ctypes.byref(self.MaxV_c))
        if err:
            print("get velocity failed with error code ", err)
            return
        self.Acce = self.Acce_c.value
        self.MaxV = self.MaxV_c.value
        return self.Acce, self.MaxV

    # Sets jog velocity parameters.
    # Returns The error code (see Error Codes) or zero if successful.
    def set_jog_vel_params(self, JogAcce, JogMaxV):
        err = lib.SCC_SetJogVelParams(self.SN, JogAcce, JogMaxV)
        if err:
            print("set Jog velocity failed with error code ", err)
            return

    # Gets the jog velocity parameters.
    # Returns the Acceleration and MaxVelocity
    def get_jog_vel_params(self):
        err = lib.SCC_GetJogVelParams(self.SN, ctypes.byref(self.JogAcce_c), ctypes.byref(self.JogMaxV_c))
        if err:
            print("get Jog velocity failed with error code ", err)
            return
        self.JogAcce = self.JogAcce_c.value
        self.JogMaxV = self.JogMaxV_c.value
        return self.JogAcce, self.JogMaxV

    # Sets the jog mode.
    # jogmode: Jog step 1 ,Continuous 2 ; stopmode: Immediate Stop 1 ,Profiled Stop 2
    # Returns The error code (see Error Codes) or zero if successful.
    def set_jog_mode(self, jogmode, stopmode):
        err = lib.SCC_SetJogMode(self.SN, jogmode, stopmode)
        if err:
            print("set Jog mode failed with error code ", err)
            return

    # Gets the jog mode.
    def get_jog_mode(self):
        err = lib.SCC_GetJogMode(self.SN, ctypes.byref(self.JogMode_c), ctypes.byref(self.StopMode_c))
        if err:
            print("get Jog mode failed with error code ", err)
            return
        self.JogMode = self.JogMode_c.value
        self.StopMode = self.StopMode_c.value
        return self.JogMode, self.StopMode

    # Sets the distance to move on jogging.
    # Returns The error code (see Error Codes) or zero if successful.
    def set_jog_step_size(self, stepsize):
        err = lib.SCC_SetJogStepSize(self.SN, stepsize)
        if err:
            print("set Jog step size failed with error code ", err)
            return

    # Gets the distance to move when jogging.
    # Returns The step in Device Units.
    def get_jog_step_size(self):
        err = lib.SCC_GetJogStepSize(self.SN)
        if err:
            print("get Jog step size failed with error code ", err)
            return

    # Move the device to the specified position (index).
    # Returns the error code (see Error Codes) or zero if move successfully started.
    def move_to_position(self, Position):
        err = lib.SCC_MoveToPosition(self.SN, Position)
        if err:
            print("move to position failed with error code ", err)
            return

    # Start moving at the current velocity in the specified direction.
    # direction: 1 forwards, 2 backwards
    # Returns The error code (see Error Codes) or zero if successful.
    def move_at_velocity(self, direction):
        err = lib.SCC_MoveAtVelocity(self.SN, direction)
        if err:
            print("move at velocity failed with error code ", err)
            return

    # Stop the current move using the current velocity profile.
    # Returns The error code (see Error Codes) or zero if successful.
    def stop_profiled(self):
        err = lib.SCC_StopProfiled(self.SN)
        if err:
            print("stop moving failed with error code ", err)
            return

    # Get the current position.
    # The current position is the last recorded position.
    # The current position is updated either by the polling mechanism or by calling RequestPosition or RequestStatus.
    # Returns The current position in Device Units.
    def get_position(self):
        return lib.SCC_GetPosition(self.SN)

    #check if the motor is moving
    # Returns 1 for moving, 0 for stationary
    def is_moving(self):
        bits = ctypes.wintypes.DWORD(lib.SCC_GetStatusBits(self.SN))
        if ((bits.value >> 4) & 1) or ((bits.value >> 5) & 1):
            return True
        else:
            return False




