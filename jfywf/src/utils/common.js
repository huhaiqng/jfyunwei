export function scrollTo(index) {
  // 获取目标的 offsetTop
  // css选择器是从 1 开始计数，我们是从 0 开始，所以要 +1
  // const targetOffsetTop = document.querySelector(`.content div:nth-child(${index + 1})`).offsetTop
  const targetOffsetTop = document.getElementById(index).offsetTop
  // 获取当前 offsetTop
  let scrollTop = document.documentElement.scrollTop || document.body.scrollTop
  // 定义一次跳 50 个像素，数字越大跳得越快，但是会有掉帧得感觉，步子迈大了会扯到蛋
  const STEP = 2000
  // 判断是往下滑还是往上滑
  if (scrollTop > targetOffsetTop) {
    // 往上滑
    smoothUp()
  } else {
    // 往下滑
    smoothDown()
  }
  // 定义往下滑函数
  function smoothDown() {
    // 如果当前 scrollTop 小于 targetOffsetTop 说明视口还没滑到指定位置
    if (scrollTop < targetOffsetTop) {
      // 如果和目标相差距离大于等于 STEP 就跳 STEP
      // 否则直接跳到目标点，目标是为了防止跳过了。
      if (targetOffsetTop - scrollTop >= STEP) {
        scrollTop += STEP
      } else {
        scrollTop = targetOffsetTop
      }
      document.body.scrollTop = scrollTop
      document.documentElement.scrollTop = scrollTop
      // 关于 requestAnimationFrame 可以自己查一下，在这种场景下，相比 setInterval 性价比更高
      requestAnimationFrame(smoothDown)
    }
  }
  // 定义往上滑函数
  function smoothUp() {
    if (scrollTop > targetOffsetTop) {
      if (scrollTop - targetOffsetTop >= STEP) {
        scrollTop -= STEP
      } else {
        scrollTop = targetOffsetTop
      }
      document.body.scrollTop = scrollTop
      document.documentElement.scrollTop = scrollTop
      requestAnimationFrame(smoothUp)
    }
  }
}
