from pyChatGPT import ChatGPT

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..0I5JzENg-ZAX4NPh.iFEdqZPpaS8m_mJDxHI0yxh5VeDygT7vPw4DnKGTxHGp02lNHFtQjZWBcByUJ9fO6gIcxEI8wzqzcw9HY_DJ--r5F1sVMJoor8rckcecG8oKks3SIIg0Oi7M-d0VbHIDnXVee581xvEawTUL8uA0JxvOzY8PABeDd_BNRjyahBOxkf9N-JFiJXkK2Fx_jLB_xPyWrAT6DShSbeML86vj9Hd6Yi8LBwClQS5wD05gABjd8WryVdgr1VxTtLM_uxk7swgEHjbtfsgQU-9-HkvOzkSoi1T_Ak4QLjAH-5_EuHlzYSYyXUbZL82np45nbFXzwxOTpTn2ATNSgPwVj5khNDn3eUVSk8m5aSrNSkWYHS-8X5yzwEXxkUbJ70C_fC2aPjFv14BeHpwnyr_kqpZua8sXuZZ2jrNR02bEShcTN0vn_5_ZMHZX6sU4i7aKrxSykwHI_anHmP7f7-7GuufoKiydN9N5zQaE-lYJzvfXue6ea-6DQEVGF0_-qYb1S1C2HB-BdJPJrYIs5Y9ANGH9bNvJnw9XYHeMTnI4tHACpRN4_1YLIeaPyurLpT1_36zLoC1XpOUsyLVdmeNJtEnnP_aGsrcxH2MmpFznaMuc7lmQaBvR_kYnKZpp50QhUlWnm86PI5GVREDc0y4ntvZcFpciZDedPtXkZo2z7AVOEwvhrDAyabYwnA3FCM4XBtjCL1S0Ok1XHdQe_WJc8ralBdGshUaJUFzASSZ3r1Xbc5A3zowXzxk_e3Jx9kryqcx5zW8cn1Xo-YT45xxrx-684Tqahr3cGV6Y3PlMQ65rcvr3ebj6mRDhwXtjmi_ctvaT5nXHPJmV3i8AqiQHC_vsnGmbxDJtDx78amHhnz19u7DGXDh1Y0jYiB0UKtoOO9oCLe-PAxCMGAroWERZiTDigRoJpLjx_StlhZiRLoP5JAJH-bXPmUd4RWxX-vZfKE36V0HGDf0Wdi2jReTAyN0PDuYxB5Nz6P73A15WVuKx4hjQJXlA7z8rcRxVYG9ynod6UAW1ATbJdTxAqhnl00CZ94RR33gPYaYs_hKj0rbdwiJxDwChNSONcWjWWgvqt1hCXKT3moSc4JAEaufxvt1COM_ABIR1xqG6tpBkuysX5UXy9oAh6Yq1q1cSsBBVRtjdqhOiaNuNzHW7DJelTpq10I2Bx_yvKQ7XJiZGMAfPR2rSFl4_rwbnxUZ0T7aGqtg9SbEtaLvZYVaEsrMMM73wzkirCmDw-APWSRcgBy5EOot5SWcnH-UE_MwI6OVczkZjHtyLwlKmQmxYQoHQkXUeotIynk0G2rnWA92hrcBQkyo3PGLCJVqVCPgTYl4sPFom28bkqtmKYu4fpkFawJeFSLA6ZjmNgzOMiRNrQsTQz6PnCu-p1Y0HVdfM6fY74Ui4GmVnpJLetS9-0Z5bryCB-i2Ih68e00_3tgseIXROrH75u5alW6Zo-NoUwK3c6wMWwn5ZJvvVvsf8JE0z_1rcIsCfBr0-wswu41Fb7_n7egMzroZJjQ6RCHHjNfb-E3d6Q9HRae2XTudNxeto_6gzFGITdC1EakBC37BoZ-pTPs1XdKx6CG__x5AtVOP4IyHk0Ib-zJGcmJRZG4kDasUfAhOCJWkmsJppcbT3s0aObYya2BrGQbeeeMunQgN528DQ_WY7JSwU8zKMBbiWkqrvELIJaEbYOVwX0-8tLFSQAwjhwotcApSuA48JI71LHwyFFCVOPRZRxpoZjjqJsTiY6yC-kcvgACQmT0O2i8MS6tz4oyAeFtPJbvcOK-yABuxSE0XYLh98-SWkeY_rtecVuM9pBG7SSIcyrHYl0tMjv4GJ7dO8NL8h-bEL_z60dxA1bQrIfJrthnHMgG9Kg_PaJgjcMmfDP8Vm0FxqNNaBP2FwfNaK7xtulocoWlFggbwKJ46YYTYKlGvwVC9P027ruPd11iAjQl8O2-a7BaEy7k_60FKQl5Gfch35GU9aX-rjZMrGOE9btob5LX8Vi7skI-YOsPv1TgXRKyZM7YubFSpVjszgQ7ehEX9UPzcBmWFRIXbuJoywe40d5XZY8JeArwVEVN_gd40glUI18hgVU7dyGe9-RUetVf4TDoVG9ncwBiRHHC3oa-TZhxtqVd7MTCSAA6YCxXT-wOyYpuS6EHh5sMRHvoSSs010DqPtKa0o7XDj_vraMdXBsUYbIYQT5S9RKhcyNfeHAyKK8Gzrjkk9UG8Qbk-pDI-K4vKlADEU0b5nXwRjGPBRhUNBixF0-zu6VtyaXHzkbNQp-_m_2zlIXdX0y8bKTgwBXTBJlDDUt2HiDzNzP5GL2XboyUOOpJK1tPgSCagGRMT90vBWD3ZGJjX_dmmvPIhiSbB9K6ME0lzdoV8v17UUT7laMPAvW7u1LmkGzu9st34IVanfyLHCibXRK90H9Iy4PAA5wkMVTFaUPvgkYj0mCmZrt1krlcKXgm54iwdLC5Z9DIjPxxatZ8Mysi13hjZFHn_LH-YloiKBp4M6Bhk6mfUsdhZnJv0O1tKgUALqjwEqNMg7uEbzpATBsA9qA6zFpk-jHhM4c4rV0eNHDlLzGSN1mcc-D_kigSjv3d5T4G2q1R93vyummhBvmq9F_NkKSOklYZMlhMxGHCIpg9p4S740k5Vp4OJQcZFOt376zxYZgQ.JXstcmx-O_VtR2heEzp8bA'  

# api = ChatGPT(session_token, chrome_args=['--window-size=1280,768'], conversation_id='eb35cda8-c12d-41db-a173-bc3f1df79069')

def ask (text) :

    resp = api.send_message(text)
    return resp

if __name__ == '__main__':

    api = ChatGPT(session_token, chrome_args=['--window-size=1280,768'])
    resp = api.send_message('Hello')

    question = ''
    api = ChatGPT(session_token, chrome_args=['--window-size=1280,768'], conversation_id=resp['conversation_id'])

    while True:
        text = input('\nYou: ')
        if not text == '!!' : 
            question += text
            continue
        else :
            resp = ask(question)
            question = ''
        print ('===='*4)
        print('\nBot: ' + resp['message'])
