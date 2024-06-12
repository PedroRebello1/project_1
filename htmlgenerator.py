import pandas as pd

def load_news(filename='news.csv'):
    df = pd.read_csv(filename)
    return df

def generate_html(news_df):
    # Open the HTML file for writing with UTF-8 encoding
    with open('news.html', 'w', encoding='utf-8') as f:
        # Write the HTML header
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>News Viewer</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<h1>News Viewer</h1>\n')
        f.write('<table border="1">\n')
        f.write('<tr><th>Title</th><th>Published</th><th>Source</th></tr>\n')

        # Write each row of news data as a table row in HTML
        for _, row in news_df.iterrows():
            published = str(row['published'])
            f.write(f'<tr><td>{row["title"]}</td><td>{published}</td><td>{row["source"]}</td></tr>\n')

        # Close the HTML table and body
        f.write('</table>\n')
        f.write('</body>\n')
        f.write('</html>\n')


if __name__ == '__main__':
    news_df = load_news()
    generate_html(news_df)
