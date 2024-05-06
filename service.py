import asyncio
import string
import time

from fastapi import FastAPI, File, Response, Request, Header
import uvicorn
import requests
import sqlite3
import random
from datetime import datetime
import datetime as dttime
from pydantic import BaseModel
from typing import Union, Optional

app = FastAPI()

userinvit = 'xxxxxx'
imageURL = 'xxx.xx.xx.xxx:8070'
def easyprint(x):
    print('{}>>{}'.format(str(datetime.now().replace(microsecond=0)),x))

@app.get("/api/jiage")
async def get_image():
    with open("image/jiage.png", "rb") as image_file:
        image_data = image_file.read()
    return Response(content=image_data, media_type="image/png")

@app.get("/api/syimage")
async def get_image():
    with open("image/image.png", "rb") as image_file:
        image_data = image_file.read()
    return Response(content=image_data, media_type="image/png")

@app.get("/api/syimagepath")
async def get_image(custom:Union[str,None]=Header(None,convert_underscores=True)):
    if custom == 'chenjijun':
        return {'return':f'http://{imageURL}/api/syimage'}

@app.get("/api/dlimage")
async def get_image():
    with open("image/denglubj.png", "rb") as image_file:
        image_data = image_file.read()
    return Response(content=image_data, media_type="image/png")

@app.get("/api/dlimagepath")
async def get_image(custom:Union[str,None]=Header(None,convert_underscores=True)):
    if custom == 'chenjijun':
        return {'return':f'http://{imageURL}/api/dlimage'}

WECHAT_APPID = 'xxxxx'
WECHAT_APPSECRET = 'xxxxx'

# 微信登录凭证校验接口 URL

