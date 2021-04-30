<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.name" placeholder="名称" style="width:400px" class="filter-item" @keyup.enter.native="getList" />
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="getList">
        搜索
      </el-button>
      <el-button type="primary" class="filter-item" icon="el-icon-edit" @click="handleCreate">
        新增
      </el-button>
    </div>
    <el-table :key="tableKey" :data="list" border fit highlight-current-row style="width:100%">
      <el-table-column label="序号" align="center" width="50px">
        <template slot-scope="{$index}">
          <span>{{ $index + 1 + (listQuery.page - 1)*listQuery.limit }}</span>
        </template>
      </el-table-column>
      <el-table-column label="名称">
        <template slot-scope="{row}">
          <span class="link-type" @click="showDetail(row)">{{ row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="用户名">
        <template slot-scope="{row}">
          <span>{{ row.username }}</span>
        </template>
      </el-table-column>
      <el-table-column label="地址">
        <template slot-scope="{row}">
          <span class="link-type"><a :href="row.addr" target="blank">{{ row.addr }}</a></span>
        </template>
      </el-table-column>
      <el-table-column label="备注">
        <template slot-scope="{row}">
          <span>{{ row.remark }}</span>
        </template>
      </el-table-column>
      <el-table-column label="创建时间" align="center" width="200px">
        <template slot-scope="{row}">
          <span>{{ row.created | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center" width="150px">
        <template slot-scope="{row,$index}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">编辑</el-button>
          <el-button type="danger" size="mini" @click="deleteData(row.id,$index)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogVisible">
      <el-form ref="dataForm" :model="temp" label-position="left" label-width="100px" style="margin-left:30px;margin-right:30px">
        <el-form-item label="名称" prop="name">
          <el-input v-model="temp.name" style="width:60%" />
        </el-form-item>
        <el-form-item label="用户名" prop="username">
          <el-input v-model="temp.username" style="width:60%" />
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="temp.password" style="width:60%" />
        </el-form-item>
        <el-form-item label="地址" prop="addr">
          <el-input v-model="temp.addr" style="width:60%" />
        </el-form-item>
        <el-form-item label="备注" prop="remark">
          <el-input v-model="temp.remark" style="width:60%" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="dialogStatus === 'create'?createData():updateData()">
          确定
        </el-button>
      </div>
    </el-dialog>
    <el-drawer title="详情" :visible.sync="drawerVisible" :with-header="false">
      <div class="drawer-container">
        <div>
          <h3 class="drawer-title">详情</h3>
          <div class="drawer-item">
            <el-row>
              <el-col :span="12">名称：</el-col>
              <el-col :span="12">{{ temp.name }}</el-col>
            </el-row>
          </div>
          <div class="drawer-item">
            <el-row>
              <el-col :span="12">地址：</el-col>
              <el-col :span="12">{{ temp.addr }}</el-col>
            </el-row>
          </div>
          <div class="drawer-item">
            <el-row>
              <el-col :span="12">用户名：</el-col>
              <el-col :span="12">{{ temp.username }}</el-col>
            </el-row>
          </div>
          <div class="drawer-item">
            <el-row>
              <el-col :span="12">密码：</el-col>
              <el-col :span="12">{{ temp.password }}</el-col>
            </el-row>
          </div>
          <div class="drawer-item">
            <el-row>
              <el-col :span="12">备注：</el-col>
              <el-col :span="12">{{ temp.remark }}</el-col>
            </el-row>
          </div>
          <div class="drawer-item">
            <el-row>
              <el-col :span="12">创建时间：</el-col>
              <el-col :span="12">{{ temp.created | parseTime('{y}-{m}-{d} {h}:{m}') }}</el-col>
            </el-row>
          </div>
        </div>
      </div>
    </el-drawer>
  </div>
</template>
<script>
import Pagination from '@/components/Pagination'
import { getAccounts, addAccount, updateAccount, deleteAccount } from '@/api/account'
import { encrypt, decrypt } from '@/utils/aes'
export default {
  name: 'Software',
  components: { Pagination },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      temp: {
        username: null,
        password: null,
        addr: null,
        name: null,
        remark: undefined,
        created: new Date()
      },
      tempCopy: undefined,
      listQuery: {
        page: 1,
        limit: 10,
        name: ''
      },
      dialogVisible: false,
      dialogStatus: null,
      drawerVisible: false,
      textMap: {
        create: '新增',
        edit: '编辑'
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    handleCreate() {
      this.dialogVisible = true
      this.resetTemp()
      this.dialogStatus = 'create'
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row)
      this.temp.password = decrypt(this.temp.password)
      this.dialogVisible = true
      this.dialogStatus = 'edit'
    },
    getList() {
      getAccounts(this.listQuery).then(response => {
        this.list = response.results
        this.total = response.count
        setTimeout(() => {
        }, 1.5 * 1000)
      })
    },
    createData() {
      this.tempCopy = Object.assign({}, this.temp)
      this.tempCopy.password = encrypt(this.tempCopy.password)
      addAccount(this.tempCopy).then(() => {
        this.getList()
        this.dialogVisible = false
        this.$notify({
          title: '成功',
          message: '账号新增成功！',
          type: 'success',
          duration: 2000
        })
      })
    },
    updateData() {
      this.tempCopy = Object.assign({}, this.temp)
      this.tempCopy.password = encrypt(this.tempCopy.password)
      updateAccount(this.tempCopy).then(() => {
        this.getList()
        this.dialogVisible = false
        this.$notify({
          title: '成功',
          message: '更新成功',
          type: 'success',
          duration: 2000
        })
      })
    },
    deleteData(id, index) {
      this.$confirm('确认删除', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteAccount(id).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功！',
            type: 'success',
            duration: 2000
          })
          this.list.splice(index, 1)
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    showDetail(row) {
      this.temp = Object.assign({}, row)
      this.temp.password = decrypt(this.temp.password)
      this.drawerVisible = true
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
    },
    resetTemp() {
      this.temp = {
        username: null,
        password: null,
        addr: null,
        name: null,
        remark: undefined,
        created: new Date()
      }
      this.passwordType = 'password'
    }
  }
}
</script>
<style lang="scss" scoped>
.drawer-container {
  padding: 24px;
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
</style>
