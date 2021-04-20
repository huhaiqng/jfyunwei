<template>
  <div>
    <el-scrollbar class="elsc">
      <div class="drawer-container">
        <div>
          <h3 class="drawer-title">详情</h3>
          <div class="drawer-item">
            <el-row>
              <el-col :span="12">内网地址：</el-col>
              <el-col :span="12">{{ instance.inside_addr }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">外网地址：</el-col>
              <el-col :span="12">{{ instance.outside_addr }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">角色：</el-col>
              <el-col :span="12">{{ instance.role }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">数据库路径：</el-col>
              <el-col :span="12">{{ instance.data_dir }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">版本号：</el-col>
              <el-col :span="12">{{ instance.version }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">管理员：</el-col>
              <el-col :span="12">{{ instance.manager }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">密码：</el-col>
              <el-col :span="12">{{ instance.password }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">部署方式：</el-col>
              <el-col :span="12">{{ instance.method }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">来源：</el-col>
              <el-col :span="12">{{ instance.origin }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">备注：</el-col>
              <el-col :span="12">{{ instance.cluster }}</el-col>
            </el-row>
          </div>

          <div class="drawer-item">
            <el-row>
              <el-col :span="12">创建时间：</el-col>
              <el-col :span="12">{{ instance.created | parseTime('{y}-{m}-{d} {h}:{m}') }}</el-col>
            </el-row>
          </div>

        </div>
      </div>
    </el-scrollbar>
  </div>
</template>

<script>
export default {
  name: 'MysqlInstanceDrawer',
  props: {
    instance: { type: Object, default: null }
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
