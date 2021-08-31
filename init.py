import math

def readOrinalFileToLower(path):
    file = open(path, 'r')
    lineList = []

    for lines in file:
        lines = lines.lower()
        lines = lines.rstrip()
        lineList.append(lines)
    return lineList

def read(path):
    file = open(path, "r")
    line_List = []
    for lines in file:
        line_List.append(lines)
    return line_List

def split(file):
    dictionary = dict()
    for line in file:
        for word in line.split():
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary

def pad(originalToLower):
    newList = []
    for line in originalToLower:
        line = "<s> " + line + " </s>\n"
        newList.append(line)
    return newList



def replace(newFile, pad_File, unk_Dic):
    file = open(newFile, "w")
    lineList = []
    sen = " "
    for line in pad_File:
        line = line.split()
        for words in line:
            if words not in unk_Dic:
                line[line.index(words)] = "<unk>"
            sen = " ".join(line)
        lineList.append(sen)
    for list in lineList:
        file.write(list + "\n")
    file.close()

def Brown_Learner(newFile, pad_File, dicForTrain):
    file = open(newFile, "w")
    lineList = []
    sen = ""
    for line in pad_File:
        line = line.split()
        for words in line:
            if words not in dicForTrain:
                line[line.index(words)] = "<unk>"
            sen = " ".join(line)
        lineList.append(sen)
    for list in lineList:
        file.write(list + "\n")


def findToken(path):
    file = open(path, "r")
    count = 0
    for lines in file:
        for words in lines.split():
            count += 1
    return count

def splitBi(file):
    dictionary = dict()
    newDic = dict()
    count = 0;
    for line in file:
        words = line.split()
        i = 1
        for word in words[0: len(words) - 1]:
            var = (word, words[i])
            if var in dictionary:
                dictionary[var] += 1
            else:
                dictionary[var] = 1
            i += 1
    return dictionary


def calPerForUn(TrainDic, file):
    count = 0
    nonMatchDic = dict()
    MatchDic = dict()
    for lines in file:
        for words in lines.split():
            count += 1
            if words in TrainDic:
                if words in MatchDic:
                    MatchDic[words] += 1
                else:
                    MatchDic[words] = 1
            else:
                if words in nonMatchDic:
                    nonMatchDic[words] += 1
                else:
                    nonMatchDic[words] = 1
    val = len(MatchDic) + len(nonMatchDic)
    valPer = (len(nonMatchDic)/val)*100
    return valPer


def calPerForUniTok (TrainDic, TestDic):
    token =0
    for k in TestDic:
        if k not in TrainDic.keys():
            token += TestDic.get(k,0)
    t = sum(TestDic.values())
    return (token/t)*100

def calPerForBi(TrainDic, TestDic):
    ty = 0
    for k in TestDic:
        if k not in TrainDic.keys():
            ty += 1
    t = len(TestDic)
    return (ty/t)*100


def padSen(sentence, trainDic):

    sentence = "<s> " + sentence + " </s>"
    words = sentence.lower().split()
    newWords = []
    for word in words:
        if word not in trainDic.keys():
            newWords.append("<unk>")
        else:
            newWords.append(word)
    newSent = ""
    for w in newWords:
        newSent += w + " "
    return newSent.rstrip()

###################################################################


brownTrain = 'brown-train.txt'
brownTest = 'brown-test.txt'
learnerTest = 'learner-test.txt'

padded_brownTrain = "brown-train-padded_new.txt"
padded_brownTest = "brown-test-padded_new.txt"
padded_learnerTest = "learner-test-padded_new.txt"

correct_Padded_train = "updated-brown-train.txt"  # 15031
correct_Padded_test = "updated-brown-test.txt"  # 2732
correct_Padded_learner = "updated-learner-test.txt"  # 1139

padded_Bi_Train = "Bi_train.txt"
padded_Bi_Test = "Bi_test.txt"
padded_Bi_learner = "Bi_learner.txt"

# ===================    Padding for Brown_Train      ====================================================

