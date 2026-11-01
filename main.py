from src.tools.tools import web_search,scrape_url

result = scrape_url.invoke({
    "url": "https://nodejs.org/docs/latest/api/assert.html"
})
print(result)

