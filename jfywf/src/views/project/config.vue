<template>
  <div class="app-container">
    <div class="filter-container">
      <el-select v-model="queryList.project" placeholder="项目" filterable clearable class="filter-item" style="width: 400px" @change="getList">
        <el-option v-for="item in projectList" :key="item.name" :label="item.name" :value="item.id" />
      </el-select>
      <el-button class="filter-item" icon="el-icon-edit" type="primary" @click="handleCreate">
        新增
      </el-button>
    </div>
    <el-table :key="0" :data="list" border fit highlight-current-row style="width: 100%;">
      <el-table-column label="序号" align="center" width="50px">
        <template slot-scope="{$index}">
          <span>{{ $index + 1 + (queryList.page - 1)*queryList.limit }}</span>
        </template>
      </el-table-column>
      <el-table-column label="项目">
        <template slot-scope="{row}">
          <span class="link-type" @click="showDetail(row)">{{ row.project.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="环境">
        <template slot-scope="{row}">
          <span>{{ row.env.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="创建时间">
        <template slot-scope="{row}">
          <span>{{ row.created | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center" width="80px" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-dropdown type="primary">
            <el-button size="mini" split-buttion type="primary">操作<i class="el-icon-arrow-down el-icon--right" /></el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item @click.native="handleUpdate(row)">编辑</el-dropdown-item>
              <el-dropdown-item @click.native="handleDelete(row.id)">删除</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </template>
      </el-table-column>
    </el-table>
    <pagination v-show="total>0" :total="total" :page.sync="queryList.page" :limit.sync="queryList.limit" @pagination="getList" />
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogVisible" width="60%">
      <el-row>
        <el-col :span="12">
          <el-select v-model="temp.project" placeholder="项目" class="filter-item" style="width:60%">
            <el-option v-for="item in projectList" :key="item.id" :label="item.name" :value="item.id" />
          </el-select>
        </el-col>
        <el-col :span="12">
          <el-select v-model="temp.env" placeholder="环境" class="filter-item" style="width:60%">
            <el-option v-for="item in envList" :key="item.id" :label="item.name" :value="item.id" />
          </el-select>
        </el-col>
      </el-row>
      <el-row style="margin-top:15px;">
        <tinymce ref="tinymce" v-model="temp.conf" :height="300" />
      </el-row>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          保存
        </el-button>
      </div>
    </el-dialog>
    <el-dialog :title="confTitle" :visible.sync="configDialogVisible" width="60%">
      <div class="tab-pane">
        <el-scrollbar>
          <div class="conf-text" v-html="confText" />
        </el-scrollbar>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { addConfig, deleteConfig, updateConfig, getConfig, getEnv, getProjectForConfig } from '@/api/project'
import Pagination from '@/components/Pagination'
import Tinymce from '@/components/Tinymce'
export default {
  name: 'Config',
  components: { Pagination, Tinymce },
  data() {
    return {
      list: null,
      envList: [],
      projectList: [],
      total: 0,
      temp: {
        project: null,
        env: null,
        conf: '',
        created: new Date()
      },
      confText: null,
      confTitle: null,
      queryList: {
        project: '',
        page: 0,
        limit: 10
      },
      dialogStatus: 'create',
      dialogVisible: false,
      configDialogVisible: false,
      textMap: {
        create: '新增',
        edit: '编辑'
      }
    }
  },
  created() {
    this.getList()
    getEnv().then(response => {
      this.envList = response
    })
    getProjectForConfig().then(response => {
      this.projectList = response
    })
  },
  methods: {
    getList() {
      getConfig(this.queryList).then(response => {
        this.list = response.results
        this.total = response.count
      })
    },
    restTemp() {
      this.temp = {
        project: null,
        env: null,
        conf: '',
        created: new Date()
      }
    },
    handleCreate() {
      this.dialogStatus = 'create'
      this.dialogVisible = true
      this.restTemp()
      this.setTinymceContent()
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row)
      this.setTinymceContent()
      this.temp.project = this.temp.project.id
      this.temp.env = this.temp.env.id
      this.dialogStatus = 'edit'
      this.dialogVisible = true
    },
    handleDelete(id) {
      this.$confirm('确认删除', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteConfig(id).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功！',
            type: 'success',
            duration: 2000
          })
          this.getList()
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    createData() {
      addConfig(this.temp).then(response => {
        this.getList()
        this.dialogVisible = false
        this.$notify({
          title: '成功',
          message: '新增成功！',
          type: 'success',
          duration: 2000
        })
      })
    },
    updateData() {
      updateConfig(this.temp).then(() => {
        this.getList()
        this.dialogVisible = false
        this.$notify({
          title: '成功',
          message: '更新成功！',
          type: 'success',
          duration: 2000
        })
      })
    },
    showDetail(row) {
      this.confText = row.conf
      this.confTitle = '查看: ' + row.project.name + ' ' + row.env.name
      this.configDialogVisible = true
    },
    setTinymceContent() {
      if (this.$refs.tinymce) {
        this.$refs.tinymce.setContent(this.temp.conf)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.tab-pane{
  flex: 1;
  /deep/.el-scrollbar{
    height: calc(100vh - 400px);
    .el-scrollbar__wrap{
      overflow-x: hidden;
    }
  }
  border-style: solid;
  border-radius: 3px;
  border-width:1px;
}
.conf-text{
  padding: 15px;
}
</style>
