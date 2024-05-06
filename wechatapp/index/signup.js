// index/signup.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userName: {
      "username" : "null",
      "password": "null",
      "find": "null"
    },

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  },
  onSign: function (e) {
    const formData = e.detail.value;
    console.log(formData);
    const input1 = e.detail.value.username;
    const input2 = e.detail.value.password;
    const input3 = e.detail.value.password2;
    const input4 = e.detail.value.find;
    if (
      (formData.username && formData.username.length > 2 && formData.username.length <= 15) &&
      (formData.password && formData.password.length > 5 && formData.password.length <= 15)&&
      (formData.password2 && formData.password2.length > 5 && formData.password2.length <= 15)&&
      (formData.find && formData.find.length > 4 && formData.find.length <= 11)&&
      (formData.password === formData.password2)
      ){
        wx.showModal({
          title: '提示',
          content: '是否确认注册',
          complete: (res) => {
            if (res.cancel) {
              wx.showToast({
                title: '取消注册',
                icon: 'error'
              })
            }
            if (res.confirm) {
              if (!formData.username.includes('admin')){
              delete formData.password2;
              wx.showToast({
                title: '注册中',
                icon: 'loading',
                duration: 10000
              })
              wx.request({
                url: `http://${getApp().globalData.ipaddr}/api/zhuceuser`,
                method: "POST",
                data :{
                    formData
                },header: {  
                  'Authorization': 'chenjijun' // 示例：设置授权令牌  
                },  timeout:10000,
                success:(res)=>{
                  console.log(res.data)
                  wx.hideToast()
                  if (res.data.return == 'addsuccess'){
                    wx.showToast({
                      title: '注册成功',
                      icon: "success",
                    });
                  }else if (res.data.return == 'userhaved'){
                    wx.showToast({
                      title: '相同用户名已存在',
                      icon: "none",
                    });
                  }else if (res.data.return == '邀请码错误'){
                    wx.showToast({
                      title: '邀请码错误',
                      icon: 'error',
                    });
                  }else if (res.data.detail== "Not Found"){
                    wx.showToast({
                      title: '连接错误',
                      icon: 'error',
                    });
                  }else if (res.data.return == 'cuowucangshu'){
                    wx.showToast({
                      title: '错误',
                      icon: 'error',
                    });
                  }
                },
                fail:(error)=>{
                  {console.log('cuowu')
                  wx.showToast({
                    title: '连接超时失败',
                    icon: "error",
                  });}
                }
              }
              );}else{console.log('yiyouadmin')}
              
            }
          }
        })
        
      }
      else{
        wx.showToast({
          title: '请确认输入内容',
          icon: 'none'
        });
      }
  }
})