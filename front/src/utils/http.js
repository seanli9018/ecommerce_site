import axios from "axios"
import auth from "./auth"
import router from "../routes"
const BASE_URL = "http://127.0.0.1:8000"

class Http{
  constructor() {
    this.http = axios.create({
      baseURL: BASE_URL,
      timeout: 2000,
      headers: {'X-Requested-With': 'XMLHttpRequest'}
    });
    this.http.interceptors.request.use(config => {
      const token = auth.token
      if (token) {
        config.headers.common.Authorization = "JWT " + token;
      }
      return config
    }), error => {
      return Promise.reject(error)
    };
    this.http.interceptors.response.use(response => {
      return response
    }), error =>  {
      if(error == 403){
        auth.clearUserToken()
        router.push('/login')
        this.$message.error("Please try to log in again!")
      } else if(error == 400){
        this.$message.error("Please provide valid form data!")
      } else{
        this.$message.error("Error 500, server error!")
      }
    };
  }

  login(params) {
    const url = "/login/"
    return this.http.post(url, params)
  }

  sendCaptcha(params) {
    const url = "/captcha/"
    return this.http.post(url, params)
  }

  register(data) {
    const url = "/register/"
    return this.http.post(url, data)
  }
}

export default new Http()