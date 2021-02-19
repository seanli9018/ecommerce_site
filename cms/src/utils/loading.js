import {Loading} from "element-ui"

class ECLoading{
  constructor() {
    this.config = {
      fullscreen: true,
      text: "Loading",
      background: 'rgba(0, 0, 0, 0.7)'
    }
  }

  show(){
    this.loading = Loading.service(this.config)
  }

  close(){
    this.loading.close()
  }
}

export default new ECLoading()