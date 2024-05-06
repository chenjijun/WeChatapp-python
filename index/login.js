
Page({  
  data: {  
    showPopup: false,
    gimgsrc : `http://${getApp().globalData.ipaddr}/api/jiage`,
    topImgsrc : "/image/guanggao.gif",
    userName: {
      "username" : "null",
      "password": "null"},
  },  
  onLoad: function () {
    wx.request({
      url: `http://${getApp().globalData.ipaddr}/api/dlimagepath`,
      method: 'GET',
      header:{
        'custom': 'chenjijun' 
      },
      timeout: 5000,
      success: (res) => {
        if (res.data) {  
          this.setData({
            topImgsrc:res.data.return
        });
      }
    },
      fail: (err) => {
        wx.showToast({
          title: '服务器连接失败',
          icon:'error'
        })
        console.log('获取登录图片失败')   
      }
    }) 

  },

  onTap: function() {  
    // 设置按钮为激活状态  
    this.setData({  
      isButtonActive: true  
    });  
  
    // 设置0.5秒后恢复按钮原始状态  
    setTimeout(() => {  
      this.setData({  
        isButtonActive: false  
      });  
    }, 200); // 500毫秒等于0.5秒  
  }   , 
  formSubmit: function (e) {
    const formData = e.detail.value;
    const input1 = e.detail.value.username;
    const input2 = e.detail.value.password;
    var miwen = '';
    if (
      (formData.username && formData.username.length > 2 && formData.username.length <= 15) &&
      (formData.password && formData.password.length > 4 && formData.password.length <= 15) 
      ){
        
    this.setData({
        'userName.username': input1,
        'userName.password': input2,
    });
    wx.showToast({
      title: '登陆中',
      icon: 'loading',
      duration: 10000
    })
    wx.request({
      url: `http://${getApp().globalData.ipaddr}/api/login`,
      method: "POST",
      data:{
        ...this.data.userName
      },timeout: 5000,
      success:(res) =>{
        wx.hideToast()
        console.log(res.data)
        if (res.data.return == 'canpass'){
          getApp().globalData.userInfo = input1
          getApp().globalData.yhjifen = res.data.jifen
          getApp().globalData.useradmin = res.data.user
          console.log(getApp().globalData.useradmin)
          getApp().globalData.needflash = true
          wx.switchTab({
            url: '/index/index',
          });
        } else  {
          wx.showToast({
            title: '检查账户/密码',
            icon: 'error'
          });
        }
      },
      fail:(error) =>{
        wx.showToast({
          title: '服务器连接超时',
          icon: 'none'
        });
      }
    });
  }else {
    wx.showToast({
      title: '用户名需5-15字符之间\n密码需6-15个字符之间',
      icon: 'none'
    });
  }
  },
  sign: function (e) {
    
    wx.navigateTo({
      url: '/index/signup',
      
    })
  },
  onelogin:function(e){
      wx.showToast({
        title: '登录中',
        icon: 'loading',
        duration: 10000
      })
      wx.login({
        success: (res) => {
           if(res.code){
            wx.request({
              url: `http://${getApp().globalData.ipaddr}/api/wechat/yijianlogin`,
              method: 'POST',
              header:{'Authorization': 'chenjijun'},
              data:{
                code:res.code
              },timeout:5000,
              success:(res) =>{
                wx.hideToast()
                console.log(res.data)
                if (res.data.return == 'canpass'){
                  getApp().globalData.userInfo = res.data.username
                  getApp().globalData.yhjifen = res.data.jifen
                  getApp().globalData.useradmin = res.data.user
                  getApp().globalData.needflash = true
                  wx.switchTab({
                    url: '/index/index',
                  });
                }
                    if (res.data.return == 'Failed'){
                      wx.showToast({
                        title: '登陆失败',
                        icon:'error'
                      })
                    }else if(res.data.return == 'canpas'){
                      wx.showToast({
                        title: '登陆成功',
                        icon:'success'
                      })

                    }
                       
              },fail:(error) =>{
                wx.showToast({
                  title: '登陆失败',
                  icon:'error'
                })
              }
            })
           }else{
            wx.showToast({
              title: '登陆失败',
              icon:'error'
            })
           }
        },timeout:5000,
        fail:(res)=>{
          wx.showToast({
            title: '登陆失败',
            icon:'error'
          })
        }
      })
  },

  showPopupImage: function() {
    this.setData({
      showPopup: true
    });
  },
  hidePopupImage: function() {
    this.setData({
      showPopup: false
    });
  }



})