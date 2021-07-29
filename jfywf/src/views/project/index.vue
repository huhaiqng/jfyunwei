<template>
  <div class="app-container">
    <el-row>
      <el-col :span="20" style="margin-left: 20px;">
        <div v-for="(project, index) in projects" :id="index" :key="project.id" class="tb">
          <h3>{{ project.name }}</h3>
          <el-tabs v-model="activeNameListTemp[index].url" type="border-card" style="margin-bottom: 50px;">
            <el-tab-pane label="访问地址" :name="activeNameList[index].url">
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
            <el-tab-pane label="服务器" :name="activeNameList[index].host">
              <el-table
                :key="project.id"
                :data="project.hosts"
                fit
                highlight-current-row
              >
                <el-table-column label="服务器名称">
                  <template slot-scope="{row}">
                    <span>{{ row.name }}</span>
                  </template>
                </el-table-column>
                <el-table-column label="IP 地址">
                  <template slot-scope="{row}">
                    <span>{{ row.inside_ip }}</span>
                  </template>
                </el-table-column>
                <el-table-column label="环境">
                  <template slot-scope="{row}">
                    <span>{{ row.env }}</span>
                  </template>
                </el-table-column>
                <el-table-column label="部署路径">
                  <template>
                    <span>{{ project.deploy_dir }}</span>
                  </template>
                </el-table-column>
                <el-table-column label="日志路径" width="300px">
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
            <el-tab-pane label="模块(包)" :name="activeNameList[index].module">
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
                <el-table-column label="部署路径" width="250">
                  <template slot-scope="{row}">
                    <span>{{ row.deploy_dir }}</span>
                  </template>
                </el-table-column>
                <el-table-column label="包类型">
                  <template slot-scope="{row}">
                    <span>{{ row.pkg_type }}</span>
                  </template>
                </el-table-column>
                <el-table-column label="端口号">
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
      </el-col>
      <el-col :span="3">
        <el-card class="choice">
          <div v-for="(c, index) in projects" :key="c.name" :class="{active: active===index}" style="margin-bottom: 8px;">
            <el-link :underline="false" @click="goto(index)">{{ c.name }}</el-link>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-dialog title="下载日志" :visible.sync="dialogVisible">
      <iframe :src="log_rul" class="log-container" />
    </el-dialog>
  </div>
</template>

<script>
import { getProject } from '@/api/address'
import { scrollTo } from '@/utils/common'

export default {
  name: 'Project',
  data() {
    return {
      active: 0,
      tableKey: 0,
      projects: null,
      filterProjects: null,
      dialogVisible: false,
      log_rul: null,
      activeNameList: [],
      activeNameListTemp: []
    }
  },
  created() {
    this.getList()
  },
  mounted() {
    // 监听滚动事件
    window.addEventListener('scroll', this.onScroll, false)
  },
  destroy() {
    // 必须移除监听器，不然当该vue组件被销毁了，监听器还在就会出错
    window.removeEventListener('scroll', this.onScroll)
  },
  methods: {
    getList() {
      getProject().then(response => {
        this.projects = response
        this.filterProjects = response

        for (var i = 0; i < this.projects.length; i++) {
          var tabname = { 'host': 'host-tab-' + i, 'module': 'module-tab-' + i, 'url': 'url-tab-' + i }
          this.activeNameListTemp.push(tabname)
        }
        this.activeNameList = JSON.parse(JSON.stringify(this.activeNameListTemp))
      })
    },
    downloadLog(log_url) {
      this.dialogVisible = true
      this.log_rul = log_url
    },
    goto(id) {
      // goAnchor(id)
      scrollTo(id)
    },
    onScroll() {
      // 获取所有锚点元素
      const navContents = document.querySelectorAll('.tb')
      // 所有锚点元素的 offsetTop
      const offsetTopArr = []
      navContents.forEach(item => {
        offsetTopArr.push(item.offsetTop)
      })
      // 获取当前文档流的 scrollTop
      const scrollTop = document.documentElement.scrollTop || document.body.scrollTop
      // 定义当前点亮的导航下标
      let navIndex = 0
      for (let n = 0; n < offsetTopArr.length; n++) {
        // 如果 scrollTop 大于等于第n个元素的 offsetTop 则说明 n-1 的内容已经完全不可见
        // 那么此时导航索引就应该是n了
        if (scrollTop >= offsetTopArr[n]) {
          navIndex = n
        }
      }
      this.active = navIndex
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
</style>
