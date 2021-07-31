import request from '@/utils/request'

// Host
export function getHosts(query) {
  return request({
    url: '/api/getHosts/',
    method: 'get',
    params: query
  })
}
export function addHost(data) {
  return request({
    url: '/api/hosts/',
    method: 'post',
    data
  })
}
export function updateHost(data) {
  return request({
    url: `/api/hosts/${data.id}/`,
    method: 'put',
    data
  })
}
export function deleteHost(id) {
  return request({
    url: `/api/hosts/${id}/`,
    method: 'delete'
  })
}

// 环境
export function getEnv() {
  return request({
    url: '/api/getEnv/',
    method: 'get'
  })
}

// MySQL
export function getMySQL(query) {
  return request({
    url: '/api/mysql/',
    method: 'get',
    params: query
  })
}
export function addMySQL(data) {
  return request({
    url: '/api/mysql/',
    method: 'post',
    data
  })
}
export function updateMySQL(data) {
  return request({
    url: `/api/mysql/${data.id}/`,
    method: 'put',
    data
  })
}
export function deleteMySQL(id) {
  return request({
    url: `/api/mysql/${id}/`,
    method: 'delete'
  })
}

// Config
export function getConfig(query) {
  return request({
    url: '/api/getConfig/',
    method: 'get',
    params: query
  })
}
export function addConfig(data) {
  return request({
    url: '/api/config/',
    method: 'post',
    data
  })
}
export function updateConfig(data) {
  return request({
    url: `/api/config/${data.id}/`,
    method: 'put',
    data
  })
}
export function deleteConfig(id) {
  return request({
    url: `/api/config/${id}/`,
    method: 'delete'
  })
}

// Project
export function getProjectInfo() {
  return request({
    url: '/api/getProjectInfo/',
    method: 'get'
  })
}
export function getOneProjectInfo(id) {
  return request({
    url: `/api/project/${id}/`,
    method: 'get'
  })
}
export function getProjectForConfig() {
  return request({
    url: '/api/project-for-config/',
    method: 'get'
  })
}
export function getProjectMain(query) {
  return request({
    url: '/api/project-main/',
    method: 'get',
    params: query
  })
}

// Task
export function getTaskResult(data) {
  return request({
    url: '/api/taskresult/',
    method: 'get',
    params: data
  })
}
