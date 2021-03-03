const gulp = require('gulp');
const run = require('gulp-run')

function start() {
  return run('/usr/local/bin/pm2 startOrRestart pm2.json').exec()
}

exports.default = gulp.series(start)
