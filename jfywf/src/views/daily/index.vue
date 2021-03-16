<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="queryList.task" placeholder="任务" style="width:400px" class="filter-item" @keyup.enter.native="getList" />
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="getList">
        搜索
      </el-button>
      <el-button class="filter-item" icon="el-icon-edit" type="primary" @click="handleCreate">
        新增
      </el-button>
    </div>
    <el-table :key="0" :data="list" border highlight-current-row style="width: 100%; margin-top:15px;">
      <el-table-column label="序号" align="center" width="50px">
        <template slot-scope="{$index}">
          <span>{{ $index + 1 + (queryList.page - 1)*queryList.limit }}</span>
        </template>
      </el-table-column>
      <el-table-column label="工作任务">
        <template slot-scope="{row}">
          <span>{{ row.task }}</span>
        </template>
      </el-table-column>
      <el-table-column label="完成率(%)" width="100px">
        <template slot-scope="{row}">
          <span>{{ row.rate }}</span>
        </template>
      </el-table-column>
      <el-table-column label="耗时(小时)" width="100px">
        <template slot-scope="{row}">
          <span>{{ row.time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="创建时间" width="150px">
        <template slot-scope="{row}">
          <span>{{ row.created_at | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center" width="100px" class-name="small-padding fixed-width">
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
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogVisible">
      <el-form ref="dataForm" :model="temp" label-position="left" label-width="100px" style="margin-right:30px; margin-left:30px;">
        <el-form-item label="今日工作任务" prop="task">
          <el-input v-model="temp.task" type="textarea" style="width:100%" />
        </el-form-item>
        <el-form-item label="完成率(%)" prop="rate">
          <el-input v-model="temp.rate" style="width:20%" />
        </el-form-item>
        <el-form-item label="耗时(小时)" prop="time">
          <el-input v-model="temp.time" style="width:20%" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          保存
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { addDaily, getDaily, updateDaily, deleteDaily } from '@/api/report'
import Pagination from '@/components/Pagination'
import { getUserInfo } from '@/utils/auth'
export default {
  name: 'Daily',
  components: { Pagination },
  data() {
    return {
      list: null,
      total: 0,
      temp: {
        owner: JSON.parse(getUserInfo()).id,
        task: undefined,
        rate: undefined,
        time: undefined,
        created_at: new Date()
      },
      queryList: {
        task: '',
        limit: 10
      },
      dialogStatus: 'create',
      dialogVisible: false,
      textMap: {
        create: '新增',
        edit: '编辑'
      },
      instance: undefined
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      getDaily(this.queryList).then(response => {
        this.list = response.results
        this.total = response.count
      })
    },
    restTemp() {
      this.temp = {
        owner: JSON.parse(getUserInfo()).id,
        task: undefined,
        rate: undefined,
        time: undefined,
        created_at: new Date()
      }
    },
    handleCreate() {
      this.dialogStatus = 'create'
      this.dialogVisible = true
      this.restTemp()
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row)
      this.dialogStatus = 'edit'
      this.dialogVisible = true
    },
    handleDelete(id) {
      this.$confirm('确认删除', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteDaily(id).then(() => {
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
      addDaily(this.temp).then(response => {
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
      updateDaily(this.temp).then(() => {
        this.getList()
        this.dialogVisible = false
        this.$notify({
          title: '成功',
          message: '更新成功！',
          type: 'success',
          duration: 2000
        })
      })
    }
  }
}
</script>
