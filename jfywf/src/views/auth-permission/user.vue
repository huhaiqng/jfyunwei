<template>
  <div class="app-container">
    <div class="filter-container">
      <el-select v-model="listQuery.groups" placeholder="选择组" clearable style="width: 300px" class="filter-item" @change="getList">
        <el-option v-for="item in groupList" :key="item.id" :label="item.name" :value="item.id" />
      </el-select>
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
      <el-table-column label="用户名">
        <template slot-scope="{row}">
          <span>{{ row.username }}</span>
        </template>
      </el-table-column>
      <el-table-column label="手机号码">
        <template slot-scope="{row}">
          <span>{{ row.phone }}</span>
        </template>
      </el-table-column>
      <el-table-column label="邮箱">
        <template slot-scope="{row}">
          <span>{{ row.email }}</span>
        </template>
      </el-table-column>
      <el-table-column label="超级用户">
        <template slot-scope="{row}">
          <span>{{ row.is_superuser?"是":"否" }}</span>
        </template>
      </el-table-column>
      <el-table-column label="早会主持">
        <template slot-scope="{row}">
          <span>{{ row.hosted?"已完成":"未完成" }}</span>
        </template>
      </el-table-column>
      <el-table-column label="组">
        <template slot-scope="{row}">
          <span v-for="(g, i) in row.groups" :key="g.id">{{ i===0?g.name:", " + g.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="创建时间">
        <template slot-scope="{row}">
          <span>{{ row.date_joined | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
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
      <el-form ref="temp" :model="temp" :rules="formRules" label-position="left" label-width="100px" style="margin-left:30px;margin-right:30px">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="temp.username" style="width:60%" />
        </el-form-item>
        <el-form-item label="手机号码" prop="phone">
          <el-input ref="phone" v-model="temp.phone" style="width:60%" />
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-if="setPasswordStatus" ref="password" v-model="temp.password" type="password" placeholder="******" style="width:60%" />
          <el-button v-if="!setPasswordStatus" round size="mini" icon="el-icon-edit" @click="handelChangePassword">修改密码</el-button>
        </el-form-item>
        <el-form-item v-if="setPasswordStatus" label="确认密码" prop="confirm_password">
          <el-input ref="confirm_password" v-model="temp.confirm_password" type="password" placeholder="******" style="width:60%" />
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input ref="email" v-model="temp.email" style="width:60%" />
        </el-form-item>
        <el-form-item label="组" prop="groups">
          <el-select v-model="temp.groups" multiple style="width:60%">
            <el-option v-for="item in groupList" :key="item.id" :label="item.name" :value="item.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="超级用户" prop="use">
          <el-checkbox v-model="temp.is_superuser">是</el-checkbox>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="handelCancel('temp')">
          取消
        </el-button>
        <el-button type="primary" @click="dialogStatus === 'create'?createData('temp'):updateData('temp')">
          确定
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
import Pagination from '@/components/Pagination'
import { getUser, addUser, updateUser, deleteUser, getGroup } from '@/api/auth-permission'
import { validPassword } from '@/utils/validate'
export default {
  name: 'Software',
  components: { Pagination },
  data() {
    const validatePassword = (rule, value, callback) => {
      if (!validPassword(value)) {
        callback(new Error('密码必须是6到12位，包含数字和大小写字母'))
      } else {
        callback()
      }
    }
    const validateConfirmPassword = (rule, value, callback) => {
      if (value !== this.temp.password) {
        callback(new Error('2次密码输入不一致'))
      } else {
        callback()
      }
    }
    return {
      tableKey: 0,
      list: null,
      groupList: null,
      total: 0,
      temp: {
        username: null,
        password: null,
        confirm_password: null,
        is_superuser: false,
        email: null,
        is_staff: false,
        date_joined: new Date(),
        groups: [],
        phone: null
      },
      listQuery: {
        page: 1,
        limit: 10,
        groups: ''
      },
      groupListQuery: {
        page: 1
      },
      dialogVisible: false,
      dialogStatus: null,
      textMap: {
        create: '新增',
        edit: '编辑'
      },
      formRules: {
        password: [{ trigger: 'blur', validator: validatePassword }],
        confirm_password: [{ trigger: 'blur', validator: validateConfirmPassword }]
      },
      setPasswordStatus: true
    }
  },
  created() {
    this.getList()
    this.getGroupList()
  },
  methods: {
    getList() {
      var userQueryList = {}
      if (this.listQuery.groups) {
        userQueryList = this.listQuery
      } else {
        userQueryList = { page: this.listQuery.page, limit: this.listQuery.limit }
      }
      getUser(userQueryList).then(response => {
        this.list = response.results
        this.total = response.count
      })
    },
    getGroupList() {
      getGroup(this.groupListQuery).then(response => {
        this.groupList = response
      })
    },
    handleCreate() {
      this.dialogVisible = true
      this.resetTemp()
      this.dialogStatus = 'create'
      // this.getGroupList()
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row)
      this.temp.groups = this.temp.groups.map(h => h.id)
      this.dialogVisible = true
      this.dialogStatus = 'edit'
      this.setPasswordStatus = false
      // this.getGroupList()
    },
    createData(userForm) {
      this.$refs[userForm].validate((valid) => {
        if (valid) {
          addUser(this.temp).then(() => {
            this.getList()
            this.dialogVisible = false
            this.$notify({
              title: '成功',
              message: '账号新增成功！',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    updateData(userForm) {
      if (this.setPasswordStatus) {
        this.$refs[userForm].validate((valid) => {
          if (valid) {
            updateUser(this.temp).then(() => {
              this.getList()
              this.$refs[userForm].resetFields()
              this.dialogVisible = false
              this.$notify({
                title: '成功',
                message: '更新成功',
                type: 'success',
                duration: 2000
              })
            })
          }
        })
      } else {
        updateUser(this.temp).then(() => {
          this.getList()
          this.$refs[userForm].resetFields()
          this.dialogVisible = false
          this.$notify({
            title: '成功',
            message: '更新成功',
            type: 'success',
            duration: 2000
          })
        })
      }
    },
    deleteData(id, index) {
      this.$confirm('确认删除', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteUser(id).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功！',
            type: 'success',
            duration: 2000
          })
          this.getList()
          // this.list.splice(index, 1)
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    handelCancel(form) {
      this.$refs[form].resetFields()
      this.dialogVisible = false
    },
    resetTemp() {
      this.temp = {
        username: null,
        password: null,
        confirm_password: null,
        is_superuser: false,
        email: null,
        is_staff: false,
        date_joined: new Date(),
        groups: []
      }
      this.setPasswordStatus = true
    },
    handelChangePassword() {
      this.setPasswordStatus = true
      this.temp.password = ''
    }
  }
}
</script>
