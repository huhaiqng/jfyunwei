import request from '@/utils/request'

export function getAddress() {
  return request({
    url: '/api/address/',
    method: 'get'
  })
}

export function getProject() {
  return request({
    url: '/api/project/',
    method: 'get'
  })
}
