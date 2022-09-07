from OpenFileWithData import OpenFileWithData
from seartDEV_TryLogin import TryLogin

path = OpenFileWithData("login.json")

loginInJSON = path.open()

websiteToTest = 'https://dev321.seart.pl/'
accountUrl = 'https://dev321.seart.pl/customer/account/'


def datasFromJson():
    for loginData in loginInJSON['loginDatas']:
        email = loginData['loginEmail']
        loginPass = loginData['loginPass']
        nickName = loginData['nickName']
        testDatas = TryLogin(1, email, loginPass, nickName, websiteToTest, accountUrl)
        testDatas.login()


datasFromJson()


