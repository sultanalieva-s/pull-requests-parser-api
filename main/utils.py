import requests
from bs4 import BeautifulSoup as BS


def parse_pull_requests(github_repo_html):
    pull_requests_link = get_pull_requests_link(github_repo_html)
    pull_requests_html = get_pull_requests_html(pull_requests_link)
    pull_requests_data = get_pull_requests_data(pull_requests_html)
    return pull_requests_data


def get_pull_requests_link(github_repo_html):
    soup = BS(github_repo_html, 'lxml')
    pull_requests_link = soup.find('ul', class_='UnderlineNav-body list-style-none').find('a', id='pull-requests-tab').get('href')
    return 'https://github.com/' + pull_requests_link


def get_pull_requests_html(pull_requests_link):
    pull_requests_html = requests.get(pull_requests_link).text
    return pull_requests_html


def get_pull_requests_data(pull_requests_html):
    soup = BS(pull_requests_html, 'lxml')

    pull_req_nav = soup.find('div', class_='Box mt-3 Box--responsive hx_Box--firstRowRounded0')

    pull_requests_titles = pull_req_nav.findAll('a', class_='Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title')
    pull_requests_assignees_reviewers = pull_req_nav.findAll('div', class_='flex-shrink-0 col-3 pt-2 text-right pr-3 no-wrap d-flex hide-sm')

    pull_requests_data = []
    for pull_request_index in range(len(pull_requests_titles)):
        pull_request_data = dict()

        pull_request_data['title'] = pull_requests_titles[pull_request_index].text
        pull_request_data['link'] = 'https://github.com' + pull_requests_titles[pull_request_index].get('href')

        assignees_reviewers_div = pull_requests_assignees_reviewers[pull_request_index]
        assignees_reviewers_spans = assignees_reviewers_div.findAll('span', class_='ml-2 flex-1 flex-shrink-0')
        reviewer_span = assignees_reviewers_spans[0]
        assignees_span = assignees_reviewers_spans[1]

        try:
            reviewer = reviewer_span.find('img', class_='from-avatar avatar-user').get('alt')
        except:
            reviewer = ''

        try:
            assignees = assignees_span.find('img', class_='from-avatar avatar-user').get('alt')
        except:
            assignees = ''

        pull_request_data['reviewers'] = reviewer
        pull_request_data['assignees'] = assignees

        pull_requests_data.append(pull_request_data)

    return pull_requests_data
