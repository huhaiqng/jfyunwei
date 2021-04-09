<template>
  <div class="app-container">
    <el-row v-for="(r, i) in rows_num" :key="i" :gutter="20">
      <el-col v-for="(o, j) in addr_num > (i+1)*12 ? 12 : addr_num - i*12" :key="j" :span="2">
        <a :href="addrs[12*i + j].url" target="_blank">
          <el-card shadow="hover" :body-style="{ padding: '10px' }">
            <el-image :src="addrs[12*i + j].img" fit="fill" />
            <div style="padding: 10px;">
              <span style="text-align:center;display:block;"> {{ addrs[12*i + j].name }} </span>
            </div>
          </el-card>
        </a>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getAddress } from '@/api/address'

export default {
  name: 'Dashboard',
  data() {
    return {
      addrs: null,
      addr_num: null,
      rows_num: 0
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  created() {
    getAddress().then(response => {
      this.addrs = response
      this.addr_num = this.addrs.length
      this.rows_num = Math.ceil(this.addrs.length / 12)
    })
  }
}
</script>

<style lang="scss" scoped>
.el-row {
  margin-bottom: 15px;
  &:last-child {
    margin-bottom: 0;
  }
}
.bottom {
  margin-top: 13px;
  line-height: 12px;
}
.button {
  padding: 0;
  float: right;
}
.image {
  width: 100%;
  height: 100%;
  display: block;
}
.clearfix:before,
.clearfix:after {
    display: table;
    content: "";
}
.clearfix:after {
    clear: both
}
</style>
