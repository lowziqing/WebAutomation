from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import *


def main():

    global condition
    condition = True

    from SeleniumScript import SeleniumFunctions
    from SeleniumScript import LoginManager
    from SeleniumScript import TimeManager
    TM = TimeManager.TimeManager()
    sf = SeleniumFunctions.Functions()
    credentials = LoginManager.get_login()

    def execute_schedule():
        day = TM.getDateTime()['currentDay']
        website = TM.checkDays(day)
        global condition
        sf.newBrowser(website)
        condition = True

    def set_false():
        global condition
        condition = False

    def tick():
        print('Tick! The time is: %s' % datetime.now())

    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()

    # schedule = BackgroundScheduler()
    # schedule.add_job(set_false, 'cron', hour=9, minute=16)
    # schedule.add_job(LoginManager.reminder, 'cron', hour=9, minute=16)
    # schedule.add_job(execute_schedule, 'cron', hour=9, minute=18)
    # schedule.start()

    # getting the browser
    sf.getDriver().get("https://infosecindustry.com/alerts-grid/")
    sf.getDriver().maximize_window()
    sf.getDriver().implicitly_wait(15)
    sf.newTab("https://www.fireeye.com/cyber-map/threat-map.html")
    sf.newTab("https://cybermap.kaspersky.com/")

    # # actual code
    # sf.getDriver().set_window_size(2900, 2100)
    # sf.getDriver().get("https://siem.chevron.com")
    # sf.getDriver().implicitly_wait(15)
    # sf.inputs("//input[@type='text']", credentials['username'])
    # sf.inputs("//input[@type='password']", credentials['password'])
    # sf.tabEnter(1)
    #
    # # FirePower Sensor
    # sf.newTab(
    #     "https://hlspsl01.hou150.chevrontexaco.net:8000/en-US/account/login?return_to=%2Fen-US%2Fapp%2Fcvx_security%2Ffireeye_sensor_dashboard#en-US/account/login?return_to=%2Fen-US%2Fapp%2Fcvx_security%2Ffireeye_sensor_dashboard")
    # sf.inputs("//input[@type='text']", credentials['username'])
    # sf.inputs("//input[@type='password']", credentials['password'])
    # sf.tabEnter(1)
    #
    # # FireEye Sensor
    # sf.newTab("https://hlspsl01.hou150.chevrontexaco.net:8000/en-US/app/cvx_security/firesight_sensor_dashboard")
    #
    # # Wildfire Alert
    # sf.newTab("https://hlspsl01.hou150.chevrontexaco.net:8000/en-US/app/cvx_security/wildfire_alerts")
    #
    # # TMG Hunting
    # sf.newTab(
    #     "https://hlspsl01.hou150.chevrontexaco.net:8000/en-US/app/cvx_security/tmg_hunting?form.CAI_Person_token=*&form.dest_host_token=*&form.dest_ip_token=*&form.cs_User_Agent_token=*&form.src_ip_token=*&form.http_content_type_token=*")
    #
    # # Open DNS CnC
    # sf.newTab("https://hlspsl01.hou150.chevrontexaco.net:8000/en-US/app/cvx_security/open_dns_cnc")
    #
    # # infosec industry
    # sf.newTab("https://infosecindustry.com/alerts-grid/")
    #
    # # KasperSky CyberThreat
    # sf.newTab("https://cybermap.kaspersky.com/")

    counter = 0
    while True:
        while condition:
            length = len(sf.getDriver().window_handles)
            sf.getDriver().switch_to.window(sf.getDriver().window_handles[counter])
            sleep(30)
            counter += 1
            if counter >= length:
                counter = 0
        while not condition:
            sleep(10)
            print "doing other stuff"


if __name__ == "__main__":
    main()
