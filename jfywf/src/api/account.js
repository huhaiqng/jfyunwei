import request from '@/utils/request'

export function getAccounts(query) {
  return request({
    url: '/api/accounts/',
    method: 'get',
    params: query
  })
}
export function addAccount(data) {
  return request({
    url: '/api/accounts/',
    method: 'post',
    data
  })
}
export function updateAccount(data) {
  return request({
    url: `/api/accounts/${data.id}/`,
    method: 'put',
    data
  })
}
export function deleteAccount(id) {
  return request({
    url: `/api/accounts/${id}/`,
    method: 'delete'
  })
}
