<template>
  <div class="app-container">
    <el-row>
      <el-col :span="20">
        <div v-for="(project, index) in projects" :id="index" :key="project.id" class="tb">
          <div v-if="project.hosts.length>0">
            <h4>{{ project.name }}</h4>
            <el-table
              :key="project.id"
              :data="project.hosts"
              fit
              highlight-current-row
            >
              <el-table-column label="显示名称">
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
          </div>
        </div>
      </el-col>
      <el-col :span="4">
        <el-card class="choice">
          <div v-for="(c, index) in projects" :key="c.name" :class="{active: active===index}" style="margin-bottom: 8px;">
            <el-link v-if="c.hosts.length>0" :underline="false" @click="goto(index)">{{ c.name }}</el-link>
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
      log_rul: null
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
