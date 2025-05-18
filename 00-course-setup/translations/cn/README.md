<<<<<<< HEAD
# 课程介绍和学习环境设置

我们非常高兴您能够开始学习本课程，希望您能通过学习使用生成式 AI 构建有趣的应用！

为了让您提升学习效率，我们创建了该页面，概述了所有关于本课程需要设置的步骤、相关技术要求以及如何获取帮助。

## 安装步骤

要开始学习本课程，您需要完成以下设置。

### 1. Fork this Repo

[Fork 这个完整的 repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到你自己的 GitHub 账号下以便您能完成代码的修改和完成相关的挑战. 您也可以 [给该 repo star (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) 让您更容易找到它和相关的 Repo.

### 2. 创建 GitHub Codespaces

为了避免运行代码时出现任何依赖性问题，我们建议在 GitHub Codespace 中运行本课程的相关例子。

这可以通过选择该 Repo 版本上的“Code”选项并选择 **Codespaces** 选项来创建。

### 3. 存储您的 API Keys

在构建任何类型的应用程序时，确保 API Keys 的安全非常重要。 我们建议您不要将任何 API 密钥直接存储在您正在使用的代码中，因为将这些详细信息提交到公共存储库可能会导致不必要的费用成本和问题。

![Dialog showing buttons to create a codespace](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

## 在您的设备上本地运行

要在本地运行代码，您需要安装某个版本的 Python。 个人建议安装 **[miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)** - 这是相当轻量级的安装，支持不同 Python **虚拟环境** 的 `conda` 包管理器 。

安装 miniconda 后，您需要克隆存储库并创建一个用于本课程的 Python 虚拟环境：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### 使用 Visual Studio Code Python 插件

学习本课程，建议使用 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-bethanycheum) 的 [Python 插件](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-bethanycheum).

> **注意**：在 VS Code 中克隆并打开该目录后，会自动建议您安装 Python 插件。 还必须如上所述要求安装 miniconda。

> **注意**：如果 VS Code 建议您在容器中重新打开 Repo，您需要拒绝此操作以使用本地 Python 安装的环境。

### 在浏览器中使用 Jupyter 

您还可以直接从自己计算机上的浏览器使用 Jupyter 环境。 实际上，经典的 Jupyter 和 Jupyer Hub 都提供了相当便捷的开发环境，具有代码自动完成、代码高亮等功能。

要在本地启动 Jupyter，请转到课程目录，然后执行：

```bash
jupyter notebook
```
or
```bash
jupyterhub
```
然后，您可以导航到任何“.ipynb”文件，打开它们进行学习。

### 在容器中运行

我们也可以在容器中运行代码。 由于我们的 Repo 包含特殊的 “.devcontainer” 文件夹，该文件夹指示如何为此 Repo 创建容器，因此 VS Code 将允许您重新打开容器中的代码。 这需要安装 Docker，而且会比较复杂，所以我们推荐给更有经验的用户。

使用 GitHub Codespaces 时确保 API Secrets 安全的最佳方法之一是使用 Codespace Secrets。 请按照本指南了解如何[管理 Codespace Secrets ](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)。

## 相关课程和技术要求

该课程有 6 节基础课和 6 节相关的编程课。

对于编程课，我们使用 Azure OpenAI Service 。 您将需要访问 Azure OpenAI 服务和 API Key 才能运行此代码。 您可以通过这里 [完成此申请](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOFA5Qk1UWDRBMjg0WFhPMkIzTzhKQ1dWNyQlQCN0PWcu&culture=en-us&country=us?WT.mc_id=academic-105485-koreyst) 来申请访问权限。

当您等待审核时，每个编码课程还包含一个“README.md”文件，您可以在里面查看代码和相关内容

## 首次使用 Azure OpenAI Service

如果这是您第一次使用 Azure OpenAI Service，请按照本指南了解如何[创建和部署 an Azure OpenAI Service 资源.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 找到志同道合的人

我们在官方 [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 中创建了学习频道，用于结识其他学习者。 这是与其他志同道合的企业家、学生以及任何希望在生成式人工智能领域提升水平的人建立联系的方式。

[![加入 Discord 频道](https://dcbadge.vercel.app/api/server/ByRwuEEgH4?WT.mc_id=academic-105485-koreyst)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

项目团队也将在这个 Discord server 上为任何学习者提供帮助。

## 贡献该内容

本课程是一项开源计划。 如果您发现需要改进的地方或问题，请创建 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或记录 [GitHub 问题](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

课程项目团队将跟踪所有贡献，为开源做出贡献是在生成人工智能领域建立职业生涯的绝佳方式。

大多数贡献都要求您遵循贡献者许可协议 (CLA)，声明您有权并且实际上授予我们使用您的贡献的权利。 有关详细信息，请访问[CLA，贡献者许可协议网站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：翻译此存储库中的文本时，请确保不使用机器翻译。 我们将通过社区验证翻译，因此请用您熟悉的语言进行翻译。

当您提交拉取请求时，CLA-bot 将自动确定您是否需要提供 CLA 并适当地描述 PR（例如标签、评论）。 只需按照机器人提供的说明进行操作即可。 您只需使用我们的 CLA 在所有存储库中执行一次此操作。

该项目采用了微软开源行为准则。 有关更多信息，请阅读行为准则常见问题解答，或联系 [电子邮件 opencode](opencode@microsoft.com) 提出任何其他问题或意见。

## 我们一起开始进入学习

现在您已经完成了完成本课程所需的设置步骤，让我们开始进入[生成式人工智能和 LLMs 简介](../../../01-introduction-to-genai/translations/cn/README.md?WT.mc_id=academic-105485-koreyst)。
=======
# 课程介绍和学习环境设置

我们非常高兴您能够开始学习本课程，希望您能通过学习使用生成式 AI 构建有趣的应用！

为了让您提升学习效率，我们创建了该页面，概述了所有关于本课程需要设置的步骤、相关技术要求以及如何获取帮助。

## 安装步骤

要开始学习本课程，您需要完成以下设置。

### 1. Fork this Repo

[Fork 这个完整的 repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到你自己的 GitHub 账号下以便您能完成代码的修改和完成相关的挑战. 您也可以 [给该 repo star (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) 让您更容易找到它和相关的 Repo.

### 2. 创建 GitHub Codespaces

为了避免运行代码时出现任何依赖性问题，我们建议在 GitHub Codespace 中运行本课程的相关例子。

这可以通过选择该 Repo 版本上的“Code”选项并选择 **Codespaces** 选项来创建。

### 3. 存储您的 API Keys

在构建任何类型的应用程序时，确保 API Keys 的安全非常重要。 我们建议您不要将任何 API 密钥直接存储在您正在使用的代码中，因为将这些详细信息提交到公共存储库可能会导致不必要的费用成本和问题。

![Dialog showing buttons to create a codespace](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

## 在您的设备上本地运行

要在本地运行代码，您需要安装某个版本的 Python。 个人建议安装 **[miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)** - 这是相当轻量级的安装，支持不同 Python **虚拟环境** 的 `conda` 包管理器 。

安装 miniconda 后，您需要克隆存储库并创建一个用于本课程的 Python 虚拟环境：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### 使用 Visual Studio Code Python 插件

学习本课程，建议使用 [Visual Studio Code](https://code.visualstudio.com/?WT.mc_id=academic-77998-bethanycheum) 的 [Python 插件](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-bethanycheum).

> **注意**：在 VS Code 中克隆并打开该目录后，会自动建议您安装 Python 插件。 还必须如上所述要求安装 miniconda。

> **注意**：如果 VS Code 建议您在容器中重新打开 Repo，您需要拒绝此操作以使用本地 Python 安装的环境。

### 在浏览器中使用 Jupyter 

您还可以直接从自己计算机上的浏览器使用 Jupyter 环境。 实际上，经典的 Jupyter 和 Jupyer Hub 都提供了相当便捷的开发环境，具有代码自动完成、代码高亮等功能。

要在本地启动 Jupyter，请转到课程目录，然后执行：

```bash
jupyter notebook
```
or
```bash
jupyterhub
```
然后，您可以导航到任何“.ipynb”文件，打开它们进行学习。

### 在容器中运行

我们也可以在容器中运行代码。 由于我们的 Repo 包含特殊的 “.devcontainer” 文件夹，该文件夹指示如何为此 Repo 创建容器，因此 VS Code 将允许您重新打开容器中的代码。 这需要安装 Docker，而且会比较复杂，所以我们推荐给更有经验的用户。

使用 GitHub Codespaces 时确保 API Secrets 安全的最佳方法之一是使用 Codespace Secrets。 请按照本指南了解如何[管理 Codespace Secrets ](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)。

## 相关课程和技术要求

该课程有 6 节基础课和 6 节相关的编程课。

对于编程课，我们使用 Azure OpenAI Service 。 您将需要访问 Azure OpenAI 服务和 API Key 才能运行此代码。 您可以通过这里 [完成此申请](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOFA5Qk1UWDRBMjg0WFhPMkIzTzhKQ1dWNyQlQCN0PWcu&culture=en-us&country=us?WT.mc_id=academic-105485-koreyst) 来申请访问权限。

当您等待审核时，每个编码课程还包含一个“README.md”文件，您可以在里面查看代码和相关内容

## 首次使用 Azure OpenAI Service

如果这是您第一次使用 Azure OpenAI Service，请按照本指南了解如何[创建和部署 an Azure OpenAI Service 资源.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 找到志同道合的人

我们在官方 [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 中创建了学习频道，用于结识其他学习者。 这是与其他志同道合的企业家、学生以及任何希望在生成式人工智能领域提升水平的人建立联系的方式。

[![加入 Discord 频道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

项目团队也将在这个 Discord server 上为任何学习者提供帮助。

## 贡献该内容

本课程是一项开源计划。 如果您发现需要改进的地方或问题，请创建 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或记录 [GitHub 问题](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

课程项目团队将跟踪所有贡献，为开源做出贡献是在生成人工智能领域建立职业生涯的绝佳方式。

大多数贡献都要求您遵循贡献者许可协议 (CLA)，声明您有权并且实际上授予我们使用您的贡献的权利。 有关详细信息，请访问[CLA，贡献者许可协议网站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：翻译此存储库中的文本时，请确保不使用机器翻译。 我们将通过社区验证翻译，因此请用您熟悉的语言进行翻译。

当您提交拉取请求时，CLA-bot 将自动确定您是否需要提供 CLA 并适当地描述 PR（例如标签、评论）。 只需按照机器人提供的说明进行操作即可。 您只需使用我们的 CLA 在所有存储库中执行一次此操作。

该项目采用了微软开源行为准则。 有关更多信息，请阅读行为准则常见问题解答，或联系 [电子邮件 opencode](opencode@microsoft.com) 提出任何其他问题或意见。

## 我们一起开始进入学习

现在您已经完成了完成本课程所需的设置步骤，让我们开始进入[生成式人工智能和 LLMs 简介](../../../01-introduction-to-genai/translations/cn/README.md?WT.mc_id=academic-105485-koreyst)。
>>>>>>> c7e53753e825243de60044c9109ebfedd95bb273
