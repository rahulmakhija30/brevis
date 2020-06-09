from youtube_search import YoutubeSearch
def youtube_scrapper(query,search_results=3):
  results = YoutubeSearch(query, max_results=search_results).to_dict()
  res={}
  for d in results:
    res[d["title"]]="www.youtube.com"+d["link"]
  return res

#Driver Code
if __name__ == "__main__":
  query=input("Enter Query : ")
  search_results=int(input("Enter number of results to be fetched : "))
  res=youtube_scrapper(query,search_results)
  print(res)
