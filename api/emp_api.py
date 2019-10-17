"""
封装员工操作函数

"""
# 定义操作类
import app
import logging

class EmployeeTest:
    # 员工-增函数
    def add_emp(self, session, username, mobile, workNumber):
        # session.post(url,data=)
        logging.info("执行员工新增")
        mydata = {
            "username": username,
            "mobile": mobile,
            "workNumber": workNumber
        }
        return session.post(app.IHRM_URL + "/api/sys/user", json=mydata, headers={"Authorization":"Bearer "+app.TOKEN_LOGIN})

    # 员工-改函数
    def updata_emp(self, session, userid,username):
        # session.post(url,data=)
        updata_data = {
            "username": username
        }
        return session.put(app.IHRM_URL + "/api/sys/user/"+userid, json=updata_data, headers={"Authorization":"Bearer "+app.TOKEN_LOGIN})


    # 员工-查函数
    def find_emp(self,session,userid):

        return session.get(app.IHRM_URL + "/api/sys/user/" + userid,
                           headers={"Authorization": "Bearer " + app.TOKEN_LOGIN})

    # 员工-删函数
    def del_emp(self,session,userid):
        return session.delete(app.IHRM_URL + "/api/sys/user/" + userid,
                           headers={"Authorization": "Bearer " + app.TOKEN_LOGIN})