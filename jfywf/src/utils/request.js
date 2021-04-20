import axios from 'axios'
import { Message } from 'element-ui'
import store from '@/store'
import { getToken } from '@/utils/auth'
// import router from '@/router'

// create an axios instance
const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 30000 // request timeout
})

// request interceptor
service.interceptors.request.use(
  config => {
    if (config.url !== '/api/o/token/') {
      config.headers['Authorization'] = 'Bearer ' + getToken()
    }
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
    const res = response.data
    return res
  },
  error => {
    if (error.response.status === 401) {
      store.dispatch('user/resetToken')
    } else if (error.response.status >= 400) {
      Message({
        message: error.response.data,
        type: 'warning'
      })
    } else if (error.response.status >= 500) {
      Message({
        message: '后端服务器出错！',
        type: 'warning'
      })
    }
    return Promise.reject(error)
  }
)

export default service
