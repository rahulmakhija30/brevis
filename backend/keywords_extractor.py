import RAKE
import operator
def get_keywords(text,n):
    stop_dir = "SmartStoplist.txt"
    rake_object = RAKE.Rake(stop_dir)
    keywords_weighted = rake_object.run(text)
    keywords=list()
    for word,weight in keywords_weighted:
        keywords.append(word)
    #Handling Error
    if(n > len(keywords)):
        print("No. of keywords entered is more than the maximum number of keywords.")
        return -1
    return keywords[:n]

#Driver Code
if __name__=="__main__":
    text =input("Enter text : ")
    keyword_number=int(input("Enter number of keywords to be extracted : "))
    keywords=get_keywords(text,keyword_number)
    if(keywords!=-1):
        print ("keywords: ", keywords)

