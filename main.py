from smart_m3.m3_kp_api import *

if __name__ == '__main__':
    kp = m3_kp_api(PrintDebug=True)
    kp.clean_sib()  # remove all data from Smart Space
    kp.leave()
