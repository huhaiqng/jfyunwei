<template>
  <div class="app-container">
    <el-table :key="tableKey" :data="list" border fit highlight-current-row style="width:100%;margin-top:15px;">
      <el-table-column label="序号" align="center" width="50px">
        <template slot-scope="{$index}">
          <span>{{ $index + 1 + (queryList.page - 1)*queryList.per_page }}</span>
        </template>
      </el-table-column>
      <el-table-column label="名称">
        <template slot-scope="{row}">
          <span>{{ row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="名称">
        <template slot-scope="{row}">
          <span>{{ row.description }}</span>
        </template>
      </el-table-column>
      <el-table-column label="路径">
        <template slot-scope="{row}">
          <span>{{ row.path_with_namespace }}</span>
        </template>
      </el-table-column>
      <el-table-column label="地址">
        <template slot-scope="{row}">
          <span>{{ row.http_url_to_repo }}</span>
        </template>
      </el-table-column>
    </el-table>
    <pagination v-show="total>0" :total="total" :page.sync="queryList.page" :limit.sync="queryList.per_page" @pagination="getList" />
  </div>
</template>
<script>
import { getGitLabProjects } from '@/api/gitlab'
import Pagination from '@/components/Pagination'
export default {
  name: 'GitlabProject',
  components: { Pagination },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      temp: {
        name: null,
        permissions: []
      },
      queryList: {
        per_page: 10,
        page: 1
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      getGitLabProjects(this.queryList).then(response => {
        this.list = response.data
        this.total = parseInt(response.headers['x-total'])
      })
    }
  }
}
</script>
