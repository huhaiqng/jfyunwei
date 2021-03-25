<template>
  <div class="app-container">
    <el-table :key="tableKey" :data="list" border fit highlight-current-row style="width:100%;margin-top:15px;">
      <el-table-column label="序号" align="center" width="50px">
        <template slot-scope="{$index}">
          <span>{{ $index + 1 + (queryList.page - 1)*queryList.per_page }}</span>
        </template>
      </el-table-column>
      <el-table-column label="群组名称">
        <template slot-scope="{row}">
          <span>{{ row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="路径">
        <template slot-scope="{row}">
          <span>{{ row.full_path }}</span>
        </template>
      </el-table-column>
      <el-table-column label="描述">
        <template slot-scope="{row}">
          <span>{{ row.description }}</span>
        </template>
      </el-table-column>
      <el-table-column label="地址">
        <template slot-scope="{row}">
          <span class="link-type"><el-link type="primary" :href="row.web_url" target="_blank">{{ row.web_url }}</el-link></span>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center" width="120px">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="showProjects(row.id, row.name)">查看项目</el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="queryList.page" :limit.sync="queryList.per_page" @pagination="getList" />

    <el-dialog :title="groupName" :visible.sync="dialogVisible" width="60%">
      <el-table key="2" :data="groupProjects">
        <el-table-column property="name" label="名称" width="250" />
        <el-table-column property="description" label="描述" width="250" />
        <el-table-column property="http_url_to_repo" label="地址">
          <template slot-scope="{row}">
            <span><el-link type="primary" :href="row.http_url_to_repo" target="_blank">{{ row.http_url_to_repo }}</el-link></span>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
  </div>
</template>
<script>
import { getGitLabGroups, getGitLabGroupProjects } from '@/api/gitlab'
import Pagination from '@/components/Pagination'
export default {
  name: 'GitlabGroup',
  components: { Pagination },
  data() {
    return {
      tableKey: 0,
      list: null,
      groupProjects: null,
      groupName: undefined,
      total: 0,
      temp: {
        name: null,
        permissions: []
      },
      queryList: {
        per_page: 10,
        page: 1
      },
      dialogVisible: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      getGitLabGroups(this.queryList).then(response => {
        this.list = response.data
        this.total = parseInt(response.headers['x-total'])
      })
    },
    showProjects(id, name) {
      this.groupName = name
      this.dialogVisible = true
      getGitLabGroupProjects(id).then(response => {
        this.groupProjects = response.data
      })
    }
  }
}
</script>
