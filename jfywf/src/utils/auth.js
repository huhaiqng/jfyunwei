import Cookies from 'js-cookie'

// tonken
export function getToken() {
  return Cookies.get('access_token')
}

export function setToken(token) {
  return Cookies.set('access_token', token)
}

export function removeToken() {
  return Cookies.remove('access_token')
}

// refresh_token
export function getRefreshToken() {
  return Cookies.get('refresh_token')
}

export function setRefreshToken(token) {
  return Cookies.set('refresh_token', token)
}

export function removeRefreshToken() {
  return Cookies.remove('refresh_token')
}

// userNmae
export function setUserName(username) {
  return Cookies.set('FA0zrJIe', username)
}

export function removeUserName() {
  return Cookies.remove('FA0zrJIe')
}

export function getUserName() {
  return Cookies.get('FA0zrJIe')
}

// userInfo
export function setUserInfo(userInfo) {
  return Cookies.set('userInfo', userInfo)
}

export function getUserInfo() {
  return Cookies.get('userInfo')
}

export function removeUserInfo(userInfo) {
  return Cookies.remove('userInfo')
}
