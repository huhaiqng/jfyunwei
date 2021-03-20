import request from '@/utils/request'

export function getGaingon666Domain(data) {
  return request({
    url: '/api/getGaingon666Domain/',
    method: 'get',
    params: data
  })
}

export function getGaingon666DomainRecord(data) {
  return request({
    url: '/api/getGaingon666DomainRecord/',
    method: 'get',
    params: data
  })
}

export function getLingfannaoDomain(data) {
  return request({
    url: '/api/getLingfannaoDomain/',
    method: 'get',
    params: data
  })
}

export function getLingfannaoDomainRecord(data) {
  return request({
    url: '/api/getLingfannaoDomainRecord/',
    method: 'get',
    params: data
  })
}
