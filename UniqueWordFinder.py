import math

from bs4 import BeautifulSoup
import urllib.request
import re
import math


def Q3_P1():
    arrOfURLS = []
    NumOfUniquesPerURL = []
    TotalNumOfWordsPerURl = []
    tfOfCoronavirus = []
    tfOfMask = []
    tfOfHealth = []
    idfOfCoronavirus = 0
    idfOfMask = 0
    idfOfHealth = 0
    tfidfOfCoronavirus = []
    tfidfOfMask = []
    tfidfOfHealth = []
    arrOfStopWords = []

    #stop words file
    stopWordsFile = open('stop_words.txt', 'r')
    for x in stopWordsFile:
        arrOfStopWords.append(x.strip())
    #print(arrOfStopWords)

    # list of URLS to operate on
    textFileWithURLS = open("urls.txt", "r")
    for i in textFileWithURLS:
        arrOfURLS.append(i.strip())
    #print(arrOfURLS)

    for i in arrOfURLS:
        # Finding all Paragraph tags
        r = urllib.request.urlopen(i).read()
        soup = BeautifulSoup(r)
        paragraph = soup.find_all('p')
        # words per URL into lists
        dictOfWordsPerURL = {}

        # putting all of the words in a url into an list
        wordsPerUrl = []
        frequencyOfCoronavirus = []
        frequencyOfMask = []
        frequencyOfHealth = []

        for j in paragraph:
            pText = j.getText().lower()

            wordsInParagraph = re.sub(r'\W', ' ', pText)
            wordsInParagraph = re.findall(r'\S+', wordsInParagraph)
            for words in list(wordsInParagraph):
                for moreWords in list(arrOfStopWords):
                    if words == moreWords:
                        wordsInParagraph.remove(moreWords)

            coronavirus = re.findall(r'coronavirus', pText)
            frequencyOfCoronavirus.extend(coronavirus)
            mask = re.findall(r'mask', pText)
            frequencyOfMask.extend(mask)
            health = re.findall(r'health', pText)
            frequencyOfHealth.extend(health)

            wordsPerUrl.extend(wordsInParagraph)
        # Keeping Track of Total Length of URL
        TotalNumOfWordsPerURl.append(len(wordsPerUrl))

        #findTF
        tfOfCoronavirus.append(len(frequencyOfCoronavirus)/len(wordsPerUrl))
        tfOfMask.append(len(frequencyOfMask)/len(wordsPerUrl))
        tfOfHealth.append(len(frequencyOfHealth)/len(wordsPerUrl))
        #findIDF
        idfOfCoronavirus = math.log(len(arrOfURLS)/1 + len(frequencyOfCoronavirus))
        idfOfMask = math.log(len(arrOfURLS) / 1 + len(frequencyOfMask))
        idfOfHealth = math.log(len(arrOfURLS) / 1 + len(frequencyOfHealth)+1)




        # dictionary to find frequency of words and find the Unique Words
        uniqueWords = []
        for k in wordsPerUrl:
            if dictOfWordsPerURL.get(k):
                dictOfWordsPerURL[k] += 1
            else:
                dictOfWordsPerURL.update({k: 1})
        for key, values in dictOfWordsPerURL.items():
            uniqueWords.append(key)

        # finding Number of Unique Words Per URL
        NumOfUniquesPerURL.append(len(uniqueWords))

    # findTFIDF
    #tfidfOfCoronavirus = (tfOfCoronavirus * int(idfOfCoronavirus))
    #tfidfOfMask = (tfOfMask * int(idfOfMask))
    #tfidfOfHealth = (tfOfHealth * int(idfOfHealth))

    tfidfOfCoronavirus = [i * idfOfCoronavirus for i in tfOfCoronavirus]
    tfidfOfMask = [i * idfOfMask for i in tfOfMask]
    tfidfOfHealth = [i * idfOfHealth for i in tfOfHealth]




   
    #testing basic output
    f.write("unique: " + str(NumOfUniquesPerURL) + "\n")
    f.write("length: " + str(TotalNumOfWordsPerURl) + "\n")
    f.write("tf coronavirus: " + str(tfOfCoronavirus) + "\n")
    f.write("tf mask: " + str(tfOfMask) + "\n")
    f.write("tf health: " + str(tfOfHealth) + "\n")
    f.write("idf coronavirus: " + str(idfOfCoronavirus) + "\n")
    f.write("idf mask: " + str(idfOfMask) + "\n")
    f.write("idf health: " + str(idfOfHealth) + "\n")
    f.write("tf-idf coronavirus: " + str(tfidfOfCoronavirus) + "\n")
    f.write("tf-idf mask: " + str(tfidfOfMask) + "\n")
    f.write("tf-idf health: " + str(tfidfOfHealth) + "\n")


Q3_P1()
