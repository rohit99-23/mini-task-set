from googlesearch import search

# Simple list of URLs
for url in search("example query", num_results=10):
    print(url)

# Advanced: include titles and descriptions
results = search("example query", advanced=True)
for r in results:
    print(r.title, r.url, r.description)
