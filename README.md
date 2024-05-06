一个简单的包裹登记程序（未完成），使用微信小程序做前端，python FASTAPI+UVICORN做后端，python tkinter做管理端，服务器使用 Oracle Always Free centos8 1G/1核（使用request 进行多线程测试同时发送500次新增订单请求未丢失）

 微信小程序端使用JavaScript，可注册账号密码进行登录OR调用微信OPENID自动创建账号（3个随机字符+5个随机数字）一键登录，
 管理员账号通过账户密码登录，账号密码验证通过后端服务器sqlite内容进行验证（未对密码进行加密）
 小程序内管理员可修改货物状态，查询所有货物，将货物加入箱号中
 
 可点击首页图片可跳出价格图片
 使用微信条码扫描接口实现使用摄像头/相册图片自动识别输入快递单号

微信小程序：

![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/087ea6b9-0270-43f9-87a4-82cae31a3485)
![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/4b4e8d2f-b5ac-4c1e-8d5b-d94f07ba5d38)
![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/9a6cde48-df87-4f4c-aa0f-3f62ab0bcdb1)
![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/b2e91724-a5a7-47ec-8081-2a459358b2a5)
![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/f716058e-61b1-4002-9dc4-32be3b1ac454)
![image](https://github.com/chenjijun/WeChatapp-python/assets/5528543/925386af-2eb6-48f5-b0a2-cb6b28036308)