# original = dict()
# original = readOrinalFileToLower(brownTrain) ## change file name here
#
# pad_File = dict()
# pad_File= pad(original)
#
#
# #split method takes any string file and seperates it
# split_Line = dict()
# split_Line = split(pad_File)
# #print(len(split_Line))
#
# # gives a dictionary will <unk> as a value
# # create a new file and saves it there
# # replace(padded_brownTrain, pad_File, DicForTrain) ## change file neme here

# =============      Displays padded document  ===============================

DicForTrain = dict()
DicForTrain = split(read(padded_brownTrain))
print("Ans 1: Total unique words in Training: ", len(DicForTrain))
#

# ======================     Padding for Brown_Test  =========================================
# originalforTest = dict()
# originalforTest = readOrinalFileToLower(brownTest)
#
# pad_File_Test = dict()
# pad_File_Test = pad(originalforTest)
#
# split_Line_Test = dict()
# split_Line_Test = split(pad_File_Test)
#
# Brown_Learner(padded_brownTest, pad_File_Test, DicForTrain)

# =============      Displays padded document  ===============================

# DicForTest = dict()
# DicForTest = split(read(padded_brownTest))
# print("Total unique words in Test: ", len(DicForTest))

# ======================     Padding for Brown_Test  =========================================
# originalforLearner = dict()
# originalforLearner = readOrinalFileToLower(learnerTest)
#
# pad_File_Learner = dict()
# pad_File_Learner = pad(originalforLearner)
#
# split_Line_Learner = dict()
# split_Line_Learner = split(pad_File_Learner)
#
# Brown_Learner(padded_learnerTest, pad_File_Learner, DicForTrain)

# =============      Displays padded document  ===============================
# DicForLearner = dict()
# DicForLearner = split(read(padded_learnerTest))
# print("Total unique words in learner: ", len(DicForLearner))

# ==============     Find Tokenizer      =======================

totalToken = findToken(padded_brownTrain)
print("Ans 2: Total Token in Training: ", totalToken)

#
#
#
# # checks if the value exists in the unk_Dic, if it does not exist replace with unk
# #a = split(replace(pad_File, unk_Dic))
# # print(len(a))
#
#
# newDic = dict()
# newDic = split(read(padded_learnerTest)) ## change file name here
# print(len(newDic))


# how code works for brown-train?



# ======================     Padded Bigram       ===========================================
original = dict()
original = readOrinalFileToLower(brownTest)

pad_File = dict()
pad_File = pad(original)

DicForBi = dict()
DicForBi = splitBi(readOrinalFileToLower(padded_brownTrain))


DicForBiLearner = dict()
DicForBiLearner = splitBi(readOrinalFileToLower(padded_learnerTest))


DicForBiTr = dict()
DicForBiTr = splitBi(read(padded_brownTrain))

DicForBiTs = dict()
DicForBiTs = splitBi(read(padded_brownTest))

DicForBiLs = dict()
DicForBiLs = splitBi(read(padded_learnerTest))



# ============== Question 3 ====================
print("Ans 3 ")
TrainDic = dict()
TrainDic = split(pad(readOrinalFileToLower(brownTrain)))

TestDic = dict()
TestDic = split(pad(readOrinalFileToLower(brownTest)))

LearnerDic = dict()
LearnerDic = split(pad(readOrinalFileToLower(learnerTest)))


perValUni = calPerForUn(TrainDic, pad(readOrinalFileToLower(brownTest)))
print("Percentage for Unigram in Brown Test (type): ", perValUni)

perValUni = calPerForUniTok(TrainDic, TestDic)
print("Percentage of Token for Unigram in Brown Test (token): ", perValUni)

perValUni = calPerForUn(TrainDic, pad(readOrinalFileToLower(learnerTest)))
print("Percentage for Unigram in Learner Test (type): ", perValUni)

perValUni = calPerForUniTok(TrainDic, LearnerDic)
print("Percentage of Token for Unigram in Learner Test (token): ", perValUni)



# ============== Question 4 ====================
print("Ans 4")
# perValBi = calPerForBi(DicForBi, read(padded_brownTest))


