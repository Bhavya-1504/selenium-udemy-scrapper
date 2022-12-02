import requests
UDEMY_DEVELOPMENT_COURSES_URL = 'https://www.udemy.com/courses/development/'
response = requests.get(UDEMY_DEVELOPMENT_COURSES_URL)
print('Status Code', response.status_code)
with open('udemy-development.html', 'w') as f:
  f.write(response.text)