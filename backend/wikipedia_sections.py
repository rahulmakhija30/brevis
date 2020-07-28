#To fetch top N sections (other than summary) for a keyword from Wikipedia
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
def print_sections(keywords,number_sections):
  res={}
  for word in keywords:
    page_py = wiki_wiki.page(word)
    if page_py.exists() == True:
      res[word] = fetch_sections(page_py,number_sections)
    else:
      res["Not Found"]="Page for the entered query does not exists."
  return res

def fetch_sections(page_py,number_sections):
  res={}
  count=0
  for section in page_py.sections:
    res[section.title] = section.text
    count+=1
    if(count==number_sections):
      break
  return res


if __name__ == "__main__":
  keywords=["Machine Learning","Artificial Intelligence","Git"]
  res=print_sections(keywords,1)
  for keyword,content in res.items():
    for title,text in content.items():
      print("Keyword :",keyword)
      print("Title :",title)
      print("Content :",text)
      print()