@app.post("/api/login")
async def postlogin(request: Request) -> dict:
    data = await request.json()
    easyprint(data)
    if 'username' in data and 'password' in data:
        duibi = (data["username"],data["password"])
        checkone = str(data["username"])
        checktwo = str(data["password"])
        easyprint(duibi)
        with sqlite3.connect('userandpass.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user WHERE username=? AND password=?",(checkone,checktwo))
            users = cursor.fetchall()
        if users:
            return {'return':'canpass','user':users[0][4],'jifen':users[0][3]}
        else:
            return {'return':'cantpass'}

@app.post("/api/wechat/yijianlogin")
async def wechat_login(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun':
        data = await request.json()
        code = data.get('code')
        if not code:
            return {'return': 'Failed'}
        else:                # 调用微信登录凭证校验接口
            response = requests.get(f'https://api.weixin.qq.com/sns/jscode2session?appid={WECHAT_APPID}&secret={WECHAT_APPSECRET}&js_code={code}&grant_type=authorization_code')
            result =  response.json()
            easyprint(result)
            if response.status_code != 200 or 'openid' not in result:
                return {'return': 'Failed'}
                # 返回 openid 和 session_key
            else:
                getopenid =  result['openid']
                with sqlite3.connect('userandpass.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM user WHERE openid=?", (getopenid,))
                    valus = cursor.fetchall()
                    easyprint(valus)
                    if valus:
                        # with sqlite3.connect('dingdan.db') as ddconn:
                        #     cursor = ddconn.cursor()
                        #     table_name = valus[0][1]
                        #     try:
                        #         cursor.execute(f"PRAGMA table_info({table_name})")
                        #         results = cursor.fetchall()
                        #         if results:
                        #             print(f"Table {table_name} exists.")
                        #         else:
                        #             print(f"Table {table_name} does not exist.")
                        #             cursor.execute(f'''
                        #                            CREATE TABLE {table_name}(
                        #                            id INTEGER PRIMARY KEY,
                        #                            user TEXT,
                        #                            leixing TEXT,
                        #                            kdgs TEXT,
                        #                            danhao TEXT,
                        #                            wpxx TEXT,
                        #                            status TEXT,
                        #                            lxhm TEXT,
                        #                            beizhu TEXT,
                        #                            tianjiasj TEXT,
                        #                            rukusj TEXT,
                        #                            chukusj TEXT，
                        #                            wanchengsj TEXT
                        #                       );
                        #                            ''')
                        #             ddconn.commit()
                        #     except sqlite3.OperationalError:
                        #         print(f"Table {table_name} does not exist.")
                        #         return {'return': 'Failed'}
                        return {'return': 'canpass', 'username': valus[0][1], 'user': valus[0][4], 'jifen': valus[0][3]}
                    else:
                        useradd = ''.join(random.choices(string.ascii_letters, k=3) +random.choices(string.digits, k=5))

                        with sqlite3.connect('userandpass.db') as conn:
                            cursor = conn.cursor()
                            cursor.execute("SELECT * FROM user WHERE username=?", (useradd,))
                            users = cursor.fetchall()
                            while 1 :
                                if users:
                                    useradd = random.choices(string.ascii_letters, k=3)  +  random.choices(string.digits, k=5)
                                    cursor.execute("SELECT * FROM user WHERE username=?", (useradd,))
                                    users = cursor.fetchall()
                                    time.sleep(1)
                                else:
                                    break
                            creattime = str(datetime.now().replace(microsecond=0))
                            cursor.execute('''
                                    INSERT INTO user (username, password, points, userrole, findpasswd, creattime,openid)
                                    VALUES (?,?,?,?,?,?,?)
                                    ''', (useradd, 'test123456', '0', 'localuser', '123456', creattime,result['openid'],))
                            users = cursor.fetchall()
                            conn.commit()
                            cursor.execute("SELECT * FROM user WHERE openid=?", (result['openid'],))
                            valus = cursor.fetchall()
                            conn.close()
                            # with sqlite3.connect('dingdan.db') as ddconn:
                            #     cursor = ddconn.cursor()
                            #     table_name = useradd
                            #     try:
                            #         cursor.execute(f"PRAGMA table_info({table_name})")
                            #         results = cursor.fetchall()
                            #         if results:
                            #             print(f"Table {table_name} exists.")
                            #         else:
                            #             print(f"Table {table_name} does not exist.")
                            #             cursor.execute('''
                            #                            CREATE TABLE 我都想笑了(
                            #                            id INTEGER PRIMARY KEY,
                            #                            user TEXT,
                            #                            leixing TEXT,
                            #                            kdgs TEXT,
                            #                            danhao TEXT,
                            #                            wpxx TEXT,
                            #                            status TEXT,
                            #                            lxhm TEXT,
                            #                            beizhu TEXT,
                            #                            tianjiasj TEXT,
                            #                            rukusj TEXT,
                            #                            chukusj TEXT,
                            #                             );
                            #                            ''')
                            #             ddconn.commit()
                            #     except sqlite3.OperationalError:
                            #         print(f"Table {table_name} does not exist.")
                            return {'return': 'canpass','username': useradd,'user':valus[0][4] , 'jifen': valus[0][3]}

@app.post("/api/zhuceuser")
async def sign_user(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun':
        data = await request.json()
        if 'formData' in data:
            easyprint(data)
            data = data['formData']
            if data['yqm'] == userinvit :
                creattime = str(datetime.now().replace(microsecond=0))
                usersign = str(data['username'])
                usersignpw = str(data['password'])
                passfind = str(data['find'])
                print(usersign)
                with sqlite3.connect('userandpass.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM user WHERE username=?", (usersign,))
                    users = cursor.fetchall()
                    if users:
                        return {'return': 'userhaved'}
                    else:
                        cursor.execute('''
                        INSERT INTO user (username, password, points, userrole, findpasswd, creattime)
                        VALUES (?,?,?,?,?,?)
                        ''', (usersign, usersignpw, '0', 'localuser', passfind, creattime,))
                        users = cursor.fetchall()
                        conn.commit()
                        # with sqlite3.connect('dingdan.db') as ddconn:
                        #     cursor = ddconn.cursor()
                        #     try:
                        #         cursor.execute(f"PRAGMA table_info({usersign})")
                        #         results = cursor.fetchall()
                        #         if results:
                        #             print(f"Table {usersign} exists.")
                        #         else:
                        #             print(f"Table {usersign} does not exist.")
                        #             cursor.execute(f'''
                        #                            CREATE TABLE {usersign}(
                        #                            id INTEGER PRIMARY KEY,
                        #                            user TEXT,
                        #                            leixing TEXT,
                        #                            kdgs TEXT,
                        #                            danhao TEXT,
                        #                            wpxx TEXT,
                        #                            status TEXT,
                        #                            lxhm TEXT,
                        #                            beizhu TEXT,
                        #                            tianjiasj TEXT,
                        #                            rukusj TEXT,
                        #                            chukusj TEXT
                        #                       );
                        #                            ''')
                        #             ddconn.commit()
                        #     except sqlite3.OperationalError:
                        #         print(f"Table {usersign} does not exist.")
                        #         return {'return': 'Failed'}
                        return {'return': 'addsuccess'}
            else:
                return {'return': '邀请码错误'}
    else:
        return {'return': 'cuowucangshu'}



@app.post("/api/adddingdan")   # 串行非异步
async def sign_user(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun':
        data = await request.json()
        easyprint(data)
        if 'user' in data:
            if data['user'] and data['danhao']:
                try:
                    with sqlite3.connect('userandpass.db') as conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM user WHERE username=?", (data['user'],))
                        valus = cursor.fetchall()
                        if valus:
                            with sqlite3.connect('dingdan.db') as conn:
                                cursor = conn.cursor()
                                cursor.execute("SELECT * FROM alldingdan WHERE danhao=?", (data['danhao'],))
                                value = cursor.fetchall()
                                if value:
                                    return {'return':'单号已存在'}
                                else:
                                    addtime = str(datetime.now().replace(microsecond=0))
                                    cursor.execute(f'''
                                    INSERT INTO alldingdan (user, leixing, kdgs, danhao, lxhm, wpxx, beizhu, tianjiasj,  status)
                                    VALUES (?,?,?,?,?,?,?,?,?)
                                    ''',(data['user'], data['leixing'], data['kdgs'],data['danhao'],data['lxhm'],data['wpxx'],
                                         data['beizhu'],addtime,'未收货'))
                                    conn.commit()
                                    cursor.execute('SELECT * FROM alldingdan WHERE danhao=?', (data['danhao'],))
                                    value = cursor.fetchall()
                                    if value:
                                        return {'return': '添加成功','values':value}
                                    else:
                                        return {'return': '添加失败'}
                        else:
                            return {'return': '用户名不存在'}
                except Exception as e:
                    easyprint(e)
                    return {'return': '添加失败'}
    else:
        return {'return': '添加失败'}




####################################################################################################


def phoneCon(user,check):
    if check == 0:
        sqlinput = "SELECT * FROM alldingdan WHERE user=? and status=?"
        params = (user,"已完成")
        rebackdd = '无已完成订单'
    else:
        sqlinput = "SELECT * FROM alldingdan WHERE user=? and status!=?"
        params = (user,"已完成",)
        rebackdd = '无未完成订单'
    with sqlite3.connect('dingdan.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sqlinput,params)
        reback = cursor.fetchall()
        if not reback:
            easyprint(rebackdd)
            return {'return': rebackdd}
        else:
            easyprint(reback)
            return {'return': '查询成功', 'valuess': reback}



def phoneConadmin(check):
    with sqlite3.connect('dingdan.db') as conn:
        cursor = conn.cursor()
        # cursor.execute("SELECT * FROM alldingdan WHERE status='已完成';")
        # tables = cursor.fetchall()
        rows = []
        if check == 0:
            cursor.execute("SELECT * FROM alldingdan WHERE status='已完成';")
            rows += cursor.fetchall()[::-1]
            if not rows:
                return {'return': '无已完成订单'}
            else:
                easyprint(rows)
                return {'return': '查询成功', 'valuess': rows}
        else:
            cursor.execute("SELECT * FROM alldingdan WHERE status!='已完成'")
            rows += cursor.fetchall()[::-1]
            if not rows:
                return {'return': '无已完成订单'}
            else:
                easyprint(rows)
                return {'return': '查询成功', 'valuess': rows}


#########################################################################################################




@app.post("/api/dingdancx")    # 串行非异步
async def dingdan_cx(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'phonerequest' in data:
            data = data['phonerequest']
            user = data['user']
            if user == 'admin':
                if data['content'] == 'finish':
                    return  phoneConadmin(0)

                if data['content'] == 'unfinish':
                    return phoneConadmin(1)

                if data['content'] == 'all':
                    with sqlite3.connect('dingdan.db') as conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM alldingdan ;")
                        rows = []
                        rows += cursor.fetchall()[::-1]
                        if not rows:
                            return {'return': '无订单'}
                        else:
                            return {'return': '查询成功', 'valuess': rows}
            else:
                if data['content'] == 'finish':
                    return phoneCon(user,0)

                if data['content'] == 'unfinish':
                    return phoneCon(user, 1)

                if data['content'] == 'all':
                    with sqlite3.connect('dingdan.db') as conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM alldingdan WHERE user=?", (user,))
                        rows = cursor.fetchall()
                        if not rows:
                            return {'return': '无订单'}
                        else:
                            return {'return': '查询成功', 'valuess': rows}



        if 'putvalue' in data:
            user = data['putvalue']
            if user['user']== 'admin':
                if 'curr' in user:
                    username = user['curr']
                    with sqlite3.connect('dingdan.db') as conn:
                        cursor = conn.cursor()
                        # cursor.execute("SELECT * FROM dingdan WHERE user=?", (user,))
                        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%{username}%'")
                        # columns = [col[0] for col in cursor.description]
                        # value = [dict(zip(columns, row)) for row in cursor.fetchall()]
                        values = cursor.fetchall()
                        if not values:
                            return {'return': '无提交记录'}
                        else:
                            for j in values:
                                table_name = j[0]
                                cursor.execute(f"SELECT * FROM {table_name}")
                                table_content = cursor.fetchall()
                                return {'return': '查询成功', 'valuess': table_content}
                if 'status' in user:
                    status = user['status']
                    with sqlite3.connect('dingdan.db') as conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                        tables = cursor.fetchall()
                        rows = []
                        for table in tables:
                            table_name = table[0]
                            cursor.execute(f"SELECT * FROM {table_name}")
                            rows += cursor.fetchall()
                        if not rows:
                            return {'return': '无提交记录'}
                        else:
                            rebacks = []
                            for i in rows:
                                if status in i[6]:
                                    rebacks.append(i)
                            return {'return': '查询成功', 'valuess': rebacks}

                if 'danhao' in user:
                    danhao = user['danhao']
                    with sqlite3.connect('dingdan.db') as conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                        tables = cursor.fetchall()
                        rows = []
                        for table in tables:
                            table_name = table[0]
                            cursor.execute(f"SELECT * FROM {table_name}")
                            rows += cursor.fetchall()
                        if not rows:
                            return {'return': '无提交记录'}
                        else:
                            rebacks = []
                            for i in rows:
                                if danhao in i[4]:
                                    rebacks.append(i)
                            return {'return': '查询成功', 'valuess': rebacks}
            else:
                if 'curr' in user:
                    status = user['curr']
                    with sqlite3.connect('dingdan.db') as conn:
                        cursor = conn.cursor()
                        cursor.execute(f"SELECT * FROM {user['user']} WHERE state LIKE '%{status}%'")
                        tables = cursor.fetchall()

                        if not tables:
                            return {'return': '无提交记录'}
                        else:
                            return {'return': '查询成功', 'valuess': tables}

                if 'danhao' in user:
                    danhao = user['danhao']
                    with sqlite3.connect('dingdan.db') as conn:
                        cursor = conn.cursor()
                        cursor.execute(f"SELECT * FROM {user['user']} WHERE danhao LIKE '%{danhao}%'")
                        tables = cursor.fetchall()
                        if not tables:
                            return {'return': '无提交记录'}
                        else:
                            return {'return': '查询成功', 'valuess': tables}

                if 'beizhu' in user:
                    beizhu = user['beizhu']
                    with sqlite3.connect('dingdan.db') as conn:
                        cursor = conn.cursor()
                        cursor.execute(f"SELECT * FROM {user['user']} WHERE beizhu LIKE '%{beizhu}%'")
                        tables = cursor.fetchall()
                        if not tables:
                            return {'return': '无提交记录'}
                        else:
                            return {'return': '查询成功', 'valuess': tables}
    else:
        return {'return': '查询失败'}

@app.post("/api/shouhuo")    # 串行非异步
async def shou_huo(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        data = data['requestvalue']
        creattime = str(datetime.now().replace(microsecond=0))
        if 'danhao' in data:
            with sqlite3.connect('dingdan.db') as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM alldingdan WHERE danhao=?",(data['danhao'],))
                rows = cursor.fetchall()
                if not rows:
                    return {'return': '无提交记录'}
                else:
                    try:
                        if data['requestvalue'] == '已入库':
                            update_query = f"""  
                            UPDATE alldingdan
                            SET status = ?, rukusj = ?  
                            WHERE danhao = ?  
                            """
                            cursor.execute(update_query, ('已入库', creattime, data['danhao']))
                            conn.commit()
                            return {'return': '更新状态成功'}
                        else:
                            update_query = f"""  
                                            UPDATE alldingdan
                                            SET status = ?, chukusj = ?  
                                            WHERE danhao = ?  
                                            """
                            cursor.execute(update_query, ('已出库', creattime, data['danhao']))
                            conn.commit()
                            return {'return': '更新状态成功'}
                    except Exception as e:

                        easyprint(e)
                        return {'return': '操作失败'}
        else:
            return {'return': '操作失败'}

    else:
        return {'return': '操作失败'}

@app.post("/api/jichu")    # 串行非异步
async def shou_huo(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'danhao' in data:
            with sqlite3.connect('userandpass.db') as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM dingdan WHERE danhao=? ",(data['danhao'],))
                value = cursor.fetchall()
                if not value:
                    return {'return': '无提交记录'}
                else:
                    creattime = str(datetime.now().replace(microsecond=0))
                    update_query = """  
                    UPDATE dingdan  
                    SET status = ?, chukusj = ? 
                    WHERE danhao = ?  
                    """
                    cursor.execute(update_query, ('已寄往国外', creattime, data['danhao']))
                    conn.commit()
                    cursor.execute("SELECT status FROM dingdan WHERE danhao = ?", (data['danhao'],))
                    result = cursor.fetchone()
                    if '已寄往国外' in result:
                        return {'return': '更新状态成功'}
                    else:
                        return {'return': '操作失败'}
        else:
            return {'return': '操作失败'}
    else:
        return {'return': '操作失败'}

@app.post("/api/dingdanxg")
async def dingdan_cx(request: Request,Authorization: Optional[str] = Header(None)) :
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'postlist' in data:
            gvalues = data['postlist']
            changeid = gvalues[0]
            changeuser = gvalues[1]
            if changeid and changeuser :
                with sqlite3.connect('dingdan.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT * FROM {changeuser} WHERE id=? and user=? ",(changeid,changeuser,))
                    value = cursor.fetchall()
                    if not value:
                        return {'return':'无该ID/USER记录'}
                    else:
                        update_sql = f"""  
                                UPDATE {changeuser}  
                                SET leixing=? ,kdgs=?, danhao=?, wpxx=?,status=?, lxhm=?,  beizhu=?, tianjiasj=?, rukusj=?, chukusj=? 
                                WHERE id = ?  AND user = ?
                                """
                        cursor.execute(update_sql,(gvalues[2], gvalues[3], gvalues[4], gvalues[5], gvalues[6], gvalues[7]
                                       ,gvalues[8], gvalues[9], gvalues[10], gvalues[11], gvalues[0], gvalues[1]))

                        conn.commit()
                        return {'return': '修改成功' }
    else:
        return {'return': '查询失败'}

@app.post("/api/sjdingdanruku")
async def dingdan_cx(request: Request,Authorization: Optional[str] = Header(None)) :
    if Authorization == 'chenjijun123':

        dataone = await request.json()
        easyprint(dataone)
        if 'request' in dataone:
            data = dataone['request']
            changeid = data['0']
            changeuser = data['1']
            if changeid and changeuser :
                creattime = str(datetime.now().replace(microsecond=0))
                with sqlite3.connect('dingdan.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT * FROM alldingdan WHERE id=? and user=? ",(changeid,changeuser,))
                    value = cursor.fetchall()
                    if not value:
                        return {'return':'无该ID/USER记录'}
                    else:
                        update_sql = f"""  
                                UPDATE alldingdan  
                                SET status=?, rukusj=?
                                WHERE id = ?  AND user = ?
                                """
                        cursor.execute(update_sql,('已入库',creattime, changeid, changeuser))
                        conn.commit()
                        return {'return': '修改成功','time':creattime }
    else:
        return {'return': '查询失败'}

@app.post("/api/sjdingdanchuku")
async def dingdan_cx(request: Request,Authorization: Optional[str] = Header(None)) :
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'request' in data:
            data = data['request']
            changeid = data['0']
            changeuser = data['1']
            creattime = str(datetime.now().replace(microsecond=0))
            if changeid and changeuser :
                with sqlite3.connect('dingdan.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT * FROM alldingdan WHERE id=? and user=? ",(changeid,changeuser,))
                    value = cursor.fetchall()
                    if not value:
                        return {'return':'无该ID/USER记录'}
                    else:
                        update_sql = f"""  
                               UPDATE alldingdan  
                               SET status=?, chukusj=?
                               WHERE id = ?  AND user = ?
                               """
                        cursor.execute(update_sql,('已出库',creattime, changeid, changeuser))
                        print(value)
                        conn.commit()
                        return {'return': '修改成功','time':creattime }
    else:
        return {'return': '查询失败'}


@app.post("/api/addbox")
async def addbox(request: Request,Authorization: Optional[str] = Header(None)) :
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'boxname' in data:
            creattime = str(datetime.now().replace(microsecond=0))
            boxname = data['boxname']
            boxweight = '未定义'
            statu = '已创建'
            with sqlite3.connect('dingdan.db') as con:
                cursor = con.cursor()
                cursor.execute("SELECT * FROM boxinfo WHERE boxname=?", (boxname,))
                value = cursor.fetchall()
                if value:
                    return {'return': '箱号已存在' }
                else:
                    cursor.execute("INSERT INTO boxinfo(boxname,boxcreattime,boxweight,status) VALUES (?,?,?,?)",
                                   (boxname,creattime,boxweight,statu))
                    con.commit()
                    return {'return': '添加成功' }

@app.post("/api/getallbox")
async def getallbox(request: Request,Authorization: Optional[str] = Header(None)) :
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'requestvalue' in data:
            with sqlite3.connect('dingdan.db') as con:
                cursor = con.cursor()
                cursor.execute("SELECT boxname FROM boxinfo ")
                value = cursor.fetchall()
                if value:
                    return {'return': '查询成功','boxs':value[::-1] }
                else:
                    return {'return': '无箱号' }

@app.post("/api/danhaotobox")
async def danhaotobox(request: Request,Authorization: Optional[str] = Header(None)) :
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'danhaotobox' in data:
            data = data['danhaotobox']
            danhao = data['danhao']
            box = list(data['box'])[0]
            addtime = str(datetime.now().replace(microsecond=0))
            with sqlite3.connect('dingdan.db') as con:
                cursor = con.cursor()
                cursor.execute("SELECT * FROM alldingdan WHERE danhao=?",(danhao,))
                value = cursor.fetchall()
                print(value)
                if value:
                    # cursor.execute("SELECT * FROM allbox WHERE danhao=?", (danhao,))
                    # value = cursor.fetchall()
                    # print(value)
                    # if value:
                    #     return {'return': '单号已存在'}
                    # else:
                    update_query = f"""  
                                    UPDATE alldingdan
                                    SET xianghao = ?
                                    WHERE danhao = ?
                                    """
                    cursor.execute(update_query, (box, danhao,))
                    con.commit()
                    cursor.execute("SELECT * FROM allbox WHERE danhao=?",(danhao,))
                    value = cursor.fetchall()
                    print(value)
                    if not value:
                        cursor.execute("INSERT INTO allbox(boxname,danhao,addtime) VALUES (?,?,?)",
                                       (box,danhao,addtime,))
                        con.commit()
                        return {'return': '添加成功'}
                    else:
                        update_query = f"""  
                                        UPDATE allbox
                                        SET boxname = ?
                                        WHERE danhao = ?
                                        """
                        cursor.execute(update_query, (box, danhao,))

                        return {'return': '添加成功'}
                else:
                    return {'return': '无单号记录' }

@app.post("/api/setboxweight")
async def setboxweight(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'requestvalue' in data:
            data = data['requestvalue']
            box = list(data['box'])[0]
            weight = data['weight']
            easyprint(box,weight)
            with sqlite3.connect('dingdan.db') as con:
                cursor = con.cursor()
                cursor.execute("SELECT * FROM boxinfo WHERE boxname=?",(box,))
                value = cursor.fetchall()
                easyprint(value)
                if value:
                    update_query = f"""  
                                    UPDATE boxinfo
                                    SET boxweight = ?
                                    WHERE boxname = ?
                                    """
                    cursor.execute(update_query, (weight,box,))
                    con.commit()
                    return {'return': '修改成功'}

                else:
                    return {'return': '无箱号' }


@app.post("/api/getboxinfo")
async def getboxinfo(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'requestvalue' in data:
            data = data['requestvalue']
            box = list(data['box'])[0]
            if data['shuliang'] == 'one':
                with sqlite3.connect('dingdan.db') as con:
                    cursor = con.cursor()
                    cursor.execute("SELECT * FROM boxinfo WHERE boxname=?",(box,))
                    value = cursor.fetchall()
                    easyprint(value)
                    creattime = value[0][2]
                    weight = value[0][3]
                    status = value[0][4]
                    chukushijian = value[0][5]
                    cursor.execute("SELECT * FROM allbox WHERE boxname=?", (box,))
                    value = cursor.fetchall()
                    easyprint(value)
                    if value:
                        danhaos = []
                        for val in value:
                            danhaos.append(val[2])
                        return {'return': '获取成功','info':'有快递','creattime':creattime,
                                'weight':weight,'status':status,'danhao':danhaos,
                                'chukushijian':chukushijian}
                    else:
                        return {'return': '获取成功','info':'无快递','creattime':creattime,
                                'weight':weight,'status':status,}
@app.post("/api/boxchuku")
async def boxchuku(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        chukutime = str(datetime.now().replace(microsecond=0))
        if 'requestvalue' in data:
            data = data['requestvalue']
            box = data['box']
            with sqlite3.connect('dingdan.db') as con:
                cursor = con.cursor()
                cursor.execute("SELECT danhao FROM allbox WHERE boxname=?",(box,))
                value = cursor.fetchall()
                easyprint(value)
                if value:
                    update_query = f"""
                                    UPDATE boxinfo
                                    SET status = ?,chukutime=?
                                    WHERE boxname = ?
                                    """
                    cursor.execute(update_query, ('已出库',chukutime,box))

                    update_query = f"""
                                    UPDATE alldingdan
                                    SET status = ?,chukusj=?
                                    WHERE danhao = ?
                                    """
                    for i in value:
                        cursor.execute(update_query, ('已出库', chukutime, i[0]))

                    con.commit()
                    return {'return': '出库成功'}

                else:
                    return {'return': '修改异常' }


@app.post("/api/getviewvalue")
async def getviewvalue(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'houtairequest' in data:
            with sqlite3.connect('dingdan.db') as con:
                cursor = con.cursor()
                cursor.execute("SELECT * FROM alldingdan" )
                value = cursor.fetchall()
                cursor.execute("SELECT * FROM allbox")
                allbox = cursor.fetchall()
                cursor.execute("SELECT * FROM boxinfo")
                boxinfo = cursor.fetchall()
                if value:
                    easyprint(value)
                    return {'return': '获取成功','values':value, 'allbox':allbox, 'boxinfo':boxinfo}
                else:
                    easyprint('获取失败')
                    return {'return': '获取失败',}

@app.post("/api/statuschange")
async def statuschange(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'houtairequest' in data:
            data = data['houtairequest']
            with sqlite3.connect('dingdan.db') as con:
                update_query = f"""  
                            UPDATE alldingdan
                            SET status = ?
                            WHERE ID = ?  
                            """
                cursor = con.cursor()
                cursor.execute(update_query, (data['status'], int(data['id'])))
                con.commit()
                if cursor.rowcount > 0:
                    easyprint('修改成功')
                    return {'return': '修改成功'}

                else:
                    easyprint('修改失败')
                    return {'return': '修改失败'}

@app.post("/api/houtaichangelist")
async def houtaichangelist(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'houtairequest' in data:
            data = list((data['houtairequest'])['list'])
            with sqlite3.connect('dingdan.db') as con:
                update_query = f"""  
                            UPDATE alldingdan
                            SET leixing=?,kdgs=?,danhao=?,wpxx=?,status=?,lxhm=?,beizhu=?,tianjiasj=?,rukusj=?,chukusj=?,xianghao=?
                            WHERE ID = ?  
                            """
                cursor = con.cursor()
                cursor.execute(update_query, (data[2], data[3],data[4],data[5],data[6],data[7],data[8],
                                              data[9],data[10],data[11],data[12],int(data[0])))
                con.commit()
                if data[12] and data[12] != 'NONE':
                    print(data[4])
                    cursor.execute('SELECT * FROM allbox WHERE danhao=?',(str(data[4]),))
                    value = cursor.fetchall()
                    print(value)
                    if value:
                        update_query = f"""  
                                        UPDATE allbox
                                        SET boxname=?
                                        WHERE danhao=?  
                                        """
                        cursor.execute(update_query,(data[12],data[4]))
                    else:
                        addtime = str(datetime.now().replace(microsecond=0))
                        cursor.execute("INSERT INTO allbox(boxname,danhao,addtime) VALUES (?,?,?)",
                                       (str(data[12]), str(data[4]), addtime,))
                        con.commit()
                        if cursor.rowcount > 0:
                            easyprint('修改成功')
                            return {'return': '修改成功'}

                        else:
                            easyprint('修改失败')
                            return {'return': '修改失败'}
                elif data[12] == 'NONE':
                    cursor.execute('SELECT * FROM allbox WHERE danhao=?',(str(data[4]),))
                    value = cursor.fetchall()
                    if value:
                        cursor.execute("DELETE FROM allbox WHERE danhao=?",(str(data[4]),))
                        if cursor.rowcount > 0:
                            easyprint('修改成功')
                            return {'return': '修改成功'}

                        else:
                            easyprint('修改失败')
                            return {'return': '修改失败'}
                    else:
                        easyprint('修改成功')
                        return {'return': '修改成功'}




                if cursor.rowcount > 0:
                    easyprint('修改成功')
                    return {'return': '修改成功'}

                else:
                    easyprint('修改失败')
                    return {'return': '修改失败'}



@app.post("/api/deldingdan")
async def deldingdan(request: Request,Authorization: Optional[str] = Header(None)):
    if Authorization == 'chenjijun123':
        data = await request.json()
        easyprint(data)
        if 'houtairequest' in data:
            data = data['houtairequest']
            if data['delbox'] != 'no':
                with sqlite3.connect('dingdan.db') as con:
                    cursor = con.cursor()
                    cursor.execute('DELETE  FROM allbox WHERE danhao=?',(str(data['delbox']),))
                    con.commit()
            with sqlite3.connect('dingdan.db') as con:
                update_query = """  
                            DELETE FROM alldingdan
                            WHERE ID = ?  
                            """
                cursor = con.cursor()
                cursor.execute(update_query, ((data['id'],)))
                con.commit()
                if cursor.rowcount > 0:
                    easyprint('删除成功')
                    return {'return': '删除成功'}

                else:
                    easyprint('删除失败')
                    return {'return': '删除失败'}

        




# uvicorn.run(app = app, host = "127.0.0.1", port=80)
