from __future__ import unicode_literals

from django.db import models, connection



class Article(models.Model):
    def __unicode__(self):
        return self.title


    @staticmethod
    def login(username, password):
        try:
            cur = connection.cursor()
            #cur.execute("CALL PROC_LM_FETCH_LOGIN_VALIDATION('" + username + "','" + password + "')")
            cur.execute("""SELECT UID,Emailid, Name, IsActive
FROM tbl_user_master
where Emailid='""" + username + """' and password='"""+ password + """' and isactive=1;""")

            dictreturn = Article.formatqueryresult(cur)
            cur.close()
            connection.close()
            return dictreturn
        except Exception, err:
            return err
            cur.close()
            connection.close()

    @staticmethod
    def adduser(Name,Email,Phone,passw):
        try:
            cur = connection.cursor()
            cur.execute("INSERT INTO `demo`.`tbl_user_master`(`Name`,`EmailID`,`Password`,`phone`,`IsActive`,`CreatedAt`)VALUES('"+ str(Name) +"','"+ str(Email) +"','"+ passw +"','"+ str(Phone) +"',1,now());")
            dictreturn = Article.formatqueryresult(cur)
            cur.close()
            return dictreturn
        except Exception, err:
            return err


    @staticmethod
    def configureuser(apikey,screat,uid):
        try:
            cur = connection.cursor()
            cur.execute("INSERT INTO `demo`.`tbl_demo_key`(`apikey`,`Secret`,`isactive`,`CreatedAt`,`CreatedAt_by`)VALUES('"+ str(apikey) +"','"+ str(screat) +"',1,now(),'"+ str(uid) +"')");
            dictreturn = Article.formatqueryresult(cur)
            cur.close()
            return dictreturn
        except Exception, err:
            return err

    @staticmethod
    def launchinstance(sizeoffleet,tyinstances,maxprice,exptime,uid):
        try:
            cur = connection.cursor()
            cur.execute("INSERT INTO `demo`.`tbl_demo_instance`(`sizeof_instance`,`typeof_instance`,`max_price`,`expirationtime`,`CreatedAt`,`CreatedAt_by`)VALUES('"+ sizeoffleet +"','"+ tyinstances +"','"+ maxprice +"','"+ exptime +"',now(),'"+ str(uid) +"');")
            dictreturn = Article.formatqueryresult(cur)
            cur.close()
            return dictreturn
        except Exception, err:
            return err


    @staticmethod
    def fetch_instancedetail():
        try:
            cur = connection.cursor()
            cur.execute("SELECT id,sizeof_instance,typeof_instance,max_price,expirationtime,status FROM `demo`.`tbl_demo_instance`;")
            dictreturn = Article.formatqueryresult(cur)
            cur.close()
            return dictreturn
        except Exception, err:
            return err


    @staticmethod
    def updatestatus(uid,id):
        try:
            cur = connection.cursor()
            cur.execute("UPDATE `demo`.`tbl_demo_instance` SET `status` = 'active',`CreatedAt_by` = '"+ str(uid) +"' WHERE `ID` = '"+ str(id)+"';")
            dictreturn = Article.formatqueryresult(cur)
            cur.close()
            return 'success'
        except Exception, err:
            return err


    @staticmethod
    def deactive(uid,id):
        try:
            cur = connection.cursor()
            cur.execute("UPDATE `demo`.`tbl_demo_instance` SET `status` = 'deactive',`CreatedAt_by` = '"+ str(uid) +"' WHERE `ID` = '"+ str(id)+"';")
            dictreturn = Article.formatqueryresult(cur)
            cur.close()
            return 'success'
        except Exception, err:
            return err




    @staticmethod
    def formatqueryresult(cur):
        desc = cur.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cur.fetchall()
        ]