perValBi =calPerForBi(DicForBiTr, DicForBiTs)
print("Percentage for Bigram in Brown Test (type): ", perValBi)

perValBi = calPerForUniTok(DicForBiTr, DicForBiTs)
print("Percentage for Bigram in Brown Test (token): ", perValBi)

perValBi = calPerForBi(DicForBiTr, DicForBiLs)
print("Percentage for Bigram in Learner Test (type): ", perValBi)

perValBi = calPerForUniTok(DicForBiTr, DicForBiLs)
print("Percentage for Bigram in Learner Test (token): ", perValBi)






# perValBi = calPerForBi(DicForBiLearner, pad(readOrinalFileToLower(learnerTest)))
# print("Percentage for Bigram in Learner Test: ", perValBi)

# ============== Question 5 ====================


def ppCheckSmoothing(DicForTrain, sentence, DicForBi):
    probability = 1.0
    words = sentence.split()
    j = 1
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[j]
        j += 1
        if DicForTrain.get(w1, 0) == 0:
            w1 = "<unk>"
        if DicForTrain.get(w2, 0) == 0:
            w2 = "<unk>"
        wp = biProbSmooth(w1, w2, DicForTrain, DicForBi)
        probability *= wp
    return probability

def biProb(w1, w2, DicForTrain, DicForBi):
    t1 = DicForBi.get((w1, w2), 0)
    t2 = DicForTrain.get(w1,0)
    if t1 == 0 or t2 == 0:
        return 0
    else:
        return t1/t2

def biProbSmooth(w1, w2, DicForTrain, DicForBi):
    t1 = DicForBi.get((w1, w2), 0) + 1
    t2 = DicForTrain.get(w1,0) + len(DicForTrain)
    if t1 == 0 or t2 == 0:
        return 0
    else:
        return t1/t2

def ppCheckBi(DicForTrain, sentence, DicForBi):
    probability = 1.0
    words = sentence.split()
    j = 1
    for i in range(len(words) -1):
        w1 = words[i]
        w2 = words[j]
        j+=1
        if DicForTrain.get(w1,0) == 0:
            w1 = "<unk>"
        if DicForTrain.get(w2, 0) == 0:
            w2 = "<unk>"
        wp = biProb(w1, w2, DicForTrain, DicForBi)
        probability *= wp
    return probability

def ppCheckUni(trainDic, sentence, totalToken):
    probability = 1.0
    words = sentence.split()
    for word in words:
        if word in trainDic:
            valForTrain = trainDic[word]
            probability *= valForTrain / totalToken
    return probability


print("Ans 5: ")
sen1 = "He was laughed off the screen ."
sen2 = "There was no compulsion behind them ."
sen3 = "I look forward to hearing your reply ."

pS1 = padSen(sen1, DicForTrain)
pS2 = padSen(sen2, DicForTrain)
pS3 = padSen(sen3, DicForTrain)

probabilityForUni = 1.0

print("=========                   Unigram                   =========")
probabilityForUni = ppCheckUni(TrainDic, pS1, totalToken)
print("Log Prob check for Unigram:",sen1, " = ",math.log(probabilityForUni, 2))
probabilityForUni = ppCheckUni(DicForTrain, sen2, totalToken)
print("Log Prob check for Unigram:", sen2, " = ",math.log(probabilityForUni, 2))
probabilityForUni = ppCheckUni(TrainDic, sen3, totalToken)
print("Log Prob check for Unigram:",sen3, " = ", math.log(probabilityForUni, 2))


print("=========                     Bigram                   =========")
Prob = ppCheckBi(DicForTrain, pS1, DicForBi)
if Prob == 0:
    print("Log Prob check for Bigram: ", sen1," = <und> ")
else:
    print("Log Prob check for Bigram: ", sen1," = " ,math.log(Prob, 2))

Prob = ppCheckBi(DicForTrain, pS2, DicForBi)
if Prob == 0:
    print("Log Prob check for Bigram: ", sen2," = <und> ")
