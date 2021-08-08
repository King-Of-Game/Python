# Python之旅

## 介绍

- 记录自己的成长

## git 

### 提交类型

- refactor: 重构代码或其他优化举措
- feat: 新增功能
- fix: 修复 bug
- docs: 文档相关的改动
- style: 对代码的格式化改动，代码逻辑并未产生任何变化(例如代码缩进，分号的移除和添加)
- test: 新增或修改测试用例
- chore: 项目工程方面的改动，代码逻辑并未产生任何变化
- revert: 恢复之前的提交

### 常用命令

- git add fileName
- git status
- git commit --amend 'msg'
- git log
- git push origin HEAD:refs/for/分支名
- git reset HEAD^            # 回退所有内容到上一个版本  

### example

- git commit [file] -m 'feat: 增加文件  project-001'

### submission process
1. 拉取项目
   - git clone ssh://project/
2. 在项目目录下修改和账户相同的邮箱与真实的姓名
   - git config --global user.email xx@qq.com
   - git config --global user.name yixuan
3. 在本地仓库新增分支（和待上传的远程分支名字相同）
   1. git init
   2. git branch -a
   3. git checkout -b dev_name
4. 先提交代码到本地仓库
   - git add .
   - git commit . -m 'feat: 增加分页功能 project-001'
5. 提交代码到仓库
   - git push origin HEAD:refs/for/release_v1.0