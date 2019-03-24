@echo off

rem compile scss
echo Compiling SCSS to CSS
pysassc vendor/bootstrap/scss/bootstrap.scss static/css/bootstrap/bootstrap.css

rem minify css
echo Minifying CSS
css-html-js-minify static/css/bootstrap/bootstrap.css

rem Copy vendor files
echo Copying vendor files to static/*
cp vendor/bootstrap/dist/js/bootstrap.min.js static/js/bootstrap/bootstrap.min.js
cp vendor/Font-Awesome-Pro/css/all.min.css static/css/fontawesome/all.min.css
