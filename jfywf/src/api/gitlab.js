import request from '@/utils/gitlab-request'

export function getGitLabProjects(data) {
  return request({
    url: '/api/v4/projects/',
    method: 'get',
    params: data
  })
}

export function getGitLabGroups(data) {
  return request({
    url: '/api/v4/groups/',
    method: 'get',
    params: data
  })
}

export function getGitLabGroupProjects(id) {
  return request({
    url: `/api/v4/groups/${id}/projects`,
    method: 'get',
    params: { 'per_page': 100 }
  })
}
