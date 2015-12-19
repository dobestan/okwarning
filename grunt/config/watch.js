module.exports = {
  sass: {
    files: './okwarning/okwarning/static/scss/**/*.scss',
    tasks: ['compass'],
  },

  es6: {
    files: './okwarning/okwarning/static/es6/**/*.js',
    tasks: ['browserify'],
  },
}
