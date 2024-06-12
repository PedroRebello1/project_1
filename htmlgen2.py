import csv
import datetime
from dateutil import parser

# Read the CSV file
news_data = {}
with open('news.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        source = row['source']
        if source not in news_data:
            news_data[source] = []
        news_data[source].append(row)

# Sort the news items by date/time
for source, news_list in news_data.items():
    news_data[source] = sorted(news_list, key=lambda x: parser.parse(x['published']), reverse=True)

# Create the HTML content
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Compilado Noticias</title>
    <link rel="stylesheet" href="styles.css"> <!-- Include the CSS file -->
</head>
<body>
    <h1>News Viewer</h1>
    <div class="news-container">
'''

for source, news_list in news_data.items():
    html_content += f'<div class="news-column">'
    html_content += f'<h2>{source}</h2>'
    
    for news in news_list:
        title = news['title']
        link = news['link']
        published = news['published']
        
        # Parse and format the published date
        try:
            published_date = parser.parse(published)
            formatted_date = published_date.strftime('%d/%m/%Y | %H:%M')
        except ValueError:
            formatted_date = news['published']  # Use original if parsing fails

        html_content += f'''
        <div class="news-card">
            <h3>{title}</h3>
            <p><a href="{link}">Read more</a></p>
            <p class="published">{formatted_date}</p>
        </div>
        '''

    html_content += '</div>'

html_content += '''
    </div>
</body>
</html>'''

# Write the HTML content to a file
with open('news.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