else:
    print("Log Prob check for Bigram: ", sen2," = " ,math.log(Prob, 2))

Prob = ppCheckBi(DicForTrain, pS3, DicForBi)
if Prob == 0:
    print("Log Prob check for Bigram: ", sen3," = <und>")
else:
    print("Log Prob check for Bigram: ", sen3," = " ,math.log(Prob, 2))


print("=========                     Bigram Smoothing                      =========")

p = ppCheckSmoothing(DicForTrain, pS1, DicForBi)
print("Log Prob check for Bigram: ",sen1," = ", math.log(p, 2))
p = ppCheckSmoothing(DicForTrain, pS2, DicForBi)
print("Log Prob check for Bigram: ",sen2," = ", math.log(p, 2))
p = ppCheckSmoothing(DicForTrain, pS3, DicForBi)
print("Log Prob check for Bigram: ",sen3," = ", math.log(p, 2))


#=================== Question 6 ================

def ppCheckUniForPer(trainDic, sentence, totalToken):
    probability = 0.0
    words = sentence.split()
    for word in words:
        if word in trainDic:
            valForTrain = trainDic[word]
            wp = valForTrain / totalToken
            probability += math.log(wp, 2)
    return math.pow(2, -(probability/len(words)))

def ppCheckBiForPer(DicForTrain, sentence, DicForBi):
    probability = 0.0
    words = sentence.split()
    j = 1
    for i in range(len(words) -1):
        w1 = words[i]
        w2 = words[j]
        j+=1
        if DicForTrain.get(w1,0) == 0:
            w1 = "<unk>"
        if DicForTrain.get(w2, 0) == 0:
            w2 = "<unk>"
        wp = biProb(w1, w2, DicForTrain, DicForBi)
        if wp == 0.0:
            return "<und>"
        else:
            probability += math.log(wp, 2)
    per = math.pow(2, -(probability/len(words)))
    return per

def ppCheckBiSmoothForPer(DicForTrain, sentence, DicForBi):
    probability = 0.0
    words = sentence.split()
    j = 1
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[j]
        j += 1
        if DicForTrain.get(w1, 0) == 0:
            w1 = "<unk>"
        if DicForTrain.get(w2, 0) == 0:
            w2 = "<unk>"
        wp = biProbSmooth(w1, w2, DicForTrain, DicForBi)
        if wp == 0.0:
            return "<und>"
        else:
            probability += math.log(wp, 2)
    return math.pow(2, -(probability/len(words)))


print("Ans 6:")
print("=========                      Unigram                      =========")
per = ppCheckUniForPer(DicForTrain, pS1, totalToken)
print("Perplexities for Unigram: ", sen1, " = " , per)
per = ppCheckUniForPer(DicForTrain, pS2, totalToken)
print("Perplexities for Unigram: ", sen2, " = " , per)
per = ppCheckUniForPer(DicForTrain, pS3, totalToken)
print("Perplexities for Unigram: ", sen3, " = " , per)

print("=========                      Bigram                       =========")
per = ppCheckBiForPer(DicForTrain, pS1, DicForBi)
print("Perplexities for Bigram: ", sen1, " = " , per)
per = ppCheckBiForPer(DicForTrain, pS2, DicForBi)
print("Perplexities for Bigram: ", sen2, " = " , per)
per = ppCheckBiForPer(DicForTrain, pS3, DicForBi)
print("Perplexities for Bigram: ", sen3, " = " , per)

print("=========                    Bigram Smoothing               =========")
per = ppCheckBiSmoothForPer(DicForTrain, pS1, DicForBi)
print("Perplexities for Bigram Smoothing: ", sen1, " = " , per)
per = ppCheckBiSmoothForPer(DicForTrain, pS2, DicForBi)
print("Perplexities for Bigram Smoothing: ", sen2, " = " , per)
per = ppCheckBiSmoothForPer(DicForTrain, pS3, DicForBi)
print("Perplexities for Bigram Smoothing: ", sen3, " = " , per)

#=================      Question 7      =============

