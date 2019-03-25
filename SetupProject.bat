@echo off

rem compile scss
rem echo Compiling SCSS to CSS
rem pysassc vendor/bootstrap/scss/bootstrap.scss static/css/bootstrap/bootstrap.css

rem minify css
rem echo Minifying CSS
rem css-html-js-minify static/css/bootstrap/bootstrap.css

rem Copy vendor files
echo Copying vendor files to static/*
cp vendor/Font-Awesome-Pro/css/all.min.css static/css/fontawesome/all.min.css
xcopy /E %CD%\vendor\Font-Awesome-Pro\webfonts %CD%\static\webfonts

cp vendor/gameforest/dist/css/theme.min.css static/css/theme.min.css
cp vendor/gameforest/dist/js/theme.bundle.min.js static/js/theme.bundle.min.js
cp vendor/gameforest/dist/js/theme.min.js static/js/theme.min.js

xcopy /E %CD%\vendor\gameforest\dist\plugins %CD%\static\plugins
