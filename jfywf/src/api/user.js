import request from '@/utils/request'

export function login(data) {
  var loginData = new FormData()
  loginData.append('username', data.username)
  loginData.append('password', data.password)
  loginData.append('grant_type', 'password')
  loginData.append('scope', 'write')
  loginData.append('client_id', 'QtAHW8JbkYA3dOgEzTjn2veQphnplznzeE6A8kDk')
  loginData.append('client_secret', 'ON01I8ocs6zSQQOP32vecYvGY3eDc8Q7C2w2soXOk8e2TcL4i9wrUImwQ7E9b3ncbskTVGaOj2wjN0T0gi46iiyjftFuWEqYWGtLOCcnyuw1a8u2VVISon3OyPOEDWsR')

  return request({
    url: '/api/o/token/',
    method: 'post',
    data: loginData
  })
}

export function refreshToken(token) {
  var refreshTokenData = new FormData()
  refreshTokenData.append('grant_type', 'refresh_token')
  refreshTokenData.append('refresh_token', token)
  refreshTokenData.append('client_id', 'QtAHW8JbkYA3dOgEzTjn2veQphnplznzeE6A8kDk')
  refreshTokenData.append('client_secret', 'ON01I8ocs6zSQQOP32vecYvGY3eDc8Q7C2w2soXOk8e2TcL4i9wrUImwQ7E9b3ncbskTVGaOj2wjN0T0gi46iiyjftFuWEqYWGtLOCcnyuw1a8u2VVISon3OyPOEDWsR')

  return request({
    url: '/api/o/token/',
    method: 'post',
    data: refreshTokenData
  })
}

export function getUserInfo(data) {
  return request({
    url: '/api/user/',
    method: 'get',
    params: data
  })
}

export function getL1Menu() {
  return request({
    url: '/api/getL1Menu/',
    method: 'get'
  })
}

export function getL2Menu(data) {
  return request({
    url: '/api/getL2Menu/',
    method: 'get',
    params: data
  })
}

export function getUserHostedInfo() {
  return request({
    url: '/api/getUserHostedInfo/',
    method: 'get'
  })
}
