from seartDEV_TryLogin import TryLogin

websiteToTest = 'https://dev321.seart.pl/'
accountUrl = 'https://dev321.seart.pl/customer/account/'
testDatas_1 = TryLogin(1, 'wiktor.cwiertnia.seart@gmail.com', 'Test123*', 'wiktor TEST!', websiteToTest, accountUrl)
testDatas_2 = TryLogin(2, 'wiktor.cwiertnia@seart.pl', 'Test123*', 'wiktor TEST', websiteToTest, accountUrl)

testDatas_2.login()
testDatas_1.login()

