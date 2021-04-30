<template>
  <div class="app-container">
    <el-table :key="tableKey" :data="list" border fit highlight-current-row style="width:100%; margin-top:15px">
      <el-table-column label="序号" align="center" width="50px">
        <template slot-scope="{$index}">
          <span>{{ $index + 1 + (listQuery.page - 1)*listQuery.limit }}</span>
        </template>
      </el-table-column>
      <el-table-column label="任务名称">
        <template slot-scope="{row}">
          <span>{{ row.task_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="开始时间">
        <template slot-scope="{row}">
          <span>{{ row.date_created | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>
      <el-table-column label="结束时间">
        <template slot-scope="{row}">
          <span>{{ row.date_done | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>
      <el-table-column label="参数">
        <template slot-scope="{row}">
          <span>{{ row.task_args }}</span>
        </template>
      </el-table-column>
      <el-table-column label="返回结果">
        <template slot-scope="{row}">
          <span>{{ row.result }}</span>
        </template>
      </el-table-column>
      <el-table-column label="执行状态">
        <template slot-scope="{row}">
          <span>{{ row.status }}</span>
        </template>
      </el-table-column>
    </el-table>
    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
  </div>
</template>
<script>
import Pagination from '@/components/Pagination'
import { getTaskResult } from '@/api/project'
export default {
  name: 'TaskResult',
  components: { Pagination },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      temp: {
        task_name: null,
        date_created: null,
        date_done: null,
        task_args: null,
        result: false,
        status: false
      },
      listQuery: {
        page: 1,
        limit: 10
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      getTaskResult(this.listQuery).then(response => {
        this.list = response.results
        this.total = response.count
      })
    }
  }
}
</script>
