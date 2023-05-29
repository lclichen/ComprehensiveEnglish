# 适用范围

本抓取脚本适用于：

中国科学技术大学 研究生综合英语 高新校区版

Comprehensive English for Graduate Students

[iTEST智能测评云平台](https://itestcloud.unipus.cn/)

## Demo

[Demo](http://home.ustc.edu.cn/~lclichen/eng/)

## 使用说明

1. 登录网站后使用开发者工具复制cookies到`cookie.txt`中
2. 完成听力测试后，点击查看报告->考试概览中的项目，使用开发者工具中的网络选项卡进行抓包（detail页面），获取载荷中每一次考试的epid、每一Part的nodeId（相同结构的考试会有相同的nodeId列表，应该）
3. 执行`python 听力抓取.py`，输出的markdown文件位于`Listen`文件夹内。
4. 使用VSCode的`Markdown Preview Enhanced`扩展，id:shd101wyy.markdown-preview-enhanced，将预览的markdown文件转换为html网页。
5. 打开网页即可预览。

## 注意

可能存在抓取到不该存在的内容的情况，如<!-- -->包裹的注释，请手动删去。
