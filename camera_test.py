from pyueye import ueye
import numpy
import ctypes
import time
import cv2


hCam = ueye.HIDS(0)             #0: first available camera;  1-254: The camera with the specified camera ID
sInfo = ueye.SENSORINFO()
cInfo = ueye.CAMINFO()
pcImageMemory = ueye.c_mem_p()
MemID = ueye.int()
rectAOI = ueye.IS_RECT()
pitch = ueye.INT()
nBitsPerPixel = ueye.INT(16)    #take 8 bits per pixel for monochrome
m_nColorMode = ueye.INT()		# Y8/RGB16/RGB24/REG32
bytes_per_pixel = ueye.INT()
auto_info = ueye.UEYE_AUTO_INFO()

a = ueye.is_InitCamera(hCam, None)
b = ueye.is_GetCameraInfo(hCam, cInfo)
c = ueye.is_GetSensorInfo(hCam, sInfo)

d = ueye.is_ResetToDefault(hCam)
e = ueye.is_SetDisplayMode(hCam, ueye.IS_SET_DM_DIB)

g = ueye.is_AOI(hCam, ueye.IS_AOI_IMAGE_GET_AOI, rectAOI, ueye.sizeof(rectAOI))
width = rectAOI.s32Width
height = rectAOI.s32Height

h = ueye.is_AllocImageMem(hCam, width, height, nBitsPerPixel, pcImageMemory, MemID)
i = ueye.is_SetImageMem(hCam, pcImageMemory, MemID)
f = ueye.is_SetColorMode(hCam, ueye.IS_CM_MONO12)

ueye.is_CaptureVideo(hCam, ueye.IS_WAIT)

j = ueye.is_InquireImageMem(hCam, pcImageMemory, MemID, width, height, nBitsPerPixel, pitch)




IMAGE_FILE_PARAMS = ueye.IMAGE_FILE_PARAMS(pcImageMemory, MemID)
IMAGE_FILE_PARAMS.nFileType = ueye.IS_IMG_PNG
k = ueye.sizeof(IMAGE_FILE_PARAMS)

nEnable = ctypes.c_int(ueye.IS_AUTOPARAMETER_ENABLE)
state = ctypes.c_int()

m = ueye.is_AutoParameter(hCam, ueye.IS_AES_CMD_SET_ENABLE, nEnable, ueye.sizeof(nEnable))
n = ueye.is_AutoParameter(hCam, ueye.IS_AES_CMD_GET_ENABLE, state, ueye.sizeof(state))

while True:

    data = numpy.ctypeslib.as_array(ctypes.cast(pcImageMemory, ctypes.POINTER(ctypes.c_ubyte)), (height * pitch, ))

    data.dtype = 'uint16'
    # data1 = data.astype('uint8')
    data1 = data/4095*255
    data2 = data1.astype('uint8')
    # mem = ctypes.create_string_buffer(height * pitch)
    # ctypes.memmove(mem, pcImageMemory, height * pitch)
    # data = numpy.frombuffer(mem, dtype=numpy.uint16)
    # data.dtype = 'uint8'

    frame = numpy.reshape(data2, (height.value, width.value))

    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow("SimpleLive_Python_uEye_OpenCV", frame)

    ueye.is_GetAutoInfo(hCam, auto_info)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) == ord('s'):
        print('s')
        ueye.is_ImageFile(hCam, ueye.IS_IMAGE_FILE_CMD_SAVE, IMAGE_FILE_PARAMS, k)



ueye.is_FreeImageMem(hCam, pcImageMemory, MemID)
ueye.is_ExitCamera(hCam)