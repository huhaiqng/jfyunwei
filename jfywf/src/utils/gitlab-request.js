import axios from 'axios'
import { Message } from 'element-ui'
// import router from '@/router'

// create an axios instance
const service = axios.create({
  baseURL: 'http://192.168.40.9', // url = base url + request url
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 30000 // request timeout
})

// request interceptor
service.interceptors.request.use(
  config => {
    config.headers['PRIVATE-TOKEN'] = 'p64dE1TA-sKzZfCh-vFR'
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

// response interceptor
service.interceptors.response.use(
  /**
   * If you want to get http information such as headers or status
   * Please return  response => response
  */

  /**
   * Determine the request status by custom code
   * Here is just an example
   * You can also judge the status by HTTP Status Code
   */
  response => {
    return response
  },
  error => {
    Message({
      message: '后端服务器出错！',
      type: 'warning'
    })
    return Promise.reject(error)
  }
)

export default service
