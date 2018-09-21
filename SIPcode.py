import pjsua as sip
import sys
import time
def log_cb(level, str, len):
print(str)
#Cll back instance
class Calling_back_account(sip.AccountCallback):
def __init__ (self,account):
sip.AccountCallback.__init__(self, account)
#Clling to URI
class SRCallCallback(sip.CallCallback):
def __init__(self, call):
sip.CallCallback.__init__(self, call)
def Active_state(self):
print("Call is :", self.call.info().state_text),
print("last code :", self.call.info().last_code),
print("(" + self.call.info().last_reason + ")")
#Disconnection
if (self.call.info().state_text == 'DISCONNCTD'):
print 'Press anykey to Unregister.....'
return
try:
#Instance creation
sip_lib = sip.Lib()
sip_lib.init(log_cfg = sip.LogConfig(level=3, callback=log_cb))
#creating Transport Object Instance...
client_IP_address = raw_input('Enter Client IP address :')
transport_socket = sip.TransportConfig()
transport_socket.port = 5060
transport_socket.bound_addr = client_IP_address
print('Binding IP ' + client_IP_address + 'to default port no 5060.....'),
transport_bind =sip_lib.create_transport(sip.TransportType.UDP,transport_socket)
print('OK')
#Starting SIP libraries
sip_lib.start()
sip_lib.set_null_snd_dev()
#Starting Registering Process
r_IP=raw_input("Enter IP address of the Server: ")
r_name=raw_input("Enter Username: ")
r_pwd=raw_input("Enter Password: ")
print 'Setting same display name as user name.....'
r_Dname=r_name
print 'Staring Registration.....'
conf_of_account = sip.AccountConfig(domain = r_IP, username = r_name, password=r_pwd, display =
r_Dname, proxy = 'sip:%s:5060' % r_IP)
conf_of_account.id ="sip:%s" % (r_name)
conf_of_account.reg_uri ='sip:%s:%s' % (r_IP,transport_socket.port)
account_callback = Calling_back_account(conf_of_account)
acc = sip_lib.create_account(conf_of_account,cb=account_callback)
#Setting value to Calling_back_account class
acc.set_callback(account_callback)
print('Status= ',acc.info().reg_status,'(' + acc.info().reg_reason + ')')
time.sleep(5)
print 'Registration is Complete....'
Reg_unreg=raw_input("you want to unregister?...")
if (Reg_unreg=="y"):
acc.set_registration(False)
else:
#Cll
c_ID = raw_input('Enter UID to make call : ')
print 'Calling %s.....' % (c_ID)
s_URI = 'sip:%s@%s:%s' % (c_ID,r_IP,transport_socket.port)
call = acc.make_call(s_URI, SRCallCallback(acc))
#Unreg
input = sys.stdin.readline().rstrip('\r\n')
print 'Unregistering.....'
time.sleep(2)
sip_lib.destroy()
time.sleep(2)
sip_lib= None
sys.exit(1)
#Excpt
except sip.Error, err:
print 'Initializations Error', err
sip_lib.destroy()