import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='bank')
mycursor=mydb.cursor()
mycursor.execute("INSERT  INTO account   VALUES(1231231231,'deepanshu','delhi','uttam_nagar',\
110059,'wz-241',999981754,'saving',999999888,4884)")

mycursor.execute("INSERT  INTO account   VALUES(12312312312,'yatika','delhi','uttam nagar',\
110059,'wz-241',599998176,'saving', 999985498,4664 )")


mycursor.execute("INSERT  INTO account   VALUES(1231231233,'palak','punjab','amritsar',\
560023,'a-56',963255845,'current',007896332,8558)")


mycursor.execute("INSERT  INTO account   VALUES(1231231234,'pavani','punjab','amritsar',\
560023,'a=54',456978985,'current', 008963452,1221)")


mycursor.execute("INSERT  INTO account   VALUES(1231231235,'kritika','punjab','ludhiana',\
567589,'a=89',078945663,'saving',063745663,5225)")


mycursor.execute("INSERT  INTO account   VALUES(1231231236,'gunika','punjab','ludhiana',\
567589,'a=86',078563987,'current',056385274,7887)")

mycursor.execute("INSERT  INTO account   VALUES(1231231237,'shinaya','harayana','kkr',\
423659,'a=78',085296345,'saving',078529636,5995)")

mycursor.execute("INSERT  INTO account   VALUES(1231231238,'aman','delhi','rohini',\
110049,'a=25',056396265,'current',08997659,3663)")

mycursor.execute("INSERT  INTO account   VALUES(123231239,'ankit','delhi','vikaspuri',\
110056,'a=546',075361254,'saving',07896588,6556)")

mydb.commit()