def ppTotalCorporaUniForPer(trainDic, sentence, totalToken):
    probability = 0.0
    words = sentence.split()
    for word in words:
        if word in trainDic:
            valForTrain = trainDic[word]
            wp = valForTrain / totalToken
            probability += math.log(wp, 2)
    return probability

def ppTotalCoporakBiSmoothForPer(DicForTrain, sentence, DicForBi):
    probability = 0.0
    words = sentence.split()
    j = 1
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[j]
        j += 1
        if DicForTrain.get(w1, 0) == 0:
            w1 = "<unk>"
        if DicForTrain.get(w2, 0) == 0:
            w2 = "<unk>"
        wp = biProbSmooth(w1, w2, DicForTrain, DicForBi)
        if wp == 0.0:
            return "<und>"
        else:
            probability += math.log(wp, 2)
    return probability

def ppTotalCorporaBiForPer(DicForTrain, sentence, DicForBi):
    probability = 0.0
    words = sentence.split()
    j = 1
    for i in range(len(words) -1):
        w1 = words[i]
        w2 = words[j]
        j+=1
        if DicForTrain.get(w1,0) == 0:
            w1 = "<unk>"
        if DicForTrain.get(w2, 0) == 0:
            w2 = "<unk>"
        wp = biProb(w1, w2, DicForTrain, DicForBi)
        if wp == 0.0:
            return "<und>"
        else:
            probability += math.log(wp, 2)
    return probability


print("Ans 7:")
print("=============                      Brown Test               ===================")
tot_prob = 0.0
brown_test_lines = read(padded_brownTest)
for l in brown_test_lines:
    p = ppTotalCorporaUniForPer(DicForTrain, l, totalToken)
    tot_prob += p
wholePer = math.pow(2, -(tot_prob/findToken(padded_brownTest)))
print(padded_brownTest, "Unigram", wholePer)

tot_prob = 0.0
brown_test_lines = read(padded_brownTest)
for l in brown_test_lines:
    p = ppTotalCorporaBiForPer(DicForTrain, l, DicForBi)
    if p == "<und>":
        print(padded_brownTest, "Bigram", p)
        break
    tot_prob += p
# wholePer = math.pow(2, -(tot_prob/findToken(padded_brownTest)))
# print(padded_brownTest, "bigram", wholePer)

tot_prob = 0.0
brown_test_lines = read(padded_brownTest)
for l in brown_test_lines:
    p = ppTotalCoporakBiSmoothForPer(DicForTrain, l, DicForBi)
    if p == "<und>":
        print(padded_brownTest, "Bigram Smoohting", p)
        break
    tot_prob += p
wholePer = math.pow(2, -(tot_prob/findToken(padded_brownTest)))
print(padded_brownTest, "Bigram Smoohting", wholePer)



print("=============                    Learner Test                 ===================")
tot_prob = 0.0
learner_test_lines = read(padded_learnerTest)
for l in learner_test_lines:
    p = ppTotalCorporaUniForPer(DicForTrain, l, totalToken)
    tot_prob += p
wholePer = math.pow(2, -(tot_prob/findToken(padded_learnerTest)))
print(padded_learnerTest, "Unigram", wholePer)

tot_prob = 0.0
learner_test_lines = read(padded_learnerTest)
for l in learner_test_lines:
    p = ppTotalCorporaBiForPer(DicForTrain, l, DicForBi)
    if p == "<und>":
        print(padded_learnerTest, "Bigram", p)
        break
    tot_prob += p
# wholePer = math.pow(2, -(tot_prob/findToken(padded_brownTest)))
# print(padded_brownTest, "bigram", wholePer)

tot_prob = 0.0
learner_test_lines = read(padded_learnerTest)
for l in learner_test_lines:
    p = ppTotalCoporakBiSmoothForPer(DicForTrain, l, DicForBi)
    if p == "<und>":
        print(padded_learnerTest, "Bigram smoohting", p)
        break
    tot_prob += p
wholePer = math.pow(2, -(tot_prob/findToken(padded_learnerTest)))
print(padded_learnerTest, "Bigram Smoohting", wholePer)