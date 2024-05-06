// index/index2.js
Page({
  data: {
    userInfo1 : 'user',
    yhjifen1: 0,
    phonerequest: {
      'user' : '',
      'content': 'finish',
    },
    dataList: '',
    dataListbackup: '',
    useradmin: '',
    showButton: false ,
    userarray: ['单号','备注信息'],
    array: ['单号','备注信息','状态','用户名'],
    index: 0,
    inputValue: '',
    sjshoudongsh: {
      'request': '',
      'time': ''
    },
    listcount: ''
  },


  myHistory : function (e) {
    var userInfo = getApp().globalData.userInfo;
    console.log(userInfo)
    this.setData({
      'phonerequest.user': userInfo,  
      'phonerequest.content': 'all' 
    });
    wx.showToast({
      title: '获取中',
      icon: 'loading',
    })
    var phonerequest = this.data.phonerequest
    wx.request({
      url: `http://${getApp().globalData.ipaddr}/api/dingdancx`,
      method:'POST',
      header:{
        'Authorization': 'chenjijun123'
      },
      data:{
        phonerequest
      },timeout:5000,
      success:(res) =>{
        if(res.data.return == '查询成功'){
          wx.hideToast()
          const newData = res.data.valuess.map((item, index) => ({  
            ...item, // 其他从网络获取的属性  
            showButton: false // 初始化为false  
          }));  
          console.log(newData)
          var len = res.data.valuess.length
        this.setData({
          dataList: newData,
          listcount: len,
          dataListbackup: newData,
        });
        wx.showToast({
          title: '查询成功',
          icon:'success',
          duration:500
        })
      }else if(res.data.return == '无提交记录'){

        wx.showToast({
          title: '无添加记录',
          icon: 'error'
        })
      }
      },fail:(error)=>{
         wx.showToast({
           title: '查询失败',
           icon: 'error'
         })
      }
    });
  },

  myHistoryfinish : function (e) {
    var userInfo = getApp().globalData.userInfo;
    console.log(userInfo)
    this.setData({
      'phonerequest.user': userInfo, 
      'phonerequest.content': 'finish'   
    });
    var phonerequest = this.data.phonerequest
    wx.showToast({
      title: '获取中',
      icon: 'loading',
    })
    wx.request({
      url: `http://${getApp().globalData.ipaddr}/api/dingdancx`,
      method:'POST',
      header:{
        'Authorization': 'chenjijun123'
      },
      data:{
        phonerequest
      },timeout:5000,
      success:(res) =>{
        if(res.data.return == '查询成功'){
          wx.hideToast()
          const newData = res.data.valuess.map((item, index) => ({  
            ...item, // 其他从网络获取的属性  
            showButton: false // 初始化为false  
          }));  
          console.log(newData)
          var len = res.data.valuess.length
          wx.showToast({
            title: '查询成功',
            icon: 'success'
          })
        this.setData({
          dataList: newData,
          listcount: len
        });
      }else if(res.data.return == '无提交记录'){

        wx.showToast({
          title: '无添加记录',
          icon: 'error'
        })
      }else if (res.data.return == '无已完成订单'){
        wx.showToast({
          title: '无已完成订单',
          icon: 'error'
        })
        this.setData({
          dataList: '',
          listcount: 0
        });
      }
      },fail:(error)=>{
         wx.showToast({
           title: '查询失败',
           icon: 'error'
         })
      }
    });
  },

  myHistoryunfinish : function (e) {
    var userInfo = getApp().globalData.userInfo;
    console.log(userInfo)
    this.setData({
      'phonerequest.user': userInfo, 
      'phonerequest.content': 'unfinish'   
    });
    var phonerequest = this.data.phonerequest
    wx.showToast({
      title: '获取中',
      icon: 'loading',
    })
    wx.request({
      url: `http://${getApp().globalData.ipaddr}/api/dingdancx`,
      method:'POST',
      header:{
        'Authorization': 'chenjijun123'
      },
      data:{
        phonerequest
      },timeout:5000,
      success:(res) =>{
        if(res.data.return == '查询成功'){
          wx.hideToast()
          const newData = res.data.valuess.map((item, index) => ({  
            ...item, // 其他从网络获取的属性  
            showButton: false // 初始化为false  
          }));  
          console.log(newData)
          var len = res.data.valuess.length
          wx.showToast({
            title: '查询成功',
            icon: 'success',
            duration: 500
          })
        this.setData({
          dataList: newData,
          listcount:len
        });
        
      }else if(res.data.return == '无提交记录'){
        wx.showToast({
          title: '无添加记录',
          icon: 'error'
        })
      }else if (res.data.return == '无未完成订单'){
        wx.showToast({
          title: '无已完成订单',
          icon: 'error'
        })
        
      }
      },fail:(error)=>{
         wx.showToast({
           title: '查询失败',
           icon: 'error'
         })
      }
    });
  },
   
  

  saomiaosh : function (e) {
    var requestvalue= {
      requestvalue : '',
      danhao : ''
    }
    var buttonName = e.currentTarget.dataset.name;
    var dataList1 = this.data.dataList
    var that = this
    wx.authorize({
      scope: 'scope.camera',
      success(){
        wx.scanCode({
          onlyFromCamera:false,
          scanType:"barCode",
          success:(res)=>{
            if(res.scanType =="CODE_128" ){
              var danhao =  res.result;
              console.log(res.result)
              wx.showModal({
                title: '请确认',
                content: `快递单号：${res.result}\r\n是否修改`,
                complete: (res) => {
                  if (res.cancel) {
                    wx.showToast({
                      title: '取消',
                      icon: 'error'
                    })
                  }
                  if (res.confirm) { 
                    wx.showToast({
                      title: '查询中',
                      icon:'loading',
                    })
                    requestvalue.danhao = danhao
                    requestvalue.requestvalue = buttonName
                    console.log(danhao)
                      wx.request({
                        url: `http://${getApp().globalData.ipaddr}/api/shouhuo`,
                        method: 'POST',
                        header: {  
                          'Authorization': 'chenjijun123' // 示例：设置授权令牌  
                        },  timeout:10000,
                        data:{
                          requestvalue
                        },
                        success: (res) => {  
                          console.log(res.data)
                          wx.hideToast()
                         if (res.data.return === '更新状态成功'){
                          console.log(res.data.return)
                          for (var i = 0; i < dataList1.length; i++) {  
                            if (dataList1[i][4] === danhao) {  
                              dataList1[i][6] = buttonName;  
                            }  
                          }
                            that.setData({  
                              dataList: dataList1
                            });  
                           wx.showToast({
                             title: '更新成功',
                             icon: 'success'
                           })
                         } else {
                           wx.showToast({
                             title: res.data.return,
                             icon:'error'
                           })

                         }
                        },  
                        fail: (error) => {  
                          wx.showToast({
                            title: '服务器错误',
                            icon: 'error'
                          }) 
                          // 在这里你可以处理错误  
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
          fail:(error)=>{
            wx.showToast({
              title: '扫描失败',
              icon: 'error'
            });
          }
        });
      }
    })
  },
  bindInput: function(e) {
    this.setData({
      inputValue: e.detail.value
    });},
  
  saomiaojc : function (e) {
    var dataList1 = this.data.dataList
    var that = this
    wx.authorize({
      scope: 'scope.camera',
      success(){
        wx.scanCode({
          onlyFromCamera:false,
          scanType:"barCode",
          success:(res)=>{
            if(res.scanType =="CODE_128" ){
              var danhao =  res.result;
              console.log(res.result)
              wx.showModal({
                title: '请确认',
                content: `快递单号：${res.result}\r\n是否修改`,
                complete: (res) => {
                  if (res.cancel) {
                    wx.showToast({
                      title: '取消',
                      icon: 'error'
                    })
                  }
                  if (res.confirm) { 
                    wx.showToast({
                      title: '查询中',
                      icon: 'loading',
                    })
                      wx.request({
                        url: `http://${getApp().globalData.ipaddr}/api/jichu`,
                        method: 'POST',
                        header: {  
                          'Authorization': 'chenjijun123' // 示例：设置授权令牌  
                        },  timeout:10000,
                        data:{
                            danhao
                        },
                        success: (res) => {  
                          wx.hideToast()
                          console.log(dataList1)
                          for (var i = 0; i < dataList1.length; i++) {  
                            if (dataList1[i][4] === danhao) {  
                              dataList1[i][6] = '已寄往国外';  
                            }  
                          }
                            that.setData({  
                              dataList: dataList1
                            });  
                         if (res.data.return === '更新状态成功'){
                           wx.showToast({
                             title: '更新成功',
                             icon: 'success'
                           })
                         } 
                        },  
                        fail: (error) => {  
                          wx.showToast({
                            title: '服务器错误',
                            icon: 'error'
                          }) 
                          // 在这里你可以处理错误  
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
          fail:(error)=>{
            wx.showToast({
              title: '扫描失败',
              icon: 'error'
            });
          }
        });
      }
    })
    
  },
  
  mohu : function (e){
    var userInfo = getApp().globalData.userInfo;
    var that = this
    const pickerValue = this.data.array[this.data.index]; // 获取 picker 组件当前选中的值  
    const inputValue = this.data.inputValue; // 获取 input 组件的值  
    // 在这里可以使用 pickerValue 和 inputValue 进行你的筛选逻辑  
    console.log('Picker 值:', pickerValue);  
    console.log('Input 值:', inputValue); 
    var value = ''
    var putvalue = {
      'user': userInfo,
    }; 
    var mohushuju = that.data.dataList
    if (inputValue){
      if (pickerValue === '用户名'){value = 'curr'}
      if (pickerValue === '单号'){value = 'danhao'}
      if (pickerValue === '状态'){value = 'status'}
      if (pickerValue === '备注信息'){value = 'beizhu'}
      putvalue[value] = inputValue;
    wx.showModal({
      title: '请确认',
      content: `筛选条件：${pickerValue}\r\n筛选内容：${inputValue}\r\n`,
      complete: (res) => {
        if (res.cancel) {      
        }
        if (res.confirm) {
          wx.showToast({
            title: '请求中',
            icon: 'loading',
            duration: 5001
          })
          if(!that.data.dataList){
          wx.request({
            url: `http://${getApp().globalData.ipaddr}/api/dingdancx`,
            method: 'POST',
            header:{
              'Authorization': 'chenjijun123'
            },
            data:{
               putvalue
            },timeout:5000,
            success:(res)=>{
              wx.hideToast()
              console.log(res.data)
              if(res.data.return == '查询成功'){
              const newData = res.data.valuess.map((item, index) => ({  
                ...item, // 其他从网络获取的属性  
                showButton: false // 初始化为false  
              }));  
              var len = newData.length
              console.log(newData)
              that.setData({
                dataList:newData,
                listcount: len,
                dataListbackup: newData,
              })
            }else if(res.data.return == '无提交记录') {
              wx.showToast({
                title: '无记录',
                icon: 'error'
              })
            }
          },fail:(error)=>{
            wx.showToast({
              title: '服务器连接异常',
              icon: 'error'
            })
          }
          })  }else{
            wx.hideToast()
            var index1 = {
              '用户名':1,
              '单号':4,
              '状态':6,
              '备注信息':7
            }
            var list1 = []
            var i = ''
            console.log(mohushuju)
            for( i of mohushuju){
                if(i[index1[pickerValue]].includes(inputValue)){
                  list1 = list1.concat(i);
                }
            }

            if(list1){
            var len = list1.length
            that.setData({
              dataList:list1,
              listcount:len
            })
          }else{
            wx.showToast({
              title: '无数据',
              icon:'error'
            })
          }


          }
        }
      }
    })
  }

  },
  bindPickerChange: function (e) {  
    // 获取用户选择的索引值  
    const index1 = e.detail.value;  
    // 你可以在这里根据索引值更新 array 或执行其他操作  
    console.log('用户选择的索引值：', index1);  
    this.setData({  
      index: index1  
    });  
  },


  onShow: function () {
    if (getApp().globalData.needflash === true){
      getApp().globalData.needflash = false
      wx.reLaunch({
        url: '/index/index2',
      })}
    var userInfo = getApp().globalData.userInfo;
    var yhjifen = getApp().globalData.yhjifen;
    var useradmin = getApp().globalData.useradmin;
    
    this.setData({
      userInfo1: userInfo,
      yhjifen1: yhjifen,
      useradmin1 : useradmin,
    });
    if (!userInfo){
      wx.showToast({
        title: '请重新登录',
        icon:'none'
      });
      wx.redirectTo({
        url: '/index/login',
      })
    }
  },
  gotobox: function(e){
     wx.navigateTo({
       url: '/index/box',
     })
  },

  toggleButton: function(e) {  
  
    const index = e.currentTarget.dataset.index; // 获取当前点击项的索引  
    const dataList = this.data.dataList;  
    // 检查索引是否有效  
    if (index >= 0 && index < dataList.length) {  
      // 切换对应项的showButton值  
      dataList[index].showButton = !dataList[index].showButton;  
      // 更新数据以触发视图重新渲染  
      this.setData({  
        dataList  
      });  
    }} ,
  
  sdruku: function(e){
    var changevalue = this.data.dataList
    var that = this
    var index = e.currentTarget.dataset.index;
    console.log(this.data.dataList[index][0])
   
    if (this.data.dataList[index][6] === '已入库'){
      wx.showToast({
        title: '重复入库',
        icon: 'error',
      })
    }else{
      this.setData({
        'sjshoudongsh.request' : this.data.dataList[index],
    
      })
      wx.showToast({
        title: '请求中',
        icon: 'loading',
      })
      
      wx.request({
        url: `http://${getApp().globalData.ipaddr}/api/sjdingdanruku`,
        method: 'POST',
        header:{
          'Authorization': 'chenjijun123'
        },timeout:5000,
        data:{
          ...this.data.sjshoudongsh
        },success:(e)=>{
          wx.hideToast()
          if(e.data.return != '修改成功'){
            wx.showToast({
              title: e.data.return,
              icon:'error'
            })
          }else{
           
              wx.showToast({
                title: '修改成功',
                icon: 'success'
              })
              changevalue[index][6] = '已入库'
              changevalue[index][10] = e.data.time
               that.setData({
        dataList: changevalue
      });
          }
        },fail:(e)=>{    
            wx.showToast({
              title: '连接错误',
              icon:'error'
            })    
        }
      }) 
    }
  },
  sdchuku: function(e){
    var changevalue = this.data.dataList
    var that = this
    var index = e.currentTarget.dataset.index;
   
    if (this.data.dataList[index][6] === '已出库'){
      wx.showToast({
        title: '重复入库',
        icon: 'error',
      })
    }else{
      this.setData({
        'sjshoudongsh.request' : this.data.dataList[index],
    
      })
      wx.showToast({
        title: '请求中',
        icon: 'loading',
      })
      
      wx.request({
        url: `http://${getApp().globalData.ipaddr}/api/sjdingdanchuku`,
        method: 'POST',
        header:{
          'Authorization': 'chenjijun123'
        },timeout:5000,
        data:{
          ...this.data.sjshoudongsh
        },success:(e)=>{
          wx.hideToast()
          if(e.data.return != '修改成功'){
            wx.showToast({
              title: e.data.return,
              icon:'error'
            })
          }else{
           
              wx.showToast({
                title: '修改成功',
                icon: 'success'
              })
              changevalue[index][6] = '已出库'
              changevalue[index][11] = e.data.time
               that.setData({
        dataList: changevalue
      });
          }
        },fail:(e)=>{    
            wx.showToast({
              title: '连接错误',
              icon:'error'
            })    
        }
      }) 
    }
  },
  reset: function(e){
   var len = this.data.dataListbackup.length
    this.setData({
      dataList : this.data.dataListbackup,
      listcount:len
    })
  },
  





  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */


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