<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="queryList.inside_addr" placeholder="内网地址" style="width:400px" class="filter-item" @keyup.enter.native="getList" />
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="getList">
        搜索
      </el-button>
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
      <el-table-column label="内网地址">
        <template slot-scope="{row}">
          <span class="link-type" @click="showDetail(row)">{{ row.inside_addr }}</span>
        </template>
      </el-table-column>
      <el-table-column label="外网地址">
        <template slot-scope="{row}">
          <span>{{ row.outside_addr }}</span>
        </template>
      </el-table-column>
      <el-table-column label="角色">
        <template slot-scope="{row}">
          <span>{{ row.role }}</span>
        </template>
      </el-table-column>
      <el-table-column label="数据库路径">
        <template slot-scope="{row}">
          <span>{{ row.data_dir }}</span>
        </template>
      </el-table-column>
      <el-table-column label="版本号">
        <template slot-scope="{row}">
          <span>{{ row.version }}</span>
        </template>
      </el-table-column>
      <el-table-column label="部署方式">
        <template slot-scope="{row}">
          <span>{{ row.method }}</span>
        </template>
      </el-table-column>
      <el-table-column label="来源">
        <template slot-scope="{row}">
          <span>{{ row.origin }}</span>
        </template>
      </el-table-column>
      <el-table-column label="备注">
        <template slot-scope="{row}">
          <span>{{ row.cluster }}</span>
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
      <el-form ref="dataForm" :model="temp" label-position="left" label-width="100px" style="margin-right:30px; margin-left:30px;">
        <el-row>
          <el-col :span="12">
            <el-form-item label="内网地址" prop="inside_addr">
              <el-input v-model="temp.inside_addr" style="width:80%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="外网地址" prop="outside_addr">
              <el-input v-model="temp.outside_addr" style="width:80%" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="角色" prop="role">
              <el-select v-model="temp.role" style="width:60%">
                <el-option value="master">master</el-option>
                <el-option value="slave">slave</el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="数据库路径" prop="data_dir">
              <el-input v-model="temp.data_dir" style="width:60%" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="管理员" prop="manger">
              <el-input v-model="temp.manager" style="width:60%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="密码" prop="password">
              <el-input v-model="temp.password" style="width:60%" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="部署方式" prop="method">
              <el-select v-model="temp.method" class="filter-item" style="width:60%">
                <el-option value="normal">normal</el-option>
                <el-option value="docker">docker</el-option>
                <el-option value="docker-compose">docker-compose</el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="版本号" prop="version">
              <el-input v-model="temp.version" style="width:60%" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="来源" prop="origin">
              <el-select v-model="temp.origin" class="filter-item" style="width:60%">
                <el-option value="自建">自建</el-option>
                <el-option value="阿里云">阿里云</el-option>
                <el-option value="华为云">华为云</el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="备注" prop="cluster">
              <el-input v-model="temp.cluster" style="width:80%" />
            </el-form-item>
          </el-col>
        </el-row>
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
    <el-drawer title="详情" :visible.sync="drawerVisible" :with-header="false">
      <mysql-drawer :instance="instance" />
    </el-drawer>
  </div>
</template>

<script>
import { addMySQL, deleteMySQL, updateMySQL, getMySQL } from '@/api/project'
import Pagination from '@/components/Pagination'
import MysqlDrawer from '@/components/Drawer/mysql'
import { encrypt, decrypt } from '@/utils/aes'
export default {
  name: 'MySQL',
  components: { Pagination, MysqlDrawer },
  data() {
    return {
      list: null,
      total: 0,
      temp: {
        inside_addr: undefined,
        outside_addr: undefined,
        role: 'master',
        data_dir: '/var/lib/mysql',
        version: '5.7',
        manager: 'root',
        password: undefined,
        method: 'normal',
        origin: '自建',
        cluster: undefined,
        created: new Date()
      },
      tempCopy: undefined,
      queryList: {
        inside_addr: '',
        page: 0,
        limit: 10
      },
      dialogStatus: 'create',
      dialogVisible: false,
      textMap: {
        create: '新增',
        edit: '编辑'
      },
      drawerVisible: false,
      instance: undefined
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      getMySQL(this.queryList).then(response => {
        this.list = response.results
        this.total = response.count
      })
    },
    restTemp() {
      this.temp = {
        inside_addr: undefined,
        outside_addr: undefined,
        role: 'master',
        data_dir: '/var/lib/mysql',
        version: '5.7',
        manager: 'root',
        password: undefined,
        method: 'normal',
        origin: '自建',
        cluster: undefined,
        created: new Date()
      }
    },
    handleCreate() {
      this.dialogStatus = 'create'
      this.dialogVisible = true
      this.restTemp()
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row)
      this.temp.password = decrypt(this.temp.password)
      this.dialogStatus = 'edit'
      this.dialogVisible = true
    },
    handleDelete(id) {
      this.$confirm('确认删除', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteMySQL(id).then(() => {
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
      this.tempCopy = Object.assign({}, this.temp)
      this.tempCopy.password = encrypt(this.tempCopy.password)
      addMySQL(this.tempCopy).then(response => {
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
      this.tempCopy = Object.assign({}, this.temp)
      this.tempCopy.password = encrypt(this.tempCopy.password)
      updateMySQL(this.tempCopy).then(() => {
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
      this.instance = Object.assign({}, row)
      this.instance.password = decrypt(this.instance.password)
      this.drawerVisible = true
    }
  }
}
</script>
