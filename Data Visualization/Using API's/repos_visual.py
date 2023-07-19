import requests
import plotly.express as px

url = 'https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers= headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
repo_links , stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

graph_title = 'Python Projects with the Highest Number of Stars on Github'
labels = {'x': 'Repository', 'y': 'Star Count'}
figure = px.bar(x=repo_links, y=stars, title= graph_title, labels= labels, hover_name= hover_texts)
figure.update_layout(title_font_size= 24, xaxis_title_font_size= 20, yaxis_title_font_size= 20)
figure.update_traces(marker_color= 'SteelBlue', marker_opacity= 0.6)
figure.show()