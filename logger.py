import time


# Config files
TAMPER_LOG = "My.log"
#msg to put into log
msg="Logged. (You can change this msg at anytime)"


def now_ts():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

def append_my_log(msg):
    try:
        with open(TAMPER_LOG, "a", encoding="utf-8") as fh:
            fh.write(f"{now_ts()} - {msg}\n")
    except Exception:
        pass
append_my_log(msg)
now_ts()
