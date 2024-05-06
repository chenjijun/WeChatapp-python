App(
  {
    globalData: {
      userInfo: '',
      yhjifen: '',
      useradmin: '',
      needflash: false,
      ipaddr: '144.22.61.220:8070'
    }
  },
  {
  onLaunch: function () {
    this.globalData.userInfo = '';
    this.globalData.yhjifen = '';
    this.globalData.useradmin = '';
    this.globalData.needflash = false;
  },
 
    
  }
)
