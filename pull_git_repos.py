import requests

username = "shizhengLi"
response = requests.get(f"https://api.github.com/users/{username}/repos")
repos = response.json()

markdown = "# 我的项目\n\n"
for repo in repos:
    markdown += f"- **[{repo['name']}]({repo['html_url']})**  \n"
    markdown += f"  项目简介：{repo['description'] or '暂无描述'}  \n"
    markdown += f"  技术栈：{repo['language'] or '未知'}  \n"
    markdown += f"  ⭐ Star: {repo['stargazers_count']} | 📅 最后更新：{repo['updated_at'][:10]}  \n\n"

with open("README01.md", "w", encoding="utf-8") as f:
    f.write(markdown)
