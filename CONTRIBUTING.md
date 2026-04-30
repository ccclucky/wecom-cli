# Contributing to WeCom CLI

感谢你对 WeCom CLI 的关注！为了保持项目的高质量和可维护性，请在提交贡献前阅读以下指南。

## 🛠️ 环境准备

本项目强制使用 `pre-commit` 进行代码质量控制。

1.  **克隆仓库**：
    ```bash
    git clone https://github.com/your-username/wecom-cli.git
    cd wecom-cli
    ```

2.  **安装开发依赖**：
    ```bash
    pip install -e ".[dev]"
    ```

3.  **激活 Hooks**：
    ```bash
    pre-commit install
    ```

## 🧪 开发流程

### 1. 修改或添加接口
如果你发现某个接口缺失或参数有误：
- 修改 `specs/wecom/<domain>.yaml` 中的定义。
- 运行代码生成：`python scripts/codegen.py`。
- **严禁直接修改 `apis/generated_client.py` 或 `cli/generated_commands.py`。**

### 2. 运行检查
在提交 commit 前，请确保通过所有检查：
```bash
pre-commit run --all-files
```

### 3. 测试要求
- 新功能必须包含单元测试（放在 `tests/` 下）。
- 我们使用 `pytest` 进行测试。

## 📝 提交规范

我们遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：
- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档更新
- `chore:` 构建过程或辅助工具的变动

## 🚀 提交 PR
- 在 PR 描述中详细说明改动的动机。
- 如果是修复接口，请附上对应的企业微信文档链接。
- PR 必须通过 GitHub Actions 的所有 CI 检查。

---

再次感谢你的贡献！
