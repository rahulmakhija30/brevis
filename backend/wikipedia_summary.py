#To check if page exists and Print the title and summary of the page
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
def scrape_summary(keywords):
  res={}
  for word in keywords:
    page_py = wiki_wiki.page(word)
    if page_py.exists() == True:#Checking if the page exists
      res[page_py.title]=page_py.summary
    else: #If the page does not exists then use key as "Not Found"
      res["Not Found"]="Page for the entered query does not exists." 
  return res

#Driver Code
if __name__ == "__main__":
  keywords=["Machine Learning","Artificial Intelligence","Dynamic Programming"]
  res=scrape_summary(keywords)
  for title,summary in res.items():
    print("Title :",title)
    print("Summary :",summary)
    print()
