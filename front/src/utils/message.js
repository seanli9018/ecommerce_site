import {Message} from "element-ui"

class ECMessage{
  constructor() {
    this.config = {
      duration: 2000,
      center: false,
      showClose: true
    }
  }

  show(){
    Message(JSON.parse(JSON.stringify(this.config)))
  }

  success(message_text="Congratulations! Successfully operation."){
    this.config.type = "success"
    this.config.message = message_text
    this.show()
  }
  info(message_text=""){
    this.config.message = message_text
    this.config.type = "info"
    this.show()
  }

  warning(message_text=""){
    this.config.message = message_text
    this.config.type = "warning"
    this.show()
  }

  error(message_text="Sorry, operation failed."){
    this.config.message = message_text
    this.config.type = "error"
    this.show()
  }
}

const message = new ECMessage()
export default message