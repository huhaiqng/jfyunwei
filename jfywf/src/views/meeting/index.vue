<template>
  <div class="app-container">
    <el-row>
      <el-col :span="3">
        <div>&nbsp;</div>
      </el-col>
      <el-col :span="18">
        <el-table :key="tableKey" :data="list" fit highlight-current-row style="margin-top:15px;margin-bottom:15px;">
          <el-table-column label="序号" align="center" width="50px">
            <template slot-scope="{$index}">
              <span>{{ $index + 1 }}</span>
            </template>
          </el-table-column>
          <el-table-column label="姓名">
            <template slot-scope="{row}">
              <span>{{ row.username }}</span>
            </template>
          </el-table-column>
          <el-table-column label="组">
            <template slot-scope="{row}">
              <span>{{ row.groups[0].name }}</span>
            </template>
          </el-table-column>
          <el-table-column label="早会主持">
            <template slot-scope="{row}">
              <el-tag size="small" :type="row.hosted?'success':'info'">
                {{ row.hosted?"已完成":"未完成" }}
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column label="主持日期">
            <template slot-scope="{row}">
              <span>{{ row.hosted_date }}</span>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import { getUserHostedInfo } from '@/api/user'
export default {
  name: 'Meeting',
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      temp: {
        username: null,
        groups: null,
        houted: null,
        hosted_date: null
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      getUserHostedInfo().then(response => {
        this.list = response
      })
    }
  }
}
</script>
