<template>
  <div class="app-container">
    <el-table :key="tableKey" :data="list" border fit highlight-current-row style="width:100%;margin-top:15px;">
      <el-table-column label="序号" align="center" width="50px">
        <template slot-scope="{$index}">
          <span>{{ $index + 1 + (queryList.page - 1)*queryList.per_page }}</span>
        </template>
      </el-table-column>
      <el-table-column label="域名">
        <template slot-scope="{row}">
          <span>{{ row.DomainName }}</span>
        </template>
      </el-table-column>
      <el-table-column label="记录数量">
        <template slot-scope="{row}">
          <span>{{ row.RecordCount }}</span>
        </template>
      </el-table-column>
      <el-table-column label="版本名">
        <template slot-scope="{row}">
          <span>{{ row.VersionName }}</span>
        </template>
      </el-table-column>
      <el-table-column label="阿里域名">
        <template slot-scope="{row}">
          <span>{{ row.AliDomain }}</span>
        </template>
      </el-table-column>
      <el-table-column label="创建时间" width="150px">
        <template slot-scope="{row}">
          <span>{{ row.CreateTime | parseTime('{y}-{m}-{d} {h}:{i}') }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center" width="100px">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="showRecords(row.DomainName)">查看记录</el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="queryList.page" :limit.sync="queryList.per_page" @pagination="getList" />

    <el-dialog :title="recordQueryList.domain_name" :visible.sync="dialogVisible" width="60%">
      <div class="tab-pane">
        <el-scrollbar>
          <el-table key="2" :data="domain_records">
            <el-table-column property="RR" label="名称" width="250" />
            <el-table-column property="Type" label="类型" width="250" />
            <el-table-column property="Value" label="值" width="250" />
            <el-table-column property="http_url_to_repo" label="地址">
              <template slot-scope="{row}">
                <span>
                  <el-link type="primary" :href="'http://' + row.RR + '.' + recordQueryList.domain_name" target="_blank">
                    {{ row.RR + '.' + recordQueryList.domain_name }}
                  </el-link>
                </span>
              </template>
            </el-table-column>
          </el-table>
        </el-scrollbar>
      </div>
      <pagination v-show="total>0" :total="recordTotal" :page.sync="recordQueryList.page" :limit.sync="recordQueryList.per_page" @pagination="getRecords" />
    </el-dialog>
  </div>
</template>
<script>
import { getGaingon666Domain, getGaingon666DomainRecord } from '@/api/domain'
import Pagination from '@/components/Pagination'
export default {
  name: 'GitlabGroup',
  components: { Pagination },
  data() {
    return {
      tableKey: 0,
      list: null,
      domain_records: null,
      total: 0,
      recordTotal: 0,
      temp: {
        name: null,
        permissions: []
      },
      queryList: {
        per_page: 10,
        page: 1
      },
      recordQueryList: {
        per_page: 10,
        page: 1,
        domain_name: undefined
      },
      dialogVisible: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      getGaingon666Domain(this.queryList).then(response => {
        this.list = response.Domains.Domain
        this.total = response.TotalCount
      })
    },
    showRecords(domain_name) {
      this.recordQueryList.domain_name = domain_name
      this.dialogVisible = true
      getGaingon666DomainRecord(this.recordQueryList).then(response => {
        this.domain_records = response.DomainRecords.Record
        this.recordTotal = response.TotalCount
      })
    },
    getRecords() {
      getGaingon666DomainRecord(this.recordQueryList).then(response => {
        this.domain_records = response.DomainRecords.Record
        this.recordTotal = response.TotalCount
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.tab-pane{
  flex: 1;
  /deep/.el-scrollbar{
    height: calc(100vh - 400px);
    .el-scrollbar__wrap{
      overflow-x: hidden;
    }
  }
}
</style>
