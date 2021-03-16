<template>
  <div class="app-container">
    <div class="filter-container">
      <el-select v-model="dailyQueryList.group" placeholder="选择组" clearable class="filter-item" @change="getUserList">
        <el-option v-for="item in groups" :key="item.id" :label="item.name" :value="item.name" />
      </el-select>
      <el-select v-model="dailyQueryList.user" placeholder="选择用户" clearable class="filter-item">
        <el-option v-for="item in users" :key="item.id" :label="item.name" :value="item.username" />
      </el-select>
      <el-date-picker
        v-model="pick_date"
        type="daterange"
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期"
      />
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="getReporList">
        搜索
      </el-button>
    </div>
    <el-table :key="0" :data="dailys" border highlight-current-row style="width: 100%; margin-top:15px;">
      <el-table-column label="序号" align="center" width="50px">
        <template slot-scope="{$index}">
          <span>{{ $index + 1 + (dailyQueryList.page - 1)*dailyQueryList.limit }}</span>
        </template>
      </el-table-column>
      <el-table-column label="用户名" width="100px">
        <template slot-scope="{row}">
          <span>{{ row.owner.username }}</span>
        </template>
      </el-table-column>
      <el-table-column label="今日工作任务">
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
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="dailyQueryList.page" :limit.sync="dailyQueryList.limit" @pagination="getReporList" />
  </div>
</template>

<script>
import { getReportDaily } from '@/api/report'
import { getUser, getGroup } from '@/api/auth-permission'
import Pagination from '@/components/Pagination'
export default {
  name: 'Report',
  components: { Pagination },
  data() {
    return {
      total: 0,
      dailys: [],
      groups: [],
      users: [],
      pick_date: null,
      dailyQueryList: {
        group: '',
        user: '',
        start_date: null,
        end_date: null,
        limit: 10
      },
      groupQueryList: {
        page: 1,
        limit: 10000,
        type: 'report'
      }
    }
  },
  created() {
    this.getGroupList()
    this.getUserList()
    // const today = new Date()
    this.pick_date = [new Date(), new Date()]
    this.getReporList()
  },
  methods: {
    getReporList() {
      this.pick_date[0].setSeconds(0)
      this.pick_date[0].setMinutes(0)
      this.pick_date[0].setHours(0)
      this.pick_date[1].setSeconds(59)
      this.pick_date[1].setMinutes(59)
      this.pick_date[1].setHours(23)
      this.dailyQueryList.start_date = this.pick_date[0]
      this.dailyQueryList.end_date = this.pick_date[1]
      getReportDaily(this.dailyQueryList).then(response => {
        this.dailys = response.results
        this.total = response.count
      })
    },
    getGroupList() {
      getGroup(this.groupQueryList).then(response => {
        this.groups = response
      })
    },
    getUserList() {
      var userQueryList = { page: 1, limit: 10000, group: this.dailyQueryList.group, type: 'report' }
      getUser(userQueryList).then(response => {
        this.users = response
      })
    }
  }
}
</script>
