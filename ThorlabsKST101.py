import ctypes
import os
from ctypes import wintypes

os.environ['path'] += ';C:\Program Files\Thorlabs\Kinesis'
lib = ctypes.cdll.LoadLibrary('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.KCube.StepperMotor.dll')


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
        return lib.SCC_Open(self.SN)

    # Starts the internal polling loop which continuously requests position and status.
    # Returns true if successful, false if not.
    def start_polling(self, ms):
        return lib.SCC_StartPolling(self.SN, ms)

    # Stop the internal polling loop.
    # Returns true if successful, false if not.
    def stop_polling(self):
        return lib.SCC_StopPolling(self.SN)

    # Home the device.
    # Returns the error code (see Error Codes) or zero if move successfully started.
    def home(self):
        return lib.SCC_Home(self.SN)

    # Sets the move velocity parameters.
    # Returns the error code (see Error Codes) or zero if successful.
    def set_vel_params(self, Acce, MaxV):
        return lib.SCC_SetVelParams(self.SN, Acce, MaxV)

    # Gets the move velocity parameters.
    # Returns the Acceleration and MaxVelocity
    def get_vel_params(self):
        lib.SCC_GetVelParams(self.SN, ctypes.byref(self.Acce_c), ctypes.byref(self.MaxV_c))
        self.Acce = self.Acce_c.value
        self.MaxV = self.MaxV_c.value
        return self.Acce, self.MaxV

    # Sets jog velocity parameters.
    # Returns The error code (see Error Codes) or zero if successful.
    def set_jog_vel_params(self, JogAcce, JogMaxV):
        return lib.SCC_SetJogVelParams(self.SN, JogAcce, JogMaxV)

    # Gets the jog velocity parameters.
    # Returns the Acceleration and MaxVelocity
    def get_jog_vel_params(self):
        lib.SCC_GetVelParams(self.SN, ctypes.byref(self.JogAcce_c), ctypes.byref(self.JogMaxV_c))
        self.JogAcce = self.JogAcce_c.value
        self.JogMaxV = self.JogMaxV_c.value
        return self.JogAcce, self.JogMaxV

    # Sets the jog mode.
    # jogmode: Jog step 1 ,Continuous 2 ; stopmode: Immediate Stop 1 ,Profiled Stop 2
    # Returns The error code (see Error Codes) or zero if successful.
    def set_jog_mode(self, jogmode, stopmode):
        return lib.SCC_SetJogMode(self.SN, jogmode, stopmode)

    # Gets the jog mode.
    def get_jog_mode(self):
        lib.SCC_GetJogMode(self.SN, ctypes.byref(self.JogMode_c), ctypes.byref(self.StopMode_c))
        self.JogMode = self.JogMode_c.value
        self.StopMode = self.StopMode_c.value
        return self.JogMode, self.StopMode

    # Sets the distance to move on jogging.
    # Returns The error code (see Error Codes) or zero if successful.
    def set_jog_step_size(self, stepsize):
        return lib.SCC_SetJogStepSize(self.SN, stepsize)

    # Gets the distance to move when jogging.
    # Returns The step in Device Units.
    def get_jog_step_size(self):
        return lib.SCC_GetJogStepSize(self.SN)

    # Move the device to the specified position (index).
    # Returns the error code (see Error Codes) or zero if move successfully started.
    def move_to_position(self, Position):
        return lib.SCC_MoveToPosition(self.SN, Position)

    # Start moving at the current velocity in the specified direction.
    # direction: 1 forwards, 2 backwards
    # Returns The error code (see Error Codes) or zero if successful.
    def move_at_velocity(self, direction):
        return lib.SCC_MoveAtVelocity(self.SN, direction)

    # Stop the current move using the current velocity profile.
    # Returns The error code (see Error Codes) or zero if successful.
    def stop_profiled(self):
        return lib.SCC_StopProfiled(self.SN)

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
            return 1
        else:
            return 0




