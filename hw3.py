def locate_word(string,substring):
    matches=[]
    index=0
    while index<len(string):
        if string[index:index+len(substring)]==substring:
            matches.append(index)
            index+=len(substring)
        else:
            index+=1
    return matches

a="Whereas it appears that a state of war exists between Austria, Prussia, Sardinia, Great Britain, and the United Netherlands, on the one part, and France on the other; and the duty and interest of the United States require, that they should with sincerity and good faith adopt and pursue a conduct friendly and impartial towards the belligerent powers:I have therefore thought fit by these presents, to declare the disposition of the United States to observe the conduct aforesaid towards those powers respectively; and to exhort and warn the citizens of the United States carefully to avoid all acts and proceedings whatsoever, which may in any manner tend to contravene such disposition.And I do hereby also make known, that whosoever of the citizens of the United States shall render himself liable to punishment or forfeiture under the law of nations, by committing, aiding or abetting hostilities against any of the said powers, or by carrying to any of them, those articles which are deemed contraband by the modern usage of nations, will not receive the protection of the United States against such punishment or forfeiture; and further that I have given instructions to those officers to whom it belongs, to cause prosecutions to be instituted against all persons, who shall, within the cognizance of the Courts of the United States, violate the law of nations, with respect to the powers at war, or any of them."
print(locate_word(a,"United States"))
print(locate_word(a,"citizens"))
print(locate_word(a,"powers"))
print(locate_word(a,"and"))

#Speech=Proclamation of Neutrality-George Washnington
#The locate_word function is used to locate all of the indexes within the string that contain the desired substring. The number of indexes located when the function runs indicates how many times the given substring can be found in the string (which in this case is the speech)
# The code works like this: while the index is less than the length of the given string, if the specific index the code is looking at is equal to the substring, then the index will be added to the matches list and then the code will move to the next index after the given substring, otherwise, the code will keep moving through the indeces until it hits the next substring. Indeces will continue to be added to the matches list until the last index is reached. Then, the matches list is returned.
#From the code I ran, I can determine a number of things about Washington's speech.
#I know that the word "United States" is found 6 times, first at index 200 and last at index 1326. The frequency of the word stayed fairly consistent throughout the speech
#The word "citizens" is found twice, first at index 542 and last at index 743. This word was found the least number of times out of all of the chosen words and were used in the middle of the speech.
#The word "powers" is found 4 times, first at index 344 and last at index 1389. Out of the chosen words, this was the last one used in the speech as it has the highest index returned.
#The word "and" is found 13, first at index 97 and last at index 1131. Given the indeces provided by the code, "and" was used most frequently at the beginning of the speech and it was also the word that occured the most out of all of the chosen words. This makes sense as it is one of the more common words in the English language
