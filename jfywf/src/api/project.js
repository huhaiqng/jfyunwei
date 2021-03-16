import request from '@/utils/request'

export function getProjectInfo() {
  return request({
    url: '/api/getProjectInfo/',
    method: 'get'
  })
}
