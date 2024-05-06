


Page({  
  data: {topImgsrc : "/image/guanggao.gif",  
         userInfo1 : '',
         kddh : '',
         tijiaoshuju: {
          leixing: '',
          user : '',
          kdgs: '',
          danhao : '',
          lxhm : '',
          wpxx : '',
          beizhu : '',
          tianjiasj: '',
        },
        kdType: '',

  },  
  kdTypeChange: function (e) {
    this.setData({
      kdType: e.detail.value
    });
    console.log(e.detail.value)
  },
  onLoad: function () {
    var userInfo = getApp().globalData.userInfo;
    // 设置文本显示
    this.setData({
      userInfo1: userInfo
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
    wx.request({
      url: `http://${getApp().globalData.ipaddr}/api/syimagepath`,
      header:{
        'custom': 'chenjijun' 
      },
      timeout: 10000,
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
      }
    }) 
  },
  

  tuiChu: function (e) {
    wx.redirectTo({
      url: '/index/login',
    })
  },
  handleSubmit:function (e) {
    console.log(e.detail.value)
    const formData = e.detail.value;
    var userInfo = getApp().globalData.userInfo;
    if (
      (formData.kdgs && formData.kdgs.length > 1 && formData.kdgs.length <= 10) &&
      (formData.danhao && formData.danhao.length > 5 && formData.danhao.length <= 30)&&
      (formData.lxhm && formData.lxhm.length > 5 && formData.lxhm.length <= 30)&&
      (formData.kdType.length > 1)
      ){
        wx.showModal({
          title: '请确认登记信息',
          content: `类型：${formData.kdType}\r\n快递公司：${formData.kdgs}
          快递单号：${formData.danhao}\r\n物品信息：${formData.wpxx}
          联系号码：${formData.lxhm}\r\n备注：${formData.beizhu}`,
          complete: (res) => {
            if (res.cancel) {
              wx.showToast({
                title: '取消',
                icon: 'error'
              })
            }
            if (res.confirm) {
              let now = new Date(); // 创建一个新的Date对象  
              now.setMilliseconds(0); // 设置毫秒为0  
              let nowtime = now.toLocaleString('zh-CN', { hour12: false }).replace(/\//g, '-').replace(/上午|下午/, ' ');  
              this.setData({
                'tijiaoshuju.leixing' : formData.kdType,
                'tijiaoshuju.user' : userInfo,
                'tijiaoshuju.kdgs' : formData.kdgs,
                'tijiaoshuju.danhao' : formData.danhao,
                'tijiaoshuju.lxhm' : formData.lxhm,
                'tijiaoshuju.wpxx' : formData.wpxx,
                'tijiaoshuju.beizhu' : formData.beizhu,
                'tijiaoshuju.tianjiasj': nowtime,
            });  
            console.log(this.data.tijiaoshuju)
            wx.request({
              url: `http://${getApp().globalData.ipaddr}/api/adddingdan`,
              method: 'POST',
              header:{
                'Authorization': 'chenjijun'
              },
              data: {
                ...this.data.tijiaoshuju
              },timeout: 5000,
              success:(res) =>{
                console.log(res.data)
                if (res.data.return == '单号已存在'){
                    wx.showToast({
                      title: '添加失败，单号已存在',
                      icon:'none'
                    })
                }else if (res.data.return == '添加成功') {
                  wx.showToast({
                    title: '添加成功',
                    icon: 'success'
                });
              }else if (res.data.return == '添加失败') {
                wx.showToast({
                  title: '添加失败',
                  icon: 'error'
              });
            }
              },
            fail:(error) =>{ 
                wx.showToast({  
                  title: '请求超时，请检查网络连接',  
                  icon: 'none'  
                });        
            }
            });
            }
          }
        });
        
    }else{
        wx.showToast({
          title: '信息异常',
          icon: 'error'
        })
      }
  
  },
  jiage: function(){
      
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
              wx.showToast({
                title: '扫描成功',
              });
              console.log(res.result)
              that.setData({  
                kddh: res.result
              }); 
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
    
  }
    

});