from ronglian_sms_sdk import SmsSDK

accId = '8aaf070875774c6d0175819b8f4f02ff'
accToken = 'f47258de51bb441bb7d87e36959f64c7'
appId = '8aaf070875774c6d0175819b90450305'


def send_messages(mobile, datas):
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    datas = datas
    print(tid, datas, mobile)
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)
