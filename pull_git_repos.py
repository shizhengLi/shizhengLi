# import requests

# username = "shizhengLi"
# response = requests.get(f"https://api.github.com/users/{username}/repos")
# repos = response.json()

# markdown = "# 我的项目\n\n"
# for repo in repos:
#     markdown += f"- **[{repo['name']}]({repo['html_url']})**  \n"
#     markdown += f"  项目简介：{repo['description'] or '暂无描述'}  \n"
#     markdown += f"  技术栈：{repo['language'] or '未知'}  \n"
#     markdown += f"  ⭐ Star: {repo['stargazers_count']} | 📅 最后更新：{repo['updated_at'][:10]}  \n\n"

# with open("README.md", "w", encoding="utf-8") as f:
#     f.write(markdown)



import requests

username = "shizhengLi"
page = 1
repos = []
while True:
    response = requests.get(f"https://api.github.com/users/{username}/repos?page={page}&per_page=100")
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        break
    page_repos = response.json()
    if not page_repos:  # 没有更多仓库
        break
    repos.extend(page_repos)
    page += 1

markdown = "# 我的项目\n\n"
for repo in repos:
    markdown += f"- **[{repo['name']}]({repo['html_url']})**  \n"
    markdown += f"  项目简介：{repo['description'] or '暂无描述'}  \n"
    markdown += f"  技术栈：{repo['language'] or '未知'}  \n"
    markdown += f"  ⭐ Star: {repo['stargazers_count']} | 📅 最后更新：{repo['updated_at'][:10]}  \n\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown)
