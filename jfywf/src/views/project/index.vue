<template>
  <div>
    <el-row>
      <el-col :span="3" style="background-color: white;">
        <div class="down-tree">
          <el-scrollbar>
            <el-tree :data="projects" :highlight-current="true" :props="defaultProps" style="#f0f2f5;padding-top: 10px;" @node-click="showProjectInfo" />
          </el-scrollbar>
        </div>
      </el-col>
      <el-col :span="21">
        <div class="project-scrollbar">
          <el-scrollbar>
            <div class="tb">
              <h3 style="margin-left:30px">{{ project.name }}</h3>
              <el-tabs v-model="activeName" type="border-card" style="margin: 20px;">
                <el-tab-pane label="访问地址" name="url">
                  <el-table
                    :key="project.id"
                    :data="project.urls"
                    fit
                    highlight-current-row
                  >
                    <el-table-column label="名称-环境" width="400px">
                      <template slot-scope="{row}">
                        <span class="link-type"><a :href="row.url" target="_blank">{{ row.env.name }} - {{ row.name }}</a></span>
                      </template>
                    </el-table-column>
                    <el-table-column label="地址">
                      <template slot-scope="{row}">
                        <span class="link-type"><el-link type="primary" :href="row.url" target="_blank">{{ row.url }}</el-link></span>
                      </template>
                    </el-table-column>
                  </el-table>
                </el-tab-pane>
                <el-tab-pane label="服务器" name="host">
                  <el-table
                    :key="project.id"
                    :data="project.hosts"
                    fit
                    highlight-current-row
                  >
                    <el-table-column label="服务器名称" width="200px">
                      <template slot-scope="{row}">
                        <span>{{ row.name }}</span>
                      </template>
                    </el-table-column>
                    <el-table-column label="IP 地址" width="200px">
                      <template slot-scope="{row}">
                        <span>{{ row.inside_ip }}</span>
                      </template>
                    </el-table-column>
                    <el-table-column label="环境" width="200px">
                      <template slot-scope="{row}">
                        <span>{{ row.env }}</span>
                      </template>
                    </el-table-column>
                    <el-table-column label="部署路径">
                      <template>
                        <span>{{ project.deploy_dir }}</span>
                      </template>
                    </el-table-column>
                    <el-table-column label="日志路径">
                      <template>
                        <span>{{ project.log_dir }}</span>
                      </template>
                    </el-table-column>
                    <el-table-column label="操作" align="center" width="120px">
                      <template slot-scope="{row}">
                        <el-button type="primary" size="mini" @click="downloadLog(row.hostname+project.log_dir)">下载日志</el-button>
                      </template>
                    </el-table-column>
                  </el-table>
                </el-tab-pane>
                <el-tab-pane label="模块(包)" name="module">
                  <el-table
                    :key="project.id"
                    :data="project.modules"
                    fit
                    highlight-current-row
                  >
                    <el-table-column label="模块名">
                      <template slot-scope="{row}">
                        <span>{{ row.module }}</span>
                      </template>
                    </el-table-column>
                    <el-table-column label="包名" width="400px">
                      <template slot-scope="{row}">
                        <span>{{ row.pkg_name }}</span>
                      </template>
                    </el-table-column>
                    <el-table-column label="部署路径" width="300px">
                      <template slot-scope="{row}">
                        <span>{{ row.deploy_dir }}</span>
                      </template>
                    </el-table-column>
                    <el-table-column label="包类型" width="80px">
                      <template slot-scope="{row}">
                        <span>{{ row.pkg_type }}</span>
                      </template>
                    </el-table-column>
                    <el-table-column label="端口号" width="80px">
                      <template slot-scope="{row}">
                        <span>{{ row.port }}</span>
                      </template>
                    </el-table-column>
                    <el-table-column label="日志文件" width="350px">
                      <template slot-scope="{row}">
                        <span>{{ row.logfile }}</span>
                      </template>
                    </el-table-column>
                  </el-table>
                </el-tab-pane>
              </el-tabs>
            </div>
          </el-scrollbar>
        </div>
      </el-col>
    </el-row>

    <el-dialog title="下载日志" :visible.sync="dialogVisible">
      <iframe :src="log_url" class="log-container" />
    </el-dialog>
  </div>
</template>

<script>
import { getOneProjectInfo, getProjectForConfig } from '@/api/project'

export default {
  name: 'Project',
  data() {
    return {
      projects: null,
      project: {},
      dialogVisible: false,
      log_url: null,
      activeName: 'url',
      defaultProps: {
        children: 'children',
        label: 'name'
      }
    }
  },
  created() {
    getProjectForConfig().then(response => {
      this.projects = response

      if (this.projects.length > 0) {
        getOneProjectInfo(this.projects[0].id).then(response => {
          this.project = response
        })
      }
    })
  },
  methods: {
    downloadLog(log_url) {
      this.dialogVisible = true
      this.log_url = log_url
    },
    showProjectInfo(node) {
      getOneProjectInfo(node.id).then(response => {
        this.project = response
      })
    }
  }
}
</script>

<style lang='scss' scoped>
.choice {
  position: fixed;
  margin-left: 20px;
}
.active {
  color: #dddde2;
  background-color: #e2e2e2;
}
.tb {
  width: 100%;
  margin-bottom:15px;
}
.log-container {
  position: relative;
  width: 100%;
  height: 500px;
  padding-bottom: 16px;
  border:none;
}
.down-tree{
  flex: 1;
  // border-right:1px solid rgba(211,219,222,1);
  // background-color: #f0f2f5;
  /deep/.el-scrollbar{
    height: calc(100vh - 50px);
    .el-scrollbar__wrap{
      overflow-x: hidden;
    }
  }
}
.project-scrollbar{
  flex: 1;
  /deep/.el-scrollbar{
    height: calc(100vh - 50px);
    .el-scrollbar__wrap{
      overflow-x: hidden;
    }
  }
}
</style>
