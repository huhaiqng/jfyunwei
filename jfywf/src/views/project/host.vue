<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.inside_ip" placeholder="IP 地址" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.env" placeholder="环境" clearable class="filter-item" style="width: 200px">
        <el-option v-for="item in envOptions" :key="item.id" :label="item.name" :value="item.name" />
      </el-select>
      <el-select v-model="listQuery.cloud_user" placeholder="云账号" clearable class="filter-item" style="width: 200px">
        <el-option v-for="item in cloudUserOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        搜索
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        添加
      </el-button>
    </div>

    <el-table
      :key="tableKey"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
    >
      <el-table-column label="序号" align="center" width="60px">
        <template slot-scope="{$index}">
          <span>{{ $index + 1 + (listQuery.page - 1)*listQuery.limit }}</span>
        </template>
      </el-table-column>
      <el-table-column label="主机名">
        <template slot-scope="{row}">
          <span class="link-type" @click="showDetail(row)">{{ row.hostname }}</span>
        </template>
      </el-table-column>
      <el-table-column label="内网 IP">
        <template slot-scope="{row}">
          <span>{{ row.inside_ip }}</span>
        </template>
      </el-table-column>
      <el-table-column label="外网 IP">
        <template slot-scope="{row}">
          <span>{{ row.outside_ip }}</span>
        </template>
      </el-table-column>
      <el-table-column label="系统版本">
        <template slot-scope="{row}">
          <span>{{ row.os }}</span>
        </template>
      </el-table-column>
      <el-table-column label="位置">
        <template slot-scope="{row}">
          <span>{{ row.cloud }}</span>
        </template>
      </el-table-column>
      <el-table-column label="云账号">
        <template slot-scope="{row}">
          <span>{{ row.cloud_user }}</span>
        </template>
      </el-table-column>
      <el-table-column label="项目" width="200px">
        <template slot-scope="{row}">
          <span v-for="p in row.project" :key="p.id">
            <div>{{ p.name }}</div>
          </span>
        </template>
      </el-table-column>
      <el-table-column label="环境">
        <template slot-scope="{row}">
          <span>{{ row.env }}</span>
        </template>
      </el-table-column>
      <el-table-column label="创建时间">
        <template slot-scope="{row}">
          <span>{{ row.created | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center" width="100px" class-name="small-padding fixed-width">
        <template slot-scope="{row, $index}">
          <el-dropdown type="primary">
            <el-button size="mini" split-buttion type="primary">操作<i class="el-icon-arrow-down el-icon--right" /></el-button>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item @click.native="handleUpdate(row)">编辑</el-dropdown-item>
              <el-dropdown-item @click.native="handleDelete(row.id, $index)">删除</el-dropdown-item>
              <el-dropdown-item v-if="row.status" @click.native="hostProblem(row, false)">标记故障</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible" width="60%">
      <el-form ref="dataForm" :model="temp" label-position="left" label-width="100px" style="margin-right:30px; margin-left:30px;">
        <el-row>
          <el-col :span="12">
            <el-form-item label="主机名" prop="hostname">
              <el-input v-model="temp.hostname" style="width:60%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="显示名称" prop="name">
              <el-input v-model="temp.name" style="width:60%" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="内网 IP" prop="inside_ip">
              <el-input v-model="temp.inside_ip" style="width:60%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="外网 IP" prop="outside_ip">
              <el-input v-model="temp.outside_ip" style="width:60%" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="内网端口号" prop="inside_port">
              <el-input v-model="temp.inside_port" style="width:60%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="外网端口号" prop="outside_port">
              <el-input v-model="temp.outside_port" style="width:60%" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="系统版本" prop="os">
              <el-select v-model="temp.os" class="filter-item">
                <el-option v-for="item in versionOptions" :key="item.id" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="CPU 核数" prop="cpu">
              <el-select v-model="temp.cpu" class="filter-item">
                <el-option v-for="item in cpuOptions" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="内存大小" prop="memory">
              <el-select v-model="temp.memory" class="filter-item">
                <el-option v-for="item in memoryOptions" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="硬盘大小" prop="disk">
              <el-select v-model="temp.disk" class="filter-item">
                <el-option v-for="item in diskOptions" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="位置" prop="position">
              <el-select v-model="temp.cloud" class="filter-item">
                <el-option v-for="item in cloudOptions" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="云账号" prop="cloud_user">
              <el-select v-model="temp.cloud_user" class="filter-item">
                <el-option v-for="item in cloudUserOptions" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="用户" prop="user">
              <el-select v-model="temp.user" class="filter-item">
                <el-option v-for="item in userOptions" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="环境" prop="env">
              <el-select v-model="temp.env" class="filter-item">
                <el-option v-for="item in envOptions" :key="item.id" :label="item.name" :value="item.name" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item label="密码" prop="password">
          <el-input v-model="temp.password" style="width:60%" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          保存
        </el-button>
      </div>
    </el-dialog>

    <el-drawer title="详情" :visible.sync="drawerVisible" :with-header="false">
      <host-drawer-content :host="temp" />
    </el-drawer>
  </div>
</template>

<script>
import { getHosts, addHost, updateHost, deleteHost, getEnv } from '@/api/project'
import waves from '@/directive/waves' // waves directive
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import { encrypt, decrypt } from '@/utils/aes'
import HostDrawerContent from '@/components/Drawer/HostDrawerContent'

export default {
  name: 'Host',
  components: { Pagination, HostDrawerContent },
  directives: { waves },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listQuery: {
        page: 1,
        inside_ip: '',
        env: '',
        cloud_user: '',
        limit: 10
      },
      versionOptions: ['CentOS 6', 'CentOS 7', 'Windows Server 2008 R2'],
      cpuOptions: [4, 8, 16, 32],
      userOptions: ['root', 'administrator'],
      memoryOptions: ['4G', '8G', '16G', '32G'],
      diskOptions: ['40G', '100G', '200G'],
      cloudOptions: ['阿里云', '华为云', 'IDC 托管', '公司机房'],
      cloudUserOptions: ['gainhon666', 'lingfannao', '胡振春221240096', '水贝珠宝商业运营管理', 'zhangtian2018', '其它'],
      adminOptions: ['root', 'administrator'],
      envOptions: undefined,
      dialogUploadVisible: false,
      temp: {
        name: undefined,
        hostname: undefined,
        inside_ip: undefined,
        outside_ip: '0.0.0.0',
        inside_port: 22,
        outside_port: 22,
        os: 'CentOS 7',
        cpu: 4,
        memory: '8G',
        disk: '100G',
        cloud: '阿里云',
        cloud_user: 'gainhon666',
        env: '测试环境',
        user: 'root',
        password: undefined,
        created: new Date()
      },
      tempCopy: undefined,
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: '编辑',
        create: '添加',
        detail: '详情'
      },
      downloadLoading: false,
      drawerVisible: false,
      tableHeader: [],
      uploadSuccessCount: 0,
      uploadFailCount: 0
    }
  },
  created() {
    this.getList()
    getEnv().then(response => {
      this.envOptions = response
    })
  },
  methods: {
    getList() {
      getHosts(this.listQuery).then(response => {
        this.list = response.results
        this.total = response.count
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleModifyStatus(row, status) {
      this.$message({
        message: '操作Success',
        type: 'success'
      })
      row.status = status
    },
    resetTemp() {
      this.temp = {
        name: undefined,
        hostname: undefined,
        inside_ip: undefined,
        outside_ip: '0.0.0.0',
        inside_port: 22,
        outside_port: 22,
        os: 'CentOS 7',
        cpu: 4,
        memory: '8G',
        disk: '100G',
        cloud: '阿里云',
        cloud_user: 'gainhon666',
        env: '测试环境',
        user: 'root',
        password: undefined,
        created: new Date()
      }
      this.passwordType = 'password'
    },
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.tempCopy = Object.assign({}, this.temp)
          this.tempCopy.password = encrypt(this.tempCopy.password)
          addHost(this.tempCopy).then(() => {
            this.getList()
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '主机新增成功！',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.temp.password = decrypt(this.temp.password)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.tempCopy = Object.assign({}, this.temp)
          this.tempCopy.password = encrypt(this.tempCopy.password)
          updateHost(this.tempCopy).then(() => {
            this.getList()
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功！',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    handleDelete(id, index) {
      this.$confirm('确认删除', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteHost(id).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功！',
            type: 'success',
            duration: 2000
          })
          // this.list.splice(index, 1)
          this.getList()
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    showDetail(row) {
      this.temp = Object.assign({}, row)
      this.temp.password = decrypt(this.temp.password)
      this.drawerVisible = true
    }
  }
}
</script>
