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
            cur.execute("""SELECT UID,Emailid,Concat(Firstname,' ',Lastname) as Name, IsActive
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
            cur.execute("INSERT INTO `demo`.`tbl_user_master`(Firstname`,`Lastname`,`EmailID`,`Password`,`last_login`,`IsActive`,`CreatedAt`)VALUES('"+ Name +"','"+ Email +"','"+ Phone +"','"+ passw +"',1,1,now());")
            dictreturn = Article.formatqueryresult(cur)
            cur.close()
            return dictreturn
        except Exception, err:
            return err


    @staticmethod
    def configureuser(apikey,screat,uid):
        try:
            cur = connection.cursor()
            cur.execute("INSERT INTO `demo`.`tbl_demo_key`(`apikey`,`screat`,`IsActive`,`CreatedAt`,`Created_by`)VALUES('"+ apikey +"','"+ screat +"',1,now(),'"+ uid +"');")
            dictreturn = Article.formatqueryresult(cur)
            cur.close()
            return dictreturn
        except Exception, err:
            return err

    @staticmethod
    def launchinstance(sizeoffleet,tyinstances,maxprice,exptime,uid):
        try:
            cur = connection.cursor()
            cur.execute("INSERT INTO `demo`.`tbl_active_instance`(sizeof_fleet`,`typeof_instance`,`max_price`,`exp_time`,`Created_by`,`IsActive`,`CreatedAt`)VALUES('"+ sizeoffleet +"','"+ tyinstances +"','"+ maxprice +"','"+ exptime +"','"+ uid +"',1,now());")
            dictreturn = Article.formatqueryresult(cur)
            cur.close()
            return dictreturn
        except Exception, err:
            return err


    @staticmethod
    def launchinstance(sizeoffleet,tyinstances,maxprice,exptime):
        try:
            cur = connection.cursor()
            cur.execute("select * from tbl_instance_master")
            dictreturn = Article.formatqueryresult(cur)
            cur.close()
            return dictreturn
        except Exception, err:
            return err



    @staticmethod
    def formatqueryresult(cur):
        desc = cur.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cur.fetchall()
        ]

