一个简单的包裹登记程序（未完成），使用微信小程序做前端，python FASTAPI+UVICORN做后端，python tkinter做管理端，
服务器使用 Oracle Always Free centos8 1G/1核（使用request 进行多线程测试同时发送500次新增订单请求未丢失）

 微信小程序端使用JavaScript，可注册账号密码进行登录OR调用微信OPENID自动创建账号（3个随机字符+5个随机数字）一键登录，
 管理员账号通过账户密码登录，账号密码验证通过后端服务器sqlite内容进行验证（未对密码进行加密）
 登录后使用header内固定字段进行验证（后期修改为登录成功获取随机验证信息进行对比验证）
 小程序内管理员可修改货物状态，查询所有货物，将货物加入箱号中
 可点击首页图片可跳出价格图片
 使用微信条码扫描接口实现使用摄像头/相册图片自动识别输入快递单号

 tkinter管理可操作订单、账号、箱信息等

微信小程序：

![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/087ea6b9-0270-43f9-87a4-82cae31a3485)
![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/4b4e8d2f-b5ac-4c1e-8d5b-d94f07ba5d38)
![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/9a6cde48-df87-4f4c-aa0f-3f62ab0bcdb1)
![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/f716058e-61b1-4002-9dc4-32be3b1ac454)

python-tkinter：

![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/36115c62-d127-4afb-a638-09810d866eb2)
![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/494e734f-fe07-4faa-a029-280c513f96d5)
![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/fa25587f-46f7-4d89-92c8-58c316ecaab1)

SQLite：

![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/b1b21d16-8f05-40b0-91cb-edf29c643c6c)


