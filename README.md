# Full_Stack_phase0
AI全栈学习Phase0仓库


# phase0简单介绍

## 教程：
1. [现代开发环境教程](learning_file\modern_python_and_uv_guide.md)
2. [AI开发装饰器和闭包](learning_file\python_decorators_and_functional_guide.md)
3. [python异步编程](learning_file\python_async_programming_guide.md)
4. [python面向对象编程和现代系统](learning_file\python_oop_and_typing_guide.md)

## phase0成果
[指导文件](learning_file\phase0_week1_hands_on_project.md)

[GitHub仓库地址](https://github.com/Equinox-HHan/AI_Full_Stack)


## Sub_module

如果目前子项目 B 还是一个完全没有创建的新项目，整体流程遵循：**先在 GitHub 建立子项目并初始化初始提交，再回到主项目将其挂载为 Submodule**。

以下是完整的实操步骤：

---

### 第一阶段：在 GitHub 与本地初始化子项目 B

Git Submodule 要求目标仓库必须至少存在一个 Commit（空仓库无法被挂载为子模块）。

#### 1. 在 GitHub 上创建仓库 B

1. 登录 GitHub，点击右上角 **+** $\rightarrow$ **New repository**。
2. 填写仓库名（如 `Repo-B`），属性选择 **Public** 或 **Private**。
3. **重要**：勾选 **Add a README file**（这样仓库创建后会自动生成初始 commit，无需手动推空代码）。
4. 点击 **Create repository**。
5. 复制仓库 B 的 Git 地址（如 `[https://github.com/](https://github.com/)<你的用户名>/Repo-B.git`）。

---

### 第二阶段：在本地主项目 A 中接入子模块

#### 2. 进入本地主项目目录

打开终端或命令行，进入主项目 A 的本地工作根目录：

```bash
cd /path/to/Repo-A

```

#### 3. 执行添加子模块命令

运行 `git submodule add`，指定仓库地址以及希望它存放在主项目中的文件夹路径（例如 `packages/Repo-B` 或 `libs/Repo-B`）：

```bash
git submodule add https://github.com/<你的用户名>/Repo-B.git libs/Repo-B

```

* **执行结果：**
* Git 会自动从 GitHub 拉取 `Repo-B` 的代码并新建 `libs/Repo-B` 文件夹。
* 根目录下会自动生成一个 `.gitmodules` 文件，用于记录子模块的映射关系。



#### 4. 提交并推送到主项目 A

查看当前工作区变更：

```bash
git status

```

此时会看到暂存区有两个新条目：`.gitmodules` 和 `libs/Repo-B`。

执行提交和推送：

```bash
git add .
git commit -m "feat: add submodule Repo-B"
git push origin main

```

* **验证：** 打开 GitHub 网页端的 `Repo-A`，会看到 `libs/Repo-B` 显示为一个带小文件夹/链条图标的目录，后面跟着一串哈希值（如 `@ 7a1b2c3`），点击它能直接跳转到 `Repo-B` 的主页。

---

### 第三阶段：后续日常开发与代码同步

#### 场景 1：在主项目内直接开发子项目 B 的代码并提交

不需要单独在外面克隆一份 B，直接在 `libs/Repo-B` 目录下操作即可：

```bash
# 1. 进入子模块文件夹
cd libs/Repo-B

# 2. 确保在主分支上（submodule 默认可能处于 detached HEAD 游离状态）
git checkout main

# 3. 新建或修改子项目的文件
echo "export const utils = () => {};" > index.js

# 4. 提交并推送到 B 的远程仓库
git add .
git commit -m "feat: add utils function"
git push origin main

# 5. 回到主项目 A 记录这次更新
cd ../..
git add libs/Repo-B
git commit -m "chore: update submodule Repo-B reference"
git push origin main

```

#### 场景 2：他人（或换电脑）克隆主项目 A

直接普通 `git clone` 主项目时，子模块文件夹默认是空的。需要带上递归参数：

```bash
# 方式 A：一次性完整克隆（推荐）
git clone --recurse-submodules https://github.com/<你的用户名>/Repo-A.git

# 方式 B：如果不小心已经普通克隆了，手动拉取子模块代码
cd Repo-A
git submodule update --init --recursive

```