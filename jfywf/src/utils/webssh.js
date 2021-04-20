import { decrypt } from '@/utils/aes'

export function sshConnectHost(host) {
  var hostname = 'hostname' + '=' + host.ip
  var username = 'username' + '=' + host.admin
  var password = 'password' + '=' + decrypt(host.password)
  window.open('http://127.0.0.1:8888/?' + hostname + '&' + username + '&' + password)
}
