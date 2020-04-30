#引入flask程序包，网页框架
import flask
#实例化flask对象
app = flask.Flask(__name__)
#路由控制语句，
'''
@app.route("/")
def index():
    try:
        #服务器用Flask中的request对象的args来存储GET的参数
        province = flask.request.args.get("province")if "province" in flask.request.args else ""
        city = flask.request.args.get("city")if "city" in flask.request.args else ""
        return province +"," + city

        #服务器读取主页index至data
        #fobj = open("index.htm","rb")
        #data = fobj.read()
        #fobj.close()
        #return data


    except Exception as err:
        return str(err)

'''
@app.route("/",methods = ["POST"])
def index2():
    try:
        #服务器用Flask中的request对象的form来存储POST的参数
        province = flask.request.form.get("province")if "province" in flask.request.args else ""
        city = flask.request.form.get("city")if "city" in flask.request.args else ""
        return province +",,,,,,,,," + city
    except Exception as err:
        return str(err)


@app.route("/hi")
def hi():
    return "hi! how are you"



if __name__ =="__main__":
    app.run()
