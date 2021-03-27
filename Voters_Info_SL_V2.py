# Made by GH0STH4CK3R - t.me/Dimuth92
# If you copy this give me credits

import requests , time , base64 
from colorama import Fore , init
from bs4 import BeautifulSoup as bSoup
init()

def v_info() :
    # Banner
    banner = """
  █ █ █▀█ ▀█▀ █▀▀ █▀█ █▀   █ █▄ █ █▀▀ █▀█   █▀ █  
  ▀▄▀ █▄█  █  ██▄ █▀▄ ▄█   █ █ ▀█ █▀  █▄█   ▄█ █▄▄ """

    tagline = "------ [+] Made By GH0STH4CK3R -----[+] V2.0 ------"

    print(Fore.LIGHTGREEN_EX + banner)
    print(Fore.LIGHTYELLOW_EX + tagline)
    print(Fore.LIGHTWHITE_EX + "")
    
    NICno = input("Enter NIC Number (with V) : ")
    phonenum = input("Enter Phone Number        : ")

    url2 = "https://eservices.elections.gov.lk/myVoterRegistration_otpe.aspx"
    #Made by GH0STH4CK3R
    headers1 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Length": "3830",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "PrefLang=pl=EN; ASP.NET_SessionId=bc0q0kwcqrncejl511gfmmh0",
        "Host": "eservices.elections.gov.lk",
        "Origin": "https://eservices.elections.gov.lk",
        "Referer": "https://eservices.elections.gov.lk/myVoterRegistration_otpe.aspx",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36 OPR/74.0.3911.218"
    }
    data2 = {"__EVENTTARGET": "ctl00$ContentPlaceHolder1$cmdSendOTP","__EVENTARGUMENT": "","__LASTFOCUS": "","__VIEWSTATE": "/wEPDwUJNjg5OTk1ODI0D2QWAmYPZBYCAgMPZBYCAgUPZBY+AgEPDxYCHgRUZXh0BU88YSBocmVmPSAnaHR0cDovL3d3dy5lbGVjdGlvbnMuZ292LmxrJyB0YXJnZXQ9J19ibGFuayc+d3d3LmVsZWN0aW9ucy5nb3YubGs8L2E+ZGQCAw8PFgIfAAVDWW91IGFyZSBub3Qgc2lnbmVkIGluICg8YSBocmVmPSAnTG9naW4uYXNweCcgdGFyZ2V0PScnPlNpZ24gSW48L2E+KWRkAgcPDxYCHwAFGlZvdGVyIFJlZ2lzdHJhdGlvbiBEZXRhaWxzZGQCCQ8PFgIfAAUBLWRkAgsPDxYCHghJbWFnZVVybAUNaW1hZ2VzL3NpLnBuZ2RkAg0PDxYCHwEFDWltYWdlcy90YS5wbmdkZAIPDw8WAh8BBQ5pbWFnZXMvZW5zLnBuZ2RkAhEPDxYCHwAFAkVOZGQCFw8PFgIfAAUITklDIE5vIDpkZAIbDw8WAh8ABQZZZWFyIDpkZAIdDxBkEBUFBDIwMTkEMjAxOAQyMDE3BDIwMTYEMjAxNRUFAjI1AjI0AjIzAjIyAjIxFCsDBWdnZ2dnFgFmZAIfDw8WAh8ABRFBZG1pbi4gRGlzdHJpY3QgOmRkAiEPEGQQFRoFKEFsbCkHQ29sb21ibwdHYW1wYWhhCEthbHV0YXJhBUthbmR5Bk1hdGFsZQtOdXdhcmFlbGl5YQVHYWxsZQZNYXRhcmEKSGFtYmFudG90YQZKYWZmbmEIVmF2dW5peWEKQmF0dGljYWxvYQZBbXBhcmELVHJpbmNvbWFsZWUKS3VydW5lZ2FsYQhQdXR0YWxhbQxBbnVyYWRoYXB1cmELUG9sb25uYXJ1d2EHQmFkdWxsYQpNb25hcmFnYWxhCVJhdG5hcHVyYQdLZWdhbGxlC0tpbGlub2NoY2hpCk11bGxhaXRpdnUGTWFubmFyFRoBMAExATIBMwE0ATUBNgE3ATgBOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNRQrAxpnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAiMPDxYCHwAFATBkZAIlDw8WAh8ABQExZGQCKQ8PFgIfAAUCMjVkZAIrDw8WAh8ABQEwZGQCLQ8PFgIfAAUBMGRkAi8PDxYCHwAFAjI1ZGQCMw8PFgIfAAULTW9iaWxlIE5vIDpkZAJNDw8WAh8ABQpPVFAgY29kZSA6ZGQCUQ8QZBAVABUAFCsDABYAZAJTDw8WAh8ABSBQbGVhZSB0eXBlIHRoZSBjb2RlIHNob3duIGJlbG93LmRkAlUPDxYCHwAFBVJlc2V0ZGQCVw8PFgIfAAUHRGlzcGxheWRkAlkPDxYCHgdUb29sVGlwBQhQcmV2aW91c2RkAlsPDxYCHwAFAzAvMGRkAl0PDxYCHwIFBE5leHRkZAJfDzwrAA8CAA8WBB4LXyFEYXRhQm91bmRnHgtfIUl0ZW1Db3VudAIBZA4UKwABFggeBE5hbWUFAS0eCklzUmVhZE9ubHloHgRUeXBlGSsCHglEYXRhRmllbGQFAS0WAmYPZBYGZg8PFgIeB1Zpc2libGVoZGQCAQ9kFgICAQ8PFgIfAAUBLWRkAgIPDxYCHwloZGQCYQ8PFgQfAAUPUHJpbnQgUG9sbCBDYXJkHgdFbmFibGVkaGRkAmMPDxYCHwAFDE1ha2UgYSBRdWVyeWRkGAIFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYIBRJjdGwwMCRJbWFnZUJ1dHRvbjEFEmN0bDAwJEltYWdlQnV0dG9uMgUlY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpbWJDaXRpemVuMQUfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpbWJTSQUfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpbWJUQQUfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpbWJFTgUhY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpbWJCYWNrBSFjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGltYkhvbWUFJWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkRGV0YWlsc1ZpZXcPFCsAB2RkZGRkFgACAWRmv6SkVXa8yE1qn2oAbReC09BvEZRXH5Y3grYLPUHuBg==","__VIEWSTATEGENERATOR": "35FBDAE6","__EVENTVALIDATION": "/wEdADNj+WbuihENgao3+ZxpR3QyD4zZrxX92uOlyIx1SyGTQiueDLEPWeU4qWuAtwlPZSPXp57/av0E0d6vd6N5edPfZ2X15PJ/w4IRv5x8jy1AFiO+LHyjvzGQe3iTyzrXt7ZKUOE88GeIt/Qnt7ZMmctsIzT4p9HvCmi7w3jk6rh+Mt00fctLXhtNzUH5DRJbMBoNv19SIlJDE27dPYRn+SaxnSWAvpNYtpoFNuLcPYsBLzAK8FESVDOCdFSNEx2tZddFU25gPDuv1hKTmG4mIOnncN5yhcw2J5PBzZF48+dOve6gGpGe3fwcm9eXNP1Xb4COiwCDHcdDOoz8GYpH21I307moeY2nrOull428hMlNYSjlRsWVRt0UElPDHMZ/BCtuVh92qiyxuYDc1zDRif9Xx9Ut0rAfk+69pq1E5TvNfTt2vCgdkAQlYPQ3QnQZEIbBXOYENR3G2KYc3dV4RKLLKw0RQyW2Gj7bpLg8oivqJ+qOt1mYpJE8BzzeSWVcFo59j2NPnbzZpukgGTPL3PKWXOmuz70eZZOsu/7EplmtKCbfwo053MjGFKc8I7DQlQb35Yp7afMgY6jv6pXAKHj5anHq4iySfESuuEzTsyd+cf0W5hpwLk8JKB2yeI20SlJYTRAFrkc7Pbz6KUlLLPnBRVnxlsP4YEkAI/Na68rH3jREy7qdY0GnIkJTVvXLiYfASrDFobJ2e6xTS20HqDyRVxOYaFezMMfJGIN3x1jS8v0EG5CCwMSuzD9r6wMpk0NYPe8KZ6rAmutbQhiZn/vBVvcVrkXKDBzYXFaMLDU1SYODjExe58WZ+PD98Qv0gIsT/OSJj0wU1a495HDcFYeX6wWtM7veujrE8cUcUxOLyxzYmOwojoVF8xYTiro+H04ECPZW0w9UfDE0cr8jwVfSZ6TXjKJsvMwUTIRaf9x951cLt7URgsAS1QEKctnUAhkc6K3mi0I43NdvJcSVFC6vJNe+Z88mjbPQwu1KGEJviagpFfvJ5CIKofZX3ipjHgY24Swft4uq1JDcE7oQeENCuH8AoW4E9pplrnuvXCWQ1zPH4vWrUrrVB5hnSpxosC7q0QahOHh9sg3EDWkQxI4hetNNHcBhoV6tGs6aweSp7g==","ctl00$ContentPlaceHolder1$txtNIC": NICno,"ctl00$ContentPlaceHolder1$ddlRev": "25","ctl00$ContentPlaceHolder1$ddlEDis": "0","ctl00$ContentPlaceHolder1$txtMob": phonenum,"ctl00$ContentPlaceHolder1$txtCode": ""} #Made by GH0STH4CK3R
    
    res1 = requests.post(url2 ,headers=headers1,data=data2)
    
    otp = input("Enter OTP Number          : ")
    data1 = {"__EVENTTARGET": "ctl00$ContentPlaceHolder1$cmdDisplay","__EVENTARGUMENT": "","__LASTFOCUS": "","__VIEWSTATE": "/wEPDwUJNjg5OTk1ODI0D2QWAmYPZBYCAgMPZBYCAgUPZBY+AgEPDxYCHgRUZXh0BU88YSBocmVmPSAnaHR0cDovL3d3dy5lbGVjdGlvbnMuZ292LmxrJyB0YXJnZXQ9J19ibGFuayc+d3d3LmVsZWN0aW9ucy5nb3YubGs8L2E+ZGQCAw8PFgIfAAVDWW91IGFyZSBub3Qgc2lnbmVkIGluICg8YSBocmVmPSAnTG9naW4uYXNweCcgdGFyZ2V0PScnPlNpZ24gSW48L2E+KWRkAgcPDxYCHwAFGlZvdGVyIFJlZ2lzdHJhdGlvbiBEZXRhaWxzZGQCCQ8PFgIfAAUBLWRkAgsPDxYCHghJbWFnZVVybAUNaW1hZ2VzL3NpLnBuZ2RkAg0PDxYCHwEFDWltYWdlcy90YS5wbmdkZAIPDw8WAh8BBQ5pbWFnZXMvZW5zLnBuZ2RkAhEPDxYCHwAFAkVOZGQCFw8PFgIfAAUITklDIE5vIDpkZAIbDw8WAh8ABQZZZWFyIDpkZAIdDxBkEBUFBDIwMTkEMjAxOAQyMDE3BDIwMTYEMjAxNRUFAjI1AjI0AjIzAjIyAjIxFCsDBWdnZ2dnFgFmZAIfDw8WAh8ABRFBZG1pbi4gRGlzdHJpY3QgOmRkAiEPEGQQFRoFKEFsbCkHQ29sb21ibwdHYW1wYWhhCEthbHV0YXJhBUthbmR5Bk1hdGFsZQtOdXdhcmFlbGl5YQVHYWxsZQZNYXRhcmEKSGFtYmFudG90YQZKYWZmbmEIVmF2dW5peWEKQmF0dGljYWxvYQZBbXBhcmELVHJpbmNvbWFsZWUKS3VydW5lZ2FsYQhQdXR0YWxhbQxBbnVyYWRoYXB1cmELUG9sb25uYXJ1d2EHQmFkdWxsYQpNb25hcmFnYWxhCVJhdG5hcHVyYQdLZWdhbGxlC0tpbGlub2NoY2hpCk11bGxhaXRpdnUGTWFubmFyFRoBMAExATIBMwE0ATUBNgE3ATgBOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNRQrAxpnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAiMPDxYCHwAFATBkZAIlDw8WAh8ABQExZGQCKQ8PFgIfAAUCMjVkZAIrDw8WAh8ABQEwZGQCLQ8PFgIfAAUBMGRkAi8PDxYCHwAFAjI1ZGQCMw8PFgIfAAULTW9iaWxlIE5vIDpkZAJNDw8WAh8ABQpPVFAgY29kZSA6ZGQCUQ8QZBAVABUAFCsDABYAZAJTDw8WAh8ABSBQbGVhZSB0eXBlIHRoZSBjb2RlIHNob3duIGJlbG93LmRkAlUPDxYCHwAFBVJlc2V0ZGQCVw8PFgIfAAUHRGlzcGxheWRkAlkPDxYCHgdUb29sVGlwBQhQcmV2aW91c2RkAlsPDxYCHwAFAzAvMGRkAl0PDxYCHwIFBE5leHRkZAJfDzwrAA8CAA8WBB4LXyFEYXRhQm91bmRnHgtfIUl0ZW1Db3VudAIBZA4UKwABFggeBE5hbWUFAS0eCklzUmVhZE9ubHloHgRUeXBlGSsCHglEYXRhRmllbGQFAS0WAmYPZBYGZg8PFgIeB1Zpc2libGVoZGQCAQ9kFgICAQ8PFgIfAAUBLWRkAgIPDxYCHwloZGQCYQ8PFgQfAAUPUHJpbnQgUG9sbCBDYXJkHgdFbmFibGVkaGRkAmMPDxYCHwAFDE1ha2UgYSBRdWVyeWRkGAIFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYIBRJjdGwwMCRJbWFnZUJ1dHRvbjEFEmN0bDAwJEltYWdlQnV0dG9uMgUlY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpbWJDaXRpemVuMQUfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpbWJTSQUfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpbWJUQQUfY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpbWJFTgUhY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpbWJCYWNrBSFjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGltYkhvbWUFJWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkRGV0YWlsc1ZpZXcPFCsAB2RkZGRkFgACAWRmv6SkVXa8yE1qn2oAbReC09BvEZRXH5Y3grYLPUHuBg==","__VIEWSTATEGENERATOR": "35FBDAE6","__EVENTVALIDATION": "/wEdADNj+WbuihENgao3+ZxpR3QyD4zZrxX92uOlyIx1SyGTQiueDLEPWeU4qWuAtwlPZSPXp57/av0E0d6vd6N5edPfZ2X15PJ/w4IRv5x8jy1AFiO+LHyjvzGQe3iTyzrXt7ZKUOE88GeIt/Qnt7ZMmctsIzT4p9HvCmi7w3jk6rh+Mt00fctLXhtNzUH5DRJbMBoNv19SIlJDE27dPYRn+SaxnSWAvpNYtpoFNuLcPYsBLzAK8FESVDOCdFSNEx2tZddFU25gPDuv1hKTmG4mIOnncN5yhcw2J5PBzZF48+dOve6gGpGe3fwcm9eXNP1Xb4COiwCDHcdDOoz8GYpH21I307moeY2nrOull428hMlNYSjlRsWVRt0UElPDHMZ/BCtuVh92qiyxuYDc1zDRif9Xx9Ut0rAfk+69pq1E5TvNfTt2vCgdkAQlYPQ3QnQZEIbBXOYENR3G2KYc3dV4RKLLKw0RQyW2Gj7bpLg8oivqJ+qOt1mYpJE8BzzeSWVcFo59j2NPnbzZpukgGTPL3PKWXOmuz70eZZOsu/7EplmtKCbfwo053MjGFKc8I7DQlQb35Yp7afMgY6jv6pXAKHj5anHq4iySfESuuEzTsyd+cf0W5hpwLk8JKB2yeI20SlJYTRAFrkc7Pbz6KUlLLPnBRVnxlsP4YEkAI/Na68rH3jREy7qdY0GnIkJTVvXLiYfASrDFobJ2e6xTS20HqDyRVxOYaFezMMfJGIN3x1jS8v0EG5CCwMSuzD9r6wMpk0NYPe8KZ6rAmutbQhiZn/vBVvcVrkXKDBzYXFaMLDU1SYODjExe58WZ+PD98Qv0gIsT/OSJj0wU1a495HDcFYeX6wWtM7veujrE8cUcUxOLyxzYmOwojoVF8xYTiro+H04ECPZW0w9UfDE0cr8jwVfSZ6TXjKJsvMwUTIRaf9x951cLt7URgsAS1QEKctnUAhkc6K3mi0I43NdvJcSVFC6vJNe+Z88mjbPQwu1KGEJviagpFfvJ5CIKofZX3ipjHgY24Swft4uq1JDcE7oQeENCuH8AoW4E9pplrnuvXCWQ1zPH4vWrUrrVB5hnSpxosC7q0QahOHh9sg3EDWkQxI4hetNNHcBhoV6tGs6aweSp7g==","ctl00$ContentPlaceHolder1$txtNIC": NICno,"ctl00$ContentPlaceHolder1$ddlRev": "25","ctl00$ContentPlaceHolder1$ddlEDis": "0","ctl00$ContentPlaceHolder1$txtMob": phonenum,"ctl00$ContentPlaceHolder1$txtCode": otp}
    
    res2 = requests.post(url2 ,headers=headers1,data=data1)
    
    rc_code = res2.status_code 

    if rc_code == 200 :
        
        details = res2.text

        name = []
        value = []
        i = 0

        page_soup = bSoup(details,"html.parser")

        table = page_soup.find("table",{"id":"ContentPlaceHolder1_DetailsView"})  # Finding tags
        
        for td in table.find_all("td"):
            i += 1
            td = str(td)
            td = td.replace("<td>","")    # Removing tags
            td = td.replace("</td>","")
            
            if i % 2 == 0 :
                value.append(td)
            else :
                name.append(td)

        # Printing output     
        print(Fore.LIGHTGREEN_EX + "")
        spacebtw = ""
        for index in range(len(name)) :
            length = len(name[index])
            if length == 17 :
                spacebtw = ""
            else :
                spacebtw = (17 - length) * " "

            print(name[index],spacebtw," : ",value[index])   

    else:
        print("Something Went Wrong : ",rc_code)  

v_info()

input("\nExit >")
