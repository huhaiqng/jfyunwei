import request from '@/utils/request'

// Host
export function getHosts(query) {
  return request({
    url: '/api/hosts/',
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

// MySQL 实例
export function getMySQLInstance(query) {
  return request({
    url: '/api/mysqlInstance/',
    method: 'get',
    params: query
  })
}
export function addMySQLInstance(data) {
  return request({
    url: '/api/mysqlInstance/',
    method: 'post',
    data
  })
}
export function updateMySQLInstance(data) {
  return request({
    url: `/api/mysqlInstance/${data.id}/`,
    method: 'put',
    data
  })
}
export function deleteMySQLInstance(id) {
  return request({
    url: `/api/mysqlInstance/${id}/`,
    method: 'delete'
  })
}
export function getProjectInfo() {
  return request({
    url: '/api/getProjectInfo/',
    method: 'get'
  })
}

export function getTaskResult(data) {
  return request({
    url: '/api/taskresult/',
    method: 'get',
    params: data
  })
}
