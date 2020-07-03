project_Twitter_Data_File = open('../Coursera_Final_course_file_funtion_dictionart/project_twitter_data.csv', 'r')
resulting_Data_File = open('../Coursera_Final_course_file_funtion_dictionart/resulting_data.csv', 'w')


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(str1):
    for ch in punctuation_chars:
        str1 = str1.replace(ch, '')
    return str1


def get_pos(strSentences):
    strSentences_lower = strSentences.lower()
    strSentences = strip_punctuation(strSentences_lower)
    listStrSentences = strSentences.split()

    count = 0
    for word in listStrSentences:
        for positiveWord in positive_words:
            if word == positiveWord:
                count += 1
    return count


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_neg(str1):
    str1_lower = str1.lower()
    str1_lower_strip = strip_punctuation(str1_lower)
    str1_lower_strip_list = str1_lower_strip.split()
    count = 0
    for word in str1_lower_strip_list:
        for negative_word in negative_words:
            if word == negative_word:
                count += 1
    return count


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def writeInDataFile(resulting_Data_File):
    resulting_Data_File.write('Number of Retweets, Number of Replies, positive Score, Negative Score, Net Score')
    resulting_Data_File.write('\n')
    linesPTDF = project_Twitter_Data_File.readlines()
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        resulting_Data_File.write(
            '{}, {}, {}, {}, {}'.format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]),
                                        (get_pos(listTD[0]) - get_neg(listTD[0]))))
        resulting_Data_File.write("\n")
    writeInDataFile(resulting_Data_File)
    project_Twitter_Data_File.close()
    resulting_Data_File.close()


