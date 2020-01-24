import win32api as wapi
import win32con as wcon
def key_check():
    keys = []
    if wapi.GetAsyncKeyState(wcon.VK_UP):
        keys.append('jump')
    if wapi.GetAsyncKeyState(wcon.VK_DOWN):
        keys.append('dump')
    if wapi.GetAsyncKeyState(wcon.VK_SPACE):
        keys.append('space')
    return keys