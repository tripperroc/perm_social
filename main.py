import readText
import mentionsGraph
# import createDictScores1
# import createDictScores2
# import createDictScores3
# import createDictScores4
# import createDictScores5
import splitDataset
import extractEmotion
import createDictionaryOfScores
# import egograph

def main():
    readText.read()
    mentionsGraph.check()
    splitDataset.splitData()
    createDictionaryOfScores.createDict()
    # extractEmotion.emotion()
    # egograph
    # findAvg(dict_with_scores)
    # histogram()


if __name__ == '__main__':
    main()
