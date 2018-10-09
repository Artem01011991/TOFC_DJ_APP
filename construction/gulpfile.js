let gulp = require('gulp'),
    handlebars = require('gulp-handlebars');

gulp.task('build', function() {
    gulp.src('handlebars/*.handlebars')
        .pipe(handlebars())
        .pipe(gulp.dest('../TEST'))
});
