import request from '@/utils/gitlab-request'

export function getGitLabProjects(data) {
  return request({
    url: '/api/v4/projects/',
    method: 'get',
    params: data
  })
}
