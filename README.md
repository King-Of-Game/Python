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
- git commit --amend 'msg'    # 给上一次提交打个补丁
- git log
- git push origin HEAD:refs/for/分支名    # gerrit 的推送方式
- git reset HEAD^    # 回退所有内容到上一个版本  

### example

- git commit [file] -m 'feat: 增加文件  project-001'

### submission process
1. 从git上克隆项目到本地
   - git clone ssh://project/
2. 在项目目录下修改和账户相同的邮箱与真实的姓名
   - git config --global user.email xx@qq.com
   - git config --global user.name yixuan
   - git init  # 更新配置信息
3. 在本地仓库新增分支（和待上传的远程分支名字相同）
   - git branch -a  #查看本地和线上的所有分支
   - git branch [local_depository]  #新建本地分支
   - git checkout -b [local_depository]  #从当前分支基础上新建一个本地分支，原分支下被修改的文件会被继承
4. 查看文件修改状态
   - git status
5. 先提交代码到本地仓库
   - git add .
   - git commit . -m 'feat: 修复xxxBUG project-1 '
6. 拉取最新代码
   - git pull origin <remote_branch>:<local_branch>  #本地分支不填，默认拉取到当前分支
     - eg: git pull origin master:brantest
7. 合并到 master分支
   - git checkout master
   - git merge [your_dev_name]
8. 提交代码到远程仓库
   - git push origin <local_branch>:<remote_branch>  #git 原生推送
   - git push origin HEAD:refs/for/<remote_branch>  #gerrit 的推送方式