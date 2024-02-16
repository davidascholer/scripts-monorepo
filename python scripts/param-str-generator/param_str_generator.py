# import time
# import base64
# import hmac

# pw1 = "suKRw2tReu6KOfv9rsXKhaoYEh2bDRm/CbEATWpxPJ0="
# pw2 ="GjeiAG608tsJsQBNanE8nQ=="
# system_id = "CB8A640000ED0418"
# expire_ts = str(
#     int(
#         round(
#             (time.time()+15*60)*1000)))
# guest_key = "iNqHxQJQizYYWJtdgQb+qt/hIDUhWNZ52tjgpGHeruE=".encode('utf-8')
# print("time: "+expire_ts)
# param_str = pw1 + '.' + pw2 + '.' + system_id + '.' + expire_ts
# b = bytes(param_str, 'utf-8')
# encoded_param_str = base64.b64encode(b)
# verify = hmac.new(guest_key, msg=param_str.encode('utf-8'), digestmod='SHA256')
# ret = verify.digest()
# encoded_verify = base64.b64encode(ret)
# print(encoded_param_str.decode("utf-8") + '.' + encoded_verify.decode("utf-8"))




import time
import base64
from base64 import urlsafe_b64encode
from base64 import urlsafe_b64decode
import hmac

# # Vars/Params
# pw1 = "suKRw2tReu6KOfv9rsXKhaoYEh2bDRm/CbEATWpxPJ0="
# pw2 ="GjeiAG608tsJsQBNanE8nQ=="
# system_id = "CB8A640000ED0418"
# guest_key = "iNqHxQJQizYYWJtdgQb+qt/hIDUhWNZ52tjgpGHeruE=".encode('utf-8')
# # Expiration generation.
# expire_ts = str(
#     int(
#         round(
#             (time.time()+15*60)*1000)))

# print(expire_ts)#1686001195409

# # Create the bluetooth param string formatted for Alfred to check.
# param_str = pw1 + '.' + pw2 + '.' + system_id + '.' + expire_ts

# # Encode
# b = bytes(param_str, 'utf-8')
# encoded_param_str = base64.urlsafe_b64encode(b)

# # Generate
# verify = hmac.new(guest_key, msg=param_str.encode('utf-8'), digestmod='SHA256')
# ret = verify.digest()
# encoded_verify = base64.urlsafe_b64encode(ret).rstrip(b"=")
# print(encoded_param_str.decode("utf-8") + '.' + encoded_verify.decode("utf-8"))
#c3VLUncydFJldTZLT2Z2OXJzWEtoYW9ZRWgyYkRSbS9DYkVBVFdweFBKMD0uR2plaUFHNjA4dHNKc1FCTmFuRThuUT09LkNCOEE2NDAwMDBFRDA0MTguMTY4NjAwMTE5NTQwOQ==.MlvGzLnh-AKHijQ1_tmWT8EAcqE0fhzYuPxHT9mLWRs=



def generateParamStr(pw1, pw2, systemID, guestKey):

    # expire_ts = str(
    # int(
    #     round(
    #         (time.time()+15*60)*1000)))
    # print(expire_ts)

    expire_ts = '1686070354348'

    paramStr = pw1 + '.' + pw2 + '.' + systemID + '.' + expire_ts
    b = bytes(paramStr, 'utf-8')  # 将s的类型转化为bytes类型
    encoded_paramStr = base64.urlsafe_b64encode(b)  # base64加密

    verify = hmac.new(str.encode(guestKey), msg=paramStr.encode('utf-8'), digestmod='SHA256')
    ret = verify.digest()
    encoded_verify = base64.urlsafe_b64encode(ret).rstrip(b"=")
    print(encoded_paramStr.decode("utf-8") + '.' + encoded_verify.decode("utf-8"))
    return encoded_paramStr.decode("utf-8") + '.' + encoded_verify.decode("utf-8")


generateParamStr("suKRw2tReu6KOfv9rsXKhaoYEh2bDRm/CbEATWpxPJ0=","GjeiAG608tsJsQBNanE8nQ==","CB8A640000ED0418","iNqHxQJQizYYWJtdgQb+qt/hIDUhWNZ52tjgpGHeruE=")
