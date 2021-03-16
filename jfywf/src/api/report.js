import request from '@/utils/request'

// Daily API
export function getDaily(data) {
  return request({
    url: '/api/daily/',
    method: 'get',
    params: data
  })
}

export function addDaily(data) {
  return request({
    url: '/api/daily/',
    method: 'post',
    data
  })
}

export function updateDaily(data) {
  return request({
    url: `/api/daily/${data.id}/`,
    method: 'put',
    data
  })
}

export function deleteDaily(id) {
  return request({
    url: `/api/daily/${id}`,
    method: 'delete'
  })
}

// Daily API
export function getReportDaily(data) {
  return request({
    url: '/api/getReportDaily/',
    method: 'get',
    params: data
  })
}
