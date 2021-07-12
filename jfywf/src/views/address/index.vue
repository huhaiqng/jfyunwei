<template>
  <div class="app-container">
    <el-row>
      <el-col :span="20">
        <div v-for="(project, index) in projects" :id="index" :key="project.id" class="tb">
          <h4>{{ project.name }}</h4>
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
        </div>
      </el-col>
      <el-col :span="4">
        <el-card class="choice">
          <div v-for="(c, index) in projects" :key="c.name" :class="{active: active===index}" style="margin-bottom: 8px;">
            <el-link :underline="false" @click="goto(index)">{{ c.name }}</el-link>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { getProject } from '@/api/address'
import { scrollTo } from '@/utils/common'

export default {
  name: 'Address',
  data() {
    return {
      active: 0,
      tableKey: 0,
      projects: null,
      filterProjects: null
    }
  },
  created() {
    this.handleFilter()
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
    handleFilter() {
      getProject().then(response => {
        this.projects = response
        this.filterProjects = response
      })
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
</style>
