import request from '@/utils/request'

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
