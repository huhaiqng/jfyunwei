const getters = {
  sidebar: state => state.app.sidebar,
  device: state => state.app.device,
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  name: state => state.user.name,
  userInfo: state => state.user.userInfo,
  permission_routes: state => state.permission.routes,
  permission_add_routes: state => state.permission.addRoutes
}
export default getters
