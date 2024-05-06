// index/box.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
      inputValue: '',
      request:{
           boxname:'',
      },
      allboxvalues:[],
      index: 0,
      showsetbox:false,
      showboxin:false,
      inputweight:'',
      showboxinfo:false,
      boxinfo:{
        'weight':'',
        'danhao':[],
        'creattime':'',
        'status':'',
        'chukushijian':''
      },
      danhaolist:''
  },
  inputChange:function(e){
  this.setData({
    inputValue: e.detail.value
  });
 },
 weightChange:function(e){
  this.setData({
    inputweight: e.detail.value
  });
 },

  addbox: function(e){
    var value = this.data.inputValue
    var requestvalue = this.data.request
    if (value){
      wx.showModal({
        title: '请确认是否添加如下箱号',
        content: value,
        complete: (res) => {
          if (res.cancel) {
            wx.showToast({
              title: '取消操作',
              icon:'error'
            });
          }
          if (res.confirm) {
            this.setData({  
              request: {  
                boxname: value  
              }  
            });  
            console.log(this.data.request);
            wx.request({
              url: `http://${getApp().globalData.ipaddr}/api/addbox`,
              method: 'POST',
              header:{
                'Authorization': 'chenjijun123'
              },
              timeout: 10000,
              data:{
                  ...this.data.request
              },
              success:(res)=>{
                console.log(res.data.return)
                if(res.data.return == '添加成功'){
                  wx.showToast({
                    title: '添加成功',
                    icon:'success'
                  });
                }else if(res.data.return == '箱号已存在'){
                  wx.showToast({
                    title: '箱号已存在',
                    icon:'error'
                  });
                }else{
                  wx.showToast({
                    title: '添加失败',
                    icon:'error'
                  })  

                }
              },fail:(e)=>{
                wx.showToast({
                  title: '添加失败',
                  icon:'error'
                })
              }
            })
          }
        }
      })

    }else{
      wx.showToast({
        title: '请输入',
        icon:'error'
      })
    }
  },
  getallbox: function(e) {
    var requestvalue = {'request':'getallbox'}
    var that = this
    wx.request({
      url: `http://${getApp().globalData.ipaddr}/api/getallbox`,
      method: 'POST',
      header:{
        'Authorization': 'chenjijun123'
      },
      timeout: 10000,
      data:{
        requestvalue
      },success:(res)=>{
        if(res.data.return == '查询成功'){
          wx.showToast({
            title: '获取成功',
            icon:'success'
          })
          that.setData({
            allboxvalues : res.data.boxs,
            index : 0
          })


        }else{
          wx.showToast({
            title: '获取失败',
            icon:'error'
          })
        }
       
      },fail:(res)=>{
        wx.showToast({
          title: '获取失败',
          icon:'error'
        })
      }
  })},
  bindPickerChange: function (e) {  
    // 获取用户选择的索引值  
    const index1 = e.detail.value;  
    // 你可以在这里根据索引值更新 array 或执行其他操作  
    console.log('用户选择的索引值：', index1);  
    this.setData({  
      index: index1  
    });  
  },
  saoMiao: function () {
    var that = this; 
    wx.authorize({
      scope: 'scope.camera',
      success(){
        wx.scanCode({
          onlyFromCamera:false,
          scanType:"barCode",
          success:(res)=>{
            if(res.scanType =="CODE_128" ){
              var danhao = res.result
              wx.showModal({
                title: '是否提交该单号入箱',
                content: danhao   ,
                complete: (res) => {
                  if (res.cancel) {
                    wx.showToast({
                      title: '用户取消',
                      icon:'error'
                    })
                    
                  }
              
                  if (res.confirm) {
                    console.log(res.result)
                    const danhaotobox = {
                      'danhao': danhao,
                      'box': that.data.allboxvalues[that.data.index]
                    }
                    wx.request({
                      url: `http://${getApp().globalData.ipaddr}/api/danhaotobox`,
                      method:'POST',
                      header:{
                        'Authorization': 'chenjijun123'
                      },
                      timeout:10000,
                      data:{
                        danhaotobox
                      },success:(res)=>{
                        if(res.data.return == '添加成功'){
                          wx.showToast({
                            title: '入箱成功',
                            icon:'success'
                          })

                        }else if(res.data.return == '无单号记录'){
                         wx.showToast({
                           title: '单号未入库',
                           icon:'error'
                         })
                        }else if(res.data.return == '单号已存在'){
                          wx.showToast({
                            title: '单号已存在',
                            icon:'error'
                          })
                         }else{
                          wx.showToast({
                            title: '操作失败',
                            icon:'error'
                          })
                        }

                      },fail:(res)=>{
                        wx.showToast({
                          title: '操作失败',
                          icon:'error'
                        })

                      }
                    })     
                        }
                      }
                    })
            }else{
              wx.showToast({
                title: '扫描失败',
              });
            }
          },
          fail(){
            wx.showToast({
              title: '扫描失败',
              icon: 'error'
            });
          }
        });
      }
    })
    
  },
  showview:function(e){
      this.setData({
        showsetbox:true
      })
  },
  hideview:function(e){
    this.setData({
      showsetbox:false
    })
  },
  setboxweight: function(e){
    const weightvalue = this.data.inputweight
    const xianghao = this.data.allboxvalues[this.data.index]
    const requestvalue = {'box':xianghao,
    'weight':weightvalue+'KG'
    }
    if(weightvalue){
      wx.showModal({
        title: '请确认',
        content: '箱号：'+xianghao+'重量:'+weightvalue+'KG',
        complete: (res) => {
          if (res.cancel) {
            wx.showToast({
              title: '操作取消',
              icon:'error'
            })
          }
          if (res.confirm) {
            console.log(requestvalue)
            wx.request({
              url: `http://${getApp().globalData.ipaddr}/api/setboxweight`,
              method: 'POST',
              header:{
                'Authorization': 'chenjijun123'
              },
              timeout: 5000,
              data:{
                  requestvalue
              },success:(res)=>{
                if(res.data.return =='修改成功' ){
                  wx.showToast({
                    title: '修改成功',
                    icon:'success'
                  })
                }else{
                  wx.showToast({
                    title: '修改失败',
                    icon:'error'
                  })

                }

              },fail:(res)=>{
                wx.showToast({
                  title: '修改失败',
                  icon:'error'
                })
              }
            })
            
          }
        }
      })
    }else{
      wx.showToast({
        title: '请输入重量',
        icon:'error'
      })
    }
  },
  showboxxinxi:function(e){

    const xianghao = this.data.allboxvalues[this.data.index]
    const requestvalue = {'box':xianghao,
    'shuliang':'one'
    }
    var that = this
    if(xianghao){
      wx.request({
        url: `http://${getApp().globalData.ipaddr}/api/getboxinfo`,
        method: 'POST',
        header:{
          'Authorization': 'chenjijun123'
        },
        timeout: 5000,
        data:{
            requestvalue
        },success:(res)=>{
          if(res.data.return == '获取成功'&& res.data.info =='有快递'){
            that.setData({
              showboxin:true,
              'boxinfo.weight':res.data.weight,
              'boxinfo.status':res.data.status,
              'boxinfo.danhao':res.data.danhao,
              'boxinfo.creattime':res.data.creattime,
              'boxinfo.chukushijian':res.data.chukushijian
            })
            console.log(that.data.boxinfo)
          }else if(res.data.return == '获取成功'&& res.data.info =='无快递'){
            that.setData({
              showboxin:true,
              'boxinfo.weight':res.data.weight,
              'boxinfo.status':res.data.status,
              'boxinfo.creattime':res.data.creattime,
              'boxinfo.danhao':['无快递'],
            })

          }
          else{
            wx.showToast({
              title: '获取失败',
              icon:'error'
            })
          }

        },fail:(res)=>{
          wx.showToast({
            title: '获取失败',
            icon:'error'
          })
        }
    })
  }},
  hideboxxinxi: function(e){
    this.setData({
      showboxin:false
    })
  },
  xiangchuku:function(e){
    const chukuxianghao = this.data.allboxvalues[this.data.index]

    wx.showModal({
      title: '是否出库',
      content: '箱号：'+chukuxianghao[0],
      complete: (res) => {
        if (res.cancel) {
          wx.showToast({
            title: '操作取消',
            icon:'error'
          })
        }
    
        if (res.confirm) {
          const requestvalue = {
            'box':chukuxianghao[0],
          }
          wx.request({
            url: `http://${getApp().globalData.ipaddr}/api/boxchuku`,
        method: 'POST',
        header:{
          'Authorization': 'chenjijun123'
        },
        timeout: 5000,
        data:{
            requestvalue
        },success:(res)=>{
          if(res.data.return == '出库成功'){
            wx.showToast({
              title: '出库成功',
              icon:'success'
            })
          }else{
            wx.showToast({
              title: '出库失败',
              icon:'error'
            })

          }

        },fail:(res)=>{
          wx.showToast({
            title: '出库失败',
            icon:'error'
          })
        }
          })
          
          
        }
      }
    })

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
      this.getallbox()
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

  }
})