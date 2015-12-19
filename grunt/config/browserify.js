module.exports = {
  dist: {
    files: {
      './dist/components/js/application.js': ['./okwarning/okwarning/static/es6/application.js'],
    },
    options: {
      transform: ['babelify']
    }
  }
}
