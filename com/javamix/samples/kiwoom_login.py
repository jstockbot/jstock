from pywinauto import application
from pywinauto import timings
import time
import os

app = application.Application()
app.start("C:/KiwoomFlash3/Bin/NKMiniStarter.exe")

title = "번개3 Login"
# dlg = timings.WaitUntilPasses(20, 0.5, lambda : app.windows_(title=title))
# 위 코드를 다음과 같이 변경하자
# dlg = timings.wait_until_passes(20, 0.5, lambda: app.windows(title=title))
dlg = timings.wait_until_passes(20, 0.5, lambda: app.connect(title=title)).Dialog

pass_ctrl = dlg.Edit2
# time.sleep(10)
pass_ctrl.set_focus()
pass_ctrl.type_keys("rud7als1")

cert_ctrl = dlg.Edit3
cert_ctrl.set_focus()
cert_ctrl.type_keys("rudals@5536")

btn_ctrl = dlg.Button0
btn_ctrl.click()

time.sleep(10)
os.system("taskkill /im nkmini.exe")