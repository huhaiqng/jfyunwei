<template>
  <div>
    <el-scrollbar class="elsc">
      <div class="drawer-container">
        <div>
          <h3 class="drawer-title">详情</h3>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">显示名称：</el-col>
              <el-col :span="12">{{ host.name }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">主机名：</el-col>
              <el-col :span="12">{{ host.hostname }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">内网 IP：</el-col>
              <el-col :span="12">{{ host.inside_ip }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">外网 IP：</el-col>
              <el-col :span="12">{{ host.outside_ip }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">内网端口号：</el-col>
              <el-col :span="12">{{ host.inside_port }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">外网端口号：</el-col>
              <el-col :span="12">{{ host.outside_port }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">系统：</el-col>
              <el-col :span="12">{{ host.os }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">CPU 核数：</el-col>
              <el-col :span="12">{{ host.cpu }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">内存大小：</el-col>
              <el-col :span="12">{{ host.memory }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">硬盘大小：</el-col>
              <el-col :span="12">{{ host.disk }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">位置：</el-col>
              <el-col :span="12">{{ host.cloud }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">云账号：</el-col>
              <el-col :span="12">{{ host.cloud_user }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">环境：</el-col>
              <el-col :span="12">{{ host.env }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">用户：</el-col>
              <el-col :span="12">{{ host.user }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">密码：</el-col>
              <el-col :span="12">{{ host.password }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">创建时间：</el-col>
              <el-col :span="12">{{ host.created | parseTime('{y}-{m}-{d} {h}:{m}') }}</el-col>
            </el-row>
          </div>

        </div>
      </div>
    </el-scrollbar>
  </div>
</template>

<script>
export default {
  name: 'HostDrawerContent',
  props: {
    host: { type: Object, default: null }
  }
}
</script>

<style lang="scss" scoped>
$bg:#2d3a4b;
$dark_gray:#889aa4;
$light_gray:#eee;

.show-pwd {
  position: absolute;
  right: 41%;
  font-size: 16px;
  color: $dark_gray;
  cursor: pointer;
  user-select: none;
}
.drawer-container {
  padding: 60px;
  font-size: 14px;
  line-height: 1.5;
  word-wrap: break-word;

  .drawer-title {
    margin-bottom: 12px;
    color: rgba(0, 0, 0, .85);
    line-height: 22px;
  }

  .drawer-item {
    color: rgba(0, 0, 0, .65);
    font-size: 14px;
    padding: 12px 0;
  }
}
/deep/.elsc{
  height: 100vh;
  .el-scrollbar__wrap{
    overflow-x: hidden;
  }
}
</style>
